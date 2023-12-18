# HBSIR

**Simplify Your Analysis of Household Budget Survey Data**

## Overview

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

Getting started with the package is straightforward. Simply install it using pip:  

```sh
pip install hbsir
```

```python
import hbsir

# Load a normalized data table 
table = hbsir.load_table("Expenditures", years=[1390, 1400])

# Enrich with province name
table = hbsir.add_attribute(table, name="Province")
```

## Documentation

Full documentation is available at [iran-open-data.github.io/HBSIR/](https://iran-open-data.github.io/HBSIR/)
