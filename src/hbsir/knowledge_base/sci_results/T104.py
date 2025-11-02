from typing import Literal

import pandas as pd

from ...api import api

from .common import create_expenditure_tiers, filter_urban_rural


def create_table_for_a_year(
    year: int, urban_rural: Literal["urban", "rural"]
) -> pd.DataFrame:
    head_state = (
        api.load_table("members_properties", years=1401)
        .set_index(["Year", "ID"])
        .loc[lambda df: df["Relationship"] == "Head", ["Activity_Status"]]
    )

    table = pd.concat(
        [
            head_state,
            create_expenditure_tiers(urban_rural=urban_rural, year=year),
            api.load_table("Weight", years=year).set_index(["Year", "ID"])["Weight"],
        ],
        axis="columns",
    )
    table = filter_urban_rural(table, urban_rural)

    weight_table = (
        table.groupby(["Activity_Status", "Expenditure_Tier"], observed=True)["Weight"]
        .sum()
        .unstack()
    )
    index_weight_sum = weight_table.sum(axis="index")
    columns_weight_sum = weight_table.sum(axis="columns")
    col_sum = columns_weight_sum.div(columns_weight_sum.sum()).mul(100).rename("Total")
    main_table = weight_table.div(index_weight_sum).mul(100)
    main_table = pd.concat([col_sum, main_table], axis="columns")
    main_table = pd.concat(
        [
            main_table.sum().to_frame("Total").T,
            main_table,
        ]
    )

    main_table = main_table.fillna(0)
    main_table.index = main_table.index.astype(str)
    return main_table


def main(years: list[int], urban_rural: Literal["urban", "rural"]):
    if len(years) == 1:
        return create_table_for_a_year(years[0], urban_rural)
    raise ValueError
