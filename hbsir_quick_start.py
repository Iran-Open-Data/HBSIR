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
def _():
    import marimo as mo
    return (mo,)


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 📂 Loading Original Data

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
    hbsir.load_table("food", 1403)
    return


@app.cell(hide_code=True)
def _(available_tables, mo, year_callout):
    mo.md(rf"""
    **Try It Yourself**

    Edit the code in the next cell to explore different datasets:

    ```python
    # Try these examples:
    hbsir.load_table("cloth", 1400)
    hbsir.load_table("communication", 98)
    hbsir.load_table("employment_income", [99, 1400])
    hbsir.load_table("household_information", "1399-1401")
    ```

    ### List of Original Tables

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
        ### About Years Parameter

        The `years` parameter is flexible and accepts several formats:

        - **Single year**: `1400` (auto-detects calendar type)
        - **Two-digit year**: `98` (converts to 1398)
        - **List of years**: `[99, 1400]` (loads multiple years)
        - **Year range**: `"1399-1401"` (inclusive range)
        """),
        "info"
    )
    return (year_callout,)


@app.cell(hide_code=True)
def _(mo, processed_tables):
    mo.md(rf"""
    ## 🔧 Processed & Calculated Tables

    Beyond the original survey tables, HBSIR provides **processed tables** that combine, calculate, and enhance the data for analysis. These tables are created by the package schema and available via the same `load_table()` function.

    ### Most Useful Processed Tables

    {processed_tables}
    """)
    return


@app.cell
def _(hbsir):
    hbsir.load_table("Expenditures", 1403)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Try It Yourself**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    processed_tables = mo.accordion({
        "Expenditures": "Annualized expenditure data across all categories with normalized durations and prices",
        "Total_Expenditure": "Household-level total expenditure aggregates (both gross and net)",
        "Income_Breakdown": "Detailed breakdown of income by type (cash, non-cash, employment, etc.)",
        "Total_Income": "Household-level total income aggregates",
        "Imputed_Rent": "Calculated rental value for owner-occupied housing",
        "Equivalence_Scale": "Various equivalence scales for per-capita analysis (OECD, square root, etc.)",
        "Adult_Equivalent_Scale": "Nutrition-based adult equivalence scales",
        "CPI": "Consumer Price Index data for inflation adjustments"
    })
    return (processed_tables,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ⚖️ Adding Survey Weights

    Many analyses require using sampling weights to ensure your results are representative of the national population. The `add_weight()` function adds these weights to your dataset.
    """)
    return


@app.cell
def _(hbsir):
    total_expenditure = hbsir.load_table("Total_Expenditure", 1403)
    total_expenditure.head()
    return (total_expenditure,)


@app.cell
def _(hbsir, total_expenditure):
    total_expenditure_with_weight = hbsir.add_weight(total_expenditure)
    total_expenditure_with_weight.head()
    return


@app.cell
def _(hbsir):
    hbsir.load_table("Total_Expenditure", 1403).pipe(hbsir.add_weight)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🏷️ Adding Geographic Attributes

    The `add_attribute()` function enriches your data with geographic and demographic attributes like urban/rural status, province, and county information based on household IDs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Basic Usage

    Add attributes to any table that contains **year** and household IDs:

    ```python
    # Add urban/rural classification
    table = hbsir.add_attribute(table, "Urban_Rural")

    # Add province information
    table = hbsir.add_attribute(table, "Province")

    # Add county information (available from 1377)
    table = hbsir.add_attribute(table, "County")
    ```

    **Supported attributes:**
    - `"Urban_Rural"` - Urban or rural status
    - `"Province"` - Province name and code
    - `"County"` - County name and code (from 1377)
    """)
    return


@app.cell
def _(hbsir):
    # Example: Load data and add attributes
    households_attributes = hbsir.load_table("household_information", 1400)

    # Add urban/rural and province attributes
    households_attributes = hbsir.add_attribute(households_attributes, "Urban_Rural")
    households_attributes = hbsir.add_attribute(households_attributes, "Province")

    households_attributes.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Advanced Usage

    You can customize which aspects of the attribute to include:

    ```python
    # Get only Farsi names
    table = hbsir.add_attribute(
        table,
        "Province",
        aspects="farsi_name",
        column_names="Province_Farsi"
    )

    # Get both code and name
    table = hbsir.add_attribute(
        table,
        "Urban_Rural",
        aspects=["code", "name"]
    )
    ```

    **Available aspects:**
    - `"name"` - English name (default)
    - `"farsi_name"` - Persian name
    - `"code"` - Administrative code

    *These attributes are essential for geographic analysis and filtering data by region.*
    """)
    return


@app.cell
def _(hbsir):
    # Example: Load data and add attributes
    households_attributes_fa = hbsir.load_table("household_information", 1400)

    # Add urban/rural and province attributes
    households_attributes_fa = hbsir.add_attribute(households_attributes_fa, "Urban_Rural", aspects="farsi_name")
    households_attributes_fa = hbsir.add_attribute(households_attributes_fa, "Province", aspects="farsi_name")

    households_attributes_fa.head()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🏷️ Adding Classification Labels

    The `add_classification()` function decodes commodity, industry, and occupation codes into meaningful descriptive categories.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Basic Usage

    Automatically classify commodity codes in expenditure data:

    ```python
    # Add classification to expenditure data
    table = hbsir.add_classification(table)

    # Classify at specific hierarchy levels
    table = hbsir.add_classification(
        table,
        levels=2,
        column_names="Category"
    )
    ```
    """)
    return


@app.cell
def _(hbsir):
    # Example: Classify expenditure data
    expenditures = hbsir.load_table("Expenditures", 1400)

    # Add classification at level 2
    classified_data = hbsir.add_classification(
        expenditures, levels=2, column_names="Category"
    )

    classified_data.head()
    return (expenditures,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Advanced Classification

    ```python
    # Classify specific target columns
    table = hbsir.add_classification(
        table,
        target="Commodity_Code",
        name="original",
        levels=[1, 2, 3],
        aspects=["label", "farsi_name"],
    )

    # Classify occupation data
    employment_data = hbsir.load_table("employment_income", 1400)
    classified_employment = hbsir.add_classification(
        employment_data,
        target="Occupation_Code",
    )
    ```

    **Key parameters:**
    - `target`: Column containing codes to classify (auto-detected if not specified)
    - `levels`: Hierarchy levels (1-4 for COICOP)
    - `aspects`: Types of labels ("label", "farsi_label")
    - `name`: Classification system ("original", "Food_NonFood", "Durability")

    *Classification makes coded data human-readable and enables category-based analysis.*
    """)
    return


@app.cell
def _(expenditures, hbsir):
    hbsir.add_classification(expenditures, name="Durability").head()
    return


@app.cell
def _(hbsir):
    employment_data = hbsir.load_table("employment_income", 1400)
    classified_employment = hbsir.add_classification(
        employment_data,
        target="Industry_Code",
        levels=[1, 2, 3, 4],
    )
    classified_employment.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Quick Start Complete!

    You've learned the essential HBSIR functions:

    - **`load_table()`** - Load original and processed data
    - **`add_weight()`** - Add sampling weights
    - **`add_attribute()`** - Add geographic and demographic attributes
    - **`add_classification()`** - Decode commodity and occupation codes
    - **Flexible year formats** - Single years, lists, and ranges

    ### Next Steps

    - [Explore the full documentation](https://iran-open-data.github.io/HBSIR/)
    - [Check out tutorial example](https://iran-open-data.github.io/HBSIR/tutorials/tehran_rents/)
    - [Browse available tables](https://iran-open-data.github.io/HBSIR/tables/)

    Happy analyzing! 📊
    """)
    return


if __name__ == "__main__":
    app.run()
