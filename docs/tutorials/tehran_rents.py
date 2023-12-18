# # An Overview: Rental Expenditures in Tehran
#
# In this tutorial, we will analyze the residential rental expenses of
# Tehran residents step-by-step. The goal is to provide an overview of
# the top features of the hbsir package.
#
# We will get started right away by importing the necessary libraries!

import pandas as pd
import hbsir

# ## Loading Data
#
# In order to kick off our analysis, let's begin by loading the necessary data.
# While information about rent is available in the "home" table, for a more
# comprehensive overview, we'll load the "Expenditures" table for the year 1401,
# which includes all household expenditures.

table = hbsir.load_table("Expenditures", 1401)
table.head()

# > A comprehensive description of the structure and content of all
# > tables is available in the
# > [documentation](https://iran-open-data.github.io/HBSIR/tables/).

# ## Adding Household Attributes
#
# As we are interested in analyzing urban households, we'll filter the data
# to focus on this segment.
#
# First, we add the "Urban_Rural" attribute to the table.

table = hbsir.add_attribute(table, name="Urban_Rural")
table.head()

# We also need to add province information:

table = hbsir.add_attribute(table, name="Province")
table.head()

# Now that we have urban/rural and province data, we can filter the table
# to only include urban Tehran households:

filt = (table["Urban_Rural"] == "Urban") & (table["Province"] == "Tehran")
table = table.loc[filt]
table.head()

# ## Adding Classification
#
# In the Iran Household Budget Survey, various codes exist for commodities,
# occupations, industries, etc. Each code can be decoded in multiple ways.
# Rather than hardcoding the meanings of these codes, HBSIR provides a function
# to interpret them flexibly based on the user's needs.
#
# While delving into all the intricacies of this function is an advanced topic,
# basic usage is straightforward. For example:

hbsir.add_classification(table, name="Food_NonFood").head()

# In our case, we need the _original_ Statistical Center of Iran (SCI) COICOP
# codes. COICOP is available at 4 classification levels in this dataset.
# We will use level 2 and name the output column "COICOP":

table = hbsir.add_classification(
    table,
    name="original",
    levels=2,
    column_names="COICOP",
)
table.head()

# At this level, there is a category representing rent:
# "actual_rentals_for_housing"

# ## Household Aggregation
#
# For any meaningful analysis, we need to incorporate sampling weights to make
# the data representative. But first, we will aggregate the data by household
# to calculate total and rental expenditure for each household.
#
# We can perform this aggregation using Pandas' groupby method:

total_expenditure = table.groupby(["Year", "ID"])["Gross_Expenditure"].sum()
total_expenditure = total_expenditure.rename("Total_Expenditure")
total_expenditure.head()

# This sums the gross expenditure for each unique combination of year and
# household ID.
#
# Next, we will filter just the "actual_rentals_for_housing" category to
# calculate rental expenditure specifically:

filt = table["COICOP"] == "actual_rentals_for_housing"
rental_expenditure = table.loc[filt].groupby(["Year", "ID"])["Gross_Expenditure"].sum()
rental_expenditure = rental_expenditure.rename("Rental_Expenditure")
rental_expenditure.head()

# With these two aggregated expenditure series, we can simply concatenate
# them column-wise. Since the indices are unique, this joins the data without
# duplication:

expenditure_table = pd.concat([total_expenditure, rental_expenditure], axis="columns")
expenditure_table = expenditure_table.fillna(0)
expenditure_table.head()

# With our aggregated household expenditure data in place, we are now ready to
# proceed to adding sampling weights.

# ## Adding Sampling Weights
#
# Sampling weights for 1396 and onward are available in the
# "household_information" table. For prior years, the weights are not included
# in the raw data but HBSIR has integrated them from the SCI summary data.
# The add_weight function handles these differences behind the scenes and adds
# the appropriate sampling weights regardless of year.
#
# So we can simply call:

expenditure_table = hbsir.add_weight(expenditure_table)
expenditure_table.head()

# ## Adding Deciles
#
# Finally, to compare rental expenditure across different income levels,
# we want to categorize households into deciles by income. We can do this
# using the add_decile function:

expenditure_table = hbsir.calculate.add_decile(
    expenditure_table,
    on_variable="Income",
    equivalence_scale="OECD_Modified",
    groupby=["Urban_Rural", "Province"],
)
expenditure_table.head()

# The groupby parameter allows deciling within segments, rather than across the
# full population. Here we group by urban/rural status and province, meaning
# income deciles will be defined separately for each combination of these groups.
# This allows more relevant comparison of households.
#
# But what is this "equivalence_scale" parameter? By default value, "Household",
# deciling occurs on the absolute income value regardless of household size.
# With "Per_Capita", the income is divided by the number of members first.
# "OECD", "OECD_Modified", and "Square_Root" are in-between options accounting
# for economies of scale in larger households.
#
# > For more detailed information on equivalence scales, see
# > [the OECD Note on Equivalence Scales](https://www.oecd.org/els/soc/OECD-Note-EquivalenceScales.pdf).
#
# With all necessary columns added, we can now proceed to the analysis!

# ## Calculate Weighted Average
#
# Finally, we want to analyze the data by calculating the weighted average
# expenditure (total and rental) for each income decile. HBSIR provides a
# convenient function for this common task:

average_expenditure = hbsir.calculate.average_table(
    expenditure_table,
    groupby=["Decile"],
    columns=["Total_Expenditure", "Rental_Expenditure"]
)
average_expenditure

# With the weighted averages, we can easily calculate rental expenditure as
# a percentage of total expenditure for each decile:

ratio = (
    average_expenditure["Rental_Expenditure"]
    / average_expenditure["Total_Expenditure"]
    * 100
)
ratio

# Finally, we can visualize the results in a bar chart:

ratio.plot.bar()

# And with that, we have explored the key steps for analyzing rental
# expenditure data with HBSIR! This concludes our introductory tutorial
# walking through the main functions of the package.