from typing import Literal

import pandas as pd

from ...api import api

from .common import create_expenditure_tiers, filter_urban_rural

INDEX = [
    "Total",
    "Agriculture, forestry and fishing",  #
    "Mining and quarrying",
    "Manufacturing",
    "Electricity, gas, steam and air conditioning supply",
    "Construction",
    "Wholesale and retail trade; repair of motor vehicles and motorcycles",
    "Accommodation and food service activities",
    "Transportation and storage",
    "Information and communication",
    "Financial and insurance activities",
    "Real estate activities",
    "Public administration and defence; compulsory social security",
    "Education",
    "Human health and social work activities",
    "Other service activities",
    "Administrative and support service activities",
    "Arts, entertainment and recreation",
    "Professional, scientific and technical activities",
    "Water supply; sewerage, waste management and remediation activities",
    (
        "Activities of households as employers; undifferentiated goods- "
        "and services-producing activities of households for own use"
    ),
    "Unemployed",
]


def create_table_for_a_year(
    year: int, urban_rural: Literal["urban", "rural"]
) -> pd.DataFrame:
    activity_state = (
        api.load_table("members_properties", years=1401)
        .set_index(["Year", "ID", "Member_Number"])
        .loc[lambda df: df["Relationship"] == "Head", ["Activity_State"]]
    )

    income_table = pd.concat(
        [
            api.load_table("employment_income", years=year),
            api.load_table("self_employed_income", years=year),
        ],
        ignore_index=True,
    )
    industry = (
        income_table.drop_duplicates(["ID", "Member_Number"], keep="first")
        .pipe(api.add_classification, target="Industry_Code", aspects="title")
        .set_index(["Year", "ID", "Member_Number"])
        .loc[:, ["Industry"]]
    )

    industry = activity_state.join(industry, how="left").droplevel(-1)
    filt = industry["Activity_State"] != "Employed"
    industry.loc[filt, "Industry"] = "Unemployed"
    filt = industry["Industry"].isna() & (industry["Activity_State"] == "Employed")
    industry.loc[filt, "Industry"] = "Unknown or Other"

    industry = industry["Industry"]

    table = pd.concat(
        [
            industry,
            create_expenditure_tiers(urban_rural=urban_rural, year=year),
            api.load_table("Weight", years=year).set_index(["Year", "ID"])["Weight"],
        ],
        axis="columns",
    )

    table = filter_urban_rural(table, urban_rural)

    weight_table = (
        table.groupby(["Industry", "Expenditure_Tier"], observed=True)["Weight"]
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
    main_table = main_table.loc[INDEX]
    return main_table


def main(years: list[int], urban_rural: Literal["urban", "rural"] = "urban"):
    if len(years) == 1:
        return create_table_for_a_year(years[0], urban_rural)
    raise ValueError
