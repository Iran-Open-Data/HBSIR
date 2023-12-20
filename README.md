# HBSIR - Household Budget Survey of Iran in Python

## Overview

HBSIR is a Python package for working with microdata from the Household Budget 
Survey of Iran (HBSIR). It provides a high-level API for easily loading, 
exploring and analyzing this nationally representative household survey.

The key capabilities of HBSIR include:

- Loading survey tables for multiple years in raw, cleaned or normalized form
- Enriching data by adding geographical attributes and classification systems 
- Performing correct weighted statistical analysis with integrated sampling weights  
- Calculating metrics like weighted averages and distributional statistics
- Accessing pre-processed tables and visualizations stored in a Knowledge Base
- Handling all necessary data processing and configuration behind the scenes

HBSIR aims to make analysis of the Household Budget Survey straightforward for 
researchers, analysts and policymakers even without programming expertise. 
The simple verb-based API provides a smooth on-ramp while harnessing the full 
power of Pandas and Python under the hood.

## Motivation

The HBSIR Data Python Package addresses the historical challenges in analyzing 
Household Budget Survey data from Iran. The complex nature of the data, with 
its ever-changing codings, inconsistent table schemas, and lack of 
standardization, has made analysis a daunting task. This package aims to 
simplify the entire process—from data extraction to analysis—allowing 
researchers to focus on deriving meaningful insights rather than wrestling 
with data complexities.

Recognizing the difficulties posed by the original MS Access format and the 
lack of standardization across different years, the HBSIR Data Python Package 
offers a solution. By providing a uniform API, streamlining data loading, and 
introducing a customizable schema system, we aim to make HBSIR data more 
accessible and usable for all researchers. This package empowers users to 
overcome the challenges associated with HBSIR data, enabling them to 
contribute to a deeper understanding of household budget dynamics in Iran.

## Getting Started

Getting started with HBSIR is quick and easy. 

First, install the package using pip:

```sh
pip install hbsir
```

Then import the library and load a table:

```python
import hbsir

table = hbsir.load_table("Expenditures", years=[1390, 1400])
```

The load_table function, by default, retrieves normalized, analysis-ready data. 
Just specify the table name and year(s).

Further data enrichment occurs through HBSIR's verb-based API:

```python
table = hbsir.add_attribute(table, name="Province")
```

This adds a province name column for geographical analysis.

For more examples of data loading, transformation and analysis refer to the 
[complete documentation](https://iran-open-data.github.io/HBSIR/). 

## Contributing

HBSIR warmly welcomes contributions from the community!

As an open source project aimed at accessibility, we highly encourage 
submissions and improvements from all users.

In particular, assistance with updating and expanding the documentation is 
invaluable. As the capabilities of HBSIR grow, keeping the docs updated is 
an ongoing effort. All contributions to the documentation are appreciated.

More broadly, please open issues or pull requests for:

- Reporting bugs
- Suggesting new features
- Improving existing code

The HBSIR contributors will do their best to respond promptly and incorporate 
changes that align with the project's overall vision and aims.

As an open dataset and software project, transparency and community 
participation are vital to the success and impact of HBSIR. We welcome you 
to get involved!

## Related Packages

HBSIR is built on top of the [BSSIR](https://github.com/Iran-Open-Data/BSSIR) 
(Basic Survey Structure of Iran) library 
which provides shared data loading and transformation functionality across 
multiple socioeconomic surveys from Iran.

Specifically, HBSIR utilizes capabilities from BSSIR to:

- Read complex raw survey data files
- Standardize schemas across years
- Integrate metadata like regional attributes
- Manage data configurations

This enables HBSIR to focus specifically on provisions for analyzing the 
Household Budget Survey without having to reimplement common data handling 
mechanisms.

The modular design centered around BSSIR also allows the HBSIR data access 
API to be reused easily. Two other survey-specific libraries that inherit 
directly from HBSIR are:

- [LFSIR](https://github.com/Iran-Open-Data/LFSIR): For the Iran Labor Force Survey
- CNSIR: For the Iran Census and Sample Survey

So in summary, BSSIR provides base survey data infrastructure, while HBSIR, 
LFSIR and CNSIR build on top of it with added provisions for analyzing their 
respective datasets. This hierarchy of packages allows collaborative 
development and maintenance.

``` mermaid
flowchart TD
    BSSIR --> HBSIR
    BSSIR --> LFSIR
    BSSIR --> CNSIR

    click BSSIR "https://github.com/Iran-Open-Data/BSSIR"
    click HBSIR "https://github.com/Iran-Open-Data/HBSIR"
    click LFSIR "https://github.com/Iran-Open-Data/LFSIR"
    click CNSIR "https://github.com/Iran-Open-Data/CNSIR"
```
