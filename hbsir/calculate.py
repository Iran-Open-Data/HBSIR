"""
This module contains functions for calculating various metrics.
"""

import pandas as pd

from .api import api


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
    api.calculate.weighted_average(
        table=table,
        weight_col=weight_col,
        columns=columns,
    )


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
    api.calculate.average_table(
        table=table,
        weight_col=weight_col,
        groupby=groupby,
        columns=columns,
    )
