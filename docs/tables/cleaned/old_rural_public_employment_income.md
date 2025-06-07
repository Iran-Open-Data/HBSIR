# old_rural_public_employment_income

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

| Years     | ID                                                                      |
|:----------|:------------------------------------------------------------------------|
| 1363-1368 | [ADDRESS](/HBSIR/tables/raw/old_rural_public_employment_income#address) |


#### Summary Statistics

**numeric data**

|   Year | Count   | Mean      | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:----------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939.0  | 104263.98 | 71273.61             | 1021.0    | 91212.0  | 234093.0  |
|   1364 | 2060.0  | 110502.75 | 75084.39             | 1013.0    | 94101.5  | 234175.0  |
|   1365 | 408.0   | 87629.79  | 67179.88             | 1010.0    | 73539.5  | 234017.0  |
|   1366 |         |           |                      |           |          |           |
|   1367 |         |           |                      |           |          |           |
|   1368 | 698.0   | 103989.49 | 74516.97             | 1004.0    | 94061.5  | 234052.0  |


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
| 1363-1368 | [COL01](/HBSIR/tables/raw/old_rural_public_employment_income#col01) |


#### Summary Statistics

**numeric data**

|   Year | Count   | Mean   | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:-------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939.0  | 1.79   | 1.6                  | 1.0       | 1.0      | 15.0      |
|   1364 | 2060.0  | 1.7    | 1.47                 | 1.0       | 1.0      | 14.0      |
|   1365 | 408.0   | 1.68   | 1.46                 | 1.0       | 1.0      | 10.0      |
|   1366 |         |        |                      |           |          |           |
|   1367 |         |        |                      |           |          |           |
|   1368 | 698.0   | 1.71   | 1.87                 | 1.0       | 1.0      | 25.0      |


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
| 1363-1368 | [COL02](/HBSIR/tables/raw/old_rural_public_employment_income#col02) |


#### Summary Statistics

**numeric data**

|   Year | Count   | Mean   | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:-------|:---------------------|:----------|:---------|:----------|
|   1363 | 1627.0  | 599.79 | 316.72               | 22.0      | 589.0    | 999.0     |
|   1364 | 1781.0  | 596.17 | 320.04               | 13.0      | 589.0    | 999.0     |
|   1365 | 334.0   | 548.4  | 327.68               | 23.0      | 589.0    | 999.0     |
|   1366 |         |        |                      |           |          |           |
|   1367 |         |        |                      |           |          |           |
|   1368 | 596.0   | 536.36 | 324.5                | 31.0      | 552.0    | 999.0     |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1363 | X01     |             nan |          16 |
|   1363 | X03     |             nan |         296 |
|   1364 | X03     |             nan |         279 |
|   1365 | X03     |             nan |          74 |
|   1368 | X01     |             nan |           4 |
|   1368 | X03     |             nan |          86 |
|   1368 | X04     |             nan |          12 |


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
| 1363-1368 | [COL03](/HBSIR/tables/raw/old_rural_public_employment_income#col03) |


#### Summary Statistics

**boolean data**

|   Year | True              | False              | Missing   |
|-------:|:------------------|:-------------------|:----------|
|   1363 | 80.66013408973699 | 19.339865910263022 | 0.0       |
|   1364 | 82.96116504854369 | 17.038834951456312 | 0.0       |
|   1365 | 81.37254901960785 | 18.627450980392158 | 0.0       |
|   1366 |                   |                    |           |
|   1367 |                   |                    |           |
|   1368 | 90.11461318051576 | 9.885386819484241  | 0.0       |


### Annual_Continuous_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL05
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Continuous_Income                                            |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL05](/HBSIR/tables/raw/old_rural_public_employment_income#col05) |


#### Summary Statistics

**numeric data**

|   Year | Count   | Mean      | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:----------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939.0  | 397009.38 | 245198.86            | 0.0       | 412200.0 | 2347200.0 |
|   1364 | 2060.0  | 436671.75 | 359183.81            | 2800.0    | 450000.0 | 9531072.0 |
|   1365 | 408.0   | 467399.03 | 435862.5             | 15000.0   | 490140.0 | 7573900.0 |
|   1366 |         |           |                      |           |          |           |
|   1367 |         |           |                      |           |          |           |
|   1368 | 698.0   | 596092.62 | 311036.38            | 0.0       | 615174.0 | 1745186.0 |


### Annual_Temporary_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL07
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Temporary_Income                                             |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL07](/HBSIR/tables/raw/old_rural_public_employment_income#col07) |


#### Summary Statistics

**numeric data**

|   Year | Count   | Mean     | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:---------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939.0  | 24567.58 | 53512.9              | 0.0       | 0.0      | 480000.0  |
|   1364 | 2060.0  | 20810.94 | 45340.35             | 0.0       | 0.0      | 375000.0  |
|   1365 | 408.0   | 23931.46 | 53023.64             | 0.0       | 0.0      | 408000.0  |
|   1366 |         |          |                      |           |          |           |
|   1367 |         |          |                      |           |          |           |
|   1368 | 698.0   | 52769.74 | 86581.63             | 0.0       | 9000.0   | 850000.0  |


### Annual_Net_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL09
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Net_Income                                                   |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [COL09](/HBSIR/tables/raw/old_rural_public_employment_income#col09) |


#### Summary Statistics

**numeric data**

|   Year | Count   | Mean      | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:----------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939.0  | 421576.94 | 267302.5             | 0.0       | 432320.0 | 2347200.0 |
|   1364 | 2060.0  | 457482.69 | 371379.41            | 2800.0    | 471872.0 | 9683472.0 |
|   1365 | 408.0   | 491330.47 | 446704.97            | 15000.0   | 511752.0 | 7573900.0 |
|   1366 |         |           |                      |           |          |           |
|   1367 |         |           |                      |           |          |           |
|   1368 | 698.0   | 648862.38 | 346502.5             | 0.0       | 674060.0 | 1972000.0 |


