# old_urban_public_employment_income

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

| Years     | ID                                                                      |
|:----------|:------------------------------------------------------------------------|
| 1363-1368 | [ADDRESS](/HBSIR/tables/raw/old_urban_public_employment_income#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |        Mean |   Standard Deviation |     Minimum |      Median |     Maximum |
|-------:|--------:|------------:|---------------------:|------------:|------------:|------------:|
|   1363 |    6501 | 1.11977e+06 |              76458.5 | 1.001e+06   | 1.10221e+06 | 1.23451e+06 |
|   1364 |    6051 | 1.11761e+06 |              76440   | 1.00101e+06 | 1.10208e+06 | 1.23442e+06 |
|   1365 |    1207 | 1.14285e+06 |              84472.5 | 1.00101e+06 | 1.131e+06   | 1.23422e+06 |
|   1366 |    1146 | 1.13929e+06 |              83794.2 | 1.001e+06   | 1.1135e+06  | 1.23421e+06 |
|   1367 |    1651 | 1.13752e+06 |              80860.3 | 1.00101e+06 | 1.11303e+06 | 1.23427e+06 |
|   1368 |    2133 | 1.1183e+06  |              81997.3 | 1.001e+06   | 1.113e+06   | 1.23427e+06 |


### Member_Number

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL01
      type: UInt8
    
    ```
#### Column Codes

| Years     | Member_Number                                                       |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL01](/HBSIR/tables/raw/old_urban_public_employment_income#col01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |    6501 |   1.77 |                 1.46 |         0 |        1 |        14 |
|   1364 |    6051 |   1.6  |                 1.3  |         1 |        1 |        14 |
|   1365 |    1207 |   1.59 |                 1.24 |         1 |        1 |        11 |
|   1366 |    1146 |   1.56 |                 1.13 |         1 |        1 |         9 |
|   1367 |    1651 |   1.6  |                 1.2  |         1 |        1 |        12 |
|   1368 |    2133 |   1.54 |                 1.2  |         1 |        1 |        15 |


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

| Years     | Occupation_Code                                                     |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL02](/HBSIR/tables/raw/old_urban_public_employment_income#col02) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |    5826 | 456.7  |               325.18 |        13 |      391 |       999 |
|   1364 |    5577 | 462.21 |               327.97 |        13 |      392 |       999 |
|   1365 |    1108 | 474.68 |               330.51 |        13 |      393 |       999 |
|   1366 |    1032 | 468.91 |               322.9  |        13 |      391 |       999 |
|   1367 |    1494 | 429.9  |               315.21 |        13 |      322 |       999 |
|   1368 |    1911 | 435.59 |               316.92 |        13 |      331 |       999 |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1363 | X01     |             nan |          37 |
|   1363 | X03     |             nan |         638 |
|   1364 | X01     |             nan |           4 |
|   1364 | X03     |             nan |         470 |
|   1365 | X03     |             nan |          99 |
|   1366 | X01     |             nan |           2 |
|   1366 | X02     |             nan |           2 |
|   1366 | X03     |             nan |          93 |
|   1366 | X04     |             nan |          17 |
|   1367 | X01     |             nan |           4 |
|   1367 | X02     |             nan |           1 |
|   1367 | X03     |             nan |         125 |
|   1367 | X04     |             nan |          27 |
|   1368 | X01     |             nan |           2 |
|   1368 | X02     |             nan |           1 |
|   1368 | X03     |             nan |         183 |
|   1368 | X04     |             nan |          36 |


### Currently_in_This_Job

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL03
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Currently_in_This_Job                                               |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL03](/HBSIR/tables/raw/old_urban_public_employment_income#col03) |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1363 |  91.34 |    8.66 |         0 |
|   1364 |  92.07 |    7.93 |         0 |
|   1365 |  92.13 |    7.87 |         0 |
|   1366 |  93.11 |    6.89 |         0 |
|   1367 |  93.64 |    6.36 |         0 |
|   1368 |  94.94 |    5.06 |         0 |


### Annual_Gross_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL05
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Gross_Income                                                 |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL05](/HBSIR/tables/raw/old_urban_public_employment_income#col05) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|------------:|
|   1363 |    6501 | 636141 |               469603 |         0 |   597888 | 1.2516e+07  |
|   1364 |    6051 | 690691 |               423143 |      3070 |   653624 | 1.15607e+07 |
|   1365 |    1207 | 721151 |               385816 |      3750 |   694800 | 3.91601e+06 |
|   1366 |    1146 | 762580 |               569623 |         0 |   727240 | 1.48334e+07 |
|   1367 |    1651 | 836551 |               650920 |         0 |   775400 | 9.955e+06   |
|   1368 |    2133 | 899599 |               645120 |         0 |   840000 | 1.328e+07   |


### Annual_Continuous_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL07
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Continuous_Income                                            |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL07](/HBSIR/tables/raw/old_urban_public_employment_income#col07) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|------------:|
|   1363 |    6501 | 540013 |               278378 |         0 |   526248 | 2.16012e+06 |
|   1364 |    6051 | 593906 |               283523 |      3070 |   579864 | 2.8532e+06  |
|   1365 |    1207 | 621751 |               305451 |      3750 |   612600 | 2.98122e+06 |
|   1366 |    1146 | 648977 |               314591 |         0 |   638244 | 2.4292e+06  |
|   1367 |    1651 | 699933 |               349955 |         0 |   675696 | 4.87794e+06 |
|   1368 |    2133 | 746041 |               334806 |         0 |   726144 | 2.80703e+06 |


### Annual_Temporary_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL09
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Temporary_Income                                             |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL09](/HBSIR/tables/raw/old_urban_public_employment_income#col09) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |          Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|-----------------:|
|   1363 |    6501 | 34595.8 |              85097.5 |         0 |        0 |      2.60919e+06 |
|   1364 |    6051 | 35741.8 |              78529   |         0 |        0 |      1.65e+06    |
|   1365 |    1207 | 35192.4 |              69351.5 |         0 |        0 | 806000           |
|   1366 |    1146 | 47311.4 |              87784.1 |         0 |     9000 |      1.409e+06   |
|   1367 |    1651 | 51517.1 |              90681.3 |         0 |     9000 |      1.15026e+06 |
|   1368 |    2133 | 66883   |             110297   |         0 |     9000 |      2.034e+06   |


### Annual_Net_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL11
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Net_Income                                                   |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL11](/HBSIR/tables/raw/old_urban_public_employment_income#col11) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|------------:|
|   1363 |    6501 | 574608 |               306313 |         0 |   556600 | 4.33315e+06 |
|   1364 |    6051 | 629648 |               306824 |      3070 |   610000 | 3.09708e+06 |
|   1365 |    1207 | 656944 |               326350 |      3750 |   647136 | 2.98122e+06 |
|   1366 |    1146 | 696289 |               343583 |         0 |   683922 | 3.35519e+06 |
|   1367 |    1651 | 751450 |               374067 |         0 |   729616 | 4.98394e+06 |
|   1368 |    2133 | 812924 |               373865 |         0 |   786000 | 3.35069e+06 |


