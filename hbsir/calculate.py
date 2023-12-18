"""
This module contains functions for calculating various metrics.
"""
# pylint: disable=too-many-arguments
# pylint: disable=unused-argument
# pylint: disable=too-many-locals

from typing import Iterable

import pandas as pd

from bssir.calculator import Calculator
from bssir.calculator.quantile import _EquivalenceScale, _QuantileBase

from .api import api


calculate = Calculator(api)


def __get_optional_params(local_variables: dict) -> dict:
    return {key: value for key, value in local_variables.items() if value is not None}


def weighted_average(
    table: pd.DataFrame,
    weight_col: str | None = None,
    columns: list[str] | None = None,
) -> pd.Series:
    """Calculates the weighted average of the given columns.

    Parameters
    ----------
    table : pd.DataFrame
        The table to calculate the weighted average for.
    weight_col : str | None, optional
        The column to use as the weight, by default None
    columns : list[str] | None, optional
        The columns to calculate the weighted average for, by default None

    Returns
    -------
    pd.Series
        The weighted average of the given columns.
    """
    parameters = __get_optional_params(locals())
    return calculate.weighted_average(**parameters)


def average_table(
    table: pd.DataFrame,
    weight_col: str | None = None,
    groupby: list[str] | None = None,
    columns: list[str] | None = None,
) -> pd.DataFrame:
    """Calculates the weighted average of the given columns for each group.

    Parameters
    ----------
    table : pd.DataFrame
        The table to calculate the weighted average for.
    weight_col : str | None, optional
        The column to use as the weight, by default None
    groupby : list[str] | None, optional
        The columns to group by, by default None
    columns : list[str] | None, optional
        The columns to calculate the weighted average for, by default None

    Returns
    -------
    pd.DataFrame
        The weighted average of the given columns for each group.
    """
    parameters = __get_optional_params(locals())
    return calculate.average_table(**parameters)


def quantile(
    table: pd.DataFrame | pd.Series | None = None,
    quantile_column_name: str | None = None,
    bins: int = -1,
    weight_column: str | None = None,
    on_variable: _QuantileBase | None = None,
    on_column: str | None = None,
    weighted: bool = True,
    adjust_weight_for_household_size: bool = False,
    equivalence_scale: _EquivalenceScale = "Household",
    for_all: bool = True,
    annual: bool = True,
    groupby: str | Iterable[str] | None = None,
    years: list[int] | None = None,
) -> pd.Series:
    """Calculates weighted quantiles for the given column.

    Parameters
    ----------
    table : pd.DataFrame | pd.Series, optional
        Table containing column to calculate quantiles for.
    on_variable : _QuantileBase, optional
        Variable to calculate quantiles on.
    on_column : str, optional
        Column name to calculate quantiles on.
    bins : int, optional
        Number of quantile bins to create.

    Other parameters
    ----------------
    quantile_column_name : str, optional
        Name for added quantile column.
    weight_column : str, optional
        Column name to use for weighting rows.
    weighted : bool, optional
        Whether to calculate weighted quantiles.
    adjust_weight_for_household_size : bool, optional
        Adjust weights for household size.
    equivalence_scale : _EquivalenceScale, optional
        Household equivalence scale to use.
    for_all : bool, optional
        Calculate quantiles across all rows.
    annual : bool, optional
        Annualize quantiles.
    groupby : str | list[str], optional
        Column(s) to group by.
    years : list[int], optional
        Years to include.

    Returns
    -------
    pd.Series
        Series with quantiles for each row.
    """
    parameters = __get_optional_params(locals())
    return calculate.quantile(**parameters)


def add_quantile(
    table: pd.DataFrame | pd.Series | None = None,
    quantile_column_name: str | None = None,
    bins: int = -1,
    weight_column: str | None = None,
    on_variable: _QuantileBase | None = None,
    on_column: str | None = None,
    weighted: bool = True,
    adjust_weight_for_household_size: bool = False,
    equivalence_scale: _EquivalenceScale = "Household",
    for_all: bool = True,
    annual: bool = True,
    groupby: str | Iterable[str] | None = None,
    years: list[int] | None = None,
) -> pd.DataFrame:
    """Adds quantiles as a column to the input table.

    Parameters
    ----------
    table : DataFrame | Series, optional
        Table to add quantiles to.
    bins : int, optional
        Number of quantile bins to create.
    on_variable : _QuantileBase, optional
        Variable to calculate quantiles on.
    on_column : str, optional
        Column to calculate quantiles on.

    Other parameters
    ----------------
    quantile_column_name : str, optional
        Name for added quantile column.
    weight_column : str, optional
        Column name to use for weighting rows.
    weighted : bool, optional
        Whether to calculate weighted quantiles.
    adjust_weight_for_household_size : bool, optional
        Adjust weights for household size.
    equivalence_scale : _EquivalenceScale, optional
        Household equivalence scale to use.
    for_all : bool, optional
        Calculate quantiles across all rows.
    annual : bool, optional
        Annualize quantiles.
    groupby : str | list[str], optional
        Column(s) to group by.
    years : list[int], optional
        Years to include.

    Returns
    -------
    DataFrame
        Input table with added quantile column.
    """
    parameters = __get_optional_params(locals())
    return calculate.add_quantile(**parameters)


def add_decile(
    table: pd.DataFrame | pd.Series | None = None,
    quantile_column_name: str | None = None,
    weight_column: str | None = None,
    on_variable: _QuantileBase | None = None,
    on_column: str | None = None,
    weighted: bool = True,
    adjust_weight_for_household_size: bool = False,
    equivalence_scale: _EquivalenceScale = "Household",
    for_all: bool = True,
    annual: bool = True,
    groupby: str | Iterable[str] | None = None,
    years: list[int] | None = None,
) -> pd.DataFrame:
    """Adds deciles as a column to the input table.

    Parameters
    ----------
    table : DataFrame | Series, optional
        Table to add quantiles to.
    bins : int, optional
        Number of quantile bins to create.
    on_variable : _QuantileBase, optional
        Variable to calculate quantiles on.
    on_column : str, optional
        Column to calculate quantiles on.

    Other parameters
    ----------------
    quantile_column_name : str, optional
        Name for added quantile column.
    weight_column : str, optional
        Column name to use for weighting rows.
    weighted : bool, optional
        Whether to calculate weighted quantiles.
    adjust_weight_for_household_size : bool, optional
        Adjust weights for household size.
    equivalence_scale : _EquivalenceScale, optional
        Household equivalence scale to use.
    for_all : bool, optional
        Calculate quantiles across all rows.
    annual : bool, optional
        Annualize quantiles.
    groupby : str | list[str], optional
        Column(s) to group by.
    years : list[int], optional
        Years to include.

    Returns
    -------
    DataFrame
        Input table with added decile column.
    """
    parameters = __get_optional_params(locals())
    return calculate.add_decile(**parameters)


def add_percentile(
    table: pd.DataFrame | pd.Series | None = None,
    quantile_column_name: str | None = None,
    weight_column: str | None = None,
    on_variable: _QuantileBase | None = None,
    on_column: str | None = None,
    weighted: bool = True,
    adjust_weight_for_household_size: bool = False,
    equivalence_scale: _EquivalenceScale = "Household",
    for_all: bool = True,
    annual: bool = True,
    groupby: str | Iterable[str] | None = None,
    years: list[int] | None = None,
) -> pd.DataFrame:
    """Adds percentiles as a column to the input table.

    Parameters
    ----------
    table : DataFrame | Series, optional
        Table to add quantiles to.
    bins : int, optional
        Number of quantile bins to create.
    on_variable : _QuantileBase, optional
        Variable to calculate quantiles on.
    on_column : str, optional
        Column to calculate quantiles on.

    Other parameters
    ----------------
    quantile_column_name : str, optional
        Name for added quantile column.
    weight_column : str, optional
        Column name to use for weighting rows.
    weighted : bool, optional
        Whether to calculate weighted quantiles.
    adjust_weight_for_household_size : bool, optional
        Adjust weights for household size.
    equivalence_scale : _EquivalenceScale, optional
        Household equivalence scale to use.
    for_all : bool, optional
        Calculate quantiles across all rows.
    annual : bool, optional
        Annualize quantiles.
    groupby : str | list[str], optional
        Column(s) to group by.
    years : list[int], optional
        Years to include.

    Returns
    -------
    DataFrame
        Input table with added percentile column.
    """
    parameters = __get_optional_params(locals())
    return calculate.add_percentile(**parameters)
