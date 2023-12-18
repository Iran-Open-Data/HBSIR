from typing import Literal

import pandas as pd

from ...api import api
from ...calculate import calculate

from .common import filter_urban_rural


def create_table_for_a_year(
    year: int, urban_rural: Literal["urban", "rural", "both"]
) -> pd.DataFrame:
    members = (
        api.load_table("Number_of_Members", years=year)
        .set_index(["Year", "ID"])
        .loc[:, "Members"]
        .rename("Value")
    )

    table = pd.concat(
        [
            members,
            calculate.quantile(
                years=[year],
                on_variable="Net_Expenditure",
                groupby=["Urban_Rural"],
                bins=10,
                quantile_column_name="Decile",
            ),
            api.load_table("Weight", years=year).set_index(["Year", "ID"])["Weight"],
        ],
        axis="columns",
    )
    table = filter_urban_rural(table, urban_rural)

    total = calculate.weighted_average(table, columns=["Value"]).iloc[0]

    average_number_of_members = (
        table.groupby("Decile", observed=True)
        .apply(calculate.weighted_average, columns=["Value"])
        .rename(columns={"Value": "Average"})
    )
    average_number_of_members.loc["Total"] = total

    table["Value"] = table["Value"].clip(0, 10)
    weight_table = (
        table.groupby(["Value", "Decile"], observed=True)["Weight"].sum().unstack()
    )
    index_weight_sum = weight_table.sum(axis="index")
    columns_weight_sum = weight_table.sum(axis="columns")
    col_sum = columns_weight_sum.div(columns_weight_sum.sum()).mul(100).rename("Total")
    main_table = weight_table.div(index_weight_sum).mul(100)
    main_table = pd.concat([col_sum, main_table], axis="columns")

    average_number_of_members = average_number_of_members.T[main_table.columns]

    main_table = pd.concat(
        [
            average_number_of_members,
            main_table.sum().to_frame("Total").T,
            main_table,
        ]
    )

    main_table = main_table.fillna(0)
    main_table.index = main_table.index.astype(str)
    main_table.columns = main_table.columns.astype(str)

    return main_table


def main(years: list[int], urban_rural: Literal["urban", "rural"]):
    if len(years) == 1:
        return create_table_for_a_year(years[0], urban_rural)
    raise ValueError
