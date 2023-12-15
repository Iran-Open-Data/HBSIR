# old_other_income

## Old to New Titles

| Years     | ADDRESS   | COL01       | COL04   |
|:----------|:----------|:------------|:--------|
| 1363-1368 | ID        | Income_Code | Income  |


## New to Old Titles

| Years     | ID      | Income_Code   | Income   |
|:----------|:--------|:--------------|:---------|
| 1363-1368 | ADDRESS | COL01         | COL04    |


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

| Years     | ID                                                    |
|:----------|:------------------------------------------------------|
| 1363-1368 | [ADDRESS](/HBSIR/tables/raw/old_other_income#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |      Median |     Maximum |
|-------:|--------:|-------:|---------------------:|----------:|------------:|------------:|
|   1363 |    7306 | 736261 |               494899 |      1006 | 1.04309e+06 | 1.23451e+06 |
|   1364 |    5407 | 697144 |               500825 |      1021 | 1.02407e+06 | 1.23442e+06 |
|   1365 |    1058 | 756174 |               513466 |      1002 | 1.05202e+06 | 1.2342e+06  |
|   1366 |    1053 | 742168 |               515394 |      1001 | 1.06202e+06 | 1.23421e+06 |
|   1367 |    1665 | 662063 |               526875 |      1004 | 1.02402e+06 | 1.23427e+06 |
|   1368 |    2393 | 717342 |               505780 |      1016 | 1.04101e+06 | 1.23427e+06 |


### Income_Code

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL01
      type: UInt16
    
    ```
#### Column Codes

| Years     | Income_Code                                       |
|:----------|:--------------------------------------------------|
| 1363-1368 | [COL01](/HBSIR/tables/raw/old_other_income#col01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |    7306 | 517.39 |                 5.27 |       511 |      521 |       523 |
|   1364 |    5407 | 516.15 |                 4.6  |       511 |      514 |       522 |
|   1365 |    1058 | 515.35 |                 4.48 |       511 |      512 |       522 |
|   1366 |    1053 | 515.49 |                 4.6  |       511 |      512 |       522 |
|   1367 |    1665 | 515.96 |                 4.64 |       511 |      514 |       522 |
|   1368 |    2393 | 515.7  |                 4.57 |       511 |      513 |       522 |


### Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL04
      type: float
    
    ```
#### Column Codes

| Years     | Income                                            |
|:----------|:--------------------------------------------------|
| 1363-1368 | [COL04](/HBSIR/tables/raw/old_other_income#col04) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |    Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|-----------:|
|   1363 |    7306 | 152855 |               267234 |       100 |    48000 | 8.5858e+06 |
|   1364 |    5407 | 194604 |               283868 |       100 |    84000 | 8.5e+06    |
|   1365 |    1058 | 245697 |               329179 |      1500 |   130000 | 3.2e+06    |
|   1366 |    1053 | 255828 |               307361 |      1500 |   160000 | 3.936e+06  |
|   1367 |    1665 | 252294 |               298843 |      1000 |   160000 | 4.32e+06   |
|   1368 |    2393 | 281533 |               317141 |       100 |   216000 | 5.562e+06  |


