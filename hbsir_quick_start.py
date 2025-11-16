# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "hbsir==0.6.5",
# ]
# ///

import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # HBSIR Quick Start Guide

    **Household Budget Survey for Iran**

    A quick preview of the `hbsir` Python package for accessing Iranian household economic data.
    """)
    return


@app.cell
def _():
    # Import and setup
    import hbsir

    # Configure for the environment (Colab for cloud environments)
    hbsir.setup_config("Colab")
    return (hbsir,)


@app.cell
def _(mo):
    mo.md(r"""
    ##  Basic Usage
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📂 Loading Data

    The main function to load data is `hbsir.load_table()`.

    **Parameters:**
    - `table_name`: Name of the table to load (e.g., "food", "employment_income", "Expenditures")
    - `years`: Iranian calendar year

    **Returns:** A pandas DataFrame with the requested data.

    *For complete API documentation, see the [load_table reference](https://iran-open-data.github.io/HBSIR/api/load_table/).*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Example: Load Food Data for 1400

    Try running the example below to see how it works:
    """)
    return


@app.cell
def _(hbsir):
    hbsir.load_table("communication", 98)
    return


@app.cell(hide_code=True)
def _(available_tables, mo, year_callout):
    mo.md(rf"""
    #### Try It Yourself

    Edit the code in the next cell to explore different datasets:

    ```python
    # Try these examples:
    hbsir.load_table("cloth", 1400)
    hbsir.load_table("communication", 98)
    hbsir.load_table("employment_income", [99, 1400])
    hbsir.load_table("household_information", "1399-1401")
    ```

    {available_tables}

    {year_callout}

    """)
    return


@app.cell(hide_code=True)
def _(mo):
    available_tables = mo.accordion(
        {
            "List of Original Tables:":
            """
            **General Tables:**
        
            - `household_information`
            - `members_properties`
            - `house_specifications`
        
            **Expenditure Tables:**
        
            - `food`
            - `tobacco`
            - `cloth`
            - `home`
            - `furniture`
            - `medical`
            - `transportation`
            - `communication`
            - `entertainment`
            - `hotel`
            - `other`
            - `durable`
            - `investment`
        
            **Income Tables:**
        
            - `employment_income`
            - `self_employed_income`
            - `other_income`
            - `subsidy`
            """
        }
    )
    return (available_tables,)


@app.cell(hide_code=True)
def _(mo):
    year_callout = mo.callout(
        mo.md("""
        The `years` parameter is flexible and accepts several formats:

        - **Single year**: `1400` (auto-detects calendar type)
        - **Two-digit year**: `98` (converts to 1398)
        - **List of years**: `[99, 1400]` (loads multiple years)
        - **Year range**: `"1399-1401"` (inclusive range)
        """),
        "info"
    )
    return (year_callout,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
