from pathlib import Path
import io
from typing import Literal, Optional
from zipfile import ZipFile, ZIP_LZMA

import pandas as pd
from pandas.io.formats.style import Styler
import yaml

import hbsir


def create_household_information_part(year: int) -> pd.DataFrame:
    return (
        hbsir.load_table("household_information", years=year)
        .assign(Season_Number=lambda df: df["Season"].cat.codes.add(1))
        .pipe(
            hbsir.add_attribute,
            name="Urban_Rural",
            aspects=["code", "name"],
            column_names=["Urban_Rural_Code", "Urban_Rural"],
        )
        .assign(Urban_Rural_Code=lambda s: s["Urban_Rural_Code"].astype(str))
        .pipe(
            hbsir.add_attribute,
            name="Province",
            aspects=["code", "name"],
            column_names=["Province_Code", "Province"],
        )
        .assign(Province_Code=lambda s: s["Province_Code"].astype(str).str.pad(2, "left", "0"))
        .pipe(
            hbsir.add_attribute,
            name="County",
            aspects=["code", "name"],
            column_names=["County_Code", "County"],
        )
        .assign(County_Code=lambda s: s["County_Code"].astype(str).str.pad(4, "left", "0"))
        .set_index(["Year", "ID"])
        .loc[
            :,
            [
                "Season_Number",
                "Season",
                "Urban_Rural_Code",
                "Urban_Rural",
                "Province_Code",
                "Province",
                "County_Code",
                "County",
                "Weight",
            ]
        ]
    )

def fillna_with_false(df: pd.DataFrame) -> pd.DataFrame:
    df.loc[:, "Car":"Sewerage"] = df.loc[:, "Car":"Sewerage"].fillna(False)
    return df

def create_house_specifications_table(year: int) -> pd.DataFrame:
    return (
        hbsir.load_table("house_specifications", years=year)
        .pipe(fillna_with_false)
        .set_index(["Year", "ID"])
        .assign(
            Structure_Type = lambda df:
            df["Structure_Type"]
            .astype(str)
            .where(df["Structure_Type"].ne("Other"), df["Structure_Main_Materials"])
            .astype("category")
        )
        .assign(TV=lambda df: df["Black_and_White_TV"] | df["Color_TV"])
        .loc[
            :,
            [
                # "Dwelling_Type",
                "Tenure",
                "Structure_Type",
                "House_Area",
                "Number_of_Rooms",
                "Bathroom",
                "Kitchen",
                "Car",
                "Motorcycle",
                "TV",
                "PC",
                "Internet",
                "Phone",
                "Cellphone",
                "Refrigerator",
                "Freezer",
                "Freezer_Refrigerator",
                "Oven",
                "Vacuum_Cleaner",
                "Washing_Machine",
                "Sewing_Machine",
                "Dishwasher",
                "Microwave_Oven",
                "Pipe_Water",
                "Electricity",
                "Natural_Gas",
                "Sewerage",
                "AC",
                "Central_AC",
                "Water_Heater",
                "Central_Heating",
                "Split_AC",
                "Cooking_Fuel",
                "Heating_Fuel",
                "Hotwater_Fuel",
            ]
        ]
    )

def create_demographics_table(year: int) -> pd.DataFrame:
    return (
        hbsir.load_table("members_properties", years=year)
        .groupby(["Year", "ID"])
        .aggregate(
            Family_Size = pd.NamedAgg("Member_Number", "count"),
            Number_of_Spouses = pd.NamedAgg("Relationship", lambda s: s.eq("Spouse").sum()),
            Number_of_Childs = pd.NamedAgg("Relationship", lambda s: s.eq("Child").sum()),
            Number_of_Active_Members = pd.NamedAgg("Activity_Status", lambda s: s.eq("Employed").sum()),
            Number_of_Literate_Members = pd.NamedAgg("Is_Literate", "sum"),
            Number_of_Students = pd.NamedAgg("Is_Student", "sum"),
        )
    )

def create_equivalence_scale(year: int) -> pd.DataFrame:
    return (
        hbsir.load_table("Equivalence_Scale", years=year)
        .set_index(["Year", "ID"])
        .loc[:, ["OECD", "OECD_Modified", "Square_Root"]]
        .rename(columns=lambda n: f"{n}_Equivalence_Scale")
    )


def create_member_property(year: int, relationship: Literal["Head", "Spouse"] = "Head") -> pd.DataFrame:
    return (
        hbsir.load_table("members_properties", years=year)
        .loc[lambda df: df["Relationship"].eq(relationship)]
        .sort_values("Age")
        .drop_duplicates("ID", keep="last")
        .set_index(["Year", "ID"])
        .loc[
            :,
            [
                "Sex",
                "Age",
                "Is_Literate",
                "Is_Student",
                "Education_Level",
                "Marital_Status",
                "Activity_Status"
            ]
        ]
        .rename(columns=lambda n: f"{relationship}_{n}")
    )


def create_expenditure_totals(year: int) -> pd.DataFrame:
    return (
        hbsir.load_table("Expenditures", years=year)
        .groupby(["Year", "ID"])[["Net_Expenditure", "Gross_Expenditure"]].sum()
    )


def create_expenditure_level_1(year: int) -> pd.DataFrame:
    return (
        hbsir.load_table("Expenditures", years=year)
        .pipe(hbsir.add_classification, aspects=["name"], levels=[1], column_names=["COICOP_L1"])
        .dropna(subset="COICOP_L1")
        .groupby(["Year", "ID", "COICOP_L1"])["Gross_Expenditure"].sum()
        .unstack(-1, 0)
    )


def create_food_expenditure_level_3(year: int) -> pd.DataFrame:
    return (
        hbsir.load_table("Expenditures", years=year)
        .loc[lambda df: df["Table_Name"].eq("food")]
        .pipe(hbsir.add_classification, aspects=["name"], levels=[3], column_names=["COICOP_L3"])
        .dropna(subset="COICOP_L3")
        .groupby(["Year", "ID", "COICOP_L3"])["Gross_Expenditure"].sum()
        .unstack(-1, 0)
    )


def create_income_table(year: int) -> pd.DataFrame:
    return (
        hbsir.load_table("Income_Breakdown", years=year)
        .pivot(index=["Year", "ID"], columns="Income_Type", values="Income")
        .fillna(0)
    )

def create_level3_aggs(table: pd.DataFrame) -> pd.DataFrame:
    return (
        table
        .assign(
            Cash_Employment_Income=lambda df: df[[
                "Cash_Cooperative", "Cash_Private", "Cash_Public",
            ]].sum(axis="columns"),
            NonCash_Employment_Income=lambda df: df[[
                "NonCash_Cooperative", "NonCash_Private", "NonCash_Public",
            ]].sum(axis="columns"),

            **{
                "Cash_Self-Employed_Income": lambda df: df[[
                    "Cash_Agricultural", "Cash_NonAgricultural", "Cash_Home_Production",
                ]].sum(axis="columns"),
                "NonCash_Self-Employed_Income": lambda df: df[[
                    "NonCash_Agricultural", "NonCash_NonAgricultural", "NonCash_HomeProduction"
                ]].sum(axis="columns"),
            },

            NonCash_ImputedRent = lambda df: df[[
                "NonCash_ImputedRent_Mortgage", "NonCash_ImputedRent_Ownership"
            ]].sum(axis="columns"),

            Cash_Aid_and_Transfer=lambda df: df[[
                "Cash_Aid", "Cash_Subsidy", "Cash_Transfer",
            ]].sum(axis="columns"),
            NonCash_Aid_and_Transfer=lambda df: df[[
                "NonCash_Donation",
            ]].sum(axis="columns"),

            Cash_Other_Passive_Income=lambda df: df[[
                "Cash_Interest", "Cash_Retirement",
            ]].sum(axis="columns"),
        )
        .loc[
            :,
            [
                "Cash_Employment_Income",
                "NonCash_Employment_Income",
                "Cash_Self-Employed_Income",
                "NonCash_Self-Employed_Income",
                "Cash_Rent",
                "NonCash_ImputedRent",
                "Cash_Aid_and_Transfer",
                "NonCash_Aid_and_Transfer",
                "Cash_Other_Passive_Income",
            ]
        ]
    )

def create_level2_aggs(table: pd.DataFrame) -> pd.DataFrame:
    return (
        table
        .assign(
            Employment_Income=lambda df: df[[
                "Cash_Employment_Income", "NonCash_Employment_Income"
            ]].sum(axis="columns"),

            **{
                "Self-Employed_Income": lambda df: df[[
                    "Cash_Self-Employed_Income", "NonCash_Self-Employed_Income",
                ]].sum(axis="columns"),
            },

            Rent = lambda df: df[[
                "NonCash_ImputedRent", "Cash_Rent"
            ]].sum(axis="columns"),

            Aid_and_Transfer=lambda df: df[[
                "Cash_Aid_and_Transfer", "NonCash_Aid_and_Transfer",
            ]].sum(axis="columns"),

            Other_Passive_Income=lambda df: df[[
                "Cash_Other_Passive_Income",
            ]].sum(axis="columns"),
        )
        .loc[
            :,
            [
                "Employment_Income",
                "Self-Employed_Income",
                "Rent",
                "Aid_and_Transfer",
                "Other_Passive_Income",
            ]
        ]
    )

def create_level1_aggs(table: pd.DataFrame) -> pd.DataFrame:
    return (
        table
        .assign(
            Active_Income = lambda df: df[[
                "Employment_Income", "Self-Employed_Income"
            ]].sum(axis="columns"),
            Passive_Income = lambda df: df[[
                "Aid_and_Transfer", "Rent", "Other_Passive_Income"
            ]].sum(axis="columns"),
            Income = lambda df: df[["Active_Income", "Passive_Income"]].sum(axis="columns"),
        )
        .loc[
            :,
            [
                "Active_Income",
                "Passive_Income",
                "Income",
            ]
        ]
    )


def create_tables(year: int) -> list[pd.DataFrame]:
    income_table = create_income_table(year)
    income_level3_aggs = create_level3_aggs(income_table)
    income_level2_aggs = create_level2_aggs(income_level3_aggs)
    income_level1_aggs = create_level1_aggs(income_level2_aggs)

    tables = [
        create_household_information_part(year),
        create_house_specifications_table(year),
        create_demographics_table(year),
        create_equivalence_scale(year),
        create_member_property(year, "Head"),
        create_member_property(year, "Spouse"),
        create_expenditure_totals(year),
        create_expenditure_level_1(year),
        create_food_expenditure_level_3(year),
        income_table.drop(columns="Cash_Rent"),
        income_level3_aggs,
        income_level2_aggs,
        income_level1_aggs,
    ]
    return tables


def create_summary_table(tables: list[pd.DataFrame], columns: Optional[list[str]] = None) -> pd.DataFrame:
    summary_table = (
        pd.concat(tables, axis="columns", join="outer")
        .sort_index()
        .reset_index()
    )
    if columns is not None:
        summary_table = summary_table.loc[:, columns]
    return summary_table


def create_styled_table(tables: list[pd.DataFrame], columns: Optional[list[str]] = None) -> Styler:
    styled_df = (
        create_summary_table(tables, columns)
        .style

        .set_properties(
            ["Year", "ID"],
            **{
                "background-color": "#D9D9D9",
                "border": "2px solid #A6A6A6",
                "font-weight": "bold",
            }
        )
        .set_properties(
            tables[0].columns,
            **{
                "background-color": "#DAEEF3",
                "border": "1px solid #92CDDC",
            }
        )
        .set_properties(
            tables[1].columns,
            **{
                "background-color": "#DDD9C4",
                "border": "1px solid #948A54",
            }
        )
        .set_properties(
            tables[2].columns,
            **{
                "background-color": "#DCE6F1",
                "border": "1px solid #95B3D7",
            }
        )
        .set_properties(
            tables[3].columns,
            **{
                "background-color": "#B8CCE4",
                "border": "1px solid #95B3D7",
            }
        )
        .set_properties(
            tables[4].columns,
            **{
                "background-color": "#DCE6F1",
                "border": "1px solid #95B3D7",
            }
        )
        .set_properties(
            tables[5].columns,
            **{
                "background-color": "#B8CCE4",
                "border": "1px solid #95B3D7",
            }
        )
        .set_properties(
            tables[6].columns,
            **{
                "background-color": "#DA9694",
                "border": "1px solid #632523",
            }
        )
        .set_properties(
            tables[7].columns,
            **{
                "background-color": "#E6B8B7",
                "border": "1px solid #963634",
            }
        )
        .set_properties(
            tables[8].columns,
            **{
                "background-color": "#F2DCDB",
                "border": "1px solid #DA9694",
            }
        )
        .set_properties(
            tables[9].columns,
            **{
                "background-color": "#EBF1DE",
                "border": "1px solid #C4D79B",
            }
        )
        .set_properties(
            tables[10].columns,
            **{
                "background-color": "#D8E4BC",
                "border": "1px solid #A4C163",
            }
        )
        .set_properties(
            tables[11].columns,
            **{
                "background-color": "#C4D79B",
                "border": "1px solid #76933C",
            }
        )
        .set_properties(
            tables[12].columns,
            **{
                "background-color": "#A4C163",
                "border": "1px solid #4F6228",
            }
        )
    )

    return styled_df


def create_styled_metadata(tables: list[pd.DataFrame], metadata: pd.DataFrame) -> Styler:
    styled_df = (
        metadata.style
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(["Year", "ID"]), :], # type: ignore
            **{
                "background-color": "#D9D9D9",
                "border": "2px solid #A6A6A6",
                "font-weight": "bold",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[0].columns), slice(None)], # type: ignore
            **{
                "background-color": "#DAEEF3",
                "border": "1px solid #92CDDC",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[1].columns), slice(None)], # type: ignore
            **{
                "background-color": "#DDD9C4",
                "border": "1px solid #948A54",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[2].columns), slice(None)], # type: ignore
            **{
                "background-color": "#DCE6F1",
                "border": "1px solid #95B3D7",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[3].columns), slice(None)], # type: ignore
            **{
                "background-color": "#B8CCE4",
                "border": "1px solid #95B3D7",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[4].columns), slice(None)], # type: ignore
            **{
                "background-color": "#DCE6F1",
                "border": "1px solid #95B3D7",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[5].columns), slice(None)], # type: ignore
            **{
                "background-color": "#B8CCE4",
                "border": "1px solid #95B3D7",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[6].columns), slice(None)], # type: ignore
            **{
                "background-color": "#DA9694",
                "border": "1px solid #632523",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[7].columns), slice(None)], # type: ignore
            **{
                "background-color": "#E6B8B7",
                "border": "1px solid #963634",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[8].columns), slice(None)], # type: ignore
            **{
                "background-color": "#F2DCDB",
                "border": "1px solid #DA9694",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[9].columns), slice(None)], # type: ignore
            **{
                "background-color": "#EBF1DE",
                "border": "1px solid #C4D79B",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[10].columns), slice(None)], # type: ignore
            **{
                "background-color": "#D8E4BC",
                "border": "1px solid #A4C163",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[11].columns), slice(None)], # type: ignore
            **{
                "background-color": "#C4D79B",
                "border": "1px solid #76933C",
            }
        )
        .set_properties(
            pd.IndexSlice[metadata["Name"].isin(tables[12].columns), slice(None)], # type: ignore
            **{
                "background-color": "#A4C163",
                "border": "1px solid #4F6228",
            }
        )
    )

    return styled_df


def write_excel(year: int) -> None:
    with open(Path(__file__).parent.joinpath("v0_metadata.yaml"), encoding="utf8") as file:
        metadata = yaml.safe_load(file)
    metadata_table = pd.DataFrame(metadata["columns"])
    columns = [item["Name"] for item in metadata["columns"]]
    tables = create_tables(year)
    for table in tables:
        table.columns = table.columns.map(lambda n: n.replace("_", " "))
    styled_data = create_styled_table(tables, columns=columns)
    styled_metadata = create_styled_metadata(tables, metadata_table)
    with pd.ExcelWriter(f"Minute_Summary_{year}_V.0.1.xlsx") as excel_writer:
        styled_data.to_excel(
            excel_writer,
            sheet_name="Data",
            merge_cells=False,
            index=False,
            freeze_panes=(1, 2)
        )
        styled_metadata.to_excel(
            excel_writer,
            sheet_name="Metadata",
            index=False,
            freeze_panes=(1, 0)
        )


def write_csv(year: int) -> None:
    with open(Path(__file__).parent.joinpath("v0_metadata.yaml"), encoding="utf8") as file:
        metadata = yaml.safe_load(file)
    metadata_table = pd.DataFrame(metadata["columns"])
    tables = create_tables(year)
    summary_table = create_summary_table(tables)
    metadata_buffer = io.BytesIO()
    metadata_table.to_csv(metadata_buffer, index=False)
    data_buffer = io.BytesIO()
    summary_table.to_csv(data_buffer, index=False)
    with ZipFile(
        f"Minute_Summary_{year}_V.0.1.zip",
        mode="w",
        compression=ZIP_LZMA,
    ) as zip_file:
        zip_file.writestr("Metadata.csv", metadata_buffer.getvalue())
        zip_file.writestr("Data.csv", data_buffer.getvalue())
