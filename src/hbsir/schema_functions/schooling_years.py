"""
Schooling Years Calculation Module

This module calculates schooling years based on education levels and age,
considering both the theoretical value of degrees and physical constraints.
It handles special cases like students, primary education, and accelerated learners.

Key Concepts:
- Degree_Worth_Years: Theoretical years the degree represents
- Max_Possible_Years: Maximum physically possible years given age (starting at 6)
- Schooling_Years: Main calculation considering student status
- Conservative_Schooling_Years: Age-constrained version for reality checks
"""

import pandas as pd
import numpy as np


# Education level to typical years mapping
# Represents the theoretical years of schooling each degree represents
EDUCATION_MAPPING = {
    "Primary": 6,  # 6 years of primary education
    "Lower_Secondary": 9,  # 3 years after primary (6+3=9)
    "Higher_Secondary": 12,  # 3 years after lower secondary (9+3=12)
    "Pre_University": 12,  # Same as high school completion
    "Short_Cycle_Tertiary": 14,  # 2 years after diploma (12+2=14)
    "Bachelors": 16,  # 4 years after diploma (12+4=16)
    "Masters": 18,  # 2 years after bachelor's (16+2=18)
    "Doctoral": 22,  # 4 years after master's (18+4=22)
    "Unofficial": 3,  # Non-formal education
}

# Starting age for formal education
MIN_AGE = 6


def calculate_schooling_years(table: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate schooling years considering education levels, age, and student status.

    Parameters:
    -----------
    table : pd.DataFrame
        Input dataframe containing:
        - Education_Level: Categorical education levels
        - Age: Integer age of individuals
        - Is_Student: Boolean indicating current student status
        - Year, ID, Member_Number: Identifying columns

    Returns:
    --------
    pd.DataFrame
        Dataframe with schooling years calculations and analysis flags
    """

    # Input validation
    required_columns = [
        "Year",
        "ID",
        "Member_Number",
        "Education_Level",
        "Age",
        "Is_Student",
    ]
    missing_columns = [col for col in required_columns if col not in table.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return (
        table
        # Calculate base metrics
        .assign(
            # Theoretical years the education level represents
            Degree_Worth_Years=lambda df: df["Education_Level"].map(EDUCATION_MAPPING),

            # Maximum physically possible years given age (starting at MIN_AGE)
            Max_Possible_Years=lambda df: (df["Age"] - MIN_AGE).clip(0),

            # Calculate schooling years with special cases
            Schooling_Years=lambda df: _calculate_main_schooling_years(df),

            # Analysis flags for data quality and acceleration
            Years_Accelerated=lambda df: 
            df["Schooling_Years"].sub(df["Max_Possible_Years"]).clip(0),
            Is_Accelerated=lambda df: df["Years_Accelerated"].gt(0),

            # Conservative estimate respecting age constraints
            Conservative_Schooling_Years=lambda df:
            df[["Schooling_Years", "Max_Possible_Years"]].min(axis=1),
        )
    )


def _calculate_main_schooling_years(df):
    """
    Internal function to calculate main schooling years based on education rules.

    Rules:
    - Students get one less year than their current level (haven't completed)
    - Primary non-students with limited age get age-based calculation (dropouts)
    - Other non-students get full degree worth years
    """
    return np.where(
        # Students: subtract 1 year since they haven't completed current level
        df["Is_Student"].eq(True),
        (df["Degree_Worth_Years"] - 1).clip(0, df["Max_Possible_Years"]),

        # Non-students
        np.where(
            # Primary non-students who are young: use age-based (likely dropouts)
            df["Education_Level"].eq("Primary")
            & df["Max_Possible_Years"].lt(EDUCATION_MAPPING["Primary"]),
            df["Max_Possible_Years"],

            # Other non-students: completed education, use degree worth
            df["Degree_Worth_Years"],
        ),
    )
