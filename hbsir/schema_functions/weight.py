import pandas as pd

from ..api import api


def calculate_weight(table: pd.DataFrame) -> pd.DataFrame:
    years = table["Year"].unique()
    year = years[0]
    internal_data_path = api.defaults.package_dir / "internal_data"
    if year >= 1373:
        province_weights_path = internal_data_path / "province_weights_1373.csv"
    province_weights = pd.read_csv(province_weights_path, index_col=0)
    province_weight_share = province_weights.stack().rename("Weight_Share")

    if year > 1370:
        census_year = 1370
    census_household_count_path = internal_data_path / "census_household_count.csv"
    census_household_count = pd.read_csv(census_household_count_path)
    household_count = (
        census_household_count
        .loc[lambda df: df["Year"].eq(census_year), ["Urban", "Rural"]]
        .iloc[0]
        .rename("Household_Count")
    )

    return (
        table
        .pipe(api.add_attribute, name="Province", aspects="code")
        .pipe(api.add_attribute, name="Urban_Rural")
        .assign(
            Sample_Count=lambda df:
            df.groupby(["Province", "Urban_Rural"])["ID"].transform("count")
        )
        .join(province_weight_share, on=["Province", "Urban_Rural"])
        .join(household_count, on=["Urban_Rural"])
        .assign(
            Weight=lambda df:
            df["Household_Count"].div(df["Sample_Count"]).mul(df["Weight_Share"])
        )
        .loc[:, ["Year", "ID", "Weight"]]
    )
