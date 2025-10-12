import pandas as pd
from pandas.api.types import CategoricalDtype


def number_of_members(table: pd.DataFrame) -> pd.DataFrame:
    return (
        table.assign(Adult=lambda df: df["Age"] >= 14)
        .groupby(["Year", "ID"], as_index=False)
        .agg(
            Members=pd.NamedAgg("Member_Number", "count"),
            Adults=pd.NamedAgg("Adult", "sum"),
        )
        .assign(Childs=lambda df: df["Members"] - df["Adults"])
    )


def equivalence_scale(table: pd.DataFrame) -> pd.DataFrame:
    return table.assign(
        Household=1,
        Per_Capita=table["Members"],
        Family_Size=table["Members"],
        OECD=table["Adults"].multiply(0.7).add(0.3).add(table["Childs"].multiply(0.5)),
        OECD_Modified=table["Adults"].multiply(0.5).add(0.5)
        .add(table["Childs"].multiply(0.3)),
        Square_Root=table["Members"].pow(1/2),
    )


def adjust_month(table: pd.DataFrame) -> pd.DataFrame:
    table["Month"] = table["Month"].replace({1: 13}).sub(1)
    return table


def create_season_number(table: pd.DataFrame) -> pd.DataFrame:
    table["Season_Number"] = table["Month"].sub(1).floordiv(3).add(1)
    return table


def season_name(table: pd.DataFrame) -> pd.DataFrame:
    table["Season"] = (
        table["Season_Number"]
        .astype(CategoricalDtype([1, 2, 3, 4], ordered=True))
        .cat.rename_categories({1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"})
    )
    return table


def calculate_amount_before_1382(table: pd.DataFrame) -> pd.DataFrame:
    if "Price" not in table.columns:
        table["Amount"] = table["Kilos"]
        return table
    table["Amount"] = (
        table["Kilos"]
        .mask(
            table["Kilos"].isna() & table["Price"].notna(),
            table["Expenditure"] / table["Price"],
        )
    )
    return table


def calculate_amount_after_1383(table: pd.DataFrame) -> pd.DataFrame:
    table["Amount"] = table["Kilos"].fillna(0) + table["Grams"].fillna(0).div(1_000)
    filt = table[["Grams", "Kilos"]].notna().max(axis="columns").eq(False)
    table.loc[filt, "Amount"] = None
    filt = table["Amount"].isna() & table["Price"].gt(0)
    table["Amount"] = table["Amount"].mask(filt, table["Expenditure"]/ table["Price"])
    return table
