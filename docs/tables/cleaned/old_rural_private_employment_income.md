# old_rural_private_employment_income

## Old to New Titles

| Years     | ADDRESS   | COL01         | COL02           | COL03                 | COL05                    | COL07                   | COL09             |
|:----------|:----------|:--------------|:----------------|:----------------------|:-------------------------|:------------------------|:------------------|
| 1363-1368 | ID        | Member_Number | Occupation_Code | Currently_in_This_Job | Annual_Continuous_Income | Annual_Temporary_Income | Annual_Net_Income |


## New to Old Titles

| Years     | ID      | Member_Number   | Occupation_Code   | Currently_in_This_Job   | Annual_Continuous_Income   | Annual_Temporary_Income   | Annual_Net_Income   |
|:----------|:--------|:----------------|:------------------|:------------------------|:---------------------------|:--------------------------|:--------------------|
| 1363-1368 | ADDRESS | COL01           | COL02             | COL03                   | COL05                      | COL07                     | COL09               |


## Columns Details

### ID

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: ADDRESS
      type: UInt64
      replace: null
    1374:
      column_code: ADDRESS
      type: UInt64
      replace:
        "00\x04": null
        "01\x04": null
        "02\x04": null
        "10\x04": null
        "11\x04": null
        "12\x04": null
    1375:
      column_code: ADDRESS
      type: UInt64
      replace: null
    
    ```
#### Column Codes

| Years     | ID                                                                       |
|:----------|:-------------------------------------------------------------------------|
| 1363-1368 | [ADDRESS](/HBSIR/tables/raw/old_rural_private_employment_income#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|----------:|
|   1363 |    6646 |  98146.8 |              65789.1 |      1001 |  92167.5 |    234095 |
|   1364 |    7089 | 101353   |              68381.7 |      1002 |  92107   |    234171 |
|   1365 |    1518 |  82488.5 |              57091.1 |      1001 |  81515.5 |    234015 |
|   1366 |    1494 |  91048.7 |              62412   |      1006 |  87510   |    234042 |
|   1367 |    1989 |  92013.6 |              63127.2 |      1003 |  91077   |    234054 |
|   1368 |    3069 |  83236.6 |              59367.4 |      1003 |  82011   |    234054 |


### Member_Number

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL01
      type: UInt8
    
    ```
#### Column Codes

| Years     | Member_Number                                                        |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL01](/HBSIR/tables/raw/old_rural_private_employment_income#col01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |    6646 |   2.05 |                 1.78 |         1 |        1 |        18 |
|   1364 |    7089 |   1.94 |                 1.67 |         1 |        1 |        16 |
|   1365 |    1518 |   2.03 |                 1.74 |         1 |        1 |        12 |
|   1366 |    1494 |   1.95 |                 1.81 |         1 |        1 |        18 |
|   1367 |    1989 |   2.08 |                 1.87 |         1 |        1 |        17 |
|   1368 |    3069 |   2.07 |                 1.78 |         1 |        1 |        24 |


### Occupation_Code

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL02
      type: UInt32
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        x01: null
        x02: null
        x03: null
        x04: null
        x0000: 0
        x000: 0
    
    ```
#### Column Codes

| Years     | Occupation_Code                                                      |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL02](/HBSIR/tables/raw/old_rural_private_employment_income#col02) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |    6631 | 822.13 |               188.23 |        22 |      931 |       999 |
|   1364 |    7081 | 819.38 |               189.32 |        31 |      931 |       999 |
|   1365 |    1516 | 809.17 |               191.05 |        22 |      872 |       999 |
|   1366 |    1491 | 781.95 |               176.87 |        31 |      776 |       999 |
|   1367 |    1987 | 787.59 |               175.92 |        72 |      811 |       999 |
|   1368 |    3066 | 785.21 |               172.67 |        42 |      791 |       999 |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1363 | X01     |             nan |          12 |
|   1363 | X02     |             nan |           1 |
|   1363 | X03     |             nan |           2 |
|   1364 | X01     |             nan |           2 |
|   1364 | X03     |             nan |           6 |
|   1365 | X03     |             nan |           2 |
|   1366 | X03     |             nan |           3 |
|   1367 | X01     |             nan |           1 |
|   1367 | X03     |             nan |           1 |
|   1368 | X01     |             nan |           2 |
|   1368 | X03     |             nan |           1 |


### Currently_in_This_Job

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL03
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Currently_in_This_Job                                                |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL03](/HBSIR/tables/raw/old_rural_private_employment_income#col03) |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1363 |  53.05 |   46.95 |         0 |
|   1364 |  53.41 |   46.59 |         0 |
|   1365 |  45.98 |   54.02 |         0 |
|   1366 |  52.28 |   47.72 |         0 |
|   1367 |  59.73 |   40.27 |         0 |
|   1368 |  56.27 |   43.73 |         0 |


### Annual_Continuous_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL05
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Continuous_Income                                             |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL05](/HBSIR/tables/raw/old_rural_private_employment_income#col05) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |    6646 | 170239 |               169875 |         0 |   120000 | 2.4e+06   |
|   1364 |    7089 | 180794 |               174641 |         0 |   130000 | 2.2e+06   |
|   1365 |    1518 | 178263 |               181965 |       600 |   120000 | 3.405e+06 |
|   1366 |    1494 | 216542 |               200949 |         0 |   160000 | 2.4e+06   |
|   1367 |    1989 | 280328 |               241113 |         0 |   224500 | 2.75e+06  |
|   1368 |    3069 | 304430 |               279989 |         0 |   225000 | 4.86e+06  |


### Annual_Temporary_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL07
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Temporary_Income                                              |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL07](/HBSIR/tables/raw/old_rural_private_employment_income#col07) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 |    6646 | 1728.79 |             13646.1  |         0 |        0 |    385000 |
|   1364 |    7089 | 1618.67 |             15496.8  |         0 |        0 |    788400 |
|   1365 |    1518 |  441.25 |              4596.83 |         0 |        0 |     90000 |
|   1366 |    1494 | 1588.9  |             11551.6  |         0 |        0 |    200000 |
|   1367 |    1989 | 3165.49 |             15091.1  |         0 |        0 |    200000 |
|   1368 |    3069 | 3389.98 |             28179    |         0 |        0 |    732000 |


### Annual_Net_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL09
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Net_Income                                                    |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL09](/HBSIR/tables/raw/old_rural_private_employment_income#col09) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |    6646 | 171968 |               173496 |         0 |   120000 | 2.4e+06   |
|   1364 |    7089 | 182413 |               178566 |         0 |   130000 | 2.2e+06   |
|   1365 |    1518 | 178705 |               182782 |       600 |   120000 | 3.405e+06 |
|   1366 |    1494 | 218131 |               203850 |         0 |   160000 | 2.4e+06   |
|   1367 |    1989 | 283493 |               245168 |         0 |   225000 | 2.75e+06  |
|   1368 |    3069 | 307820 |               284991 |         0 |   225000 | 4.86e+06  |


