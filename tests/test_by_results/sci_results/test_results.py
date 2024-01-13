from pathlib import Path

import pandas as pd

import hbsir


RATIO_ERROR = 1
VALUE_ERROR = 0.25

CSV_DIR = Path(__file__).parent.joinpath("csv")


def _eq_tables(
    first: pd.DataFrame,
    second: pd.DataFrame,
    ratio_error: float = RATIO_ERROR,
    value_error: float = VALUE_ERROR,
) -> None:
    value_df = first.sub(second).abs().sub(value_error).ge(0)
    ratio_df = first.sub(second).abs().div(first).mul(100).ge(ratio_error)
    assert first.index.equals(second.index)
    assert first.columns.equals(second.columns)
    assert (value_df & ratio_df).sum().sum() == 0


def _execute_tests(table: str, year: int) -> None:
    for urban_rural in (
        "urban",
        "rural",
    ):
        abr = "U" if urban_rural == "urban" else "R"
        original = pd.read_csv(
            CSV_DIR.joinpath(f"{year}{abr}_{table}.csv"), index_col=0
        )
        created = hbsir.load_knowledge(
            f"sci_results.{table}", year, urban_rural=urban_rural
        )
        _eq_tables(original, created)


def test_T101():
    table = "T101"
    years = [1389, 1401]
    for year in years:
        _execute_tests(table=table, year=year)


def test_T102():
    table = "T102"
    years = [1401]
    for year in years:
        _execute_tests(table=table, year=year)


def test_T103():
    table = "T103"
    years = [1401]
    for year in years:
        _execute_tests(table=table, year=year)


def test_T104():
    table = "T104"
    years = [1401]
    for year in years:
        _execute_tests(table=table, year=year)


def test_T105():
    table = "T105"
    years = [1401]
    for year in years:
        _execute_tests(table=table, year=year)


def test_T116():
    table = "T116"
    years = [1401]
    for year in years:
        _execute_tests(table=table, year=year)
