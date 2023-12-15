# self_employed_income

## Old to New Titles

| Years     | ADDRESS   | COL01         | COL02             | COL03           | COL04           | COL05           | COL06           | COL07         | COL08                 | COL09                 | COL10        | COL11        | COL12   | COL13   |
|:----------|:----------|:--------------|:------------------|:----------------|:----------------|:----------------|:----------------|:--------------|:----------------------|:----------------------|:-------------|:-------------|:--------|:--------|
| 1369-1373 | ID        | Member_Number | Occupation_Code   | Industry_Code   | Employment_Type | Is_Agricultural | Wage_Cost       | Cost_of_Sales | Other_Operating_Costs | Other_Costs           | Business_Tax | Sales        | Profit  |         |
| 1374-1383 | ID        | Member_Number | Employment_Status | Occupation_Code | Industry_Code   | Employment_Type | Is_Agricultural | Wage_Cost     | Cost_of_Sales         | Other_Operating_Costs | Other_Costs  | Business_Tax | Sales   | Profit  |


| Years     | ADDRESS   | DYCOL01       | DYCOL02           | DYCOL03         | DYCOL04       | DYCOL05         | DYCOL06         | DYCOL07               | DYCOL08              | DYCOL09   | DYCOL10       | DYCOL11               | DYCOL12     | DYCOL13      | DYCOL14   | DYCOL15   |
|:----------|:----------|:--------------|:------------------|:----------------|:--------------|:----------------|:----------------|:----------------------|:---------------------|:----------|:--------------|:----------------------|:------------|:-------------|:----------|:----------|
| 1384-1401 | ID        | Member_Number | Employment_Status | Occupation_Code | Industry_Code | Employment_Type | Is_Agricultural | Working_Hours_per_Day | Working_Day_per_Week | Wage_Cost | Cost_of_Sales | Other_Operating_Costs | Other_Costs | Business_Tax | Sales     | Profit    |


## New to Old Titles

| Years     | ID      | Member_Number   | Employment_Status   | Occupation_Code   | Industry_Code   | Employment_Type   | Is_Agricultural   | Working_Hours_per_Day   | Working_Day_per_Week   | Wage_Cost   | Cost_of_Sales   | Other_Operating_Costs   | Other_Costs   | Business_Tax   | Sales   | Profit   |
|:----------|:--------|:----------------|:--------------------|:------------------|:----------------|:------------------|:------------------|:------------------------|:-----------------------|:------------|:----------------|:------------------------|:--------------|:---------------|:--------|:---------|
| 1369-1373 | ADDRESS | COL01           |                     | COL02             | COL03           | COL04             | COL05             |                         |                        | COL06       | COL07           | COL08                   | COL09         | COL10          | COL11   | COL12    |
| 1374-1383 | ADDRESS | COL01           | COL02               | COL03             | COL04           | COL05             | COL06             |                         |                        | COL07       | COL08           | COL09                   | COL10         | COL11          | COL12   | COL13    |
| 1384-1401 | ADDRESS | DYCOL01         | DYCOL02             | DYCOL03           | DYCOL04         | DYCOL05           | DYCOL06           | DYCOL07                 | DYCOL08                | DYCOL09     | DYCOL10         | DYCOL11                 | DYCOL12       | DYCOL13        | DYCOL14 | DYCOL15  |


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

| Years     | ID                                                        |
|:----------|:----------------------------------------------------------|
| 1369-1401 | [ADDRESS](/HBSIR/tables/raw/self_employed_income#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |         Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------------:|-----------------:|------------:|
|   1369 |   24550 | 335719           |     444482           |  1004           | 103138           | 1.23422e+06 |
|   1370 |   23960 | 340951           |     444497           |  1004           | 111048           | 1.23422e+06 |
|   1371 |   24136 | 349043           |     446335           |  1001           | 122004           | 1.23422e+06 |
|   1372 |   15377 | 356405           |     455167           |  1001           | 103086           | 1.23422e+06 |
|   1373 |   21557 | 443468           |     493529           |  1001           | 132001           | 1.24404e+06 |
|   1374 |   44077 |      4.18012e+06 |          4.6953e+06  | 10001           |      1.72001e+06 | 1.24401e+07 |
|   1375 |   27840 | 331547           |     444709           |  1001           |  94198           | 1.24403e+06 |
|   1376 |   26580 | 336165           |     446629           |  1002           |  94216.5         | 1.25406e+06 |
|   1377 |   22012 |      3.39517e+07 |          4.42501e+07 | 11001           |      1.01031e+07 | 1.27074e+08 |
|   1378 |   34611 |      3.61673e+07 |          4.42797e+07 | 11001           |      1.50531e+07 | 1.27074e+08 |
|   1379 |   32478 |      3.56699e+07 |          4.36712e+07 | 11001           |      1.50931e+07 | 1.27074e+08 |
|   1380 |   30263 |      3.58422e+07 |          4.38972e+07 | 11001           |      1.6043e+07  | 1.27074e+08 |
|   1381 |   35032 |      3.73791e+07 |          4.44991e+07 | 11001           |      1.70241e+07 | 1.27074e+08 |
|   1382 |   25550 |      3.82008e+07 |          4.50984e+07 | 11002           |      1.7011e+07  | 1.27114e+08 |
|   1383 |   27634 |      3.74695e+07 |          4.46284e+07 | 11001           |      1.60621e+07 | 1.27114e+08 |
|   1384 |   29117 |      3.8381e+07  |          4.4749e+07  | 11003           |      1.70421e+07 | 1.29214e+08 |
|   1385 |   32590 |      3.58351e+07 |          4.43087e+07 | 11001           |      1.6011e+07  | 1.29214e+08 |
|   1386 |   29505 |      3.93193e+07 |          4.52509e+07 | 11001           |      1.80341e+07 | 1.29214e+08 |
|   1387 |   31454 |      1.86082e+09 |          4.49535e+08 |     1e+09       |      2.06177e+09 | 2.29786e+09 |
|   1388 |   29622 |      1.82879e+09 |          4.61548e+08 |     1e+09       |      2.05016e+09 | 2.29025e+09 |
|   1389 |   28653 |      1.8561e+09  |          4.47243e+08 |     1e+09       |      2.05011e+09 | 2.29013e+09 |
|   1390 |   26002 |      1.84836e+09 |          4.52434e+08 |     1.00001e+09 |      2.0501e+09  | 2.30013e+09 |
|   1391 |   26789 |      1.86275e+09 |          4.47142e+08 |     1e+09       |      2.06009e+09 | 2.30013e+09 |
|   1392 |   24493 |      1.84516e+10 |          4.5535e+09  |     1.0001e+10  |      2.05141e+10 | 2.30037e+10 |
|   1393 |   23498 |      1.84545e+10 |          4.5718e+09  |     1.0001e+10  |      2.05141e+10 | 2.30047e+10 |
|   1394 |   22404 |      1.83112e+10 |          4.63122e+09 |     1.0001e+10  |      2.05091e+10 | 2.30047e+10 |
|   1395 |   21822 |      1.82837e+10 |          4.65243e+09 |     1.0001e+10  |      2.05101e+10 | 2.30047e+10 |
|   1396 |   22290 |      1.83363e+10 |          4.64869e+09 |     1.0001e+10  |      2.05131e+10 | 2.30047e+10 |
|   1397 |   21988 |      1.79956e+10 |          4.807e+09   |     1.0001e+10  |      2.05104e+10 | 2.30067e+10 |
|   1398 |   21651 |      1.80563e+10 |          4.75611e+09 |     1.0001e+10  |      2.05054e+10 | 2.30067e+10 |
|   1399 |   19323 |      1.8131e+10  |          4.71779e+09 |     1.0001e+10  |      2.05094e+10 | 2.30067e+10 |
|   1400 |   18570 |      1.80035e+10 |          4.77232e+09 |     1.0001e+10  |      2.05044e+10 | 2.30067e+10 |
|   1401 |   17313 |      1.78946e+10 |          4.82908e+09 |     1.0001e+10  |      2.05074e+10 | 2.30067e+10 |


### Member_Number

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL01
      type: UInt8
    1364:
      column_code: DYCOL01
      type: UInt8
    1365:
      column_code: DYCOL01
      type: UInt8
    1366:
      column_code: DYCOL01
      type: UInt8
    1367:
      column_code: DYCOL01
      type: UInt8
    1368:
      column_code: DYCOL01
      type: UInt8
    1369:
      column_code: DYCOL01
      type: UInt8
    1370:
      column_code: DYCOL01
      type: UInt8
    1371:
      column_code: DYCOL01
      type: UInt8
    1372:
      column_code: DYCOL01
      type: UInt8
    1373:
      column_code: DYCOL01
      type: UInt8
    1374:
      column_code: DYCOL01
      type: UInt8
    1375:
      column_code: DYCOL01
      type: UInt8
    1376:
      column_code: DYCOL01
      type: UInt8
    1377:
      column_code: DYCOL01
      type: UInt8
    1378:
      column_code: DYCOL01
      type: UInt8
    1379:
      column_code: DYCOL01
      type: UInt8
    1380:
      column_code: DYCOL01
      type: UInt8
    1381:
      column_code: DYCOL01
      type: UInt8
    1382:
      column_code: DYCOL01
      type: UInt8
    1383:
      column_code: DYCOL01
      type: UInt8
    1384:
      column_code: DYCOL01
      type: UInt8
    1385:
      column_code: DYCOL01
      type: UInt8
    1386:
      column_code: DYCOL01
      type: UInt8
    1387:
      column_code: DYCOL01
      type: UInt8
    1388:
      column_code: DYCOL01
      type: UInt8
    1389:
      column_code: DYCOL01
      type: UInt8
    1390:
      column_code: DYCOL01
      type: UInt8
    1391:
      column_code: DYCOL01
      type: UInt8
    1392:
      column_code: DYCOL01
      type: UInt8
    1393:
      column_code: DYCOL01
      type: UInt8
    1394:
      column_code: DYCOL01
      type: UInt8
    1395:
      column_code: DYCOL01
      type: UInt8
    1396:
      column_code: DYCOL01
      type: UInt8
    1397:
      column_code: DYCOL01
      type: UInt8
    1398:
      column_code: DYCOL01
      type: UInt8
    1399:
      column_code: DYCOL01
      type: UInt8
    1400:
      column_code: DYCOL01
      type: UInt8
    1401:
      column_code: DYCOL01
      type: UInt8
    
    ```
#### Column Codes

| Years     | Member_Number                                             |
|:----------|:----------------------------------------------------------|
| 1369-1383 | [COL01](/HBSIR/tables/raw/self_employed_income#col01)     |
| 1384-1401 | [DYCOL01](/HBSIR/tables/raw/self_employed_income#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1369 |   24550 |   1.69 |                 1.45 |         1 |        1 |        20 |
|   1370 |   23960 |   1.61 |                 1.34 |         0 |        1 |        23 |
|   1371 |   24136 |   1.67 |                 1.41 |         0 |        1 |        25 |
|   1372 |   15377 |   1.67 |                 1.52 |         1 |        1 |        91 |
|   1373 |   21557 |   1.69 |                 1.4  |         0 |        1 |        23 |
|   1374 |   44077 |   1.69 |                 1.42 |         0 |        1 |        51 |
|   1375 |   27840 |   1.77 |                 1.46 |         1 |        1 |        21 |
|   1376 |   26580 |   1.76 |                 1.47 |         1 |        1 |        23 |
|   1377 |   22012 |   1.77 |                 1.45 |         1 |        1 |        22 |
|   1378 |   34611 |   1.76 |                 1.42 |         1 |        1 |        16 |
|   1379 |   32478 |   1.77 |                 1.44 |         1 |        1 |        20 |
|   1380 |   30263 |   1.8  |                 1.46 |         1 |        1 |        21 |
|   1381 |   35032 |   1.8  |                 1.46 |         1 |        1 |        17 |
|   1382 |   25550 |   1.78 |                 1.43 |         1 |        1 |        20 |
|   1383 |   27634 |   1.8  |                 1.42 |         1 |        1 |        18 |
|   1384 |   29117 |   1.79 |                 1.41 |         1 |        1 |        15 |
|   1385 |   32590 |   1.85 |                 1.42 |         1 |        1 |        16 |
|   1386 |   29504 |   1.82 |                 1.38 |         1 |        1 |        19 |
|   1387 |   31450 |   1.76 |                 1.35 |         1 |        1 |        16 |
|   1388 |   29616 |   1.78 |                 1.37 |         1 |        1 |        19 |
|   1389 |   28652 |   1.72 |                 1.3  |         1 |        1 |        13 |
|   1390 |   25998 |   1.64 |                 1.2  |         1 |        1 |        13 |
|   1391 |   26787 |   1.65 |                 1.19 |         1 |        1 |        15 |
|   1392 |   24492 |   1.57 |                 1.08 |         1 |        1 |        12 |
|   1393 |   23495 |   1.55 |                 1.05 |         1 |        1 |        12 |
|   1394 |   22402 |   1.55 |                 1.07 |         1 |        1 |        14 |
|   1395 |   21822 |   1.52 |                 1.02 |         1 |        1 |        13 |
|   1396 |   22290 |   1.5  |                 0.99 |         1 |        1 |        16 |
|   1397 |   21983 |   1.48 |                 0.97 |         1 |        1 |        11 |
|   1398 |   21650 |   1.5  |                 0.97 |         1 |        1 |        11 |
|   1399 |   19322 |   1.5  |                 0.97 |         1 |        1 |        12 |
|   1400 |   18570 |   1.47 |                 0.92 |         1 |        1 |        11 |
|   1401 |   17313 |   1.44 |                 0.89 |         1 |        1 |         8 |


### Employment_Status

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1374:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1375:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1376:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1377:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1378:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1379:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1380:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1381:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1382:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1383:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1384:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1385:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1386:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1387:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1388:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1389:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1390:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1391:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1392:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1393:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1394:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1395:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1396:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1397:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1398:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1399:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1400:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    1401:
      column_code: DYCOL02
      type: category
      categories:
        1: Employed
        2: Unemployed
      replace:
        X01: null
        X02: null
        X03: null
        X04: null
        '3': null
        '9': null
        3: null
        4: null
        5: null
        6: null
        7: null
        9: null
    
    ```
#### Column Codes

| Years     | Employment_Status                                         |
|:----------|:----------------------------------------------------------|
| 1369-1373 |                                                           |
| 1374-1383 | [COL02](/HBSIR/tables/raw/self_employed_income#col02)     |
| 1384-1401 | [DYCOL02](/HBSIR/tables/raw/self_employed_income#dycol02) |


#### Summary Statistics

**category data**

|   Year |   Employed |   Unemployed | nan   |
|-------:|-----------:|-------------:|:------|
|   1374 |      96.54 |         3.39 | 0.07  |
|   1375 |      94.92 |         5.05 | 0.04  |
|   1376 |      97.16 |         2.84 |       |
|   1377 |      96.26 |         3.74 |       |
|   1378 |      95.59 |         4.41 |       |
|   1379 |      95.88 |         4.12 |       |
|   1380 |      95.99 |         4.01 |       |
|   1381 |      96.51 |         3.49 |       |
|   1382 |      97.24 |         2.76 |       |
|   1383 |      96.58 |         3.42 |       |
|   1384 |      95.74 |         4.26 |       |
|   1385 |      95.88 |         4.12 |       |
|   1386 |      95.57 |         4.42 | 0.0   |
|   1387 |      95.86 |         4.13 | 0.01  |
|   1388 |      96.29 |         3.69 | 0.02  |
|   1389 |      96.54 |         3.45 | 0.0   |
|   1390 |      97.14 |         2.85 | 0.02  |
|   1391 |      97.33 |         2.67 | 0.01  |
|   1392 |      98.17 |         1.82 | 0.0   |
|   1393 |      97.8  |         2.19 | 0.01  |
|   1394 |      97.75 |         2.25 | 0.0   |
|   1395 |      98.02 |         1.98 |       |
|   1396 |      98.06 |         1.94 |       |
|   1397 |      97.62 |         2.36 | 0.01  |
|   1398 |      97.54 |         2.46 | 0.0   |
|   1399 |      97.57 |         2.42 | 0.01  |
|   1400 |      98.29 |         1.71 |       |
|   1401 |      97.67 |         2.33 |       |


#### Categories

|    | 1374-1401   |
|---:|:------------|
|  1 | Employed    |
|  2 | Unemployed  |


#### Replacements

|   Year |   Value |   Replace_Value |   Frequency |
|-------:|--------:|----------------:|------------:|
|   1374 |       4 |             nan |           2 |
|   1374 |       5 |             nan |           1 |
|   1374 |       6 |             nan |           2 |
|   1374 |       7 |             nan |           1 |


### Occupation_Code

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL03
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
    1369:
      column_code: DYCOL03
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
    1370:
      column_code: DYCOL03
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
    1371:
      column_code: DYCOL03
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
    1372:
      column_code: DYCOL03
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
    1373:
      column_code: DYCOL03
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
    1374:
      column_code: DYCOL03
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
    1375:
      column_code: DYCOL03
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
    1376:
      column_code: DYCOL03
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
    1377:
      column_code: DYCOL03
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
    1378:
      column_code: DYCOL03
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
    1379:
      column_code: DYCOL03
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
    1380:
      column_code: DYCOL03
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
    1381:
      column_code: DYCOL03
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
    1382:
      column_code: DYCOL03
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
    1383:
      column_code: DYCOL03
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
    1384:
      column_code: DYCOL03
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
    1385:
      column_code: DYCOL03
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
    1386:
      column_code: DYCOL03
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
    1387:
      column_code: DYCOL03
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
    1388:
      column_code: DYCOL03
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
    1389:
      column_code: DYCOL03
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
    1390:
      column_code: DYCOL03
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
    1391:
      column_code: DYCOL03
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
    1392:
      column_code: DYCOL03
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
    1393:
      column_code: DYCOL03
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
    1394:
      column_code: DYCOL03
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
    1395:
      column_code: DYCOL03
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
    1396:
      column_code: DYCOL03
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
    1397:
      column_code: DYCOL03
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
    1398:
      column_code: DYCOL03
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
    1399:
      column_code: DYCOL03
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
    1400:
      column_code: DYCOL03
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
    1401:
      column_code: DYCOL03
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

| Years     | Occupation_Code                                           |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL02](/HBSIR/tables/raw/self_employed_income#col02)     |
| 1374-1383 | [COL03](/HBSIR/tables/raw/self_employed_income#col03)     |
| 1384-1401 | [DYCOL03](/HBSIR/tables/raw/self_employed_income#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1369 |   23654 |  630.15 |               129.85 |        21 |      613 |       999 |
|   1370 |   23388 |  631.95 |               130.84 |        21 |      613 |       999 |
|   1371 |   23485 |  634.75 |               131.91 |        22 |      613 |       999 |
|   1372 |   15080 |  634.99 |               140.2  |        22 |      613 |       986 |
|   1373 |   21052 |  634.57 |               154.01 |        14 |      613 |       999 |
|   1374 |   44066 |  634.55 |               143.39 |         0 |      613 |       999 |
|   1375 |   27840 |  634.71 |               109.46 |        11 |      612 |       933 |
|   1376 |   26580 |  636.44 |               109.21 |        11 |      612 |       933 |
|   1377 |   22012 |  635.34 |               116.14 |        11 |      611 |       933 |
|   1378 |   34611 | 6376.98 |              1119.41 |       111 |     6112 |      9333 |
|   1379 |   32478 | 6383.82 |              1112.03 |       112 |     6121 |      9333 |
|   1380 |   30263 | 6372.22 |              1116.32 |       111 |     6112 |      9333 |
|   1381 |   35032 | 6343.13 |              1157.3  |       111 |     6112 |      9333 |
|   1382 |   25550 | 6341.06 |              1163.44 |       111 |     6112 |      9333 |
|   1383 |   27634 | 6374.87 |              1203.55 |       112 |     6121 |      9333 |
|   1384 |   29117 | 6378.16 |              1182.27 |       111 |     6114 |      9333 |
|   1385 |   32590 | 6404.51 |              1202.6  |       111 |     6121 |      9333 |
|   1386 |   29504 | 6375.68 |              1225.56 |       111 |     6121 |      9333 |
|   1387 |   31450 | 6418.21 |              1232.76 |       111 |     6121 |      9333 |
|   1388 |   29616 | 6422.52 |              1233.26 |         0 |     6121 |      9333 |
|   1389 |   28652 | 6415.75 |              1243.21 |         0 |     6121 |      9333 |
|   1390 |   25998 | 6443.32 |              1256.86 |         0 |     6121 |      9333 |
|   1391 |   26787 | 6389.11 |              1202.58 |         0 |     6121 |      9333 |
|   1392 |   24492 | 6405.03 |              1237.35 |      1410 |     6121 |      9333 |
|   1393 |   23495 | 6383.6  |              1228.81 |      1410 |     6121 |      9333 |
|   1394 |   22402 | 6403.84 |              1219.65 |       111 |     6121 |      9333 |
|   1395 |   21822 | 6412.7  |              1244.45 |      1100 |     6121 |      9333 |
|   1396 |   22290 | 6396.01 |              1249.47 |      1120 |     6121 |      9629 |
|   1397 |   21983 | 6401.1  |              1313.99 |      1114 |     6121 |      9629 |
|   1398 |   21649 | 6398.16 |              1295.21 |      1115 |     6121 |      9629 |
|   1399 |   19319 | 6406.49 |              1270.83 |      1120 |     6121 |      9629 |
|   1400 |   18569 | 6403.95 |              1303.33 |      1120 |     6121 |      9629 |
|   1401 |   17313 | 6388.02 |              1325.25 |       410 |     6121 |      9629 |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1369 | X01     |             nan |           5 |
|   1369 | X02     |             nan |          12 |
|   1370 | X01     |             nan |           2 |
|   1370 | X02     |             nan |           1 |
|   1370 | X03     |             nan |           1 |
|   1371 | X01     |             nan |           1 |
|   1371 | X02     |             nan |           1 |
|   1371 | X03     |             nan |           1 |
|   1372 | X01     |             nan |           1 |
|   1372 | X02     |             nan |           1 |
|   1373 | X01     |             nan |           6 |
|   1373 | X04     |             nan |           1 |
|   1374 | x01     |             nan |           4 |
|   1374 | x03     |             nan |           1 |
|   1374 | x04     |             nan |           1 |
|   1388 | x000    |               0 |           6 |
|   1389 | x000    |               0 |           1 |
|   1390 | x000    |               0 |           1 |
|   1391 | x000    |               0 |           3 |


### Industry_Code

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1369:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1370:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1371:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1372:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1373:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1374:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1375:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1376:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1377:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1378:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1379:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1380:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1381:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1382:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1383:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1384:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1385:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1386:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1387:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1388:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1389:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1390:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1391:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1392:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1393:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1394:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1395:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1396:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1397:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1398:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1399:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1400:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    1401:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    
    ```
#### Column Codes

| Years     | Industry_Code                                             |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL03](/HBSIR/tables/raw/self_employed_income#col03)     |
| 1374-1383 | [COL04](/HBSIR/tables/raw/self_employed_income#col04)     |
| 1384-1401 | [DYCOL04](/HBSIR/tables/raw/self_employed_income#dycol04) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|----------:|
|   1369 |   23674 |  2481.93 |              2288.92 |       200 |     1121 |      9599 |
|   1370 |   23392 |  2506.11 |              2299.14 |       200 |     1121 |      9599 |
|   1371 |   23488 |  2536.16 |              2289.64 |       130 |     1122 |      9599 |
|   1372 |   15082 |  2649.76 |              2380.66 |       130 |     1122 |      9599 |
|   1373 |   21059 |  2956.14 |              2534.85 |       140 |     1122 |      9599 |
|   1374 |   44070 |  1622.25 |              2287.21 |         0 |      124 |      9899 |
|   1375 |   27840 |   153.2  |               228.61 |        11 |       12 |       970 |
|   1376 |   26580 |   155.69 |               229.02 |        11 |       12 |       950 |
|   1377 |   22012 |   161.6  |               235.21 |        11 |       12 |       950 |
|   1378 |   34611 |  1608    |              2341.11 |       111 |      124 |      9500 |
|   1379 |   32478 |  1588.11 |              2319.89 |       111 |      124 |      9500 |
|   1380 |   30263 |  1679.04 |              2396.55 |       111 |      124 |      9500 |
|   1381 |   35032 |  1710.64 |              2430.1  |       111 |      124 |      9500 |
|   1382 |   25550 |  1708    |              2441.94 |       111 |      124 |      9600 |
|   1383 |   27634 |  1740.02 |              2457.72 |       111 |      124 |      9500 |
|   1384 |   29117 |  1711.74 |              2459.7  |       111 |      124 |      9500 |
|   1385 |   32590 |  1714.36 |              2458.38 |       111 |      124 |      9600 |
|   1386 |   29504 |  1858.75 |              2540.7  |       111 |      124 |      9500 |
|   1387 |   31450 |  1881.5  |              2553.63 |         0 |      124 |      9500 |
|   1388 |   29616 |  1853.22 |              2552.47 |         0 |      124 |      9500 |
|   1389 |   28652 |  1929.49 |              2583.76 |         0 |      124 |      9500 |
|   1390 |   25998 |  2021.02 |              2616.15 |         0 |      124 |      9500 |
|   1391 |   26787 |  1934.87 |              2583.03 |         0 |      124 |      9500 |
|   1392 |   24492 | 18389.8  |             24074.9  |      1110 |     1440 |     97000 |
|   1393 |   23495 | 18549.8  |             24208.1  |      1110 |     1440 |     97000 |
|   1394 |   22402 | 19822.2  |             24786.7  |      1110 |     1440 |     97000 |
|   1395 |   21822 | 19910.7  |             24969.2  |      1110 |     1440 |     97000 |
|   1396 |   22290 | 19469.3  |             24526.1  |      1110 |     1440 |     97000 |
|   1397 |   21982 | 20667.2  |             24770.3  |      1110 |     1440 |     97000 |
|   1398 |   21649 | 20140.2  |             24846.8  |      1110 |     1440 |     97000 |
|   1399 |   19318 | 19820.5  |             24717.3  |      1110 |     1440 |     97000 |
|   1400 |   18569 | 20817.9  |             24937.2  |      1110 |     1440 |     97000 |
|   1401 |   17313 | 22313.8  |             25398.3  |      1110 |     1440 |     97000 |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1387 | x000    |               0 |           1 |
|   1388 | x000    |               0 |           6 |
|   1389 | x000    |               0 |           1 |
|   1390 | x000    |               0 |           1 |
|   1391 | x000    |               0 |           3 |


### Employment_Type

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL05
      type: category
      categories: null
      replace: null
    1369:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1370:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1371:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1372:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1373:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1374:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1375:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1376:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1377:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1378:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1379:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1380:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1381:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1382:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1383:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1384:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1385:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1386:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1387:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1388:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1389:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1390:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1391:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1392:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1393:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1394:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1395:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1396:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace: null
    1397:
      column_code: DYCOL05
      type: category
      categories:
        4: Employer
        5: Independent_Worker
        6: Family_Worker
      replace:
        1: null
    1398:
      column_code: DYCOL05
      type: category
      categories:
        1: Employer
        2: Independent_Worker
        3: Family_Worker
      replace: null
    1399:
      column_code: DYCOL05
      type: category
      categories:
        1: Employer
        2: Independent_Worker
        3: Family_Worker
      replace: null
    1400:
      column_code: DYCOL05
      type: category
      categories:
        1: Employer
        2: Independent_Worker
        3: Family_Worker
      replace: null
    1401:
      column_code: DYCOL05
      type: category
      categories:
        1: Employer
        2: Independent_Worker
        3: Family_Worker
      replace: null
    
    ```
#### Column Codes

| Years     | Employment_Type                                           |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL04](/HBSIR/tables/raw/self_employed_income#col04)     |
| 1374-1383 | [COL05](/HBSIR/tables/raw/self_employed_income#col05)     |
| 1384-1401 | [DYCOL05](/HBSIR/tables/raw/self_employed_income#dycol05) |


#### Summary Statistics

**category data**

|   Year | 5.0   | 6.0   | 4.0   | 2.0   | 3.0   | 1.0   | nan   | Independent_Worker   | Family_Worker   | Employer   |
|-------:|:------|:------|:------|:------|:------|:------|:------|:---------------------|:----------------|:-----------|
|   1369 |       |       |       | 71.5  | 19.43 | 9.08  |       |                      |                 |            |
|   1370 |       |       |       | 72.29 | 17.51 | 10.2  |       |                      |                 |            |
|   1371 |       |       |       | 71.03 | 19.67 | 9.3   |       |                      |                 |            |
|   1372 |       |       |       | 69.94 | 19.0  | 11.06 |       |                      |                 |            |
|   1373 |       |       |       | 68.1  | 19.06 | 12.85 |       |                      |                 |            |
|   1374 |       |       |       | 68.93 | 20.69 | 10.36 | 0.02  |                      |                 |            |
|   1375 |       |       |       | 63.72 | 24.1  | 12.17 |       |                      |                 |            |
|   1376 |       |       |       | 64.37 | 24.29 | 11.34 |       |                      |                 |            |
|   1377 |       |       |       | 65.9  | 23.34 | 10.76 |       |                      |                 |            |
|   1378 |       |       |       | 66.47 | 23.38 | 10.16 |       |                      |                 |            |
|   1379 |       |       |       | 65.06 | 23.39 | 11.54 |       |                      |                 |            |
|   1380 |       |       |       | 64.48 | 23.37 | 12.15 |       |                      |                 |            |
|   1381 |       |       |       | 65.27 | 22.97 | 11.75 |       |                      |                 |            |
|   1382 |       |       |       | 64.77 | 22.63 | 12.59 |       |                      |                 |            |
|   1383 |       |       |       | 63.43 | 23.94 | 12.63 |       |                      |                 |            |
|   1384 |       |       |       | 63.47 | 23.46 | 13.07 |       |                      |                 |            |
|   1385 |       |       |       | 60.36 | 26.72 | 12.92 |       |                      |                 |            |
|   1386 |       |       |       | 61.86 | 25.69 | 12.45 | 0.0   |                      |                 |            |
|   1387 |       |       |       | 64.56 | 24.27 | 11.15 | 0.01  |                      |                 |            |
|   1388 |       |       |       | 63.86 | 24.81 | 11.3  | 0.02  |                      |                 |            |
|   1389 |       |       |       | 65.58 | 22.65 | 11.76 | 0.0   |                      |                 |            |
|   1390 |       |       |       | 67.72 | 20.42 | 11.84 | 0.02  |                      |                 |            |
|   1391 |       |       |       |       |       |       | 0.01  | 66.57                | 21.73           | 11.7       |
|   1392 |       |       |       |       |       |       | 0.0   | 69.51                | 19.62           | 10.86      |
|   1393 |       |       |       |       |       |       | 0.01  | 70.85                | 19.04           | 10.1       |
|   1394 |       |       |       |       |       |       | 0.01  | 73.59                | 17.49           | 8.91       |
|   1395 |       |       |       |       |       |       |       | 74.47                | 16.29           | 9.24       |
|   1396 |       |       |       |       |       |       |       | 76.08                | 15.15           | 8.77       |
|   1397 |       |       |       |       |       |       | 0.03  | 76.36                | 14.15           | 9.45       |
|   1398 | 75.3  | 15.26 | 9.44  |       |       |       | 0.0   |                      |                 |            |
|   1399 | 75.19 | 15.85 | 8.96  |       |       |       | 0.01  |                      |                 |            |
|   1400 | 76.78 | 14.24 | 8.98  |       |       |       |       |                      |                 |            |
|   1401 | 79.96 | 11.64 | 8.4   |       |       |       |       |                      |                 |            |


#### Categories

|    | 1369-1397          | 1398-1401          |
|---:|:-------------------|:-------------------|
|  1 |                    | Employer           |
|  2 |                    | Independent_Worker |
|  3 |                    | Family_Worker      |
|  4 | Employer           |                    |
|  5 | Independent_Worker |                    |
|  6 | Family_Worker      |                    |


#### Replacements

|   Year |   Value |   Replace_Value |   Frequency |
|-------:|--------:|----------------:|------------:|
|   1397 |       1 |             nan |           2 |


### Is_Agricultural

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1369:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1370:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1371:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1372:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1373:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1374:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1375:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1376:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1377:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1378:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1379:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1380:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1381:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1382:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1383:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1384:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1385:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1386:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1387:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1388:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1389:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1390:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1391:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1392:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1393:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1394:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1395:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1396:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1397:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1398:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1399:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1400:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1401:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Is_Agricultural                                           |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL05](/HBSIR/tables/raw/self_employed_income#col05)     |
| 1374-1383 | [COL06](/HBSIR/tables/raw/self_employed_income#col06)     |
| 1384-1401 | [DYCOL06](/HBSIR/tables/raw/self_employed_income#dycol06) |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1369 |  66.48 |   33.52 |         0 |
|   1370 |  66.69 |   33.31 |         0 |
|   1371 |  65.04 |   34.96 |         0 |
|   1372 |  62.61 |   37.39 |         0 |
|   1373 |  57.79 |   42.21 |         0 |
|   1374 |  61.5  |   38.5  |         0 |
|   1375 |  65.79 |   34.21 |         0 |
|   1376 |  64.68 |   35.32 |         0 |
|   1377 |  64.26 |   35.74 |         0 |
|   1378 |  64.57 |   35.43 |         0 |
|   1379 |  64.86 |   35.14 |         0 |
|   1380 |  63.9  |   36.1  |         0 |
|   1381 |  63.68 |   36.32 |         0 |
|   1382 |  64.44 |   35.56 |         0 |
|   1383 |  64.02 |   35.98 |         0 |
|   1384 |   6.01 |   93.99 |         0 |
|   1385 |  63.79 |   36.21 |         0 |
|   1386 |  61.91 |   38.09 |         0 |
|   1387 |  61.78 |   38.22 |         0 |
|   1388 |  62.59 |   37.41 |         0 |
|   1389 |  62.1  |   37.9  |         0 |
|   1390 |  60.11 |   39.89 |         0 |
|   1391 |  62.07 |   37.93 |         0 |
|   1392 |  60.1  |   39.9  |         0 |
|   1393 |  61.04 |   38.96 |         0 |
|   1394 |  58.87 |   41.13 |         0 |
|   1395 |  58.87 |   41.13 |         0 |
|   1396 |  59.22 |   40.78 |         0 |
|   1397 |  56.3  |   43.7  |         0 |
|   1398 |  58.22 |   41.78 |         0 |
|   1399 |  58.95 |   41.05 |         0 |
|   1400 |  56.75 |   43.25 |         0 |
|   1401 |  54.07 |   45.93 |         0 |


### Working_Hours_per_Day

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL07
      type: UInt8
    
    ```
#### Column Codes

| Years     | Working_Hours_per_Day                                     |
|:----------|:----------------------------------------------------------|
| 1369-1383 |                                                           |
| 1384-1401 | [DYCOL07](/HBSIR/tables/raw/self_employed_income#dycol07) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1384 |   28840 |   5.7  |                 1.77 |         0 |        6 |         7 |
|   1385 |   32202 |   5.65 |                 3.05 |         0 |        5 |        18 |
|   1386 |   28445 |   5.9  |                 2.97 |         0 |        5 |        18 |
|   1387 |   30404 |   6.04 |                 2.97 |         0 |        6 |        32 |
|   1388 |   28777 |   5.9  |                 2.92 |         0 |        5 |        18 |
|   1389 |   27878 |   6.03 |                 2.89 |         0 |        6 |        18 |
|   1390 |   25416 |   6.23 |                 2.87 |         0 |        6 |        18 |
|   1391 |   26216 |   6.19 |                 2.87 |         0 |        6 |        18 |
|   1392 |   24142 |   6.29 |                 2.76 |         0 |        6 |        18 |
|   1393 |   23125 |   6.24 |                 2.77 |         0 |        6 |        18 |
|   1394 |   21992 |   6.37 |                 2.83 |         0 |        6 |        18 |
|   1395 |   21471 |   6.36 |                 2.79 |         0 |        6 |        18 |
|   1396 |   21924 |   6.23 |                 2.88 |         0 |        6 |        18 |
|   1397 |   21527 |   6.43 |                 2.85 |         0 |        6 |        18 |
|   1398 |   21232 |   6.35 |                 2.83 |         0 |        6 |        18 |
|   1399 |   19028 |   6.38 |                 2.79 |         0 |        6 |        18 |
|   1400 |   18338 |   6.62 |                 2.75 |         0 |        7 |        18 |
|   1401 |   16951 |   6.67 |                 2.71 |         1 |        7 |        18 |


### Working_Day_per_Week

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL08
      type: UInt8
    
    ```
#### Column Codes

| Years     | Working_Day_per_Week                                      |
|:----------|:----------------------------------------------------------|
| 1369-1383 |                                                           |
| 1384-1401 | [DYCOL08](/HBSIR/tables/raw/self_employed_income#dycol08) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1384 |   29117 |   1.35 |                 0.48 |         1 |        1 |         2 |
|   1385 |   32204 |   5.74 |                 1.8  |         0 |        7 |         7 |
|   1386 |   28465 |   5.83 |                 1.57 |         0 |        6 |         8 |
|   1387 |   30412 |   5.8  |                 1.58 |         0 |        6 |         7 |
|   1388 |   28778 |   5.61 |                 1.65 |         0 |        6 |         7 |
|   1389 |   27881 |   5.57 |                 1.68 |         0 |        6 |         7 |
|   1390 |   25418 |   5.6  |                 1.64 |         0 |        6 |         7 |
|   1391 |   26217 |   5.6  |                 1.66 |         0 |        6 |         7 |
|   1392 |   24143 |   5.64 |                 1.61 |         0 |        6 |         7 |
|   1393 |   23125 |   5.68 |                 1.61 |         0 |        6 |         7 |
|   1394 |   21991 |   5.72 |                 1.58 |         0 |        6 |         7 |
|   1395 |   21475 |   5.66 |                 1.59 |         0 |        6 |         7 |
|   1396 |   21924 |   5.55 |                 1.69 |         0 |        6 |         7 |
|   1397 |   21532 |   5.58 |                 1.66 |         0 |        6 |         7 |
|   1398 |   21233 |   5.59 |                 1.68 |         0 |        6 |         7 |
|   1399 |   19035 |   5.5  |                 1.7  |         0 |        6 |         7 |
|   1400 |   18335 |   5.52 |                 1.65 |         0 |        6 |         7 |
|   1401 |   16943 |   5.55 |                 1.59 |         1 |        6 |         7 |


### Wage_Cost

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL09
      type: float
    1369:
      column_code: DYCOL09
      type: float
    1370:
      column_code: DYCOL09
      type: float
    1371:
      column_code: DYCOL09
      type: float
    1372:
      column_code: DYCOL09
      type: float
    1373:
      column_code: DYCOL09
      type: float
    1374:
      column_code: DYCOL09
      type: float
    1375:
      column_code: DYCOL09
      type: float
    1376:
      column_code: DYCOL09
      type: float
    1377:
      column_code: DYCOL09
      type: float
    1378:
      column_code: DYCOL09
      type: float
    1379:
      column_code: DYCOL09
      type: float
    1380:
      column_code: DYCOL09
      type: float
    1381:
      column_code: DYCOL09
      type: float
    1382:
      column_code: DYCOL09
      type: float
    1383:
      column_code: DYCOL09
      type: float
    1384:
      column_code: DYCOL09
      type: float
    1385:
      column_code: DYCOL09
      type: float
    1386:
      column_code: DYCOL09
      type: float
    1387:
      column_code: DYCOL09
      type: float
    1388:
      column_code: DYCOL09
      type: float
    1389:
      column_code: DYCOL09
      type: float
    1390:
      column_code: DYCOL09
      type: float
    1391:
      column_code: DYCOL09
      type: float
    1392:
      column_code: DYCOL09
      type: float
    1393:
      column_code: DYCOL09
      type: float
    1394:
      column_code: DYCOL09
      type: float
    1395:
      column_code: DYCOL09
      type: float
    1396:
      column_code: DYCOL09
      type: float
    1397:
      column_code: DYCOL09
      type: float
    1398:
      column_code: DYCOL09
      type: float
    1399:
      column_code: DYCOL09
      type: float
    1400:
      column_code: DYCOL09
      type: float
    1401:
      column_code: DYCOL09
      type: float
    
    ```
#### Column Codes

| Years     | Wage_Cost                                                 |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL06](/HBSIR/tables/raw/self_employed_income#col06)     |
| 1374-1383 | [COL07](/HBSIR/tables/raw/self_employed_income#col07)     |
| 1384-1401 | [DYCOL09](/HBSIR/tables/raw/self_employed_income#dycol09) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------:|------------:|
|   1369 |   24550 |  54261.9         |     371244           |         0 |        0 | 3e+07       |
|   1370 |   23960 |  66377           |     620691           |         0 |        0 | 3.48e+07    |
|   1371 |   24136 |  80974.8         |     931281           |         0 |        0 | 6e+07       |
|   1372 |   15377 | 101778           |     803011           |         0 |        0 | 5.04e+07    |
|   1373 |   21557 | 145204           |     982056           |         0 |        0 | 4.8e+07     |
|   1374 |   44077 | 174544           |          1.33271e+06 |         0 |        0 | 8e+07       |
|   1375 |   27840 | 235307           |          2.14378e+06 |         0 |        0 | 1.2e+08     |
|   1376 |   26580 | 306929           |          3.70931e+06 |         0 |        0 | 4.542e+08   |
|   1377 |   22012 | 331143           |          3.35048e+06 |         0 |        0 | 2.55e+08    |
|   1378 |   34611 | 502577           |          1.15181e+07 |         0 |        0 | 1.38375e+09 |
|   1379 |   32478 | 526960           |          7.32471e+06 |         0 |        0 | 1.08e+09    |
|   1380 |   30263 | 603806           |          5.71681e+06 |         0 |        0 | 4.14e+08    |
|   1381 |   35032 | 799501           |          8.70513e+06 |         0 |        0 | 1e+09       |
|   1382 |   25550 | 990413           |          7.24366e+06 |         0 |        0 | 4.32e+08    |
|   1383 |   27634 |      1.31911e+06 |          1.27539e+07 |         0 |        0 | 1.20226e+09 |
|   1384 |   15626 |      3.03429e+06 |          2.5487e+07  |         0 |        0 | 1.69725e+09 |
|   1385 |   20192 |      3.2841e+06  |          3.06772e+07 |         0 |        0 | 2e+09       |
|   1386 |   19620 |      3.96012e+06 |          3.49993e+07 |         0 |        0 | 3e+09       |
|   1387 |   22492 |      3.95352e+06 |          2.72417e+07 |         0 |        0 | 1.75e+09    |
|   1388 |   22282 |      4.13563e+06 |          3.36616e+07 |         0 |        0 | 2.375e+09   |
|   1389 |   22610 |      4.66393e+06 |          3.7855e+07  |         0 |        0 | 3.6e+09     |
|   1390 |   20065 |      6.27972e+06 |          6.92264e+07 |         0 |        0 | 5.76e+09    |
|   1391 |   20949 |      6.29738e+06 |          4.8045e+07  |         0 |        0 | 3.36e+09    |
|   1392 |   18883 |      7.69438e+06 |          5.49994e+07 |         0 |        0 | 4.16e+09    |
|   1393 |   17456 |      9.7647e+06  |          1.0175e+08  |         0 |        0 | 1.08e+10    |
|   1394 |   17179 |      9.53682e+06 |          5.66028e+07 |         0 |        0 | 2.64e+09    |
|   1395 |   16569 |      1.15266e+07 |          8.41925e+07 |         0 |        0 | 5.5e+09     |
|   1396 |   17356 |      1.29658e+07 |          7.86237e+07 |         0 |        0 | 3.975e+09   |
|   1397 |   19055 |      2.63407e+07 |          1.07981e+09 |         0 |        0 | 1.46e+11    |
|   1398 |   19268 |      2.189e+07   |          1.96696e+08 |         0 |        0 | 1.344e+10   |
|   1399 |   16988 |      2.72155e+07 |          2.15026e+08 |         0 |        0 | 7.8e+09     |
|   1400 |   16224 |      4.1994e+07  |          3.2976e+08  |         0 |        0 | 2.077e+10   |
|   1401 |   17313 |      5.51543e+07 |          4.64185e+08 |         0 |        0 | 3.648e+10   |


### Cost_of_Sales

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL10
      type: float
    1369:
      column_code: DYCOL10
      type: float
    1370:
      column_code: DYCOL10
      type: float
    1371:
      column_code: DYCOL10
      type: float
    1372:
      column_code: DYCOL10
      type: float
    1373:
      column_code: DYCOL10
      type: float
    1374:
      column_code: DYCOL10
      type: float
    1375:
      column_code: DYCOL10
      type: float
    1376:
      column_code: DYCOL10
      type: float
    1377:
      column_code: DYCOL10
      type: float
    1378:
      column_code: DYCOL10
      type: float
    1379:
      column_code: DYCOL10
      type: float
    1380:
      column_code: DYCOL10
      type: float
    1381:
      column_code: DYCOL10
      type: float
    1382:
      column_code: DYCOL10
      type: float
    1383:
      column_code: DYCOL10
      type: float
    1384:
      column_code: DYCOL10
      type: float
    1385:
      column_code: DYCOL10
      type: float
    1386:
      column_code: DYCOL10
      type: float
    1387:
      column_code: DYCOL10
      type: float
    1388:
      column_code: DYCOL10
      type: float
    1389:
      column_code: DYCOL10
      type: float
    1390:
      column_code: DYCOL10
      type: float
    1391:
      column_code: DYCOL10
      type: float
    1392:
      column_code: DYCOL10
      type: float
    1393:
      column_code: DYCOL10
      type: float
    1394:
      column_code: DYCOL10
      type: float
    1395:
      column_code: DYCOL10
      type: float
    1396:
      column_code: DYCOL10
      type: float
    1397:
      column_code: DYCOL10
      type: float
    1398:
      column_code: DYCOL10
      type: float
    1399:
      column_code: DYCOL10
      type: float
    1400:
      column_code: DYCOL10
      type: float
    1401:
      column_code: DYCOL10
      type: float
    
    ```
#### Column Codes

| Years     | Cost_of_Sales                                             |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL07](/HBSIR/tables/raw/self_employed_income#col07)     |
| 1374-1383 | [COL08](/HBSIR/tables/raw/self_employed_income#col08)     |
| 1384-1401 | [DYCOL10](/HBSIR/tables/raw/self_employed_income#dycol10) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |        Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|--------------:|------------:|
|   1369 |   24550 | 555911           |          3.27705e+06 |         0 |  23350        | 1e+08       |
|   1370 |   23960 | 656182           |          3.66651e+06 |         0 |  26725        | 9.216e+07   |
|   1371 |   24136 | 834390           |          4.8176e+06  |         0 |  30000        | 1e+08       |
|   1372 |   15377 |      1.03964e+06 |          5.81991e+06 |         0 |  39300        | 1e+08       |
|   1373 |   21557 |      1.57573e+06 |          7.40236e+06 |         0 |  48000        | 1e+08       |
|   1374 |   44077 |      2.54222e+06 |          2.90889e+07 |         0 |  80000        | 4e+09       |
|   1375 |   27840 |      2.90362e+06 |          2.30625e+07 |         0 |  85000        | 1.8e+09     |
|   1376 |   26580 |      3.38209e+06 |          2.85338e+07 |         0 |  96000        | 1.8e+09     |
|   1377 |   22012 |      3.73601e+06 |          4.31213e+07 |         0 | 100150        | 4.8e+09     |
|   1378 |   34611 |      4.81549e+06 |          4.14312e+07 |         0 | 150000        | 3.65e+09    |
|   1379 |   32478 |      6.5942e+06  |          5.99559e+07 |         0 | 210000        | 6e+09       |
|   1380 |   30263 |      7.23388e+06 |          5.87147e+07 |         0 | 230000        | 3.40125e+09 |
|   1381 |   35032 |      9.24886e+06 |          7.16989e+07 |         0 | 347500        | 8.0643e+09  |
|   1382 |   25550 |      1.20289e+07 |          9.01933e+07 |         0 | 450000        | 7.474e+09   |
|   1383 |   27634 |      1.05336e+07 |          5.78588e+07 |         0 | 405250        | 1.68697e+09 |
|   1384 |   22546 |      1.75087e+07 |          1.22047e+08 |         0 |      1.5e+06  | 7.045e+09   |
|   1385 |   26389 |      2.17796e+07 |          1.4457e+08  |         0 |      1.8e+06  | 6e+09       |
|   1386 |   24793 |      2.73101e+07 |          1.88503e+08 |         0 |      2.05e+06 | 9.85e+09    |
|   1387 |   28252 |      2.81067e+07 |          1.62606e+08 |         0 |      2.09e+06 | 8.5e+09     |
|   1388 |   26848 |      2.95581e+07 |          2.01902e+08 |         0 |      2.2e+06  | 9.3e+09     |
|   1389 |   26596 |      3.28614e+07 |          2.06478e+08 |         0 |      2.5e+06  | 9.6e+09     |
|   1390 |   24011 |      3.74373e+07 |          1.96985e+08 |         0 |      4.2e+06  | 9.99999e+09 |
|   1391 |   24779 |      5.24541e+07 |          2.77847e+08 |         0 |      5.3e+06  | 9.6e+09     |
|   1392 |   22519 |      6.5537e+07  |          3.00328e+08 |         0 |      8.5e+06  | 9.75e+09    |
|   1393 |   21409 |      7.59338e+07 |          3.34248e+08 |         0 |      1.05e+07 | 1.8e+10     |
|   1394 |   20737 |      8.75144e+07 |          5.83607e+08 |         0 |      1.22e+07 | 5e+10       |
|   1395 |   20563 |      1.0602e+08  |          8.79076e+08 |         0 |      1.5e+07  | 9e+10       |
|   1396 |   21162 |      1.10494e+08 |          6.3615e+08  |         0 |      1.5e+07  | 4e+10       |
|   1397 |   21344 |      1.97263e+08 |          5.5708e+09  |         0 |      2e+07    | 7.8e+11     |
|   1398 |   21152 |      2.04415e+08 |          1.46356e+09 |         0 |      2.3e+07  | 1.2e+11     |
|   1399 |   18743 |      2.74139e+08 |          1.49011e+09 |         0 |      3e+07    | 8e+10       |
|   1400 |   17973 |      4.46849e+08 |          2.58142e+09 |         0 |      5e+07    | 1.5e+11     |
|   1401 |   17313 |      6.73711e+08 |          3.93872e+09 |         0 |      6e+07    | 2.475e+11   |


### Other_Operating_Costs

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL11
      type: float
    1369:
      column_code: DYCOL11
      type: float
    1370:
      column_code: DYCOL11
      type: float
    1371:
      column_code: DYCOL11
      type: float
    1372:
      column_code: DYCOL11
      type: float
    1373:
      column_code: DYCOL11
      type: float
    1374:
      column_code: DYCOL11
      type: float
    1375:
      column_code: DYCOL11
      type: float
    1376:
      column_code: DYCOL11
      type: float
    1377:
      column_code: DYCOL11
      type: float
    1378:
      column_code: DYCOL11
      type: float
    1379:
      column_code: DYCOL11
      type: float
    1380:
      column_code: DYCOL11
      type: float
    1381:
      column_code: DYCOL11
      type: float
    1382:
      column_code: DYCOL11
      type: float
    1383:
      column_code: DYCOL11
      type: float
    1384:
      column_code: DYCOL11
      type: float
    1385:
      column_code: DYCOL11
      type: float
    1386:
      column_code: DYCOL11
      type: float
    1387:
      column_code: DYCOL11
      type: float
    1388:
      column_code: DYCOL11
      type: float
    1389:
      column_code: DYCOL11
      type: float
    1390:
      column_code: DYCOL11
      type: float
    1391:
      column_code: DYCOL11
      type: float
    1392:
      column_code: DYCOL11
      type: float
    1393:
      column_code: DYCOL11
      type: float
    1394:
      column_code: DYCOL11
      type: float
    1395:
      column_code: DYCOL11
      type: float
    1396:
      column_code: DYCOL11
      type: float
    1397:
      column_code: DYCOL11
      type: float
    1398:
      column_code: DYCOL11
      type: float
    1399:
      column_code: DYCOL11
      type: float
    1400:
      column_code: DYCOL11
      type: float
    1401:
      column_code: DYCOL11
      type: float
    
    ```
#### Column Codes

| Years     | Other_Operating_Costs                                     |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL08](/HBSIR/tables/raw/self_employed_income#col08)     |
| 1374-1383 | [COL09](/HBSIR/tables/raw/self_employed_income#col09)     |
| 1384-1401 | [DYCOL11](/HBSIR/tables/raw/self_employed_income#dycol11) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------:|----------:|
|   1369 |   24550 |  37362.2         |     263487           |         0 |        0 | 1.5e+07   |
|   1370 |   23960 |  48185.3         |     414656           |         0 |        0 | 3e+07     |
|   1371 |   24136 |  59151.6         |     793464           |         0 |        0 | 6.8e+07   |
|   1372 |   15377 |  68569.9         |     489941           |         0 |        0 | 2.4e+07   |
|   1373 |   21557 | 109247           |          1.3513e+06  |         0 |        0 | 9.065e+07 |
|   1374 |   44077 | 141805           |          1.0251e+06  |         0 |        0 | 7.6e+07   |
|   1375 |   27840 | 183747           |          2.13719e+06 |         0 |        0 | 1.5e+08   |
|   1376 |   26580 | 234203           |          5.74213e+06 |         0 |        0 | 9e+08     |
|   1377 |   22012 | 196972           |          1.66347e+06 |         0 |        0 | 1.245e+08 |
|   1378 |   34611 | 252719           |          2.72659e+06 |         0 |        0 | 2.5e+08   |
|   1379 |   32478 | 282531           |          3.04147e+06 |         0 |        0 | 3.5e+08   |
|   1380 |   30263 | 303625           |          2.9202e+06  |         0 |        0 | 3e+08     |
|   1381 |   35032 | 450491           |          4.00301e+06 |         0 |        0 | 4.2e+08   |
|   1382 |   25550 | 479442           |          3.75986e+06 |         0 |        0 | 4e+08     |
|   1383 |   27634 | 638267           |          8.0176e+06  |         0 |        0 | 8e+08     |
|   1384 |   15697 |      1.02932e+06 |          5.5915e+06  |         0 |        0 | 1.625e+08 |
|   1385 |   19717 |      1.35023e+06 |          1.92773e+07 |         0 |        0 | 2.4e+09   |
|   1386 |   19198 |      1.29069e+06 |          9.78994e+06 |         0 |        0 | 9e+08     |
|   1387 |   23081 |      1.41021e+06 |          1.02465e+07 |         0 |        0 | 7e+08     |
|   1388 |   22765 |      1.3504e+06  |          8.79746e+06 |         0 |        0 | 6e+08     |
|   1389 |   23056 |      1.43615e+06 |          8.14081e+06 |         0 |        0 | 3.4e+08   |
|   1390 |   20585 |      1.99061e+06 |          3.26287e+07 |         0 |        0 | 4e+09     |
|   1391 |   21614 |      2.50994e+06 |          1.9456e+07  |         0 |        0 | 1.44e+09  |
|   1392 |   19271 |      4.10438e+06 |          4.68555e+07 |         0 |        0 | 5e+09     |
|   1393 |   18190 |      3.88508e+06 |          2.51381e+07 |         0 |        0 | 2e+09     |
|   1394 |   17853 |      4.4692e+06  |          2.4143e+07  |         0 |        0 | 1.5e+09   |
|   1395 |   17605 |      4.57208e+06 |          2.05885e+07 |         0 |        0 | 1e+09     |
|   1396 |   18390 |      4.81508e+06 |          2.71359e+07 |         0 |        0 | 2e+09     |
|   1397 |   19847 |      6.3355e+06  |          4.82893e+07 |         0 |        0 | 4.5e+09   |
|   1398 |   19956 |      8.95509e+06 |          6.39187e+07 |         0 |        0 | 5e+09     |
|   1399 |   17473 |      1.30865e+07 |          1.0677e+08  |         0 |        0 | 7.2e+09   |
|   1400 |   16698 |      2.19373e+07 |          2.08453e+08 |         0 |        0 | 1.8e+10   |
|   1401 |   17313 |      2.93265e+07 |          2.25414e+08 |         0 |        0 | 1.8e+10   |


### Other_Costs

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL12
      type: float
    1369:
      column_code: DYCOL12
      type: float
    1370:
      column_code: DYCOL12
      type: float
    1371:
      column_code: DYCOL12
      type: float
    1372:
      column_code: DYCOL12
      type: float
    1373:
      column_code: DYCOL12
      type: float
    1374:
      column_code: DYCOL12
      type: float
    1375:
      column_code: DYCOL12
      type: float
    1376:
      column_code: DYCOL12
      type: float
    1377:
      column_code: DYCOL12
      type: float
    1378:
      column_code: DYCOL12
      type: float
    1379:
      column_code: DYCOL12
      type: float
    1380:
      column_code: DYCOL12
      type: float
    1381:
      column_code: DYCOL12
      type: float
    1382:
      column_code: DYCOL12
      type: float
    1383:
      column_code: DYCOL12
      type: float
    1384:
      column_code: DYCOL12
      type: float
    1385:
      column_code: DYCOL12
      type: float
    1386:
      column_code: DYCOL12
      type: float
    1387:
      column_code: DYCOL12
      type: float
    1388:
      column_code: DYCOL12
      type: float
    1389:
      column_code: DYCOL12
      type: float
    1390:
      column_code: DYCOL12
      type: float
    1391:
      column_code: DYCOL12
      type: float
    1392:
      column_code: DYCOL12
      type: float
    1393:
      column_code: DYCOL12
      type: float
    1394:
      column_code: DYCOL12
      type: float
    1395:
      column_code: DYCOL12
      type: float
    1396:
      column_code: DYCOL12
      type: float
    1397:
      column_code: DYCOL12
      type: float
    1398:
      column_code: DYCOL12
      type: float
    1399:
      column_code: DYCOL12
      type: float
    1400:
      column_code: DYCOL12
      type: float
    1401:
      column_code: DYCOL12
      type: float
    
    ```
#### Column Codes

| Years     | Other_Costs                                               |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL09](/HBSIR/tables/raw/self_employed_income#col09)     |
| 1374-1383 | [COL10](/HBSIR/tables/raw/self_employed_income#col10)     |
| 1384-1401 | [DYCOL12](/HBSIR/tables/raw/self_employed_income#dycol12) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |          Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|----------------:|------------:|
|   1369 |   24550 |  48210           |     358808           |         0 |      0          | 3.263e+07   |
|   1370 |   23960 |  54324.2         |     297725           |         0 |      0          | 1.85293e+07 |
|   1371 |   24136 |  67522.8         |     410366           |         0 |      0          | 3.03e+07    |
|   1372 |   15377 |  81907.2         |     384690           |         0 |      0          | 2.2e+07     |
|   1373 |   21557 | 136759           |     874756           |         0 |      0          | 5.5e+07     |
|   1374 |   44077 | 168133           |     894162           |         0 |      0          | 7.7e+07     |
|   1375 |   27840 | 254674           |          1.94446e+06 |         0 |      0          | 1.8e+08     |
|   1376 |   26580 | 326709           |          2.74514e+06 |         0 |      0          | 2.8542e+08  |
|   1377 |   22012 | 351729           |          2.03566e+06 |         0 |      0          | 1.82e+08    |
|   1378 |   34611 | 440982           |          3.07275e+06 |         0 |      0          | 3.6e+08     |
|   1379 |   32478 | 514920           |          2.85563e+06 |         0 |      0          | 3e+08       |
|   1380 |   30263 | 669021           |          4.5576e+06  |         0 |      0          | 5.1275e+08  |
|   1381 |   35032 | 878020           |          4.49244e+06 |         0 |      0          | 3.8e+08     |
|   1382 |   25550 |      1.17217e+06 |          9.3963e+06  |         0 |      0          | 9e+08       |
|   1383 |   27634 |      1.33988e+06 |          7.76566e+06 |         0 |      0          | 5.24e+08    |
|   1384 |   19283 |      2.51891e+06 |          1.57084e+07 |         0 | 400000          | 1.577e+09   |
|   1385 |   23274 |      2.70059e+06 |          1.31913e+07 |         0 | 400000          | 7e+08       |
|   1386 |   22486 |      3.26974e+06 |          1.48287e+07 |         0 | 430000          | 1.2e+09     |
|   1387 |   26104 |      3.61539e+06 |          1.74865e+07 |         0 | 400000          | 1.1e+09     |
|   1388 |   25274 |      3.96275e+06 |          1.89917e+07 |         0 | 450000          | 1.3e+09     |
|   1389 |   25375 |      4.28545e+06 |          1.82105e+07 |         0 | 500000          | 1.15e+09    |
|   1390 |   22772 |      5.50783e+06 |          3.3596e+07  |         0 | 950000          | 3e+09       |
|   1391 |   23640 |      6.19116e+06 |          1.87559e+07 |         0 |      1.05e+06   | 6.975e+08   |
|   1392 |   21470 |      8.79399e+06 |          2.59466e+07 |         0 |      2e+06      | 9.6e+08     |
|   1393 |   20251 |      1.15791e+07 |          4.63355e+07 |         0 |      2.7e+06    | 3.72e+09    |
|   1394 |   19803 |      1.22415e+07 |          3.67867e+07 |         0 |      3e+06      | 1.326e+09   |
|   1395 |   19570 |      1.37723e+07 |          5.34968e+07 |         0 |      3.4e+06    | 3.5e+09     |
|   1396 |   20284 |      1.51591e+07 |          5.00661e+07 |         0 |      3e+06      | 1.9e+09     |
|   1397 |   20854 |      1.99899e+07 |          1.07747e+08 |         0 |      4e+06      | 9.8e+09     |
|   1398 |   20640 |      2.34539e+07 |          9.42115e+07 |         0 |      4.7035e+06 | 5.5e+09     |
|   1399 |   18251 |      3.25114e+07 |          1.73795e+08 |         0 |      5e+06      | 1.5e+10     |
|   1400 |   17450 |      4.53658e+07 |          1.31934e+08 |         0 |      1e+07      | 5e+09       |
|   1401 |   17313 |      6.95007e+07 |          2.72697e+08 |         0 |      1.25e+07   | 1.811e+10   |


### Business_Tax

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL13
      type: float
    1369:
      column_code: DYCOL13
      type: float
    1370:
      column_code: DYCOL13
      type: float
    1371:
      column_code: DYCOL13
      type: float
    1372:
      column_code: DYCOL13
      type: float
    1373:
      column_code: DYCOL13
      type: float
    1374:
      column_code: DYCOL13
      type: float
    1375:
      column_code: DYCOL13
      type: float
    1376:
      column_code: DYCOL13
      type: float
    1377:
      column_code: DYCOL13
      type: float
    1378:
      column_code: DYCOL13
      type: float
    1379:
      column_code: DYCOL13
      type: float
    1380:
      column_code: DYCOL13
      type: float
    1381:
      column_code: DYCOL13
      type: float
    1382:
      column_code: DYCOL13
      type: float
    1383:
      column_code: DYCOL13
      type: float
    1384:
      column_code: DYCOL13
      type: float
    1385:
      column_code: DYCOL13
      type: float
    1386:
      column_code: DYCOL13
      type: float
    1387:
      column_code: DYCOL13
      type: float
    1388:
      column_code: DYCOL13
      type: float
    1389:
      column_code: DYCOL13
      type: float
    1390:
      column_code: DYCOL13
      type: float
    1391:
      column_code: DYCOL13
      type: float
    1392:
      column_code: DYCOL13
      type: float
    1393:
      column_code: DYCOL13
      type: float
    1394:
      column_code: DYCOL13
      type: float
    1395:
      column_code: DYCOL13
      type: float
    1396:
      column_code: DYCOL13
      type: float
    1397:
      column_code: DYCOL13
      type: float
    1398:
      column_code: DYCOL13
      type: float
    1399:
      column_code: DYCOL13
      type: float
    1400:
      column_code: DYCOL13
      type: float
    1401:
      column_code: DYCOL13
      type: float
    
    ```
#### Column Codes

| Years     | Business_Tax                                              |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL10](/HBSIR/tables/raw/self_employed_income#col10)     |
| 1374-1383 | [COL11](/HBSIR/tables/raw/self_employed_income#col11)     |
| 1384-1401 | [DYCOL13](/HBSIR/tables/raw/self_employed_income#dycol13) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------:|----------:|
|   1369 |   24550 |   4444.64        |      70112.4         |         0 |        0 | 6.3e+06   |
|   1370 |   23960 |   5417.33        |      94110.6         |         0 |        0 | 8.6e+06   |
|   1371 |   24136 |  10641.3         |     474663           |         0 |        0 | 5e+07     |
|   1372 |   15377 |   9933.94        |     190078           |         0 |        0 | 1.8e+07   |
|   1373 |   21557 |  18844.5         |     389119           |         0 |        0 | 4.5e+07   |
|   1374 |   44077 |  22319.5         |     473342           |         0 |        0 | 6e+07     |
|   1375 |   27840 |  27826.5         |     749505           |         0 |        0 | 9e+07     |
|   1376 |   26580 |  27128.5         |     350345           |         0 |        0 | 2.5e+07   |
|   1377 |   22012 |  35467.5         |     933777           |         0 |        0 | 1.2e+08   |
|   1378 |   34611 |  41029.3         |     826487           |         0 |        0 | 8e+07     |
|   1379 |   32478 |  56084.9         |          1.91163e+06 |         0 |        0 | 3e+08     |
|   1380 |   30263 |  47793.1         |     625223           |         0 |        0 | 5e+07     |
|   1381 |   35032 |  81286.1         |          2.80238e+06 |         0 |        0 | 5e+08     |
|   1382 |   25550 |  63531.2         |          1.09993e+06 |         0 |        0 | 1.5e+08   |
|   1383 |   27634 |  69056.5         |          1.16545e+06 |         0 |        0 | 7.8e+07   |
|   1384 |   12066 | 210262           |          3.26196e+06 |         0 |        0 | 2.5e+08   |
|   1385 |   16099 | 213304           |          3.21392e+06 |         0 |        0 | 2.5e+08   |
|   1386 |   16729 | 335312           |          1.12735e+07 |         0 |        0 | 1.189e+09 |
|   1387 |   20636 | 223043           |          3.43341e+06 |         0 |        0 | 4e+08     |
|   1388 |   20764 | 278686           |          5.44886e+06 |         0 |        0 | 4.45e+08  |
|   1389 |   21518 | 226619           |          2.85044e+06 |         0 |        0 | 2.5e+08   |
|   1390 |   18964 | 330305           |          3.5683e+06  |         0 |        0 | 2e+08     |
|   1391 |   19959 | 472692           |          9.49921e+06 |         0 |        0 | 8.5e+08   |
|   1392 |   17847 | 436474           |          6.33802e+06 |         0 |        0 | 6e+08     |
|   1393 |   16501 | 418441           |          5.1704e+06  |         0 |        0 | 5e+08     |
|   1394 |   16347 | 543662           |          6.39403e+06 |         0 |        0 | 5e+08     |
|   1395 |   15878 | 681846           |          7.41915e+06 |         0 |        0 | 5e+08     |
|   1396 |   16672 | 764099           |          7.94167e+06 |         0 |        0 | 5.8e+08   |
|   1397 |   18786 | 911102           |          1.19573e+07 |         0 |        0 | 1e+09     |
|   1398 |   18948 |      1.01948e+06 |          1.73187e+07 |         0 |        0 | 1.7e+09   |
|   1399 |   16591 |      1.27765e+06 |          2.16501e+07 |         0 |        0 | 1.94e+09  |
|   1400 |   15830 |      2.10241e+06 |          8.44986e+07 |         0 |        0 | 8.6e+09   |
|   1401 |   17313 |      2.6395e+06  |          4.7678e+07  |         0 |        0 | 5.68e+09  |


### Sales

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL14
      type: float
    1369:
      column_code: DYCOL14
      type: float
    1370:
      column_code: DYCOL14
      type: float
    1371:
      column_code: DYCOL14
      type: float
    1372:
      column_code: DYCOL14
      type: float
    1373:
      column_code: DYCOL14
      type: float
    1374:
      column_code: DYCOL14
      type: float
    1375:
      column_code: DYCOL14
      type: float
    1376:
      column_code: DYCOL14
      type: float
    1377:
      column_code: DYCOL14
      type: float
    1378:
      column_code: DYCOL14
      type: float
    1379:
      column_code: DYCOL14
      type: float
    1380:
      column_code: DYCOL14
      type: float
    1381:
      column_code: DYCOL14
      type: float
    1382:
      column_code: DYCOL14
      type: float
    1383:
      column_code: DYCOL14
      type: float
    1384:
      column_code: DYCOL14
      type: float
    1385:
      column_code: DYCOL14
      type: float
    1386:
      column_code: DYCOL14
      type: float
    1387:
      column_code: DYCOL14
      type: float
    1388:
      column_code: DYCOL14
      type: float
    1389:
      column_code: DYCOL14
      type: float
    1390:
      column_code: DYCOL14
      type: float
    1391:
      column_code: DYCOL14
      type: float
    1392:
      column_code: DYCOL14
      type: float
    1393:
      column_code: DYCOL14
      type: float
    1394:
      column_code: DYCOL14
      type: float
    1395:
      column_code: DYCOL14
      type: float
    1396:
      column_code: DYCOL14
      type: float
    1397:
      column_code: DYCOL14
      type: float
    1398:
      column_code: DYCOL14
      type: float
    1399:
      column_code: DYCOL14
      type: float
    1400:
      column_code: DYCOL14
      type: float
    1401:
      column_code: DYCOL14
      type: float
    
    ```
#### Column Codes

| Years     | Sales                                                     |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL11](/HBSIR/tables/raw/self_employed_income#col11)     |
| 1374-1383 | [COL12](/HBSIR/tables/raw/self_employed_income#col12)     |
| 1384-1401 | [DYCOL14](/HBSIR/tables/raw/self_employed_income#dycol14) |


#### Summary Statistics

**numeric data**

|   Year |   Count |        Mean |   Standard Deviation |   Minimum |          Median |     Maximum |
|-------:|--------:|------------:|---------------------:|----------:|----------------:|------------:|
|   1369 |   24550 | 1.03189e+06 |          4.05313e+06 |         0 | 170000          | 1e+08       |
|   1370 |   23960 | 1.31694e+06 |          6.19019e+06 |         0 | 194650          | 4.2787e+08  |
|   1371 |   24136 | 1.69281e+06 |          7.90571e+06 |         0 | 230000          | 3.424e+08   |
|   1372 |   15377 | 2.05244e+06 |          1.11294e+07 |         0 | 310000          | 7.2e+08     |
|   1373 |   21557 | 3.16857e+06 |          1.10241e+07 |         0 | 415000          | 5.88e+08    |
|   1374 |   44077 | 4.52536e+06 |          3.12961e+07 |         0 | 550000          | 4.03101e+09 |
|   1375 |   27840 | 5.45757e+06 |          3.02819e+07 |         0 | 660000          | 2.121e+09   |
|   1376 |   26580 | 6.47554e+06 |          3.51039e+07 |         0 | 800000          | 2.014e+09   |
|   1377 |   22012 | 7.14683e+06 |          4.72047e+07 |         0 |      1e+06      | 4.86222e+09 |
|   1378 |   34611 | 9.06367e+06 |          5.10839e+07 |         0 |      1.125e+06  | 4.0604e+09  |
|   1379 |   32478 | 1.16139e+07 |          6.91163e+07 |         0 |      1.5e+06    | 6.664e+09   |
|   1380 |   30263 | 1.32445e+07 |          6.82024e+07 |         0 |      1.85e+06   | 3.46441e+09 |
|   1381 |   35032 | 1.75767e+07 |          8.84803e+07 |         0 |      3e+06      | 8.24678e+09 |
|   1382 |   25550 | 2.28336e+07 |          1.03926e+08 |         0 |      4.45e+06   | 7.87626e+09 |
|   1383 |   27634 | 2.30627e+07 |          7.72408e+07 |         0 |      4.3e+06    | 2.13364e+09 |
|   1384 |   24367 | 3.38532e+07 |          1.46333e+08 |         0 |      9e+06      | 9e+09       |
|   1385 |   27860 | 4.15044e+07 |          1.86108e+08 |         0 |      1.107e+07  | 8.4e+09     |
|   1386 |   26521 | 5.05367e+07 |          2.31894e+08 |         0 |      1.25e+07   | 1.5e+10     |
|   1387 |   29468 | 5.55446e+07 |          1.9938e+08  |         0 |      1.62e+07   | 8.61e+09    |
|   1388 |   27868 | 5.78447e+07 |          2.40856e+08 |         0 |      1.7e+07    | 1.2e+10     |
|   1389 |   27534 | 6.47372e+07 |          2.41e+08    |         0 |      2e+07      | 1.02e+10    |
|   1390 |   24901 | 7.78768e+07 |          2.53335e+08 |         0 |      3e+07      | 1.01662e+10 |
|   1391 |   25641 | 1.01163e+08 |          3.53282e+08 |         0 |      3.5e+07    | 1.5e+10     |
|   1392 |   23470 | 1.32766e+08 |          3.77227e+08 |         0 |      5.3885e+07 | 1.5e+10     |
|   1393 |   22232 | 1.59689e+08 |          4.24821e+08 |         0 |      7e+07      | 1.9496e+10  |
|   1394 |   21368 | 1.84616e+08 |          6.49355e+08 |         0 |      8.4e+07    | 5.241e+10   |
|   1395 |   20990 | 2.15932e+08 |          9.57871e+08 |         0 |      9.2e+07    | 9.58e+10    |
|   1396 |   21828 | 2.30586e+08 |          7.21205e+08 |         0 |      1e+08      | 4.389e+10   |
|   1397 |   21727 | 3.63786e+08 |          6.6422e+09  |         0 |      1.3e+08    | 9.4665e+11  |
|   1398 |   21376 | 4.05556e+08 |          1.62665e+09 |         0 |      1.7e+08    | 1.2227e+11  |
|   1399 |   19056 | 5.48536e+08 |          1.78144e+09 |         0 |      2.28e+08   | 8.49e+10    |
|   1400 |   18284 | 8.87107e+08 |          3.04918e+09 |         0 |      3.74e+08   | 1.52624e+11 |
|   1401 |   17313 | 1.36895e+09 |          4.62231e+09 |         0 |      6e+08      | 2.7028e+11  |


### Profit

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL15
      type: float
    1369:
      column_code: DYCOL15
      type: float
    1370:
      column_code: DYCOL15
      type: float
    1371:
      column_code: DYCOL15
      type: float
    1372:
      column_code: DYCOL15
      type: float
    1373:
      column_code: DYCOL15
      type: float
    1374:
      column_code: DYCOL15
      type: float
    1375:
      column_code: DYCOL15
      type: float
    1376:
      column_code: DYCOL15
      type: float
    1377:
      column_code: DYCOL15
      type: float
    1378:
      column_code: DYCOL15
      type: float
    1379:
      column_code: DYCOL15
      type: float
    1380:
      column_code: DYCOL15
      type: float
    1381:
      column_code: DYCOL15
      type: float
    1382:
      column_code: DYCOL15
      type: float
    1383:
      column_code: DYCOL15
      type: float
    1384:
      column_code: DYCOL15
      type: float
    1385:
      column_code: DYCOL15
      type: float
    1386:
      column_code: DYCOL15
      type: float
    1387:
      column_code: DYCOL15
      type: float
    1388:
      column_code: DYCOL15
      type: float
    1389:
      column_code: DYCOL15
      type: float
    1390:
      column_code: DYCOL15
      type: float
    1391:
      column_code: DYCOL15
      type: float
    1392:
      column_code: DYCOL15
      type: float
    1393:
      column_code: DYCOL15
      type: float
    1394:
      column_code: DYCOL15
      type: float
    1395:
      column_code: DYCOL15
      type: float
    1396:
      column_code: DYCOL15
      type: float
    1397:
      column_code: DYCOL15
      type: float
    1398:
      column_code: DYCOL15
      type: float
    1399:
      column_code: DYCOL15
      type: float
    1400:
      column_code: DYCOL15
      type: float
    1401:
      column_code: DYCOL15
      type: float
    
    ```
#### Column Codes

| Years     | Profit                                                    |
|:----------|:----------------------------------------------------------|
| 1369-1373 | [COL12](/HBSIR/tables/raw/self_employed_income#col12)     |
| 1374-1383 | [COL13](/HBSIR/tables/raw/self_employed_income#col13)     |
| 1384-1401 | [DYCOL15](/HBSIR/tables/raw/self_employed_income#dycol15) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |      Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|-------------:|-----------------:|------------:|
|   1369 |   24550 | 420627           |          1.7073e+06  | -1e+08       | 136000           | 7.635e+07   |
|   1370 |   23960 | 635664           |          4.01137e+06 | -6.2381e+07  | 178950           | 3.8495e+08  |
|   1371 |   24136 | 850978           |          6.03029e+06 | -7.15e+07    | 220000           | 6e+08       |
|   1372 |   15377 |      1.0478e+06  |          6.666e+06   | -1e+08       | 330000           | 6.1875e+08  |
|   1373 |   21557 |      1.65539e+06 |          5.95502e+06 | -1e+08       | 488000           | 4.4695e+08  |
|   1374 |   44077 |      1.86784e+06 |          5.8697e+06  | -5.1695e+07  | 513000           | 5.59432e+08 |
|   1375 |   27840 |      2.36324e+06 |          1.29803e+07 | -5.4e+08     | 650000           | 1.884e+09   |
|   1376 |   26580 |      2.91047e+06 |          8.99443e+06 | -3.36e+07    | 820000           | 6.953e+08   |
|   1377 |   22012 |      3.39931e+06 |          8.57174e+06 | -9.67248e+07 |      1e+06       | 3.6e+08     |
|   1378 |   34611 |      3.82855e+06 |          1.828e+07   | -2.692e+09   |      1e+06       | 9.05e+08    |
|   1379 |   32478 |      4.69975e+06 |          1.37093e+07 | -3.489e+08   |      1.25625e+06 | 7.2e+08     |
|   1380 |   30263 |      5.59534e+06 |          1.34268e+07 | -6.28998e+07 |      1.776e+06   | 6.192e+08   |
|   1381 |   35032 |      7.51252e+06 |          2.95315e+07 | -7.2e+07     |      2.65e+06    | 4.4394e+09  |
|   1382 |   25550 |      9.52885e+06 |          2.08281e+07 | -9.853e+08   |      3.8e+06     | 6.5e+08     |
|   1383 |   27634 |      1.12297e+07 |          3.09533e+07 | -2.3e+09     |      3.95e+06    | 1.311e+09   |
|   1384 |   29115 |      1.28421e+07 |          3.40664e+07 | -2.84e+08    |      4.8e+06     | 2.954e+09   |
|   1385 |   32590 |      1.49346e+07 |          4.06184e+07 | -1.50012e+08 |      5.7e+06     | 2.882e+09   |
|   1386 |   29504 |      1.84133e+07 |          4.13461e+07 | -2.65e+08    |      7.0625e+06  | 2.4e+09     |
|   1387 |   31451 |      1.97993e+07 |          4.78544e+07 | -7.777e+08   |      7.8e+06     | 2.8365e+09  |
|   1388 |   29617 |      2.00788e+07 |          5.04771e+07 | -1.5e+09     |      8e+06       | 3.967e+09   |
|   1389 |   28652 |      2.32972e+07 |          4.58742e+07 | -1.333e+09   |      1.1e+07     | 2.0592e+09  |
|   1390 |   25997 |      2.89398e+07 |          5.48263e+07 | -8e+08       |      1.513e+07   | 2.5597e+09  |
|   1391 |   26787 |      3.60965e+07 |          1.08022e+08 | -6.99e+08    |      1.8e+07     | 8.125e+09   |
|   1392 |   24492 |      5.02897e+07 |          8.5635e+07  | -5.18e+08    |      2.98e+07    | 3.35e+09    |
|   1393 |   23494 |      6.20331e+07 |          1.06355e+08 | -8.1482e+08  |      3.8e+07     | 4.9414e+09  |
|   1394 |   22402 |      7.39015e+07 |          1.21769e+08 | -4.15e+08    |      4.8e+07     | 5.73528e+09 |
|   1395 |   21822 |      8.35164e+07 |          1.36408e+08 | -4e+09       |      5.4e+07     | 4.8e+09     |
|   1396 |   22290 |      9.28382e+07 |          1.25625e+08 | -9.396e+08   |      6e+07       | 4.57e+09    |
|   1397 |   21983 |      1.20017e+08 |          1.91631e+08 | -7.9e+08     |      8e+07       | 9.5e+09     |
|   1398 |   21650 |      1.49739e+08 |          2.0916e+08  | -1.26e+09    |      1.0095e+08  | 7.61e+09    |
|   1399 |   19322 |      2.07606e+08 |          3.86678e+08 | -1.5e+09     |      1.34e+08    | 2.4e+10     |
|   1400 |   18570 |      3.42352e+08 |          6.41452e+08 | -2.27e+09    |      2.22e+08    | 3.95919e+10 |
|   1401 |   16908 |      5.5667e+08  |          9.53718e+08 | -2.671e+10   |      3.935e+08   | 4.10503e+10 |


