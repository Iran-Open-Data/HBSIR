# old_urban_private_employment_income

## Old to New Titles

| Years     | ADDRESS   | COL01         | COL02           | COL03                 | COL05               | COL07                    | COL09                   | COL11             |
|:----------|:----------|:--------------|:----------------|:----------------------|:--------------------|:-------------------------|:------------------------|:------------------|
| 1363-1368 | ID        | Member_Number | Occupation_Code | Currently_in_This_Job | Annual_Gross_Income | Annual_Continuous_Income | Annual_Temporary_Income | Annual_Net_Income |


## New to Old Titles

| Years     | ID      | Member_Number   | Occupation_Code   | Currently_in_This_Job   | Annual_Gross_Income   | Annual_Continuous_Income   | Annual_Temporary_Income   | Annual_Net_Income   |
|:----------|:--------|:----------------|:------------------|:------------------------|:----------------------|:---------------------------|:--------------------------|:--------------------|
| 1363-1368 | ADDRESS | COL01           | COL02             | COL03                   | COL05                 | COL07                      | COL09                     | COL11               |


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
| 1363-1368 | [ADDRESS](/HBSIR/tables/raw/old_urban_private_employment_income#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |        Mean |   Standard Deviation |     Minimum |      Median |     Maximum |
|-------:|--------:|------------:|---------------------:|------------:|------------:|------------:|
|   1363 |    5872 | 1.11139e+06 |              75135.4 | 1.00102e+06 | 1.0941e+06  | 1.23451e+06 |
|   1364 |    5668 | 1.10844e+06 |              72116.2 | 1.001e+06   | 1.09405e+06 | 1.23442e+06 |
|   1365 |    1037 | 1.12115e+06 |              79050.3 | 1.001e+06   | 1.10101e+06 | 1.23421e+06 |
|   1366 |    1061 | 1.12944e+06 |              79030.3 | 1.001e+06   | 1.10302e+06 | 1.23421e+06 |
|   1367 |    1506 | 1.12808e+06 |              74682.1 | 1.001e+06   | 1.111e+06   | 1.23428e+06 |
|   1368 |    2120 | 1.10864e+06 |              73199.5 | 1.001e+06   | 1.10107e+06 | 1.23427e+06 |


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
| 1363-1368 | [COL01](/HBSIR/tables/raw/old_urban_private_employment_income#col01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |    5872 |   2.22 |                 1.78 |         1 |        1 |        16 |
|   1364 |    5668 |   2.03 |                 1.68 |         1 |        1 |        14 |
|   1365 |    1037 |   2.22 |                 1.82 |         0 |        1 |        11 |
|   1366 |    1061 |   2.04 |                 1.65 |         1 |        1 |        12 |
|   1367 |    1506 |   2.09 |                 1.8  |         1 |        1 |        14 |
|   1368 |    2120 |   2.13 |                 1.84 |         1 |        1 |        18 |


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
| 1363-1368 | [COL02](/HBSIR/tables/raw/old_urban_private_employment_income#col02) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |    5846 | 791.79 |               231.2  |        14 |      855 |       999 |
|   1364 |    5665 | 815.86 |               226.87 |        22 |      931 |       999 |
|   1365 |    1036 | 788.91 |               226.92 |        22 |      851 |       999 |
|   1366 |    1060 | 761.89 |               231.69 |        13 |      839 |       999 |
|   1367 |    1503 | 772.97 |               233.36 |        22 |      845 |       999 |
|   1368 |    2120 | 787.84 |               217.35 |        13 |      855 |       999 |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1363 | X01     |             nan |          24 |
|   1363 | X03     |             nan |           2 |
|   1364 | X01     |             nan |           1 |
|   1364 | X02     |             nan |           1 |
|   1364 | X03     |             nan |           1 |
|   1365 | X01     |             nan |           1 |
|   1366 | X01     |             nan |           1 |
|   1367 | X03     |             nan |           3 |


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
| 1363-1368 | [COL03](/HBSIR/tables/raw/old_urban_private_employment_income#col03) |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1363 |  72.6  |   27.4  |         0 |
|   1364 |  72.64 |   27.36 |         0 |
|   1365 |  71.26 |   28.74 |         0 |
|   1366 |  75.02 |   24.98 |         0 |
|   1367 |  79.02 |   20.98 |         0 |
|   1368 |  74.15 |   25.85 |         0 |


### Annual_Gross_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL05
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Gross_Income                                                  |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL05](/HBSIR/tables/raw/old_urban_private_employment_income#col05) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |    Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|-----------:|
|   1363 |    5872 | 313461 |               312724 |         0 |   245000 | 7.355e+06  |
|   1364 |    5668 | 321756 |               339955 |         0 |   250000 | 9e+06      |
|   1365 |    1037 | 366614 |               348420 |      1200 |   300000 | 4.2e+06    |
|   1366 |    1061 | 403643 |               333008 |         0 |   350000 | 5.1742e+06 |
|   1367 |    1506 | 481721 |               407275 |         0 |   410000 | 5.4e+06    |
|   1368 |    2120 | 492638 |               395835 |         0 |   420000 | 3.6e+06    |


### Annual_Continuous_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL07
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Continuous_Income                                             |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL07](/HBSIR/tables/raw/old_urban_private_employment_income#col07) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |    Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|-----------:|
|   1363 |    5872 | 297924 |               267969 |         0 |   240000 | 5.5e+06    |
|   1364 |    5668 | 307621 |               280374 |         0 |   250000 | 8.64e+06   |
|   1365 |    1037 | 349527 |               313523 |      1200 |   300000 | 4.2e+06    |
|   1366 |    1061 | 387536 |               315389 |         0 |   342000 | 5.1742e+06 |
|   1367 |    1506 | 462952 |               379431 |         0 |   400000 | 5.4e+06    |
|   1368 |    2120 | 476720 |               377036 |         0 |   410920 | 3.6e+06    |


### Annual_Temporary_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL09
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Temporary_Income                                              |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL09](/HBSIR/tables/raw/old_urban_private_employment_income#col09) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |      Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|-------------:|
|   1363 |    5872 |  8805.29 |              42803.4 |         0 |        0 |      2e+06   |
|   1364 |    5668 |  6471.35 |              28282   |         0 |        0 | 543337       |
|   1365 |    1037 | 10001.5  |              55018.8 |         0 |        0 |      1.5e+06 |
|   1366 |    1061 |  9950.88 |              38979.3 |         0 |        0 | 817920       |
|   1367 |    1506 | 11908.1  |              39499   |         0 |        0 | 610000       |
|   1368 |    2120 | 11498.5  |              45577.9 |         0 |        0 | 680000       |


### Annual_Net_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL11
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Net_Income                                                    |
|:----------|:---------------------------------------------------------------------|
| 1363-1368 | [COL11](/HBSIR/tables/raw/old_urban_private_employment_income#col11) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |    Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|-----------:|
|   1363 |    5872 | 306729 |               279190 |         0 |   241500 | 5.5e+06    |
|   1364 |    5668 | 314093 |               287578 |         0 |   250000 | 8.64e+06   |
|   1365 |    1037 | 359529 |               332620 |      1200 |   300000 | 4.2e+06    |
|   1366 |    1061 | 397487 |               324755 |         0 |   346615 | 5.1742e+06 |
|   1367 |    1506 | 474860 |               390987 |         0 |   408250 | 5.4e+06    |
|   1368 |    2120 | 488218 |               388533 |         0 |   420000 | 3.6e+06    |


