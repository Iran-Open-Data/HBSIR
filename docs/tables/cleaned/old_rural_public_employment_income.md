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

|   Year | Count   | Mean               | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:-------------------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939    | 104263.97730789066 | 71273.607861305      | 1021      | 91212.0  | 234093    |
|   1364 | 2060    | 110502.74854368932 | 75084.38951012185    | 1013      | 94101.5  | 234175    |
|   1365 | 408     | 87629.79166666667  | 67179.87778675232    | 1010      | 73539.5  | 234017    |
|   1366 |         |                    |                      |           |          |           |
|   1367 |         |                    |                      |           |          |           |
|   1368 | 698     | 103989.49140401147 | 74516.96709472507    | 1004      | 94061.5  | 234052    |


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

|   Year | Count   | Mean               | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:-------------------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939    | 1.7890665291387313 | 1.6044198837181771   | 1         | 1.0      | 15        |
|   1364 | 2060    | 1.6990291262135921 | 1.4719983176732387   | 1         | 1.0      | 14        |
|   1365 | 408     | 1.6838235294117647 | 1.4571801681644208   | 1         | 1.0      | 10        |
|   1366 |         |                    |                      |           |          |           |
|   1367 |         |                    |                      |           |          |           |
|   1368 | 698     | 1.7106017191977076 | 1.8731438626270729   | 1         | 1.0      | 25        |


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

|   Year | Count   | Mean              | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:------------------|:---------------------|:----------|:---------|:----------|
|   1363 | 1627    | 599.7879532882606 | 316.7190484065414    | 22        | 589.0    | 999       |
|   1364 | 1781    | 596.1746209994385 | 320.0423257584734    | 13        | 589.0    | 999       |
|   1365 | 334     | 548.4011976047905 | 327.67832977841124   | 23        | 589.0    | 999       |
|   1366 |         |                   |                      |           |          |           |
|   1367 |         |                   |                      |           |          |           |
|   1368 | 596     | 536.3557046979865 | 324.4972545638909    | 31        | 552.0    | 999       |


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

|   Year | Count   | Mean         | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:-------------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939.0  | 397009.375   | 245198.859375        | 0.0       | 412200.0 | 2347200.0 |
|   1364 | 2060.0  | 436671.75    | 359183.8125          | 2800.0    | 450000.0 | 9531072.0 |
|   1365 | 408.0   | 467399.03125 | 435862.5             | 15000.0   | 490140.0 | 7573900.0 |
|   1366 |         |              |                      |           |          |           |
|   1367 |         |              |                      |           |          |           |
|   1368 | 698.0   | 596092.625   | 311036.375           | 0.0       | 615174.0 | 1745186.0 |


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

|   Year | Count   | Mean            | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:----------------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939.0  | 24567.580078125 | 53512.90625          | 0.0       | 0.0      | 480000.0  |
|   1364 | 2060.0  | 20810.935546875 | 45340.3515625        | 0.0       | 0.0      | 375000.0  |
|   1365 | 408.0   | 23931.46484375  | 53023.640625         | 0.0       | 0.0      | 408000.0  |
|   1366 |         |                 |                      |           |          |           |
|   1367 |         |                 |                      |           |          |           |
|   1368 | 698.0   | 52769.7421875   | 86581.6328125        | 0.0       | 9000.0   | 850000.0  |


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

|   Year | Count   | Mean         | Standard Deviation   | Minimum   | Median   | Maximum   |
|-------:|:--------|:-------------|:---------------------|:----------|:---------|:----------|
|   1363 | 1939.0  | 421576.9375  | 267302.5             | 0.0       | 432320.0 | 2347200.0 |
|   1364 | 2060.0  | 457482.6875  | 371379.375           | 2800.0    | 471872.0 | 9683472.0 |
|   1365 | 408.0   | 491330.46875 | 446704.96875         | 15000.0   | 511752.0 | 7573900.0 |
|   1366 |         |              |                      |           |          |           |
|   1367 |         |              |                      |           |          |           |
|   1368 | 698.0   | 648862.375   | 346502.5             | 0.0       | 674060.0 | 1972000.0 |


