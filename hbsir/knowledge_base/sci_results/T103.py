from typing import Literal

import pandas as pd

from ...api import api
from .common import create_expenditure_tiers, filter_urban_rural


def create_table_for_a_year(
    year: int, urban_rural: Literal["urban", "rural"]
) -> pd.DataFrame:
    literate_members = (
        api.load_table("members_properties", years=year)
        .assign(Employed=lambda df: df["Activity_State"] == "Employed")
        .groupby(["Year", "ID"])["Employed"]
        .sum()
        .rename("Value")
    )

    have_income_members = (
        api.load_table("Members_Total_Income", years=year)
        .groupby(["Year", "ID"])["Member_Number"]
        .count()
        .rename("Have_Income")
    )

    members = (
        api.load_table("Number_of_Members", years=year)
        .set_index(["Year", "ID"])
        .loc[:, "Members"]
    )

    table = pd.concat(
        [
            members,
            have_income_members,
            literate_members,
            create_expenditure_tiers(urban_rural=urban_rural, year=year),
            api.load_table("Weight", years=year).set_index(["Year", "ID"])["Weight"],
        ],
        axis="columns",
    )
    table = filter_urban_rural(table, urban_rural)

    total = api.calculate.weighted_average(
        table, columns=["Members", "Have_Income", "Value"]
    )

    average_number_of_members = (
        table.groupby("Expenditure_Tier", observed=True)
        .apply(
            api.calculate.weighted_average, columns=["Members", "Have_Income", "Value"]
        )
        .rename(
            columns={
                "Members": "Average_Members",
                "Have_Income": "Average_Have_Income",
                "Value": "Average_Employed",
            }
        )
    )
    average_number_of_members.loc["Total"] = total.to_list()

    table["Value"] = table["Value"].clip(0, 5)
    weight_table = (
        table.groupby(["Value", "Expenditure_Tier"], observed=True)["Weight"]
        .sum()
        .unstack()
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

    return main_table


def main(years: list[int], urban_rural: Literal["urban", "rural", "both"] = "both"):
    if len(years) == 1:
        return create_table_for_a_year(years[0], urban_rural)
    raise ValueError
