"""Common functions for all tables"""

import pandas as pd
import numpy as np

from ...api import api

CUT_BINS = {
    "urban": {
        1389: [-np.inf, 12, 16.5, 19.5, 24, 30, 45, 60, 75, 90, np.inf],
        1401: [-np.inf, 120, 195, 270, 360, 480, 600, 720, 900, 1200, np.inf],
    },
    "rural": {
        1389: [-np.inf, 7.2, 9, 12, 16.5, 19.5, 24, 30, 45, 60, np.inf],
        1401: [-np.inf, 75, 120, 195, 270, 360, 480, 600, 720, 900, np.inf],
    },
}


def create_expenditure_tiers(*, urban_rural: str, year: int):
    """Create expenditure tiers"""
    urban_rural = urban_rural.lower()
    bins = CUT_BINS[urban_rural][year]
    return pd.cut(
        api.load_table("Total_Expenditure", years=year)
        .set_index(["Year", "ID"])
        .loc[:, "Net_Expenditure"]
        .div(1e6),
        bins=bins,
        labels=(
            [f"<{bins[1]}"]
            + [f"{lower}-{higher}" for lower, higher in zip(bins[1:-2], bins[2:-1])]
            + [f"{bins[-2]}<"]
        ),
    ).rename("Expenditure_Tier")


def filter_urban_rural(table: pd.DataFrame, urban_rural: str) -> pd.DataFrame:
    """Filter to urban or rural"""
    urban_rural = urban_rural.lower()
    if urban_rural == "urban":
        table = (
            table.pipe(api.add_attribute, name="Urban_Rural")
            .loc[lambda df: df["Urban_Rural"] == "Urban"]
            .drop(columns="Urban_Rural")
        )
    elif urban_rural == "rural":
        table = (
            table.pipe(api.add_attribute, name="Urban_Rural")
            .loc[lambda df: df["Urban_Rural"] == "Rural"]
            .drop(columns="Urban_Rural")
        )
    return table
