from typing import Literal

import pandas as pd

from ...api import api
from .common import create_expenditure_tiers, filter_urban_rural


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
            create_expenditure_tiers(urban_rural=urban_rural, year=year),
            api.load_table("Weight", years=year).set_index(["Year", "ID"])["Weight"],
        ],
        axis="columns",
    )
    table = filter_urban_rural(table, urban_rural)

    total = api.calculate.weighted_average(table, columns=["Value"]).iloc[0]

    average_number_of_members = (
        table.groupby("Expenditure_Tier", observed=True)
        .apply(api.calculate.weighted_average, columns=["Value"])
        .rename(columns={"Value": "Average"})
    )
    average_number_of_members.loc["Total"] = total

    table["Value"] = table["Value"].clip(0, 10)
    weight_table = (
        table.groupby(["Value", "Expenditure_Tier"], observed=True)["Weight"]
        .sum()
        .unstack()
    )
    index_weight_sum = weight_table.sum(axis="index")
    index_sum = index_weight_sum.div(index_weight_sum.sum()).mul(100)
    index_sum.loc["Total"] = index_sum.sum()
    index_sum = index_sum.to_frame("Household_Percentage")
    columns_weight_sum = weight_table.sum(axis="columns")
    col_sum = columns_weight_sum.div(columns_weight_sum.sum()).mul(100).rename("Total")
    main_table = weight_table.div(index_weight_sum).mul(100)
    main_table = pd.concat([col_sum, main_table], axis="columns")

    average_number_of_members = average_number_of_members.T[main_table.columns]
    index_sum = index_sum.T[main_table.columns]

    main_table = pd.concat(
        [
            index_sum,
            average_number_of_members,
            main_table.sum().to_frame("Total").T,
            main_table,
        ]
    )

    main_table = main_table.fillna(0)
    main_table.index = main_table.index.astype(str)

    return main_table


def main(years: list[int], urban_rural: Literal["urban", "rural", "both"] = "both"):
    if len(years) == 1:
        return create_table_for_a_year(years[0], urban_rural)
    raise ValueError
