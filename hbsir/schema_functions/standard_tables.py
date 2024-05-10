import pandas as pd


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
        OECD=table["Adults"].multiply(0.7).add(0.3).add(table["Childs"].multiply(0.5)),
        OECD_Modified=table["Adults"]
        .multiply(0.5)
        .add(0.5)
        .add(table["Childs"].multiply(0.3)),
        Square_Root=table.eval("sqrt(Members)"),
    )


def create_season(table: pd.DataFrame) -> pd.DataFrame:
    seasons = {1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"}
    table["Season"] = pd.Series(
        data=pd.Categorical(
            table["Month"]
            .sub(1)
            .floordiv(3)
            .add(1)
            .astype("Int16")
            .map(seasons)
        ),
        index=table.index,
    )
    return table
