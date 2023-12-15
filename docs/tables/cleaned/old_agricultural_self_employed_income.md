# old_agricultural_self_employed_income

## Old to New Titles

| Years     | ADDRESS   | COL01         | COL02           | COL03                 | COL04     | COL05         | COL06                 | COL07        | COL08   | COL09   |
|:----------|:----------|:--------------|:----------------|:----------------------|:----------|:--------------|:----------------------|:-------------|:--------|:--------|
| 1363-1368 | ID        | Member_Number | Occupation_Code | Currently_in_This_Job | Wage_Cost | Cost_of_Sales | Other_Operating_Costs | Business_Tax | Sales   | Profit  |


## New to Old Titles

| Years     | ID      | Member_Number   | Occupation_Code   | Currently_in_This_Job   | Wage_Cost   | Cost_of_Sales   | Other_Operating_Costs   | Business_Tax   | Sales   | Profit   |
|:----------|:--------|:----------------|:------------------|:------------------------|:------------|:----------------|:------------------------|:---------------|:--------|:---------|
| 1363-1368 | ADDRESS | COL01           | COL02             | COL03                   | COL04       | COL05           | COL06                   | COL07          | COL08   | COL09    |


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

| Years     | ID                                                                         |
|:----------|:---------------------------------------------------------------------------|
| 1363-1368 | [ADDRESS](/HBSIR/tables/raw/old_agricultural_self_employed_income#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|------------:|
|   1363 |   18796 | 229416 |               350297 |      1001 |  94292   | 1.23451e+06 |
|   1364 |   20072 | 205756 |               322541 |      1001 |  94305.5 | 1.23433e+06 |
|   1365 |    4131 | 162611 |               285312 |      1001 |  81026   | 1.23421e+06 |
|   1366 |    3937 | 160266 |               278415 |      1002 |  91024   | 1.23421e+06 |
|   1367 |    5736 | 176958 |               295564 |      1003 |  92110   | 1.23427e+06 |
|   1368 |    8695 | 170785 |               296231 |      1001 |  91089   | 1.23426e+06 |


### Member_Number

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL01
      type: UInt8
    
    ```
#### Column Codes

| Years     | Member_Number                                                          |
|:----------|:-----------------------------------------------------------------------|
| 1363-1368 | [COL01](/HBSIR/tables/raw/old_agricultural_self_employed_income#col01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |   18796 |   1.08 |                 0.58 |         1 |        1 |        11 |
|   1364 |   20072 |   1.05 |                 0.45 |         1 |        1 |        10 |
|   1365 |    4131 |   1.07 |                 0.47 |         1 |        1 |         9 |
|   1366 |    3937 |   1.07 |                 0.51 |         0 |        1 |        13 |
|   1367 |    5736 |   1.07 |                 0.49 |         1 |        1 |        10 |
|   1368 |    8695 |   1.06 |                 0.51 |         1 |        1 |        14 |


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

| Years     | Occupation_Code                                                        |
|:----------|:-----------------------------------------------------------------------|
| 1363-1368 | [COL02](/HBSIR/tables/raw/old_agricultural_self_employed_income#col02) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |   18796 | 613.26 |                 2.9  |       600 |      613 |       649 |
|   1364 |   20072 | 613.29 |                 3.05 |       600 |      612 |       649 |
|   1365 |    4131 | 613.28 |                 3.02 |       600 |      613 |       649 |
|   1366 |    3937 | 613.22 |                 2.66 |       612 |      612 |       649 |
|   1367 |    5736 | 613.37 |                 3.18 |       612 |      613 |       641 |
|   1368 |    8695 | 613.31 |                 2.67 |       612 |      613 |       649 |


### Currently_in_This_Job

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL03
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Currently_in_This_Job                                                  |
|:----------|:-----------------------------------------------------------------------|
| 1363-1368 | [COL03](/HBSIR/tables/raw/old_agricultural_self_employed_income#col03) |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1363 |  95.32 |    4.68 |         0 |
|   1364 |  96.53 |    3.47 |         0 |
|   1365 |  97.56 |    2.44 |         0 |
|   1366 |  97.43 |    2.57 |         0 |
|   1367 |  96.88 |    3.12 |         0 |
|   1368 |  96.06 |    3.94 |         0 |


### Wage_Cost

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL04
      type: float
    
    ```
#### Column Codes

| Years     | Wage_Cost                                                              |
|:----------|:-----------------------------------------------------------------------|
| 1363-1368 | [COL04](/HBSIR/tables/raw/old_agricultural_self_employed_income#col04) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |    Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|-----------:|
|   1363 |   18796 | 25289.8 |             146208   |         0 |        0 | 1.4e+07    |
|   1364 |   20072 | 23553.9 |             177156   |         0 |        0 | 2e+07      |
|   1365 |    4131 | 24735   |              94279.1 |         0 |        0 | 2.4487e+06 |
|   1366 |    3937 | 27836.5 |             108129   |         0 |        0 | 2.7375e+06 |
|   1367 |    5736 | 32014   |             110718   |         0 |        0 | 2.9126e+06 |
|   1368 |    8695 | 37408.5 |             156564   |         0 |        0 | 6e+06      |


### Cost_of_Sales

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL05
      type: float
    
    ```
#### Column Codes

| Years     | Cost_of_Sales                                                          |
|:----------|:-----------------------------------------------------------------------|
| 1363-1368 | [COL05](/HBSIR/tables/raw/old_agricultural_self_employed_income#col05) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|------------:|
|   1363 |   18796 |  69065.9 |               783996 |         0 |    13500 | 9.58125e+07 |
|   1364 |   20072 |  72377.2 |               432291 |         0 |    17500 | 4.175e+07   |
|   1365 |    4131 |  73554.6 |               227568 |         0 |    24000 | 1.035e+07   |
|   1366 |    3937 | 104062   |               326449 |         0 |    31000 | 9.8e+06     |
|   1367 |    5736 | 138775   |               741729 |         0 |    33660 | 4.2e+07     |
|   1368 |    8695 | 184418   |               595881 |         0 |    51000 | 2.66192e+07 |


### Other_Operating_Costs

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL06
      type: float
    
    ```
#### Column Codes

| Years     | Other_Operating_Costs                                                  |
|:----------|:-----------------------------------------------------------------------|
| 1363-1368 | [COL06](/HBSIR/tables/raw/old_agricultural_self_employed_income#col06) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |    Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|-----------:|
|   1363 |   18796 |  5419.44 |              36588.6 |         0 |        0 | 2e+06      |
|   1364 |   20072 |  5332.52 |              35444.6 |         0 |        0 | 2.255e+06  |
|   1365 |    4131 |  9139.11 |              72934   |         0 |        0 | 4e+06      |
|   1366 |    3937 | 10710.2  |              53649   |         0 |        0 | 1.62e+06   |
|   1367 |    5736 | 12935    |              75504   |         0 |        0 | 2.5131e+06 |
|   1368 |    8695 | 17867    |             166705   |         0 |        0 | 1.2e+07    |


### Business_Tax

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL07
      type: float
    
    ```
#### Column Codes

| Years     | Business_Tax                                                           |
|:----------|:-----------------------------------------------------------------------|
| 1363-1368 | [COL07](/HBSIR/tables/raw/old_agricultural_self_employed_income#col07) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|------------:|
|   1363 |   18796 | 13059.9 |              62830   |         0 |        0 | 3.83083e+06 |
|   1364 |   20072 | 14702.1 |              90711.2 |         0 |        0 | 8.5e+06     |
|   1365 |    4131 | 24978.5 |             105058   |         0 |        0 | 4.183e+06   |
|   1366 |    3937 | 27829.8 |              77099.8 |         0 |      500 | 1.69e+06    |
|   1367 |    5736 | 36077.2 |             153760   |         0 |        0 | 5.59e+06    |
|   1368 |    8695 | 37258.9 |             182852   |         0 |        0 | 1.076e+07   |


### Sales

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL08
      type: float
    
    ```
#### Column Codes

| Years     | Sales                                                                  |
|:----------|:-----------------------------------------------------------------------|
| 1363-1368 | [COL08](/HBSIR/tables/raw/old_agricultural_self_employed_income#col08) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|------------:|
|   1363 |   18796 | 190264 |     911212           |         0 |    54000 | 9.69888e+07 |
|   1364 |   20072 | 199794 |     683714           |         0 |    68000 | 4.393e+07   |
|   1365 |    4131 | 248991 |     597122           |         0 |   100000 | 1.25e+07    |
|   1366 |    3937 | 307573 |     674233           |         0 |   130000 | 2e+07       |
|   1367 |    5736 | 421952 |          1.40291e+06 |         0 |   175000 | 5.58228e+07 |
|   1368 |    8695 | 490546 |          1.16057e+06 |         0 |   250000 | 5.256e+07   |


### Profit

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL09
      type: float
    
    ```
#### Column Codes

| Years     | Profit                                                                 |
|:----------|:-----------------------------------------------------------------------|
| 1363-1368 | [COL09](/HBSIR/tables/raw/old_agricultural_self_employed_income#col09) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|------------:|
|   1363 |   18796 | 107943 |               276500 |         0 |    27500 | 1.16e+07    |
|   1364 |   20072 | 115375 |               310798 |         0 |    32000 | 1.7e+07     |
|   1365 |    4131 | 122399 |               285312 |    -13339 |    30000 | 8.01e+06    |
|   1366 |    3937 | 177107 |               410947 |         0 |    60000 | 1.2904e+07  |
|   1367 |    5736 | 246187 |               905353 |         0 |    90000 | 4.81024e+07 |
|   1368 |    8695 | 269804 |               560948 |         0 |   103900 | 1.91708e+07 |


