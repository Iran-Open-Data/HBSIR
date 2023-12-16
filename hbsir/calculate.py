"""
This module contains functions for calculating various metrics.
"""
# pylint: disable=too-many-arguments
# pylint: disable=unused-argument
# pylint: disable=too-many-locals

from typing import Iterable

import pandas as pd

from bssir.calculator.quantile import _EquivalenceScale, _QuantileBase

from .api import api


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
    return api.calculate.weighted_average(**parameters)


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
    return api.calculate.average_table(**parameters)


def quantile(
    table: pd.DataFrame | pd.Series | None = None,
    quantile_column_name: str = "Quantile",
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
    parameters = __get_optional_params(locals())
    return api.calculate.quantile(**parameters)


def add_decile(
    table: pd.DataFrame | pd.Series | None = None,
    quantile_column_name: str = "Quantile",
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
    parameters = __get_optional_params(locals())
    return api.calculate.add_decile(**parameters)
