import pandas as pd

from ..api import api


def create_calorie_requirement_table() -> pd.DataFrame:
    internal_data_path = api.defaults.package_dir / "internal_data"
    calorie_requirements = pd.read_csv(
        internal_data_path / "nnftri_calorie_requirements.csv"
    )
    return (
        calorie_requirements
        .loc[lambda df: df["Age_Interval"].ne("Average")]
        .loc[lambda df: df["Sex"].ne("Average")]
        .pipe(
            lambda df: df.join(
                df["Age_Interval"]
                .str.split("-", expand=True)
                .set_axis(["min_age", "max_age"], axis="columns")
                .astype(int)
            )
        )
        .loc[lambda df: df.index.repeat(df["max_age"].sub(df["min_age"]).add(1))]
        .reset_index()
        .assign(
            cumcount=lambda df:
            df.groupby(["Age_Interval", "Sex"])["Calorie_Requirement"].cumcount(),
            Age=lambda df: df["min_age"].add(df["cumcount"]),
        )
        .set_index(["Age", "Sex"])
        .loc[:, ["Calorie_Requirement"]]
    )


def calorie_based_equivalence_scale(table: pd.DataFrame) -> pd.DataFrame:
    internal_data_path = api.defaults.package_dir / "internal_data"
    calorie_requirements = pd.read_csv(
        internal_data_path / "nnftri_calorie_requirements.csv"
    )
    average_calorie_requirement = (
        calorie_requirements
        .loc[lambda df: df["Age_Interval"].eq("Average")]
        .loc[lambda df: df["Sex"].eq("Average")]
        .loc[:, "Calorie_Requirement"]
        .iloc[0]
    )

    return (
        table
        .join(create_calorie_requirement_table(), on=["Age", "Sex"])
        .groupby(["Year", "ID"])[["Calorie_Requirement"]].sum()
        .div(average_calorie_requirement)
        .rename(columns={"Calorie_Requirement": "Adult_Equivalent_Scale_NNFTRI"})
        .reset_index()
    )
