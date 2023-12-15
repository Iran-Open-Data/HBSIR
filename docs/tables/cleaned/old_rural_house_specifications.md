# old_rural_house_specifications

## Old to New Titles

| Years     | ADDRESS   | Q1             | Q2                            | Q3              | Q4                       | Q4_01   | Q4_02      | Q4_03   | Q4_04          | Q4_05   | Q4_06    | Q4_07   | Q4_08        | Q4_09   | Q4_1   | Q4_2       | Q4_3    | Q4_4           | Q4_5   | Q4_6     | Q4_7   | Q4_8         | Q4_9   | Q5              | Q5_1       | Q5_2        | Q5_3        | Q5_4     | Q5_5            | Q6_01   | Q6_02      | Q6_03   | Q6_04          | Q6_05   | Q6_06    | Q6_07   | Q6_08        | Q6_09   | Q7_1       | Q7_2        | Q7_3        | Q7_4     | Q7_5            |
|:----------|:----------|:---------------|:------------------------------|:----------------|:-------------------------|:--------|:-----------|:--------|:---------------|:--------|:---------|:--------|:-------------|:--------|:-------|:-----------|:--------|:---------------|:-------|:---------|:-------|:-------------|:-------|:----------------|:-----------|:------------|:------------|:---------|:----------------|:--------|:-----------|:--------|:---------------|:--------|:---------|:--------|:-------------|:--------|:-----------|:------------|:------------|:---------|:----------------|
| 1363      | ID        | Tenure         | Structure_Main_Materials      | Number_of_Rooms |                          | Car     | Motorcycle | Bicycle | Sewing_Machine | Radio   | Cassette | TV      | Refrigerator | Oven    |        |            |         |                |        |          |        |              |        |                 | Pipe_Water | Electricity | Natural_Gas | Bathroom | Air_Conditioner |         |            |         |                |         |          |         |              |         |            |             |             |          |                 |
| 1364-1365 | ID        | Lives_in_House | Number_of_Households_in_House | Tenure          | Structure_Main_Materials |         |            |         |                |         |          |         |              |         |        |            |         |                |        |          |        |              |        | Number_of_Rooms |            |             |             |          |                 | Car     | Motorcycle | Bicycle | Sewing_Machine | Radio   | Cassette | TV      | Refrigerator | Oven    | Pipe_Water | Electricity | Natural_Gas | Bathroom | Air_Conditioner |
| 1366-1368 | ID        | Tenure         | Structure_Main_Materials      | Number_of_Rooms |                          |         |            |         |                |         |          |         |              |         | Car    | Motorcycle | Bicycle | Sewing_Machine | Radio  | Cassette | TV     | Refrigerator | Oven   |                 | Pipe_Water | Electricity | Natural_Gas | Bathroom | Air_Conditioner |         |            |         |                |         |          |         |              |         |            |             |             |          |                 |


## New to Old Titles

| Years     | ID      | Tenure   | Structure_Main_Materials   | Number_of_Rooms   | Car   | Motorcycle   | Bicycle   | Sewing_Machine   | Radio   | Cassette   | TV    | Refrigerator   | Oven   | Pipe_Water   | Electricity   | Natural_Gas   | Bathroom   | Air_Conditioner   | Lives_in_House   | Number_of_Households_in_House   |
|:----------|:--------|:---------|:---------------------------|:------------------|:------|:-------------|:----------|:-----------------|:--------|:-----------|:------|:---------------|:-------|:-------------|:--------------|:--------------|:-----------|:------------------|:-----------------|:--------------------------------|
| 1363      | ADDRESS | Q1       | Q2                         | Q3                | Q4_01 | Q4_02        | Q4_03     | Q4_04            | Q4_05   | Q4_06      | Q4_07 | Q4_08          | Q4_09  | Q5_1         | Q5_2          | Q5_3          | Q5_4       | Q5_5              |                  |                                 |
| 1364-1365 | ADDRESS | Q3       | Q4                         | Q5                | Q6_01 | Q6_02        | Q6_03     | Q6_04            | Q6_05   | Q6_06      | Q6_07 | Q6_08          | Q6_09  | Q7_1         | Q7_2          | Q7_3          | Q7_4       | Q7_5              | Q1               | Q2                              |
| 1366-1368 | ADDRESS | Q1       | Q2                         | Q3                | Q4_1  | Q4_2         | Q4_3      | Q4_4             | Q4_5    | Q4_6       | Q4_7  | Q4_8           | Q4_9   | Q5_1         | Q5_2          | Q5_3          | Q5_4       | Q5_5              |                  |                                 |


## Columns Details

### ID

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: ADDRESS
      type: UInt64
    
    ```
#### Column Codes

| Years     | ID                                                                  |
|:----------|:--------------------------------------------------------------------|
| 1363-1368 | [ADDRESS](/HBSIR/tables/raw/old_rural_house_specifications#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|----------:|
|   1363 |   12420 | 100225   |              66111.6 |      1001 |  92275.5 |    234095 |
|   1364 |   13587 | 103423   |              68964.5 |      1001 |  93095   |    234175 |
|   1365 |    2944 |  85060.4 |              59754.5 |      1001 |  82003.5 |    234020 |
|   1366 |    3018 |  93417.3 |              65008.7 |      1001 |  91039.5 |    234045 |
|   1367 |    4331 |  95123.2 |              62768.9 |      1001 |  92098   |    234055 |
|   1368 |    6028 |  86255.8 |              63541.8 |      1001 |  84022.5 |    234055 |


### Tenure

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q1
      type: category
      categories:
        1: Owned_Estate_Land
        2: Owned_Estate
        3: Rent
        4: Mortgage
        5: Service
        6: Free
        7: Other
    1364:
      column_code: Q3
      type: category
      categories:
        1: Owned_Estate_Land
        2: Owned_Estate
        3: Rent
        4: Mortgage
        5: Service
        6: Free
        7: Other
    1366:
      column_code: Q1
      type: category
      categories:
        1: Owned_Estate_Land
        2: Owned_Estate
        3: Rent
        4: Mortgage
        5: Service
        6: Free
        7: Other
    
    ```
#### Column Codes

| Years     | Tenure                                                    |
|:----------|:----------------------------------------------------------|
| 1363      | [Q1](/HBSIR/tables/raw/old_rural_house_specifications#q1) |
| 1364-1365 | [Q3](/HBSIR/tables/raw/old_rural_house_specifications#q3) |
| 1366-1368 | [Q1](/HBSIR/tables/raw/old_rural_house_specifications#q1) |


#### Summary Statistics

**category data**

|   Year |   Owned_Estate_Land |   Service |   Rent | Mortgage   |   Owned_Estate |   Free |
|-------:|--------------------:|----------:|-------:|:-----------|---------------:|-------:|
|   1363 |               88.31 |      1.34 |   1.1  | 0.03       |           1.47 |   7.75 |
|   1364 |               84.16 |      1.49 |   1.38 | 0.06       |           3.32 |   9.59 |
|   1365 |               87.47 |      1.15 |   1.32 |            |           0.92 |   9.14 |
|   1366 |               84.53 |      8.65 |   2.12 | 2.42       |           2.22 |   0.07 |
|   1367 |               86.4  |      7.25 |   1.57 | 1.8        |           2.79 |   0.18 |
|   1368 |               89.12 |      6.8  |   1.53 | 1.43       |           1.08 |   0.05 |


#### Categories

|    | 1363-1368         |
|---:|:------------------|
|  1 | Owned_Estate_Land |
|  2 | Owned_Estate      |
|  3 | Rent              |
|  4 | Mortgage          |
|  5 | Service           |
|  6 | Free              |
|  7 | Other             |


### Structure_Main_Materials

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q2
      type: category
      categories:
        1: Cement_Block
        2: Brick_Stone_Iron
        3: Brick_Stone_Wood
        4: Adobe_Clay_Wood
        5: Tent
        6: Other
    1364:
      column_code: Q4
      type: category
      categories:
        1: Cement_Block
        2: Brick_Stone_Iron
        3: Brick_Stone_Wood
        4: Adobe_Clay_Wood
        5: Tent
        6: Other
    1366:
      column_code: Q2
      type: category
      categories:
        1: Metal_and_Reinforced_Concrete
        2: Brick_Stone_Block_Joist
        3: Brick_Stone_Wood
        4: Cement_Block
        5: Brick_Stone
        6: Wood
        7: Adobe_Wood
        8: Adobe_Clay
        9: Other
    
    ```
#### Column Codes

| Years     | Structure_Main_Materials                                  |
|:----------|:----------------------------------------------------------|
| 1363      | [Q2](/HBSIR/tables/raw/old_rural_house_specifications#q2) |
| 1364-1365 | [Q4](/HBSIR/tables/raw/old_rural_house_specifications#q4) |
| 1366-1368 | [Q2](/HBSIR/tables/raw/old_rural_house_specifications#q2) |


#### Summary Statistics

**category data**

|   Year | Adobe_Wood   |   Brick_Stone_Wood | Brick_Stone_Block_Joist   | Adobe_Clay   |   Cement_Block |   Other | Wood   | Brick_Stone   | Metal_and_Reinforced_Concrete   | Adobe_Clay_Wood   | Brick_Stone_Iron   | Tent   |
|-------:|:-------------|-------------------:|:--------------------------|:-------------|---------------:|--------:|:-------|:--------------|:--------------------------------|:------------------|:-------------------|:-------|
|   1363 |              |              12.42 |                           |              |           3.87 |    1.18 |        |               |                                 | 70.44             | 9.45               | 2.64   |
|   1364 |              |              12.74 |                           |              |          12.77 |    2.27 |        |               |                                 | 51.09             | 11.95              | 9.19   |
|   1365 |              |              11.28 |                           |              |          11.07 |    0.58 |        |               |                                 | 55.43             | 13.45              | 8.19   |
|   1366 | 35.59        |              19.85 | 16.96                     | 15.61        |           6.2  |    3.98 | 0.46   | 0.5           | 0.86                            |                   |                    |        |
|   1367 | 36.25        |              20.23 | 15.86                     | 16.53        |           5.56 |    4.32 | 0.16   | 0.55          | 0.53                            |                   |                    |        |
|   1368 | 43.21        |              20.54 | 16.59                     | 11.63        |           5.33 |    1.51 | 0.46   | 0.4           | 0.33                            |                   |                    |        |


#### Categories

|    | 1363-1365        | 1366-1368                     |
|---:|:-----------------|:------------------------------|
|  1 | Cement_Block     | Metal_and_Reinforced_Concrete |
|  2 | Brick_Stone_Iron | Brick_Stone_Block_Joist       |
|  3 | Brick_Stone_Wood | Brick_Stone_Wood              |
|  4 | Adobe_Clay_Wood  | Cement_Block                  |
|  5 | Tent             | Brick_Stone                   |
|  6 | Other            | Wood                          |
|  7 |                  | Adobe_Wood                    |
|  8 |                  | Adobe_Clay                    |
|  9 |                  | Other                         |


### Number_of_Rooms

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q3
      type: UInt8
    1364:
      column_code: Q5
      type: UInt8
    1366:
      column_code: Q3
      type: UInt8
    
    ```
#### Column Codes

| Years     | Number_of_Rooms                                           |
|:----------|:----------------------------------------------------------|
| 1363      | [Q3](/HBSIR/tables/raw/old_rural_house_specifications#q3) |
| 1364-1365 | [Q5](/HBSIR/tables/raw/old_rural_house_specifications#q5) |
| 1366-1368 | [Q3](/HBSIR/tables/raw/old_rural_house_specifications#q3) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |   12420 |   2.47 |                 1.22 |         1 |        2 |        15 |
|   1364 |   13587 |   2.51 |                 1.32 |         0 |        2 |        40 |
|   1365 |    2944 |   2.55 |                 1.3  |         1 |        2 |        22 |
|   1366 |    3018 |   2.71 |                 1.36 |         0 |        2 |         9 |
|   1367 |    4331 |   2.76 |                 1.35 |         1 |        3 |         9 |
|   1368 |    6028 |   2.81 |                 1.29 |         0 |        3 |         9 |


### Car

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1364:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1365:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1366:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1367:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1368:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1369:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1370:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1371:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1372:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1373:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1374:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1375:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1376:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1377:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1378:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1379:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1380:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1381:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1382:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1383:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1384:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1385:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1386:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1387:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1388:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1389:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1390:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1391:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1392:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1393:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1394:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1395:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1396:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1397:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1398:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1399:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1400:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    1401:
      column_code: Q6_01
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Car                                                             |
|:----------|:----------------------------------------------------------------|
| 1363      | [Q4_01](/HBSIR/tables/raw/old_rural_house_specifications#q4_01) |
| 1364-1365 | [Q6_01](/HBSIR/tables/raw/old_rural_house_specifications#q6_01) |
| 1366-1368 | [Q4_1](/HBSIR/tables/raw/old_rural_house_specifications#q4_1)   |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   97.23 |   2.77 |         0 |
|   1364 |   97.42 |   2.58 |         0 |
|   1365 |   97.52 |   2.48 |         0 |
|   1366 |   97.15 |   2.85 |         0 |
|   1367 |   96.63 |   3.37 |         0 |
|   1368 |   97.13 |   2.87 |         0 |


### Motorcycle

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1364:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1365:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1366:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1367:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1368:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1369:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1370:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1371:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1372:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1373:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1374:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1375:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1376:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1377:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1378:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1379:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1380:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1381:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1382:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1383:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1384:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1385:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1386:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1387:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1388:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1389:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1390:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1391:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1392:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1393:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1394:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1395:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1396:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1397:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1398:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1399:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1400:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    1401:
      column_code: Q6_02
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Motorcycle                                                      |
|:----------|:----------------------------------------------------------------|
| 1363      | [Q4_02](/HBSIR/tables/raw/old_rural_house_specifications#q4_02) |
| 1364-1365 | [Q6_02](/HBSIR/tables/raw/old_rural_house_specifications#q6_02) |
| 1366-1368 | [Q4_2](/HBSIR/tables/raw/old_rural_house_specifications#q4_2)   |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   85.48 |  14.52 |         0 |
|   1364 |   84.26 |  15.74 |         0 |
|   1365 |   85.63 |  14.37 |         0 |
|   1366 |   84.96 |  15.04 |         0 |
|   1367 |   87.16 |  12.84 |         0 |
|   1368 |   87.99 |  12.01 |         0 |


### Bicycle

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1364:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1365:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1366:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1367:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1368:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1369:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1370:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1371:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1372:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1373:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1374:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1375:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1376:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1377:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1378:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1379:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1380:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1381:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1382:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1383:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1384:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1385:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1386:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1387:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1388:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1389:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1390:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1391:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1392:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1393:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1394:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1395:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1396:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1397:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1398:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1399:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1400:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    1401:
      column_code: Q6_03
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Bicycle                                                         |
|:----------|:----------------------------------------------------------------|
| 1363      | [Q4_03](/HBSIR/tables/raw/old_rural_house_specifications#q4_03) |
| 1364-1365 | [Q6_03](/HBSIR/tables/raw/old_rural_house_specifications#q6_03) |
| 1366-1368 | [Q4_3](/HBSIR/tables/raw/old_rural_house_specifications#q4_3)   |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   90.72 |   9.28 |         0 |
|   1364 |   91.76 |   8.24 |         0 |
|   1365 |   91.85 |   8.15 |         0 |
|   1366 |   90.52 |   9.48 |         0 |
|   1367 |   90.95 |   9.05 |         0 |
|   1368 |   92.04 |   7.96 |         0 |


### Sewing_Machine

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1364:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1365:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1366:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1367:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1368:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1369:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1370:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1371:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1372:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1373:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1374:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1375:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1376:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1377:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1378:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1379:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1380:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1381:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1382:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1383:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1384:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1385:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1386:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1387:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1388:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1389:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1390:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1391:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1392:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1393:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1394:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1395:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1396:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1397:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1398:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1399:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1400:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    1401:
      column_code: Q6_04
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Sewing_Machine                                                  |
|:----------|:----------------------------------------------------------------|
| 1363      | [Q4_04](/HBSIR/tables/raw/old_rural_house_specifications#q4_04) |
| 1364-1365 | [Q6_04](/HBSIR/tables/raw/old_rural_house_specifications#q6_04) |
| 1366-1368 | [Q4_4](/HBSIR/tables/raw/old_rural_house_specifications#q4_4)   |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   60.58 |  39.42 |         0 |
|   1364 |   58.58 |  41.42 |         0 |
|   1365 |   56.32 |  43.68 |         0 |
|   1366 |   54.08 |  45.92 |         0 |
|   1367 |   54.58 |  45.42 |         0 |
|   1368 |   55.96 |  44.04 |         0 |


### Radio

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1364:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1365:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1366:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1367:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1368:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1369:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1370:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1371:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1372:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1373:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1374:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1375:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1376:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1377:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1378:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1379:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1380:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1381:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1382:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1383:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1384:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1385:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1386:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1387:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1388:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1389:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1390:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1391:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1392:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1393:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1394:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1395:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1396:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1397:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1398:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1399:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1400:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    1401:
      column_code: Q6_05
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Radio                                                           |
|:----------|:----------------------------------------------------------------|
| 1363      | [Q4_05](/HBSIR/tables/raw/old_rural_house_specifications#q4_05) |
| 1364-1365 | [Q6_05](/HBSIR/tables/raw/old_rural_house_specifications#q6_05) |
| 1366-1368 | [Q4_5](/HBSIR/tables/raw/old_rural_house_specifications#q4_5)   |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1363 |  58.72 |   41.28 |         0 |
|   1364 |  56.53 |   43.47 |         0 |
|   1365 |  56.52 |   43.48 |         0 |
|   1366 |  58.28 |   41.72 |         0 |
|   1367 |  55.46 |   44.54 |         0 |
|   1368 |  59.29 |   40.71 |         0 |


### Cassette

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1364:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1365:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1366:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1367:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1368:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1369:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1370:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1371:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1372:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1373:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1374:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1375:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1376:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1377:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1378:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1379:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1380:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1381:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1382:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1383:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1384:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1385:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1386:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1387:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1388:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1389:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1390:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1391:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1392:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1393:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1394:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1395:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1396:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1397:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1398:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1399:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1400:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    1401:
      column_code: Q6_06
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Cassette                                                        |
|:----------|:----------------------------------------------------------------|
| 1363      | [Q4_06](/HBSIR/tables/raw/old_rural_house_specifications#q4_06) |
| 1364-1365 | [Q6_06](/HBSIR/tables/raw/old_rural_house_specifications#q6_06) |
| 1366-1368 | [Q4_6](/HBSIR/tables/raw/old_rural_house_specifications#q4_6)   |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   66.42 |  33.58 |         0 |
|   1364 |   67.43 |  32.57 |         0 |
|   1365 |   66.88 |  33.12 |         0 |
|   1366 |   63.42 |  36.58 |         0 |
|   1367 |   64.63 |  35.37 |         0 |
|   1368 |   62.44 |  37.56 |         0 |


### TV

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1364:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1365:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1366:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1367:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1368:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1369:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1370:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1371:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1372:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1373:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1374:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1375:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1376:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1377:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1378:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1379:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1380:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1381:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1382:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1383:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1384:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1385:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1386:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1387:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1388:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1389:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1390:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1391:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1392:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1393:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1394:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1395:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1396:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1397:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1398:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1399:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1400:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    1401:
      column_code: Q6_07
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | TV                                                              |
|:----------|:----------------------------------------------------------------|
| 1363      | [Q4_07](/HBSIR/tables/raw/old_rural_house_specifications#q4_07) |
| 1364-1365 | [Q6_07](/HBSIR/tables/raw/old_rural_house_specifications#q6_07) |
| 1366-1368 | [Q4_7](/HBSIR/tables/raw/old_rural_house_specifications#q4_7)   |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   74.24 |  25.76 |         0 |
|   1364 |   71.3  |  28.7  |         0 |
|   1365 |   69.23 |  30.77 |         0 |
|   1366 |   62.59 |  37.41 |         0 |
|   1367 |   62.46 |  37.54 |         0 |
|   1368 |   59.02 |  40.98 |         0 |


### Refrigerator

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1364:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1365:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1366:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1367:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1368:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1369:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1370:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1371:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1372:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1373:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1374:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1375:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1376:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1377:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1378:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1379:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1380:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1381:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1382:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1383:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1384:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1385:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1386:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1387:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1388:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1389:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1390:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1391:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1392:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1393:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1394:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1395:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1396:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1397:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1398:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1399:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1400:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    1401:
      column_code: Q6_08
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Refrigerator                                                    |
|:----------|:----------------------------------------------------------------|
| 1363      | [Q4_08](/HBSIR/tables/raw/old_rural_house_specifications#q4_08) |
| 1364-1365 | [Q6_08](/HBSIR/tables/raw/old_rural_house_specifications#q6_08) |
| 1366-1368 | [Q4_8](/HBSIR/tables/raw/old_rural_house_specifications#q4_8)   |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   63.52 |  36.48 |         0 |
|   1364 |   59.8  |  40.2  |         0 |
|   1365 |   56.39 |  43.61 |         0 |
|   1366 |   50.63 |  49.37 |         0 |
|   1367 |   52    |  48    |         0 |
|   1368 |   50.71 |  49.29 |         0 |


### Oven

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1364:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1365:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1366:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1367:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1368:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1369:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1370:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1371:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1372:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1373:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1374:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1375:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1376:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1377:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1378:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1379:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1380:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1381:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1382:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1383:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1384:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1385:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1386:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1387:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1388:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1389:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1390:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1391:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1392:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1393:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1394:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1395:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1396:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1397:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1398:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1399:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1400:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    1401:
      column_code: Q6_09
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Oven                                                            |
|:----------|:----------------------------------------------------------------|
| 1363      | [Q4_09](/HBSIR/tables/raw/old_rural_house_specifications#q4_09) |
| 1364-1365 | [Q6_09](/HBSIR/tables/raw/old_rural_house_specifications#q6_09) |
| 1366-1368 | [Q4_9](/HBSIR/tables/raw/old_rural_house_specifications#q4_9)   |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1363 |  46.62 |   53.38 |         0 |
|   1364 |  48.29 |   51.71 |         0 |
|   1365 |  48.37 |   51.63 |         0 |
|   1366 |  56.89 |   43.11 |         0 |
|   1367 |  52.09 |   47.91 |         0 |
|   1368 |  56.2  |   43.8  |         0 |


### Pipe_Water

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1364:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1365:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1366:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1367:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1368:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1369:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1370:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1371:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1372:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1373:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1374:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1375:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1376:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1377:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1378:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1379:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1380:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1381:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1382:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1383:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1384:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1385:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1386:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1387:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1388:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1389:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1390:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1391:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1392:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1393:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1394:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1395:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1396:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1397:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1398:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1399:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1400:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    1401:
      column_code: Q7_1
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Pipe_Water                                                    |
|:----------|:--------------------------------------------------------------|
| 1363      | [Q5_1](/HBSIR/tables/raw/old_rural_house_specifications#q5_1) |
| 1364-1365 | [Q7_1](/HBSIR/tables/raw/old_rural_house_specifications#q7_1) |
| 1366-1368 | [Q5_1](/HBSIR/tables/raw/old_rural_house_specifications#q5_1) |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1363 |  44.92 |   55.08 |         0 |
|   1364 |  48.31 |   51.69 |         0 |
|   1365 |  50.27 |   49.73 |         0 |
|   1366 |  57.26 |   42.74 |         0 |
|   1367 |  56.62 |   43.38 |         0 |
|   1368 |  56.49 |   43.51 |         0 |


### Electricity

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1364:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1365:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1366:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1367:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1368:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1369:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1370:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1371:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1372:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1373:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1374:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1375:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1376:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1377:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1378:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1379:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1380:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1381:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1382:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1383:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1384:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1385:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1386:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1387:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1388:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1389:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1390:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1391:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1392:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1393:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1394:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1395:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1396:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1397:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1398:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1399:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1400:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    1401:
      column_code: Q7_2
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Electricity                                                   |
|:----------|:--------------------------------------------------------------|
| 1363      | [Q5_2](/HBSIR/tables/raw/old_rural_house_specifications#q5_2) |
| 1364-1365 | [Q7_2](/HBSIR/tables/raw/old_rural_house_specifications#q7_2) |
| 1366-1368 | [Q5_2](/HBSIR/tables/raw/old_rural_house_specifications#q5_2) |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1363 |  57.79 |   42.21 |         0 |
|   1364 |  59.77 |   40.23 |         0 |
|   1365 |  64.16 |   35.84 |         0 |
|   1366 |  69.32 |   30.68 |         0 |
|   1367 |  68.46 |   31.54 |         0 |
|   1368 |  70.8  |   29.2  |         0 |


### Natural_Gas

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1364:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1365:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1366:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1367:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1368:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1369:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1370:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1371:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1372:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1373:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1374:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1375:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1376:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1377:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1378:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1379:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1380:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1381:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1382:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1383:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1384:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1385:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1386:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1387:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1388:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1389:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1390:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1391:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1392:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1393:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1394:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1395:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1396:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1397:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1398:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1399:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1400:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    1401:
      column_code: Q7_3
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Natural_Gas                                                   |
|:----------|:--------------------------------------------------------------|
| 1363      | [Q5_3](/HBSIR/tables/raw/old_rural_house_specifications#q5_3) |
| 1364-1365 | [Q7_3](/HBSIR/tables/raw/old_rural_house_specifications#q7_3) |
| 1366-1368 | [Q5_3](/HBSIR/tables/raw/old_rural_house_specifications#q5_3) |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   99.77 |   0.23 |         0 |
|   1364 |   99.5  |   0.5  |         0 |
|   1365 |   99.25 |   0.75 |         0 |
|   1366 |   99.34 |   0.66 |         0 |
|   1367 |   98.94 |   1.06 |         0 |
|   1368 |   99.37 |   0.63 |         0 |


### Bathroom

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1364:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1365:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1366:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1367:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1368:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1369:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1370:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1371:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1372:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1373:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1374:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1375:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1376:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1377:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1378:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1379:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1380:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1381:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1382:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1383:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1384:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1385:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1386:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1387:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1388:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1389:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1390:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1391:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1392:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1393:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1394:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1395:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1396:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1397:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1398:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1399:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1400:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    1401:
      column_code: Q7_4
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Bathroom                                                      |
|:----------|:--------------------------------------------------------------|
| 1363      | [Q5_4](/HBSIR/tables/raw/old_rural_house_specifications#q5_4) |
| 1364-1365 | [Q7_4](/HBSIR/tables/raw/old_rural_house_specifications#q7_4) |
| 1366-1368 | [Q5_4](/HBSIR/tables/raw/old_rural_house_specifications#q5_4) |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   91.7  |   8.3  |         0 |
|   1364 |   91.05 |   8.95 |         0 |
|   1365 |   90.35 |   9.65 |         0 |
|   1366 |   86.15 |  13.85 |         0 |
|   1367 |   86.59 |  13.41 |         0 |
|   1368 |   87.59 |  12.41 |         0 |


### Air_Conditioner

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1364:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1365:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1366:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1367:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1368:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1369:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1370:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1371:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1372:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1373:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1374:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1375:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1376:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1377:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1378:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1379:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1380:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1381:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1382:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1383:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1384:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1385:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1386:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1387:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1388:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1389:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1390:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1391:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1392:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1393:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1394:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1395:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1396:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1397:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1398:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1399:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1400:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    1401:
      column_code: Q7_5
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Air_Conditioner                                               |
|:----------|:--------------------------------------------------------------|
| 1363      | [Q5_5](/HBSIR/tables/raw/old_rural_house_specifications#q5_5) |
| 1364-1365 | [Q7_5](/HBSIR/tables/raw/old_rural_house_specifications#q7_5) |
| 1366-1368 | [Q5_5](/HBSIR/tables/raw/old_rural_house_specifications#q5_5) |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1363 |   94.8  |   5.2  |         0 |
|   1364 |   93.85 |   6.15 |         0 |
|   1365 |   94.33 |   5.67 |         0 |
|   1366 |   91.19 |   8.81 |         0 |
|   1367 |   91.3  |   8.7  |         0 |
|   1368 |   93.41 |   6.59 |         0 |


### Lives_in_House

??? abstract "Column Metadata"
    ``` yaml
    1364:
      column_code: Q1
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Lives_in_House                                            |
|:----------|:----------------------------------------------------------|
| 1363      |                                                           |
| 1364-1365 | [Q1](/HBSIR/tables/raw/old_rural_house_specifications#q1) |
| 1366-1368 |                                                           |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1364 |  97.54 |    2.46 |         0 |
|   1365 |  99.15 |    0.85 |         0 |


### Number_of_Households_in_House

??? abstract "Column Metadata"
    ``` yaml
    1364:
      column_code: Q2
      type: UInt8
    
    ```
#### Column Codes

| Years     | Number_of_Households_in_House                             |
|:----------|:----------------------------------------------------------|
| 1363      |                                                           |
| 1364-1365 | [Q2](/HBSIR/tables/raw/old_rural_house_specifications#q2) |
| 1366-1368 |                                                           |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1364 |   13322 |   1.34 |                 0.76 |         0 |        1 |        16 |
|   1365 |    2926 |   1.31 |                 0.77 |         1 |        1 |        16 |


