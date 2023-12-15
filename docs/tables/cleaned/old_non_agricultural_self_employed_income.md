# old_non_agricultural_self_employed_income

## Old to New Titles

| Years     | ADDRESS   | COL01         | COL02           | COL03                 | COL04     | COL05         | COL06                 | COL07       | COL08        | COL09   | COL10   |
|:----------|:----------|:--------------|:----------------|:----------------------|:----------|:--------------|:----------------------|:------------|:-------------|:--------|:--------|
| 1363-1368 | ID        | Member_Number | Occupation_Code | Currently_in_This_Job | Wage_Cost | Cost_of_Sales | Other_Operating_Costs | Other_Costs | Business_Tax | Sales   | Profit  |


## New to Old Titles

| Years     | ID      | Member_Number   | Occupation_Code   | Currently_in_This_Job   | Wage_Cost   | Cost_of_Sales   | Other_Operating_Costs   | Other_Costs   | Business_Tax   | Sales   | Profit   |
|:----------|:--------|:----------------|:------------------|:------------------------|:------------|:----------------|:------------------------|:--------------|:---------------|:--------|:---------|
| 1363-1368 | ADDRESS | COL01           | COL02             | COL03                   | COL04       | COL05           | COL06                   | COL07         | COL08          | COL09   | COL10    |


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

| Years     | ID                                                                             |
|:----------|:-------------------------------------------------------------------------------|
| 1363-1368 | [ADDRESS](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |      Median |     Maximum |
|-------:|--------:|-------:|---------------------:|----------:|------------:|------------:|
|   1363 |   10211 | 731166 |               495815 |      1004 | 1.03402e+06 | 1.23452e+06 |
|   1364 |    9938 | 683392 |               503716 |      1002 | 1.02415e+06 | 1.23441e+06 |
|   1365 |    2067 | 683164 |               516738 |      1001 | 1.03106e+06 | 1.23421e+06 |
|   1366 |    2012 | 691544 |               516006 |      1004 | 1.03301e+06 | 1.23421e+06 |
|   1367 |    2708 | 701924 |               514563 |      1002 | 1.03401e+06 | 1.23427e+06 |
|   1368 |    3985 | 684101 |               509986 |      1001 | 1.03203e+06 | 1.23428e+06 |


### Member_Number

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL01
      type: UInt8
    
    ```
#### Column Codes

| Years     | Member_Number                                                              |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL01](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |   10211 |   1.38 |                 1.37 |         1 |        1 |        80 |
|   1364 |    9938 |   1.32 |                 0.96 |         1 |        1 |        13 |
|   1365 |    2067 |   1.36 |                 1.05 |         1 |        1 |        11 |
|   1366 |    2012 |   1.34 |                 1.03 |         1 |        1 |        13 |
|   1367 |    2708 |   1.32 |                 0.97 |         1 |        1 |        12 |
|   1368 |    3985 |   1.38 |                 1.06 |         1 |        1 |        13 |


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

| Years     | Occupation_Code                                                            |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL02](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col02) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |   10179 | 657.47 |               239.56 |        21 |      754 |       999 |
|   1364 |    9936 | 669.36 |               241.82 |        21 |      754 |       999 |
|   1365 |    2066 | 676.03 |               239.11 |        22 |      754 |       999 |
|   1366 |    2012 | 668.52 |               238.31 |        13 |      753 |       999 |
|   1367 |    2707 | 660.6  |               241.06 |        23 |      753 |       999 |
|   1368 |    3985 | 650.1  |               233.94 |        22 |      753 |       999 |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1363 | X01     |             nan |          32 |
|   1364 | X01     |             nan |           2 |
|   1365 | X01     |             nan |           1 |
|   1367 | X01     |             nan |           1 |


### Currently_in_This_Job

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL03
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Currently_in_This_Job                                                      |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL03](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col03) |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1363 |  87.07 |   12.93 |         0 |
|   1364 |  87.53 |   12.47 |         0 |
|   1365 |  85.05 |   14.95 |         0 |
|   1366 |  84.54 |   15.46 |         0 |
|   1367 |  90.18 |    9.82 |         0 |
|   1368 |  86.37 |   13.63 |         0 |


### Wage_Cost

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL04
      type: float
    
    ```
#### Column Codes

| Years     | Wage_Cost                                                                  |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL04](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col04) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|----------:|
|   1363 |   10211 |  73168.2 |     591114           |         0 |        0 | 2.844e+07 |
|   1364 |    9938 |  57239.3 |     364004           |         0 |        0 | 1.2e+07   |
|   1365 |    2067 |  70480.9 |     455199           |         0 |        0 | 1e+07     |
|   1366 |    2012 |  82284.4 |     539868           |         0 |        0 | 1.2e+07   |
|   1367 |    2708 |  72513.1 |     444099           |         0 |        0 | 1e+07     |
|   1368 |    3985 | 101842   |          1.03583e+06 |         0 |        0 | 5e+07     |


### Cost_of_Sales

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL05
      type: float
    
    ```
#### Column Codes

| Years     | Cost_of_Sales                                                              |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL05](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col05) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |   Median |    Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------:|-----------:|
|   1363 |   10211 | 617357           |          2.97113e+06 |         0 |     6000 | 1e+08      |
|   1364 |    9938 | 507484           |          2.57128e+06 |         0 |        0 | 1e+08      |
|   1365 |    2067 | 611522           |          2.35332e+06 |         0 |    12000 | 5e+07      |
|   1366 |    2012 | 783987           |          3.55417e+06 |         0 |        0 | 8e+07      |
|   1367 |    2708 |      1.07438e+06 |          3.6047e+06  |         0 |    12000 | 4.9032e+07 |
|   1368 |    3985 |      1.07653e+06 |          3.88772e+06 |         0 |    25000 | 7.2e+07    |


### Other_Operating_Costs

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL06
      type: float
    
    ```
#### Column Codes

| Years     | Other_Operating_Costs                                                      |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL06](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col06) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|------------:|
|   1363 |   10211 | 31934.6 |     272818           |         0 |        0 | 2e+07       |
|   1364 |    9938 | 30015.9 |     175072           |         0 |        0 | 7.95e+06    |
|   1365 |    2067 | 32767.6 |     141529           |         0 |        0 | 2.69e+06    |
|   1366 |    2012 | 46078.9 |     244603           |         0 |        0 | 6e+06       |
|   1367 |    2708 | 71819.7 |     341949           |         0 |        0 | 8.5e+06     |
|   1368 |    3985 | 94230   |          1.13386e+06 |         0 |        0 | 6.83759e+07 |


### Other_Costs

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL07
      type: float
    
    ```
#### Column Codes

| Years     | Other_Costs                                                                |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL07](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col07) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 |   10211 | 41000.2 |               530665 |         0 |        0 |  5.06e+07 |
|   1364 |    9938 | 32578.9 |               221806 |         0 |        0 |  1.2e+07  |
|   1365 |    2067 | 35791.2 |               134705 |         0 |        0 |  1.9e+06  |
|   1366 |    2012 | 42277.2 |               224069 |         0 |        0 |  6.86e+06 |
|   1367 |    2708 | 50894.8 |               170840 |         0 |        0 |  4.2e+06  |
|   1368 |    3985 | 48335.7 |               278662 |         0 |        0 |  1.3e+07  |


### Business_Tax

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL08
      type: float
    
    ```
#### Column Codes

| Years     | Business_Tax                                                               |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL08](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col08) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|----------:|
|   1363 |   10211 |  6211.75 |              94429.6 |         0 |        0 |   7.7e+06 |
|   1364 |    9938 |  4590.24 |              58391.4 |         0 |        0 |   4e+06   |
|   1365 |    2067 | 11352.5  |             132600   |         0 |        0 |   5e+06   |
|   1366 |    2012 | 14924    |             221851   |         0 |        0 |   8.4e+06 |
|   1367 |    2708 | 10076.7  |              88151.9 |         0 |        0 |   3.7e+06 |
|   1368 |    3985 | 13438.3  |             139444   |         0 |        0 |   6e+06   |


### Sales

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL09
      type: float
    
    ```
#### Column Codes

| Years     | Sales                                                                      |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL09](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col09) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------:|------------:|
|   1363 |   10211 |      1.07276e+06 |          3.63472e+06 |         0 |   126000 | 1e+08       |
|   1364 |    9938 | 863840           |          3.01819e+06 |         0 |    25000 | 1e+08       |
|   1365 |    2067 |      1.05438e+06 |          2.99026e+06 |         0 |   100000 | 5.375e+07   |
|   1366 |    2012 |      1.27085e+06 |          4.28178e+06 |         0 |    50000 | 8.816e+07   |
|   1367 |    2708 |      1.69322e+06 |          4.29212e+06 |         0 |   188500 | 5.50368e+07 |
|   1368 |    3985 |      1.71369e+06 |          4.73211e+06 |         0 |   170000 | 9.389e+07   |


### Profit

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL10
      type: float
    
    ```
#### Column Codes

| Years     | Profit                                                                     |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [COL10](/HBSIR/tables/raw/old_non_agricultural_self_employed_income#col10) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|------------:|
|   1363 |   10211 | 451291 |               766443 |         0 |   285550 | 3.01888e+07 |
|   1364 |    9938 | 423679 |               763554 |         0 |   250000 | 4.5729e+07  |
|   1365 |    2067 | 102938 |               224882 |    -55160 |     8400 | 2.113e+06   |
|   1366 |    2012 | 539260 |               842694 |         0 |   350000 | 2.084e+07   |
|   1367 |    2708 | 697049 |               934310 |         0 |   500000 | 2e+07       |
|   1368 |    3985 | 729504 |               963139 |         0 |   500000 | 2e+07       |


