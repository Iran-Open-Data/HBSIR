"""
Main file for ordinary use
"""

from typing import Literal, get_args

import sympy
import pandas as pd

from . import metadata, utils

defaults = metadata.Defaults()
metadata_obj = metadata.Metadata()

_Attributes = Literal["Urban-Rural", "Province", "Region"]


def _check_attribute(attribute: _Attributes | list[_Attributes]):
    available_attribute = get_args(_Attributes)
    if not isinstance(attribute, list):
        attribute = [attribute]
    for atr in attribute:
        if not atr in available_attribute:
            raise KeyError(
                f"{atr} is not in attributes.\n"
                f"Available attributes: {available_attribute}")


def load_table(
    table_name: str,
    from_year=None,
    to_year=None,
    standard=True,
    add_year: bool | None = None,
) -> pd.DataFrame:
    """_summary_

    Parameters
    ----------
    table_name : str
        _description_
    from_year : _type_, optional
        _description_, by default None
    to_year : _type_, optional
        _description_, by default None
    standard : bool, optional
        _description_, by default True

    Returns
    -------
    pd.DataFrame
        _description_
    """
    from_year, to_year = utils.build_year_interval(from_year, to_year)
    if add_year is None:
        add_year = to_year - from_year > 1

    table_list = []
    for year in range(from_year, to_year):
        table = _get_parquet(table_name, year)
        if add_year:
            table["Year"] = year
        table_list.append(table)
    concat_table = pd.concat(table_list)

    if standard:
        concat_table = imply_table_schema(concat_table, table_name, year)

    return concat_table


def _get_parquet(table_name: str, year: int, download: bool = True) -> pd.DataFrame:
    file_name = f"{year}_{table_name}.parquet"
    try:
        table = pd.read_parquet(defaults.processed_data.joinpath(file_name))
    except FileNotFoundError as exc:
        if download:
            _download_parquet(table_name, year)
            table = pd.read_parquet(
                defaults.processed_data.joinpath(file_name))
        else:
            raise exc
    return table


def _download_parquet(table_name: str, year: int) -> None:
    file_name = f"{year}_{table_name}.parquet"
    file_url = f"{defaults.online_dir}/parquet_files/{file_name}"
    local_path = defaults.processed_data.joinpath(file_name)
    utils.download_file(url=file_url, path=local_path, show_progress_bar=True)


def imply_table_schema(table, table_name, year):
    """_summary_

    Parameters
    ----------
    table : _type_
        _description_
    table_name : _type_
        _description_
    year : _type_
        _description_

    Returns
    -------
    pd.DataFrame
        _description_
    """
    table_schema = metadata_obj.schema[table_name]
    instructions = table_schema["columns"]
    column_order = table_schema["order"]

    for name, instruction in instructions.items():
        instruction = metadata.get_metadata_version(instruction, year)
        table = _apply_column_instruction(table, name, instruction)

    table = _order_columns_by_schema(table, column_order)
    return table


def _apply_column_instruction(table, name, instruction):
    if instruction is None:
        pass
    elif instruction["type"] == "categorical":
        table = _apply_categorical_instruction(table, name, instruction)
    elif instruction["type"] == "numerical":
        table = _apply_numerical_instruction(table, name, instruction)

    return table


def _apply_categorical_instruction(table, column_name, instruction):
    categories = instruction["categories"]

    if column_name not in table.columns:
        table[column_name] = None

    # TODO chack column type and behave accordingly not just changing the type
    table[column_name] = table[column_name].astype(str)

    for category, condition in categories.items():
        if isinstance(condition, str):
            filt = table[column_name] == condition
        elif isinstance(condition, list):
            filt = table[column_name].isin(condition)
        elif isinstance(condition, dict):
            filt = pd.Series(False, index=table.index)
            for other_column, value in condition.items():
                filt = filt | (table[other_column] == value)
        table.loc[filt, column_name] = category

    return table


def _apply_numerical_instruction(table, column_name, instruction):
    expr = instruction["expression"]
    pandas_expr = _parse_expression(expr)
    table[column_name] = pd.eval(pandas_expr)
    return table


def _parse_expression(expression, table_name="table"):
    expr = sympy.simplify(expression)
    terms = []

    if len(expr.args) == 0:
        _, var = expr.as_coeff_Mul()
        return f"{table_name}['{var}']"

    if (len(expr.args) == 2) and (len(expr.args[1].args) == 0):
        coeff, var = expr.as_coeff_Mul()
        return f"{table_name}['{var}'] * {coeff}"

    for term in expr.args:
        coeff, var = term.as_coeff_Mul()
        terms.append(f"{table_name}['{var}'].fillna(0) * {coeff}")
    return " + ".join(terms)


def _order_columns_by_schema(table, column_order):
    new_columns = [
        column for column in column_order if column in table.columns]
    return table[new_columns]


def add_attribute(
    table: pd.DataFrame,
    year: int,
    attribute: _Attributes | list[_Attributes],
    id_column_name="ID",
    attribute_text="names",
) -> pd.DataFrame:
    """_summary_

    Parameters
    ----------
    table : pd.DataFrame
        _description_
    year : int
        _description_
    attribute : _Attributes | list[_Attributes]
        _description_
    id_column_name : str, optional
        _description_, by default "ID"

    Returns
    -------
    pd.DataFrame
        _description_
    """
    _check_attribute(attribute)
    if not isinstance(attribute, list):
        attribute_list = [attribute]
    else:
        attribute_list = attribute
    table = table.copy()

    for atr in attribute_list:
        attribute_column = get_household_attribute(
            _input=table,
            year=year,
            attribute=atr,
            id_column_name=id_column_name,
            attribute_text=attribute_text,
        )
        table[atr] = attribute_column
    return table


def get_household_attribute(
    _input: pd.DataFrame | pd.Series,
    year: int,
    attribute: _Attributes,
    id_column_name="ID",
    attribute_text="names",
) -> pd.Series:
    """_summary_

    Parameters
    ----------
    data : pd.DataFrame | pd.Series
        _description_
    year : int
        _description_
    attribute : _Attributes
        _description_

    Returns
    -------
    pd.Series
        _description_
    """
    _check_attribute(attribute)
    if isinstance(_input, pd.DataFrame):
        _input = _input[id_column_name].copy()
    if not isinstance(_input, pd.Series):
        raise ValueError
    return _get_attribute_by_id(_input, year, attribute, attribute_text)


def _get_attribute_by_id(
    household_id_column: pd.Series,
    year: int,
    attribute: _Attributes,
    attribute_text="names",
) -> pd.Series:
    attr_dict = metadata_obj.household[attribute]
    text = metadata.get_metadata_version(attr_dict[attribute_text], year)
    attr_codes = _get_attribute_code(household_id_column, year, attribute)
    return attr_codes.map(text)


def _get_attribute_code(
    household_id_column: pd.Series,
    year: int,
    attribute: _Attributes,
) -> pd.Series:
    id_length = metadata.get_metadata_version(
        metadata_obj.household["ID_Length"], year)
    attr_dict = metadata_obj.household[attribute]
    position = metadata.get_metadata_version(attr_dict["position"], year)
    start, end = position["start"], position["end"]
    attr_codes = household_id_column % pow(10, (id_length - start))
    attr_codes = attr_codes // pow(10, (id_length - end))
    return attr_codes


def add_classification(
    table: pd.DataFrame,
    classification: str,
    level: int,
    year: int,
    code_column_name: str = "Code",
    new_column_name: str | None = None
):
    """_summary_

    Parameters
    ----------
    table : pd.DataFrame
        _description_
    year : int
        _description_
    level : int
        _description_
    code_column_name : str, optional
        _description_, by default "Code"
    """
    table = table.copy()
    code_classification = get_code_classification(
        table, classification=classification, level=level,
        year=year, code_column_name=code_column_name)
    if new_column_name is None:
        new_column_name = f"{classification} - {level}"
    table[new_column_name] = code_classification
    return table


def get_code_classification(
    _input: pd.DataFrame | pd.Series,
    classification: str,
    level: int,
    year: int,
    code_column_name="Code",
) -> pd.Series:
    """_summary_

    Parameters
    ----------
    _input : pd.DataFrame | pd.Series
        _description_
    year : int
        _description_
    level : int
        _description_
    code_column_name : str, optional
        _description_, by default "Code"
    attribute_text : str, optional
        _description_, by default "names"

    Returns
    -------
    pd.Series
        _description_
    """
    if isinstance(_input, pd.DataFrame):
        _input = _input[code_column_name].copy()
    if not isinstance(_input, pd.Series):
        raise ValueError
    return _get_classification_by_code(_input, classification, level, year)


def _get_classification_by_code(
    commodity_code_column: pd.Series,
    classification: str,
    level: int,
    year: int,
) -> pd.Series:
    translator = _build_classification_translator(classification, level, year)
    return commodity_code_column.map(translator)


def _build_classification_translator(classification: str, level: int, year: int):
    commodity_codes = metadata_obj.commodities[classification]

    commodity_codes = metadata.get_metadata_version(commodity_codes, year)
    selected_items = {name: info for name, info
                      in commodity_codes.items() if info['level'] == level}

    translator = {}
    for name, info in selected_items.items():
        start, end = info['code']
        for code in range(start, end):
            translator[code] = name
    return translator
