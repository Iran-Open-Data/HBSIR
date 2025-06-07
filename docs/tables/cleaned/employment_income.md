# employment_income

## Old to New Titles

| Years     | ADDRESS   | COL01         | COL02             | COL03           | COL04         | COL05                | COL06                | COL07                     | COL08                     | COL09                    | COL10                    | COL11                   | COL12              | COL13             |
|:----------|:----------|:--------------|:------------------|:----------------|:--------------|:---------------------|:---------------------|:--------------------------|:--------------------------|:-------------------------|:-------------------------|:------------------------|:-------------------|:------------------|
| 1369      | ID        | Member_Number | Occupation_Code   | Industry_Code   | Sector        |                      | Annual_Gross_Income  |                           | Annual_Continuous_Income  |                          | Annual_Temporary_Income  |                         | Annual_Net_Income  |                   |
| 1370-1373 | ID        | Member_Number | Occupation_Code   | Industry_Code   | Sector        | Monthly_Gross_Income | Annual_Gross_Income  | Monthly_Continuous_Income | Annual_Continuous_Income  | Monthly_Temporary_Income | Annual_Temporary_Income  | Monthly_Net_Income      | Annual_Net_Income  |                   |
| 1374-1383 | ID        | Member_Number | Employment_Status | Occupation_Code | Industry_Code | Sector               | Monthly_Gross_Income | Annual_Gross_Income       | Monthly_Continuous_Income | Annual_Continuous_Income | Monthly_Temporary_Income | Annual_Temporary_Income | Monthly_Net_Income | Annual_Net_Income |


| Years     | ADDRESS   | DYCOL01       | DYCOL02           | DYCOL03         | DYCOL04       | DYCOL05   | DYCOL06               | DYCOL07              | DYCOL08              | DYCOL09             | DYCOL10                   | DYCOL11                  | DYCOL12                  | DYCOL13                 | DYCOL14            | DYCOL15           |
|:----------|:----------|:--------------|:------------------|:----------------|:--------------|:----------|:----------------------|:---------------------|:---------------------|:--------------------|:--------------------------|:-------------------------|:-------------------------|:------------------------|:-------------------|:------------------|
| 1384-1402 | ID        | Member_Number | Employment_Status | Occupation_Code | Industry_Code | Sector    | Working_Hours_per_Day | Working_Day_per_Week | Monthly_Gross_Income | Annual_Gross_Income | Monthly_Continuous_Income | Annual_Continuous_Income | Monthly_Temporary_Income | Annual_Temporary_Income | Monthly_Net_Income | Annual_Net_Income |


## New to Old Titles

| Years     | ID      | Member_Number   | Employment_Status   | Occupation_Code   | Industry_Code   | Sector   | Working_Hours_per_Day   | Working_Day_per_Week   | Monthly_Gross_Income   | Annual_Gross_Income   | Monthly_Continuous_Income   | Annual_Continuous_Income   | Monthly_Temporary_Income   | Annual_Temporary_Income   | Monthly_Net_Income   | Annual_Net_Income   |
|:----------|:--------|:----------------|:--------------------|:------------------|:----------------|:---------|:------------------------|:-----------------------|:-----------------------|:----------------------|:----------------------------|:---------------------------|:---------------------------|:--------------------------|:---------------------|:--------------------|
| 1369      | ADDRESS | COL01           |                     | COL02             | COL03           | COL04    |                         |                        |                        | COL06                 |                             | COL08                      |                            | COL10                     |                      | COL12               |
| 1370-1373 | ADDRESS | COL01           |                     | COL02             | COL03           | COL04    |                         |                        | COL05                  | COL06                 | COL07                       | COL08                      | COL09                      | COL10                     | COL11                | COL12               |
| 1374-1383 | ADDRESS | COL01           | COL02               | COL03             | COL04           | COL05    |                         |                        | COL06                  | COL07                 | COL08                       | COL09                      | COL10                      | COL11                     | COL12                | COL13               |
| 1384-1402 | ADDRESS | DYCOL01         | DYCOL02             | DYCOL03           | DYCOL04         | DYCOL05  | DYCOL06                 | DYCOL07                | DYCOL08                | DYCOL09               | DYCOL10                     | DYCOL11                    | DYCOL12                    | DYCOL13                   | DYCOL14              | DYCOL15             |


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

| Years     | ID                                                     |
|:----------|:-------------------------------------------------------|
| 1369-1402 | [ADDRESS](/HBSIR/tables/raw/employment_income#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |      Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|------------:|------------:|
|   1369 |   13132 | 629846           |     511976           |  1002          | 1.01104e+06 | 1.23422e+06 |
|   1370 |   13087 | 628592           |     511572           |  1002          | 1.01105e+06 | 1.23422e+06 |
|   1371 |   13514 | 646819           |     508069           |  1001          | 1.01307e+06 | 1.23422e+06 |
|   1372 |    8845 | 691123           |     505228           |  1003          | 1.02114e+06 | 1.23422e+06 |
|   1373 |   14813 | 772655           |     499605           |  1001          | 1.06215e+06 | 1.24404e+06 |
|   1374 |   26423 |      7.39573e+06 |          5.02199e+06 | 10001          | 1.06101e+07 | 1.24401e+07 |
|   1375 |   16818 | 640726           |     520174           |  1004          | 1.01405e+06 | 1.24404e+06 |
|   1376 |   17136 | 644769           |     519708           |  1001          | 1.02105e+06 | 1.25405e+06 |
|   1377 |   14007 |      6.21404e+07 |          5.18153e+07 | 11005          | 2.70722e+07 | 1.27074e+08 |
|   1378 |   21822 |      6.27207e+07 |          5.16361e+07 | 11001          | 2.7053e+07  | 1.27074e+08 |
|   1379 |   21108 |      6.10924e+07 |          5.13689e+07 | 11002          | 2.60331e+07 | 1.27074e+08 |
|   1380 |   20676 |      6.14975e+07 |          5.14575e+07 | 11003          | 2.60331e+07 | 1.27074e+08 |
|   1381 |   24597 |      6.28819e+07 |          5.12223e+07 | 11005          | 2.70612e+07 | 1.27074e+08 |
|   1382 |   18191 |      6.41104e+07 |          5.13188e+07 | 11001          | 2.71021e+07 | 1.27114e+08 |
|   1383 |   19605 |      6.26096e+07 |          5.13389e+07 | 11001          | 2.7054e+07  | 1.27114e+08 |
|   1384 |   21199 |      6.48009e+07 |          5.11313e+07 | 11001          | 2.91211e+07 | 1.29214e+08 |
|   1385 |   23036 |      6.32574e+07 |          5.14528e+07 | 11001          | 2.80921e+07 | 1.29214e+08 |
|   1386 |   24087 |      6.43569e+07 |          5.08929e+07 | 11007          | 2.9034e+07  | 1.29214e+08 |
|   1387 |   29355 |      1.64164e+09 |          5.03915e+08 |     1e+09      | 1.29763e+09 | 2.29786e+09 |
|   1388 |   26699 |      1.6249e+09  |          5.03681e+08 |     1e+09      | 1.28012e+09 | 2.29025e+09 |
|   1389 |   26974 |      1.6473e+09  |          5.03872e+08 |     1e+09      | 2.00003e+09 | 2.29013e+09 |
|   1390 |   25063 |      1.64431e+09 |          5.04373e+08 |     1e+09      | 1.30005e+09 | 2.30013e+09 |
|   1391 |   24337 |      1.63594e+09 |          5.05132e+08 |     1e+09      | 1.29012e+09 | 2.30013e+09 |
|   1392 |   23759 |      1.62938e+10 |          5.03504e+09 |     1.0001e+10 | 1.29046e+10 | 2.30047e+10 |
|   1393 |   23887 |      1.631e+10   |          5.03664e+09 |     1.0001e+10 | 1.29046e+10 | 2.30047e+10 |
|   1394 |   23798 |      1.6319e+10  |          5.04911e+09 |     1.0001e+10 | 1.29056e+10 | 2.30047e+10 |
|   1395 |   23564 |      1.63156e+10 |          5.04688e+09 |     1.0001e+10 | 1.29046e+10 | 2.30047e+10 |
|   1396 |   23805 |      1.63151e+10 |          5.04747e+09 |     1.0001e+10 | 1.29026e+10 | 2.30047e+10 |
|   1397 |   24482 |      1.60693e+10 |          5.01589e+09 |     1.0001e+10 | 1.27133e+10 | 2.30067e+10 |
|   1398 |   23575 |      1.61428e+10 |          5.02286e+09 |     1.0001e+10 | 1.28023e+10 | 2.30067e+10 |
|   1399 |   23073 |      1.62619e+10 |          5.01881e+09 |     1.0001e+10 | 1.28074e+10 | 2.30067e+10 |
|   1400 |   23130 |      1.61739e+10 |          5.00668e+09 |     1.0001e+10 | 1.28034e+10 | 2.30067e+10 |
|   1401 |   22615 |      1.60988e+10 |          5.01045e+09 |     1.0001e+10 | 1.27143e+10 | 2.30067e+10 |
|   1402 |   22094 |      1.60955e+10 |          5.01589e+09 |     1.0001e+10 | 1.27143e+10 | 2.30067e+10 |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1374 | 00         |             nan |           2 |
|   1374 | 01         |             nan |           2 |
|   1374 | 02         |             nan |           2 |
|   1374 | 10         |             nan |           4 |
|   1374 | 11         |             nan |           4 |
|   1374 | 12         |             nan |           3 |


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
    1402:
      column_code: DYCOL01
      type: UInt8
    
    ```
#### Column Codes

| Years     | Member_Number                                          |
|:----------|:-------------------------------------------------------|
| 1369-1383 | [COL01](/HBSIR/tables/raw/employment_income#col01)     |
| 1384-1402 | [DYCOL01](/HBSIR/tables/raw/employment_income#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1369 |   13132 |   1.79 |                 1.41 |         1 |        1 |        20 |
|   1370 |   13087 |   1.82 |                 1.44 |         0 |        1 |        15 |
|   1371 |   13514 |   1.77 |                 1.43 |         0 |        1 |        17 |
|   1372 |    8845 |   1.8  |                 1.47 |         0 |        1 |        50 |
|   1373 |   14813 |   1.83 |                 1.45 |         0 |        1 |        21 |
|   1374 |   26440 |   1.82 |                 1.43 |         0 |        1 |        20 |
|   1375 |   16818 |   1.88 |                 1.47 |         1 |        1 |        18 |
|   1376 |   17136 |   1.87 |                 1.43 |         1 |        1 |        22 |
|   1377 |   14007 |   1.93 |                 1.46 |         1 |        1 |        15 |
|   1378 |   21822 |   1.97 |                 1.5  |         1 |        1 |        15 |
|   1379 |   21108 |   1.95 |                 1.48 |         1 |        1 |        16 |
|   1380 |   20676 |   1.97 |                 1.49 |         1 |        1 |        17 |
|   1381 |   24597 |   2.02 |                 1.52 |         1 |        1 |        15 |
|   1382 |   18191 |   1.98 |                 1.49 |         1 |        1 |        22 |
|   1383 |   19604 |   2.02 |                 1.54 |         1 |        1 |        14 |
|   1384 |   21199 |   2.03 |                 1.53 |         1 |        1 |        20 |
|   1385 |   23036 |   2.02 |                 1.5  |         1 |        1 |        16 |
|   1386 |   24087 |   2.01 |                 1.47 |         1 |        1 |        13 |
|   1387 |   29355 |   1.92 |                 1.42 |         1 |        1 |        16 |
|   1388 |   26698 |   1.93 |                 1.43 |         1 |        1 |        16 |
|   1389 |   26971 |   1.92 |                 1.39 |         1 |        1 |        17 |
|   1390 |   25060 |   1.88 |                 1.36 |         1 |        1 |        16 |
|   1391 |   24335 |   1.89 |                 1.35 |         1 |        1 |        16 |
|   1392 |   23759 |   1.69 |                 1.2  |         1 |        1 |        14 |
|   1393 |   23886 |   1.73 |                 1.23 |         1 |        1 |        12 |
|   1394 |   23798 |   1.73 |                 1.21 |         1 |        1 |        13 |
|   1395 |   23564 |   1.74 |                 1.21 |         1 |        1 |        12 |
|   1396 |   23805 |   1.76 |                 1.21 |         1 |        1 |        14 |
|   1397 |   24482 |   1.69 |                 1.15 |         1 |        1 |        12 |
|   1398 |   23575 |   1.7  |                 1.16 |         1 |        1 |        14 |
|   1399 |   23073 |   1.66 |                 1.12 |         1 |        1 |        14 |
|   1400 |   23130 |   1.66 |                 1.09 |         1 |        1 |        10 |
|   1401 |   22615 |   1.66 |                 1.08 |         1 |        1 |        10 |
|   1402 |   22094 |   1.69 |                 1.1  |         1 |        1 |        11 |


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
    1402:
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

| Years     | Employment_Status                                      |
|:----------|:-------------------------------------------------------|
| 1369-1373 |                                                        |
| 1374-1383 | [COL02](/HBSIR/tables/raw/employment_income#col02)     |
| 1384-1402 | [DYCOL02](/HBSIR/tables/raw/employment_income#dycol02) |


#### Summary Statistics

**category data**

|   Year |   Employed |   Unemployed | nan   |
|-------:|-----------:|-------------:|:------|
|   1374 |      83.43 |        16.55 | 0.02  |
|   1375 |      81.48 |        18.47 | 0.04  |
|   1376 |      81.98 |        18.02 |       |
|   1377 |      80.51 |        19.49 |       |
|   1378 |      80.69 |        19.31 |       |
|   1379 |      80.87 |        19.13 |       |
|   1380 |      83.18 |        16.82 |       |
|   1381 |      84.05 |        15.95 |       |
|   1382 |      84.55 |        15.45 |       |
|   1383 |      82.52 |        17.48 | 0.01  |
|   1384 |      82.93 |        17.07 |       |
|   1385 |      83.18 |        16.82 |       |
|   1386 |      83.26 |        16.74 |       |
|   1387 |      85.04 |        14.96 |       |
|   1388 |      83.89 |        16.1  | 0.0   |
|   1389 |      86.07 |        13.92 | 0.01  |
|   1390 |      89.12 |        10.86 | 0.01  |
|   1391 |      88.96 |        11.03 | 0.01  |
|   1392 |      90.06 |         9.94 |       |
|   1393 |      89.81 |        10.19 | 0.0   |
|   1394 |      88.98 |        11.02 |       |
|   1395 |      88.95 |        11.05 |       |
|   1396 |      88.75 |        11.25 |       |
|   1397 |      89.58 |        10.42 |       |
|   1398 |      89.19 |        10.81 |       |
|   1399 |      89.1  |        10.9  |       |
|   1400 |      91.59 |         8.41 |       |
|   1401 |      92.4  |         7.6  | 0.0   |
|   1402 |      92.96 |         7.04 |       |


#### Categories

|    | 1374-1402   |
|---:|:------------|
|  1 | Employed    |
|  2 | Unemployed  |


#### Replacements

|   Year |   Value |   Replace_Value |   Frequency |
|-------:|--------:|----------------:|------------:|
|   1374 |       3 |             nan |           1 |
|   1374 |       9 |             nan |           2 |


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
    1402:
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

| Years     | Occupation_Code                                        |
|:----------|:-------------------------------------------------------|
| 1369-1373 | [COL02](/HBSIR/tables/raw/employment_income#col02)     |
| 1374-1383 | [COL03](/HBSIR/tables/raw/employment_income#col03)     |
| 1384-1402 | [DYCOL03](/HBSIR/tables/raw/employment_income#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1369 |   10658 |  646.93 |               302.85 |        13 |      700 |       999 |
|   1370 |   11008 |  643.59 |               306.32 |        11 |      641 |       999 |
|   1371 |   11379 |  640.51 |               309.15 |        13 |      700 |       999 |
|   1372 |    7642 |  621.65 |               316.73 |        13 |      626 |       999 |
|   1373 |   12716 |  616.43 |               316.72 |        11 |      626 |       999 |
|   1374 |   25261 |  635.4  |               311.9  |         0 |      629 |       999 |
|   1375 |   16818 |  664.38 |               280.03 |        11 |      742 |       933 |
|   1376 |   17136 |  667.99 |               279.18 |        11 |      743 |       933 |
|   1377 |   14007 |  675.69 |               281.5  |        11 |      744 |       933 |
|   1378 |   21822 | 6745.32 |              2793.18 |       111 |     7437 |      9333 |
|   1379 |   21108 | 6817.91 |              2770.8  |       111 |     7501 |      9333 |
|   1380 |   20676 | 6813.37 |              2757.94 |       111 |     7501 |      9333 |
|   1381 |   24597 | 6820.2  |              2788.92 |       111 |     7501 |      9333 |
|   1382 |   18191 | 6786.82 |              2768.56 |       111 |     7438 |      9333 |
|   1383 |   19604 | 6762.76 |              2794.66 |       111 |     7438 |      9333 |
|   1384 |   21199 | 6771.93 |              2794.93 |       111 |     7442 |      9333 |
|   1385 |   23036 | 6879.13 |              2768    |       111 |     8125 |      9333 |
|   1386 |   24086 | 6861.71 |              2803.46 |       111 |     8132 |      9333 |
|   1387 |   29355 | 6942.65 |              2781.74 |       111 |     8261 |      9333 |
|   1388 |   26698 | 7031.94 |              2749.98 |         0 |     8322 |      9333 |
|   1389 |   26971 | 6976.59 |              2783.66 |       111 |     8322 |      9333 |
|   1390 |   25060 | 6930.26 |              2786.53 |       111 |     8232 |      9333 |
|   1391 |   24335 | 6934.25 |              2779.11 |       111 |     8251 |      9333 |
|   1392 |   23759 | 6994.64 |              2742.93 |         0 |     8311 |      9333 |
|   1393 |   23886 | 7030.3  |              2722.58 |       111 |     8322 |      9333 |
|   1394 |   23798 | 7037.58 |              2717.54 |       111 |     8322 |      9333 |
|   1395 |   23564 | 7036.18 |              2697.82 |       111 |     8322 |      9333 |
|   1396 |   23805 | 6891.92 |              2769.74 |         0 |     8142 |      9629 |
|   1397 |   24482 | 6757.15 |              2802.7  |       410 |     7522 |      9629 |
|   1398 |   23575 | 6794.14 |              2762.65 |       410 |     7536 |      9629 |
|   1399 |   23073 | 6940.14 |              2721.56 |       410 |     8151 |      9629 |
|   1400 |   23130 | 6911.6  |              2733.31 |       410 |     8131 |      9629 |
|   1401 |   22614 | 6867.76 |              2733.63 |       410 |     8114 |      9629 |
|   1402 |   22094 | 6837.29 |              2739.64 |       410 |     7537 |      9629 |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1369 | X01     |             nan |          20 |
|   1369 | X02     |             nan |          45 |
|   1369 | X03     |             nan |         326 |
|   1369 | X04     |             nan |          70 |
|   1370 | X01     |             nan |           9 |
|   1370 | X02     |             nan |           7 |
|   1370 | X03     |             nan |         375 |
|   1370 | X04     |             nan |          85 |
|   1371 | X01     |             nan |          16 |
|   1371 | X02     |             nan |           3 |
|   1371 | X03     |             nan |         318 |
|   1371 | X04     |             nan |         124 |
|   1372 | X01     |             nan |          13 |
|   1372 | X02     |             nan |           2 |
|   1372 | X03     |             nan |         237 |
|   1372 | X04     |             nan |          79 |
|   1373 | X01     |             nan |          12 |
|   1373 | X03     |             nan |         433 |
|   1373 | X04     |             nan |         187 |
|   1374 | x01     |             nan |          38 |
|   1374 | x02     |             nan |           7 |
|   1374 | x03     |             nan |         689 |
|   1374 | x04     |             nan |         444 |
|   1388 | x000    |               0 |           1 |
|   1392 | x000    |               0 |           2 |
|   1396 | x000    |               0 |           1 |


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
    1402:
      column_code: DYCOL04
      type: UInt32
      replace:
        x0000: 0
        x000: 0
    
    ```
#### Column Codes

| Years     | Industry_Code                                          |
|:----------|:-------------------------------------------------------|
| 1369-1373 | [COL03](/HBSIR/tables/raw/employment_income#col03)     |
| 1374-1383 | [COL04](/HBSIR/tables/raw/employment_income#col04)     |
| 1384-1402 | [DYCOL04](/HBSIR/tables/raw/employment_income#dycol04) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|----------:|
|   1369 |   11124 |  5790.89 |              2930.19 |       110 |     5101 |      9600 |
|   1370 |   11484 |  5853.98 |              2910.19 |       110 |     5101 |      9599 |
|   1371 |   11840 |  5867.92 |              2876.91 |       110 |     5101 |      9599 |
|   1372 |    7973 |  5937.54 |              2870.73 |       110 |     5101 |      9599 |
|   1373 |   13348 |  6046.82 |              2827.36 |       110 |     5501 |      9600 |
|   1374 |   26437 |  4728.98 |              2714.02 |         0 |     4521 |      9999 |
|   1375 |   16818 |   441.97 |               276.92 |        11 |      452 |       980 |
|   1376 |   17136 |   446.26 |               277.81 |        11 |      452 |       970 |
|   1377 |   14007 |   434.29 |               278.68 |        11 |      452 |       970 |
|   1378 |   21822 |  4374.49 |              2792.07 |       111 |     4521 |      9800 |
|   1379 |   21108 |  4355    |              2766.37 |       111 |     4521 |      9900 |
|   1380 |   20676 |  4418.85 |              2742.59 |       111 |     4521 |      9800 |
|   1381 |   24597 |  4422.5  |              2731.13 |       111 |     4521 |      9900 |
|   1382 |   18191 |  4457.98 |              2689.68 |       111 |     4521 |      9700 |
|   1383 |   19603 |  4491.21 |              2703.25 |       111 |     4521 |      9900 |
|   1384 |   21199 |  4460.8  |              2700.37 |       111 |     4521 |      9700 |
|   1385 |   23036 |  4472.72 |              2651.64 |       111 |     4521 |      9700 |
|   1386 |   24087 |  4560.91 |              2590.12 |       111 |     4521 |      9700 |
|   1387 |   29355 |  4556.11 |              2560.9  |         0 |     4521 |      9800 |
|   1388 |   26698 |  4504.01 |              2566.22 |         0 |     4521 |      9900 |
|   1389 |   26971 |  4570.93 |              2551.08 |       111 |     4521 |      9800 |
|   1390 |   25060 |  4642.97 |              2499.22 |       111 |     4521 |      9800 |
|   1391 |   24335 |  4615.39 |              2510.69 |       111 |     4521 |      9900 |
|   1392 |   23759 | 44221.4  |             27403.3  |         0 |    41000 |     99000 |
|   1393 |   23887 | 43892.5  |             27547.9  |         0 |    41000 |     97000 |
|   1394 |   23798 | 43883.7  |             27888.3  |      1110 |    41000 |     97000 |
|   1395 |   23564 | 43568.2  |             27742.8  |      1110 |    41000 |     97000 |
|   1396 |   23805 | 43374.6  |             27818.8  |         0 |    41000 |     99000 |
|   1397 |   24482 | 43932.2  |             28067.3  |      1110 |    41000 |     99000 |
|   1398 |   23575 | 43158    |             28253.6  |      1110 |    41000 |     99000 |
|   1399 |   23073 | 42511.6  |             27726.5  |      1110 |    41000 |     97000 |
|   1400 |   23130 | 42858.9  |             27703.5  |      1110 |    41000 |     98200 |
|   1401 |   22614 | 43083.7  |             27649.7  |      1110 |    41000 |     97000 |
|   1402 |   22092 | 43068.2  |             27660.1  |      1110 |    41000 |     98200 |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1387 | x000    |               0 |           3 |
|   1388 | x000    |               0 |           1 |
|   1392 | x0000   |               0 |           1 |
|   1393 | x0000   |               0 |           1 |
|   1396 | x0000   |               0 |           1 |


### Sector

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Private
      replace: null
    1369:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Private
      replace: null
    1370:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Private
      replace: null
    1371:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Private
      replace: null
    1372:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Private
      replace: null
    1373:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Private
      replace: null
    1374:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Private
      replace:
        0.0: null
    1375:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Private
      replace:
        3: null
    1376:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Private
      replace: null
    1377:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1378:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1379:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1380:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1381:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1382:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1383:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1384:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1385:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1386:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1387:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1388:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1389:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1390:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1391:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1392:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1393:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1394:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1395:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1396:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1397:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1398:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1399:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1400:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1401:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    1402:
      column_code: DYCOL05
      type: category
      categories:
        1: Public
        2: Cooperative
        3: Private
      replace: null
    
    ```
#### Column Codes

| Years     | Sector                                                 |
|:----------|:-------------------------------------------------------|
| 1369-1373 | [COL04](/HBSIR/tables/raw/employment_income#col04)     |
| 1374-1383 | [COL05](/HBSIR/tables/raw/employment_income#col05)     |
| 1384-1402 | [DYCOL05](/HBSIR/tables/raw/employment_income#dycol05) |


#### Summary Statistics

**category data**

|   Year |   Private |   Public | Cooperative   | nan   |
|-------:|----------:|---------:|:--------------|:------|
|   1369 |     62    |    38    |               |       |
|   1370 |     60.73 |    39.27 |               |       |
|   1371 |     60.99 |    39.01 |               |       |
|   1372 |     60.25 |    39.75 |               |       |
|   1373 |     59.18 |    40.82 |               |       |
|   1374 |     58.71 |    41.04 |               | 0.25  |
|   1375 |     63.86 |    36.13 |               | 0.01  |
|   1376 |     63.18 |    36.82 |               |       |
|   1377 |     64.2  |    33.84 | 1.96          |       |
|   1378 |     67.13 |    32.13 | 0.73          |       |
|   1379 |     69.22 |    30.31 | 0.48          |       |
|   1380 |     69.97 |    29.45 | 0.58          |       |
|   1381 |     71.53 |    27.87 | 0.6           |       |
|   1382 |     72.16 |    27.32 | 0.52          |       |
|   1383 |     72.81 |    26.6  | 0.58          | 0.01  |
|   1384 |     73.66 |    25.8  | 0.53          |       |
|   1385 |     75.31 |    24.24 | 0.45          |       |
|   1386 |     76.08 |    23.51 | 0.41          |       |
|   1387 |     76.45 |    23.13 | 0.42          |       |
|   1388 |     78.18 |    21.39 | 0.43          | 0.0   |
|   1389 |     78.76 |    20.85 | 0.38          | 0.01  |
|   1390 |     78.77 |    20.82 | 0.39          | 0.01  |
|   1391 |     78.56 |    21.03 | 0.4           | 0.01  |
|   1392 |     79.02 |    20.6  | 0.38          |       |
|   1393 |     80.23 |    19.39 | 0.37          | 0.0   |
|   1394 |     80.49 |    19.18 | 0.33          |       |
|   1395 |     81    |    18.8  | 0.2           |       |
|   1396 |     81.57 |    18.17 | 0.26          |       |
|   1397 |     81.28 |    18.48 | 0.24          |       |
|   1398 |     82.05 |    17.8  | 0.15          |       |
|   1399 |     83.31 |    16.49 | 0.2           |       |
|   1400 |     83.1  |    16.76 | 0.14          |       |
|   1401 |     82.78 |    16.98 | 0.23          | 0.01  |
|   1402 |     82.98 |    16.88 | 0.13          | 0.01  |


#### Categories

|    | 1369-1376   | 1377-1402   |
|---:|:------------|:------------|
|  1 | Public      | Public      |
|  2 | Private     | Cooperative |
|  3 |             | Private     |


#### Replacements

|   Year |   Value |   Replace_Value |   Frequency |
|-------:|--------:|----------------:|------------:|
|   1374 |       0 |             nan |           5 |
|   1375 |       3 |             nan |           1 |


### Working_Hours_per_Day

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL06
      type: UInt8
    
    ```
#### Column Codes

| Years     | Working_Hours_per_Day                                  |
|:----------|:-------------------------------------------------------|
| 1369-1383 |                                                        |
| 1384-1402 | [DYCOL06](/HBSIR/tables/raw/employment_income#dycol06) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1384 |   19564 |   7.79 |                 3.01 |         0 |        8 |        24 |
|   1385 |   21291 |   7.68 |                 3.05 |         0 |        8 |        18 |
|   1386 |   20386 |   8.37 |                 2.05 |         0 |        8 |        48 |
|   1387 |   25259 |   8.39 |                 1.99 |         0 |        8 |        18 |
|   1388 |   22657 |   8.34 |                 1.93 |         0 |        8 |        18 |
|   1389 |   23443 |   8.32 |                 1.88 |         0 |        8 |        18 |
|   1390 |   22499 |   8.36 |                 1.8  |         0 |        8 |        18 |
|   1391 |   21723 |   8.35 |                 1.77 |         0 |        8 |        18 |
|   1392 |   21568 |   8.29 |                 1.72 |         0 |        8 |        18 |
|   1393 |   21563 |   8.28 |                 1.71 |         0 |        8 |        18 |
|   1394 |   21313 |   8.25 |                 1.77 |         0 |        8 |        18 |
|   1395 |   21082 |   8.2  |                 1.75 |         0 |        8 |        18 |
|   1396 |   21339 |   8.22 |                 1.83 |         0 |        8 |        18 |
|   1397 |   22106 |   8.25 |                 1.87 |         0 |        8 |        18 |
|   1398 |   21376 |   8.22 |                 1.93 |         0 |        8 |        18 |
|   1399 |   21072 |   8.17 |                 1.89 |         0 |        8 |        18 |
|   1400 |   21593 |   8.17 |                 1.89 |         0 |        8 |        18 |
|   1401 |   20923 |   8.19 |                 1.75 |         1 |        8 |        18 |
|   1402 |   20637 |   8.22 |                 1.74 |         1 |        8 |        18 |


### Working_Day_per_Week

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL07
      type: UInt8
    
    ```
#### Column Codes

| Years     | Working_Day_per_Week                                   |
|:----------|:-------------------------------------------------------|
| 1369-1383 |                                                        |
| 1384-1402 | [DYCOL07](/HBSIR/tables/raw/employment_income#dycol07) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1384 |   19485 |   5.29 |                 1.86 |         0 |        6 |         7 |
|   1385 |   21288 |   5.22 |                 1.95 |         0 |        6 |         7 |
|   1386 |   20389 |   5.62 |                 1.22 |         0 |        6 |         7 |
|   1387 |   25260 |   5.55 |                 1.26 |         0 |        6 |         8 |
|   1388 |   22657 |   5.45 |                 1.32 |         0 |        6 |         7 |
|   1389 |   23439 |   5.4  |                 1.36 |         0 |        6 |         7 |
|   1390 |   22501 |   5.48 |                 1.27 |         0 |        6 |         7 |
|   1391 |   21722 |   5.4  |                 1.28 |         0 |        6 |         7 |
|   1392 |   21569 |   5.37 |                 1.29 |         0 |        6 |         7 |
|   1393 |   21561 |   5.38 |                 1.27 |         0 |        6 |         7 |
|   1394 |   21311 |   5.36 |                 1.29 |         0 |        6 |         7 |
|   1395 |   21083 |   5.32 |                 1.33 |         0 |        6 |         7 |
|   1396 |   21340 |   5.26 |                 1.38 |         0 |        6 |         7 |
|   1397 |   22107 |   5.32 |                 1.37 |         0 |        6 |         7 |
|   1398 |   21375 |   5.33 |                 1.34 |         0 |        6 |         7 |
|   1399 |   21074 |   5.24 |                 1.37 |         0 |        6 |         7 |
|   1400 |   21596 |   5.24 |                 1.36 |         0 |        6 |         7 |
|   1401 |   20923 |   5.33 |                 1.26 |         1 |        6 |         7 |
|   1402 |   20637 |   5.36 |                 1.24 |         1 |        6 |         7 |


### Monthly_Gross_Income

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL08
      type: float
    1370:
      column_code: DYCOL08
      type: float
    1371:
      column_code: DYCOL08
      type: float
    1372:
      column_code: DYCOL08
      type: float
    1373:
      column_code: DYCOL08
      type: float
    1374:
      column_code: DYCOL08
      type: float
    1375:
      column_code: DYCOL08
      type: float
    1376:
      column_code: DYCOL08
      type: float
    1377:
      column_code: DYCOL08
      type: float
    1378:
      column_code: DYCOL08
      type: float
    1379:
      column_code: DYCOL08
      type: float
    1380:
      column_code: DYCOL08
      type: float
    1381:
      column_code: DYCOL08
      type: float
    1382:
      column_code: DYCOL08
      type: float
    1383:
      column_code: DYCOL08
      type: float
    1384:
      column_code: DYCOL08
      type: float
    1385:
      column_code: DYCOL08
      type: float
    1386:
      column_code: DYCOL08
      type: float
    1387:
      column_code: DYCOL08
      type: float
    1388:
      column_code: DYCOL08
      type: float
    1389:
      column_code: DYCOL08
      type: float
    1390:
      column_code: DYCOL08
      type: float
    1391:
      column_code: DYCOL08
      type: float
    1392:
      column_code: DYCOL08
      type: float
    1393:
      column_code: DYCOL08
      type: float
    1394:
      column_code: DYCOL08
      type: float
    1395:
      column_code: DYCOL08
      type: float
    1396:
      column_code: DYCOL08
      type: float
    1397:
      column_code: DYCOL08
      type: float
    1398:
      column_code: DYCOL08
      type: float
    1399:
      column_code: DYCOL08
      type: float
    1400:
      column_code: DYCOL08
      type: float
    1401:
      column_code: DYCOL08
      type: float
    1402:
      column_code: DYCOL08
      type: float
    
    ```
#### Column Codes

| Years     | Monthly_Gross_Income                                   |
|:----------|:-------------------------------------------------------|
| 1369      |                                                        |
| 1370-1373 | [COL05](/HBSIR/tables/raw/employment_income#col05)     |
| 1374-1383 | [COL06](/HBSIR/tables/raw/employment_income#col06)     |
| 1384-1402 | [DYCOL08](/HBSIR/tables/raw/employment_income#dycol08) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-----------------:|------------:|
|   1370 |   13087 |  72221.7         |      79603.7         |         0 |  70000           | 1.33158e+06 |
|   1371 |   13514 | 100044           |     114686           |         0 |  90000           | 2.4e+06     |
|   1372 |    8845 | 128754           |     154270           |         0 | 120000           | 4.70087e+06 |
|   1373 |   14813 | 161875           |     167923           |         0 | 150000           | 4.88415e+06 |
|   1374 |   26440 | 202054           |     228460           |         0 | 185000           | 9.73342e+06 |
|   1375 |   16818 | 269557           |     319800           |         0 | 240000           | 1.3e+07     |
|   1376 |   17136 | 341137           |     400510           |         0 | 300000           | 1.8e+07     |
|   1377 |   14007 | 409045           |     526119           |         0 | 350000           | 2.2e+07     |
|   1378 |   21822 | 476558           |     675908           |         0 | 400000           | 3.222e+07   |
|   1379 |   21108 | 560898           |     697898           |         0 | 450000           | 2e+07       |
|   1380 |   20676 | 669881           |     771426           |         0 | 520000           | 2.5e+07     |
|   1381 |   24597 | 829994           |     946444           |         0 | 659000           | 2.45e+07    |
|   1382 |   18191 |      1.05385e+06 |          1.78531e+06 |         0 | 850000           | 1.75e+08    |
|   1383 |   19605 |      1.26194e+06 |          1.96658e+06 |         0 |      1.025e+06   | 1.875e+08   |
|   1384 |   21199 |      1.52044e+06 |          1.82699e+06 |         0 |      1.25e+06    | 6.04795e+07 |
|   1385 |   23036 |      1.80912e+06 |          2.78817e+06 |         0 |      1.5e+06     | 2.97e+08    |
|   1386 |   24087 |      2.08696e+06 |          2.23282e+06 |         0 |      1.8e+06     | 7.969e+07   |
|   1387 |   29355 |      2.46336e+06 |          2.46515e+06 |         0 |      2.196e+06   | 7.77032e+07 |
|   1388 |   26699 |      2.72296e+06 |          2.83551e+06 |         0 |      2.48e+06    | 9.7e+07     |
|   1389 |   26973 |      3.18493e+06 |          3.54798e+06 |         0 |      3e+06       | 1.545e+08   |
|   1390 |   25059 |      3.88184e+06 |          4.2903e+06  |         0 |      3.5e+06     | 1.65e+08    |
|   1391 |   24336 |      4.98899e+06 |          4.64556e+07 |         0 |      4e+06       | 7.20576e+09 |
|   1392 |   23759 |      6.19735e+06 |          6.45687e+06 |         0 |      5.5e+06     | 1.6e+08     |
|   1393 |   23882 |      7.58276e+06 |          7.52524e+06 |         0 |      7e+06       | 2.1525e+08  |
|   1394 |   23798 |      8.98737e+06 |          1.03995e+07 |         0 |      8e+06       | 4.03e+08    |
|   1395 |   23564 |      1.00695e+07 |          1.27477e+07 |         0 |      8.6e+06     | 9.12e+08    |
|   1396 |   23805 |      1.1141e+07  |          1.11922e+07 |         0 |      9.33333e+06 | 3.3e+08     |
|   1397 |   24482 |      1.33882e+07 |          1.5943e+07  |         0 |      1.114e+07   | 1.2e+09     |
|   1398 |   23575 |      1.64841e+07 |          1.74813e+07 |         0 |      1.5e+07     | 1.04e+09    |
|   1399 |   23073 |      2.36146e+07 |          3.58183e+07 |         0 |      2e+07       | 4.095e+09   |
|   1400 |   23130 |      3.72057e+07 |          5.70332e+07 |         0 |      3.2e+07     | 7e+09       |
|   1401 |   22615 |      5.52249e+07 |          4.62816e+07 |         0 |      5e+07       | 1.498e+09   |
|   1402 |   22094 |      8.30324e+07 |          7.58914e+07 |         0 |      7.6275e+07  | 3.625e+09   |


### Annual_Gross_Income

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
    1402:
      column_code: DYCOL09
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Gross_Income                                    |
|:----------|:-------------------------------------------------------|
| 1369-1373 | [COL06](/HBSIR/tables/raw/employment_income#col06)     |
| 1374-1383 | [COL07](/HBSIR/tables/raw/employment_income#col07)     |
| 1384-1402 | [DYCOL09](/HBSIR/tables/raw/employment_income#dycol09) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-----------------:|------------:|
|   1369 |   13132 | 662558           |     687224           |         0 | 550000           | 2.0645e+07  |
|   1370 |   13087 | 881293           |          1.12891e+06 |         0 | 734500           | 7.44e+07    |
|   1371 |   13514 |      1.16269e+06 |          1.23023e+06 |         0 | 950000           | 3.05e+07    |
|   1372 |    8845 |      1.52538e+06 |          1.67231e+06 |         0 |      1.3195e+06  | 5.05e+07    |
|   1373 |   14813 |      1.99234e+06 |          2.02283e+06 |         0 |      1.8e+06     | 6.39386e+07 |
|   1374 |   26440 |      2.4358e+06  |          2.58743e+06 |         0 |      2.14609e+06 | 1.18001e+08 |
|   1375 |   16818 |      3.14675e+06 |          3.49586e+06 |         0 |      2.54751e+06 | 1.12675e+08 |
|   1376 |   17136 |      4.05816e+06 |          4.81983e+06 |         0 |      3.3e+06     | 2.16e+08    |
|   1377 |   14007 |      4.89608e+06 |          5.86748e+06 |         0 |      3.6e+06     | 1.67e+08    |
|   1378 |   21822 |      5.64506e+06 |          7.49904e+06 |         0 |      4.05e+06    | 3.8664e+08  |
|   1379 |   21108 |      6.66841e+06 |          7.83305e+06 |         0 |      4.8e+06     | 2.1e+08     |
|   1380 |   20676 |      8.1231e+06  |          1.06633e+07 |         0 |      5.57471e+06 | 7.11794e+08 |
|   1381 |   24597 |      9.79582e+06 |          1.08045e+07 |         0 |      7e+06       | 4.0226e+08  |
|   1382 |   18191 |      1.23027e+07 |          1.43695e+07 |         0 |      8.96e+06    | 4.552e+08   |
|   1383 |   19605 |      1.46163e+07 |          1.52989e+07 |         0 |      1.08e+07    | 8.545e+08   |
|   1384 |   21199 |      1.77105e+07 |          1.88514e+07 |         0 |      1.32e+07    | 6.384e+08   |
|   1385 |   23036 |      2.12909e+07 |          2.27756e+07 |         0 |      1.6e+07     | 6.18635e+08 |
|   1386 |   24087 |      2.51778e+07 |          2.8325e+07  |         0 |      1.86e+07    | 9.9688e+08  |
|   1387 |   29355 |      2.84707e+07 |          2.77675e+07 |         0 |      2.31e+07    | 9.37232e+08 |
|   1388 |   26698 |      3.19047e+07 |          3.38623e+07 |         0 |      2.45e+07    | 1.23e+09    |
|   1389 |   26971 |      3.67291e+07 |          5.36732e+07 |         0 |      3e+07       | 6.92475e+09 |
|   1390 |   25060 |      4.44215e+07 |          6.79786e+07 |         0 |      3.6e+07     | 9e+09       |
|   1391 |   24335 |      5.33399e+07 |          4.97495e+07 |         0 |      4.7e+07     | 1.751e+09   |
|   1392 |   23759 |      7.13913e+07 |          9.59574e+07 |         0 |      6e+07       | 7.51452e+09 |
|   1393 |   23885 |      8.80304e+07 |          7.94101e+07 |         0 |      7.2e+07     | 2.76e+09    |
|   1394 |   23798 |      1.0358e+08  |          8.90288e+07 |         0 |      8.7e+07     | 3.0843e+09  |
|   1395 |   23564 |      1.18332e+08 |          1.03779e+08 |         0 |      9.6e+07     | 2.4088e+09  |
|   1396 |   23805 |      1.32118e+08 |          1.21946e+08 |         0 |      1.06e+08    | 4.492e+09   |
|   1397 |   24482 |      1.58182e+08 |          1.42265e+08 |         0 |      1.2e+08     | 6.9095e+09  |
|   1398 |   23575 |      1.96527e+08 |          1.85919e+08 |         0 |      1.56e+08    | 8.80954e+09 |
|   1399 |   23073 |      2.77996e+08 |          2.75994e+08 |         0 |      2.29984e+08 | 2.02922e+10 |
|   1400 |   23130 |      4.39243e+08 |          6.97932e+08 |         0 |      3.6e+08     | 8.88e+10    |
|   1401 |   22615 |      6.55362e+08 |          5.38651e+08 |         0 |      6e+08       | 1.44e+10    |
|   1402 |   22094 |      9.63213e+08 |          7.39636e+08 |         0 |      8.5e+08     | 2.252e+10   |


### Monthly_Continuous_Income

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
    1402:
      column_code: DYCOL10
      type: float
    
    ```
#### Column Codes

| Years     | Monthly_Continuous_Income                              |
|:----------|:-------------------------------------------------------|
| 1369      |                                                        |
| 1370-1373 | [COL07](/HBSIR/tables/raw/employment_income#col07)     |
| 1374-1383 | [COL08](/HBSIR/tables/raw/employment_income#col08)     |
| 1384-1402 | [DYCOL10](/HBSIR/tables/raw/employment_income#dycol10) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-----------------:|------------:|
|   1370 |   13087 |  63137.4         |      58416.2         |         0 |  64008           | 1.05e+06    |
|   1371 |   13514 |  87156.7         |      80622.1         |         0 |  84000           | 1.59533e+06 |
|   1372 |    8845 | 111577           |      98575.6         |         0 | 112055           | 2.00857e+06 |
|   1373 |   14813 | 139902           |     115589           |         0 | 143507           | 2.1e+06     |
|   1374 |   26440 | 174370           |     179926           |         0 | 170200           | 8.93648e+06 |
|   1375 |   16818 | 229780           |     230493           |         0 | 220350           | 6.65e+06    |
|   1376 |   17136 | 297394           |     308949           |         0 | 287000           | 1.5e+07     |
|   1377 |   14007 | 354677           |     381397           |         0 | 320000           | 8.4e+06     |
|   1378 |   21822 | 412753           |     531330           |         0 | 384031           | 3.222e+07   |
|   1379 |   21108 | 481654           |     526346           |         0 | 450000           | 1.995e+07   |
|   1380 |   20676 | 580567           |     614755           |         0 | 500000           | 2.5e+07     |
|   1381 |   24597 | 719416           |     698536           |         0 | 649568           | 2.45e+07    |
|   1382 |   18191 | 911275           |     922432           |         0 | 815308           | 2.475e+07   |
|   1383 |   19605 |      1.09567e+06 |          1.65808e+06 |         0 |      1e+06       | 1.875e+08   |
|   1384 |   20075 |      1.3756e+06  |          1.26965e+06 |         0 |      1.25e+06    | 6e+07       |
|   1385 |   22114 |      1.61169e+06 |          1.42074e+06 |         0 |      1.5e+06     | 4.64343e+07 |
|   1386 |   23402 |      1.89476e+06 |          1.62059e+06 |         0 |      1.8e+06     | 5e+07       |
|   1387 |   28989 |      2.19838e+06 |          1.70444e+06 |         0 |      2.09733e+06 | 2.87935e+07 |
|   1388 |   26496 |      2.43499e+06 |          1.99323e+06 |         0 |      2.4e+06     | 5.85191e+07 |
|   1389 |   26916 |      2.81821e+06 |          2.30253e+06 |         0 |      2.81375e+06 | 7e+07       |
|   1390 |   24835 |      3.44486e+06 |          2.48532e+06 |         0 |      3.33667e+06 | 5e+07       |
|   1391 |   24256 |      4.13626e+06 |          3.30159e+06 |         0 |      4e+06       | 1.45836e+08 |
|   1392 |   23664 |      5.49342e+06 |          4.14952e+06 |         0 |      5e+06       | 1.6e+08     |
|   1393 |   23586 |      6.85007e+06 |          5.01906e+06 |         0 |      6.5e+06     | 1.3715e+08  |
|   1394 |   23652 |      8.01532e+06 |          6.25208e+06 |         0 |      7.62667e+06 | 2.747e+08   |
|   1395 |   23354 |      9.11553e+06 |          7.24794e+06 |         0 |      8.4e+06     | 2e+08       |
|   1396 |   23676 |      1.02168e+07 |          8.44913e+06 |         0 |      9e+06       | 2e+08       |
|   1397 |   24469 |      1.2051e+07  |          9.96509e+06 |         0 |      1.09633e+07 | 2.67e+08    |
|   1398 |   23559 |      1.49373e+07 |          1.22668e+07 |         0 |      1.4e+07     | 3e+08       |
|   1399 |   23053 |      2.14972e+07 |          1.74184e+07 |         0 |      2e+07       | 4.76067e+08 |
|   1400 |   23114 |      3.40823e+07 |          2.48756e+07 |         0 |      3.05e+07    | 5.85e+08    |
|   1401 |   22612 |      5.07423e+07 |          3.70752e+07 |         0 |      5e+07       | 1.2e+09     |
|   1402 |   22094 |      7.60941e+07 |          5.18035e+07 |         0 |      7.4e+07     | 1.2e+09     |


### Annual_Continuous_Income

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
    1402:
      column_code: DYCOL11
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Continuous_Income                               |
|:----------|:-------------------------------------------------------|
| 1369-1373 | [COL08](/HBSIR/tables/raw/employment_income#col08)     |
| 1374-1383 | [COL09](/HBSIR/tables/raw/employment_income#col09)     |
| 1384-1402 | [DYCOL11](/HBSIR/tables/raw/employment_income#dycol11) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-----------------:|------------:|
|   1369 |   13132 | 581069           |     496099           |         0 | 530940           | 1.17967e+07 |
|   1370 |   13087 | 751297           |     914931           |         0 | 700000           | 7.44e+07    |
|   1371 |   13514 | 991672           |     841711           |         0 | 875000           | 1.9144e+07  |
|   1372 |    8845 |      1.31342e+06 |          1.12717e+06 |         0 |      1.2e+06     | 3e+07       |
|   1373 |   14813 |      1.67976e+06 |          1.35317e+06 |         0 |      1.61e+06    | 3.2e+07     |
|   1374 |   26440 |      2.0178e+06  |          1.82134e+06 |         0 |      1.8666e+06  | 1.05438e+08 |
|   1375 |   16818 |      2.64006e+06 |          2.50219e+06 |         0 |      2.4e+06     | 7.98e+07    |
|   1376 |   17136 |      3.43195e+06 |          3.37745e+06 |         0 |      3e+06       | 1.8e+08     |
|   1377 |   14007 |      4.1222e+06  |          4.42678e+06 |         0 |      3.5e+06     | 1.1424e+08  |
|   1378 |   21822 |      4.78171e+06 |          6.0468e+06  |         0 |      3.8775e+06  | 3.8664e+08  |
|   1379 |   21108 |      5.61863e+06 |          5.89418e+06 |         0 |      4.5e+06     | 2.1e+08     |
|   1380 |   20676 |      6.77674e+06 |          6.40394e+06 |         0 |      5.4e+06     | 1.16911e+08 |
|   1381 |   24597 |      8.26262e+06 |          7.62793e+06 |         0 |      6.6e+06     | 2.19404e+08 |
|   1382 |   18191 |      1.03551e+07 |          9.26688e+06 |         0 |      8.4e+06     | 2.9717e+08  |
|   1383 |   19605 |      1.2538e+07  |          1.21867e+07 |         0 |      1.032e+07   | 7.72995e+08 |
|   1384 |   21060 |      1.4973e+07  |          1.30538e+07 |         0 |      1.235e+07   | 2.14672e+08 |
|   1385 |   22726 |      1.81046e+07 |          1.5867e+07  |         0 |      1.52076e+07 | 5.57212e+08 |
|   1386 |   24023 |      2.15216e+07 |          1.94476e+07 |         0 |      1.8e+07     | 8.6e+08     |
|   1387 |   29310 |      2.47851e+07 |          1.91146e+07 |         0 |      2.2e+07     | 3.39063e+08 |
|   1388 |   26685 |      2.77715e+07 |          2.16439e+07 |         0 |      2.4e+07     | 3.168e+08   |
|   1389 |   26970 |      3.21031e+07 |          2.5261e+07  |         0 |      2.88e+07    | 5.83158e+08 |
|   1390 |   25055 |      3.89507e+07 |          2.77816e+07 |         0 |      3.6e+07     | 5.76e+08    |
|   1391 |   24329 |      4.68302e+07 |          3.31857e+07 |         0 |      4.384e+07   | 9e+08       |
|   1392 |   23751 |      6.25507e+07 |          4.342e+07   |         0 |      6e+07       | 1.7648e+09  |
|   1393 |   23784 |      7.81173e+07 |          5.69797e+07 |         0 |      7.2e+07     | 2.28e+09    |
|   1394 |   23778 |      9.2494e+07  |          6.60131e+07 |         0 |      8.4e+07     | 1.4e+09     |
|   1395 |   23543 |      1.05742e+08 |          7.96409e+07 |         0 |      9.6e+07     | 1.4718e+09  |
|   1396 |   23792 |      1.19061e+08 |          9.31007e+07 |         0 |      1.008e+08   | 1.8306e+09  |
|   1397 |   24478 |      1.42259e+08 |          1.12004e+08 |         0 |      1.2e+08     | 2.934e+09   |
|   1398 |   23568 |      1.76367e+08 |          1.38592e+08 |         0 |      1.5e+08     | 3.6e+09     |
|   1399 |   23072 |      2.5089e+08  |          1.88674e+08 |         0 |      2.16e+08    | 2.76e+09    |
|   1400 |   23124 |      3.95723e+08 |          2.77829e+08 |         0 |      3.6e+08     | 3.6e+09     |
|   1401 |   22611 |      5.92957e+08 |          3.99955e+08 |         0 |      5.69386e+08 | 1.44e+10    |
|   1402 |   22094 |      8.82425e+08 |          5.80933e+08 |         0 |      8.4e+08     | 1.65e+10    |


### Monthly_Temporary_Income

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
    1402:
      column_code: DYCOL12
      type: float
    
    ```
#### Column Codes

| Years     | Monthly_Temporary_Income                               |
|:----------|:-------------------------------------------------------|
| 1369      |                                                        |
| 1370-1373 | [COL09](/HBSIR/tables/raw/employment_income#col09)     |
| 1374-1383 | [COL10](/HBSIR/tables/raw/employment_income#col10)     |
| 1384-1402 | [DYCOL12](/HBSIR/tables/raw/employment_income#dycol12) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |   Median |          Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------:|-----------------:|
|   1370 |   13087 |   3638.96        |      15932.8         |     0     |        0 | 400000           |
|   1371 |   13514 |   5092.95        |      22846.4         |     0     |        0 |      1e+06       |
|   1372 |    8845 |   7051.61        |      33020.4         |     0     |        0 |      1.328e+06   |
|   1373 |   14813 |   9966.24        |      42172.3         |     0     |        0 | 750000           |
|   1374 |   26440 |  13148.7         |      53182.9         |     0     |        0 |      1.7e+06     |
|   1375 |   16818 |  15738.8         |      66089.7         |     0     |        0 |      1e+06       |
|   1376 |   17136 |  18500.4         |      80497.9         |     0     |        0 |      2e+06       |
|   1377 |   14007 |  20936.8         |      88238.5         |     0     |        0 |      1.88e+06    |
|   1378 |   21822 |  22561.3         |     102667           |     0     |        0 |      2.6e+06     |
|   1379 |   21108 |  31499.1         |     137263           |     0     |        0 |      4e+06       |
|   1380 |   20676 |  34321.1         |     162392           |     0     |        0 |      7.2e+06     |
|   1381 |   24597 |  50774.6         |     214824           |     0     |        0 |      5.25e+06    |
|   1382 |   18191 |  57928           |     267514           |     0     |        0 |      7e+06       |
|   1383 |   19605 |  77711.7         |     321081           |     0     |        0 |      7.2e+06     |
|   1384 |   10624 | 176547           |     512461           |     0     |        0 |      1.2e+07     |
|   1385 |   14570 | 151911           |     507092           |     0     |        0 |      8.77696e+06 |
|   1386 |   16169 | 150288           |     536964           |     0     |        0 |      1e+07       |
|   1387 |   20666 | 157817           |     668246           |     0     |        0 |      3.25e+07    |
|   1388 |   20026 | 151354           |     703093           |     0     |        0 |      2.3e+07     |
|   1389 |   21112 | 164285           |     746418           |     0     |        0 |      1.418e+07   |
|   1390 |   18970 | 186108           |     953868           |     0     |        0 |      6e+07       |
|   1391 |   18480 | 233509           |     998605           |     0     |        0 |      3.6e+07     |
|   1392 |   17940 | 274366           |          1.26124e+06 |     0     |        0 |      3e+07       |
|   1393 |   17923 | 319268           |          1.45002e+06 |     0     |        0 |      3.306e+07   |
|   1394 |   18431 | 362923           |          2.29721e+06 |     0     |        0 |      1.35e+08    |
|   1395 |   17692 | 358920           |          2.24136e+06 |     0     |        0 |      1.5e+08     |
|   1396 |   18010 | 373730           |          2.49532e+06 |     0     |        0 |      1.52e+08    |
|   1397 |   24467 | 315618           |          2.0776e+06  |     0     |        0 |      7.55e+07    |
|   1398 |   23557 | 389426           |          2.56765e+06 |     0     |        0 |      8e+07       |
|   1399 |   23061 | 441544           |          3.14756e+06 |     0     |        0 |      1.5e+08     |
|   1400 |   23119 | 618480           |          5.1485e+06  |     0     |        0 |      1.56e+08    |
|   1401 |   22612 |      1.13951e+06 |          6.97349e+06 |    -2e+06 |        0 |      2.2e+08     |
|   1402 |   22094 |      1.68716e+06 |          9.99041e+06 |     0     |        0 |      2.88e+08    |


### Annual_Temporary_Income

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
    1402:
      column_code: DYCOL13
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Temporary_Income                                |
|:----------|:-------------------------------------------------------|
| 1369-1373 | [COL10](/HBSIR/tables/raw/employment_income#col10)     |
| 1374-1383 | [COL11](/HBSIR/tables/raw/employment_income#col11)     |
| 1384-1402 | [DYCOL13](/HBSIR/tables/raw/employment_income#dycol13) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |     Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-----------:|------------:|
|   1369 |   13132 |  45624           |     123661           |     0     |      0     | 7.31e+06    |
|   1370 |   13087 |  64125.1         |     138675           |     0     |      0     | 2.95326e+06 |
|   1371 |   13514 |  83267.9         |     178965           |     0     |      0     | 4e+06       |
|   1372 |    8845 | 108877           |     230330           |     0     |      0     | 5.44e+06    |
|   1373 |   14813 | 152680           |     333780           |     0     |      0     | 1.2e+07     |
|   1374 |   26440 | 216594           |     497487           |     0     |      0     | 2e+07       |
|   1375 |   16818 | 237886           |     556615           |     0     |      0     | 1.435e+07   |
|   1376 |   17136 | 301857           |     656231           |     0     |      0     | 1.2e+07     |
|   1377 |   14007 | 373266           |          1.07715e+06 |     0     |      0     | 8.1e+07     |
|   1378 |   21822 | 396015           |     980690           |     0     |      0     | 3.47e+07    |
|   1379 |   21108 | 516139           |          1.39568e+06 |     0     |      0     | 7.8e+07     |
|   1380 |   20676 | 613602           |          1.87907e+06 |     0     |      0     | 1.62575e+08 |
|   1381 |   24597 | 816479           |          1.87236e+06 |     0     |      0     | 4.07e+07    |
|   1382 |   18191 | 968700           |          2.34218e+06 |     0     |      0     | 8.34455e+07 |
|   1383 |   19605 |      1.18648e+06 |          2.6896e+06  |     0     |      0     | 4.64367e+07 |
|   1384 |   13917 |      2.27917e+06 |          4.06308e+06 |     0     |      1e+06 | 5.37e+07    |
|   1385 |   16977 |      2.3706e+06  |          4.90153e+06 |     0     | 244000     | 1.42561e+08 |
|   1386 |   18263 |      2.48066e+06 |          5.58689e+06 |     0     |      0     | 3.0175e+08  |
|   1387 |   23086 |      2.24558e+06 |          5.9332e+06  |     0     |      0     | 5.65e+08    |
|   1388 |   21950 |      2.28737e+06 |          5.62482e+06 |     0     |      0     | 2.78e+08    |
|   1389 |   23023 |      2.55652e+06 |          5.90836e+06 |     0     |      0     | 1.53e+08    |
|   1390 |   20880 |      2.97504e+06 |          6.5972e+06  |     0     |      0     | 1.56e+08    |
|   1391 |   20082 |      3.47043e+06 |          8.59669e+06 |     0     |      0     | 4.04e+08    |
|   1392 |   19470 |      4.23828e+06 |          1.01848e+07 |     0     |      0     | 3.635e+08   |
|   1393 |   19284 |      5.47063e+06 |          1.43929e+07 |     0     |      0     | 5.1672e+08  |
|   1394 |   19676 |      6.27927e+06 |          2.28416e+07 |     0     |      0     | 1.386e+09   |
|   1395 |   19281 |      6.68713e+06 |          2.21133e+07 |     0     |      0     | 1.54e+09    |
|   1396 |   19694 |      6.96729e+06 |          2.09676e+07 |     0     |      0     | 1.56e+09    |
|   1397 |   24478 |      6.66797e+06 |          1.77896e+07 |     0     |      0     | 6.5e+08     |
|   1398 |   23568 |      8.40914e+06 |          2.18914e+07 |     0     |      0     | 7.2e+08     |
|   1399 |   23071 |      1.04054e+07 |          2.61791e+07 |     0     |      0     | 8.52e+08    |
|   1400 |   23124 |      1.40479e+07 |          4.11389e+07 |     0     |      0     | 3e+09       |
|   1401 |   22613 |      2.21781e+07 |          6.1663e+07  |    -2e+07 |      0     | 1.2e+09     |
|   1402 |   22094 |      3.09852e+07 |          7.90898e+07 |     0     |      0     | 2.04e+09    |


### Monthly_Net_Income

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
    1402:
      column_code: DYCOL14
      type: float
    
    ```
#### Column Codes

| Years     | Monthly_Net_Income                                     |
|:----------|:-------------------------------------------------------|
| 1369      |                                                        |
| 1370-1373 | [COL11](/HBSIR/tables/raw/employment_income#col11)     |
| 1374-1383 | [COL12](/HBSIR/tables/raw/employment_income#col12)     |
| 1384-1402 | [DYCOL14](/HBSIR/tables/raw/employment_income#dycol14) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |          Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|----------------:|------------:|
|   1370 |   13087 |  66776.3         |      62804.6         |         0 |  65730          | 1.05e+06    |
|   1371 |   13514 |  92249.7         |      87752.1         |         0 |  87000          | 1.63133e+06 |
|   1372 |    8845 | 118629           |     108927           |         0 | 118218          | 2.00857e+06 |
|   1373 |   14813 | 149868           |     129553           |         0 | 149400          | 2.1e+06     |
|   1374 |   26440 | 191460           |     230300           |         0 | 180000          | 1.11287e+07 |
|   1375 |   16818 | 246055           |     250112           |         0 | 230000          | 6.65e+06    |
|   1376 |   17136 | 316446           |     330434           |         0 | 300000          | 1.5e+07     |
|   1377 |   14007 | 375613           |     405079           |         0 | 330000          | 8.4e+06     |
|   1378 |   21822 | 435314           |     555129           |         0 | 400000          | 3.222e+07   |
|   1379 |   21108 | 513154           |     571002           |         0 | 450000          | 1.995e+07   |
|   1380 |   20676 | 614888           |     662786           |         0 | 500200          | 2.5e+07     |
|   1381 |   24597 | 770191           |     775412           |         0 | 650000          | 2.45e+07    |
|   1382 |   18191 | 969203           |          1.00553e+06 |         0 | 840000          | 2.475e+07   |
|   1383 |   19605 |      1.17403e+06 |          1.73694e+06 |         0 |      1e+06      | 1.875e+08   |
|   1384 |   21199 |      1.3999e+06  |          1.39391e+06 |         0 |      1.2e+06    | 6e+07       |
|   1385 |   23036 |      1.66001e+06 |          1.55672e+06 |         0 |      1.5e+06    | 4.64343e+07 |
|   1386 |   24087 |      1.94265e+06 |          1.77385e+06 |         0 |      1.78e+06   | 5e+07       |
|   1387 |   29355 |      2.28803e+06 |          1.9075e+06  |         0 |      2.1e+06    | 3.84419e+07 |
|   1388 |   26698 |      2.53131e+06 |          2.19525e+06 |         0 |      2.4e+06    | 5.91191e+07 |
|   1389 |   26971 |      2.94183e+06 |          2.51066e+06 |         0 |      2.86e+06   | 7e+07       |
|   1390 |   25060 |      3.55996e+06 |          2.74884e+06 |         0 |      3.4e+06    | 6.5e+07     |
|   1391 |   24335 |      4.30546e+06 |          3.56707e+06 |         0 |      4e+06      | 1.45836e+08 |
|   1392 |   23759 |      5.67982e+06 |          4.4357e+06  |         0 |      5.2e+06    | 1.6e+08     |
|   1393 |   23883 |      7.03022e+06 |          5.39051e+06 |         0 |      6.51e+06   | 1.3715e+08  |
|   1394 |   23798 |      8.26215e+06 |          6.81319e+06 |         0 |      7.8694e+06 | 2.747e+08   |
|   1395 |   23563 |      9.3185e+06  |          7.79858e+06 |         0 |      8.46e+06   | 2e+08       |
|   1396 |   23805 |      1.04542e+07 |          9.05642e+06 |         0 |      9e+06      | 2.2131e+08  |
|   1397 |   24482 |      1.24002e+07 |          1.06664e+07 |         0 |      1.1e+07    | 2.67e+08    |
|   1398 |   23575 |      1.53538e+07 |          1.27947e+07 |         0 |      1.4e+07    | 3e+08       |
|   1399 |   23073 |      2.19254e+07 |          1.82045e+07 |         0 |      2e+07      | 4.76067e+08 |
|   1400 |   23130 |      3.47417e+07 |          2.59244e+07 |         0 |      3.1e+07    | 5.85e+08    |
|   1401 |   22615 |      5.22521e+07 |          3.90504e+07 |         0 |      5e+07      | 1.2e+09     |
|   1402 |   22094 |      7.77812e+07 |          5.44608e+07 |         0 |      7.5e+07    | 1.2e+09     |


### Annual_Net_Income

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
    1402:
      column_code: DYCOL15
      type: float
    
    ```
#### Column Codes

| Years     | Annual_Net_Income                                      |
|:----------|:-------------------------------------------------------|
| 1369-1373 | [COL12](/HBSIR/tables/raw/employment_income#col12)     |
| 1374-1383 | [COL13](/HBSIR/tables/raw/employment_income#col13)     |
| 1384-1402 | [DYCOL15](/HBSIR/tables/raw/employment_income#dycol15) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-----------------:|------------:|
|   1369 |   13132 | 626693           |     541640           |  0        | 550000           | 1.18367e+07 |
|   1370 |   13087 | 815422           |     957055           |  0        | 720000           | 7.44e+07    |
|   1371 |   13514 |      1.07494e+06 |     923272           |  0        | 920000           | 1.9576e+07  |
|   1372 |    8845 |      1.4223e+06  |          1.2274e+06  |  0        |      1.269e+06   | 3e+07       |
|   1373 |   14813 |      1.83244e+06 |          1.49139e+06 |  0        |      1.74884e+06 | 3.2e+07     |
|   1374 |   26440 |      2.25003e+06 |          1.98812e+06 |  0        |      2.05606e+06 | 9.158e+07   |
|   1375 |   16818 |      2.88411e+06 |          2.74024e+06 |  0        |      2.5e+06     | 8.23e+07    |
|   1376 |   17136 |      3.74241e+06 |          3.62811e+06 |  0        |      3.2e+06     | 1.8e+08     |
|   1377 |   14007 |      4.49546e+06 |          4.79895e+06 |  0        |      3.6e+06     | 1.1424e+08  |
|   1378 |   21822 |      5.17772e+06 |          6.38034e+06 |  0        |      4e+06       | 3.8664e+08  |
|   1379 |   21108 |      6.13477e+06 |          6.48365e+06 |  0        |      4.67606e+06 | 2.1e+08     |
|   1380 |   20676 |      7.39034e+06 |          7.19471e+06 |  0        |      5.49462e+06 | 1.73443e+08 |
|   1381 |   24597 |      9.0791e+06  |          8.60837e+06 |  0        |      6.9e+06     | 2.20677e+08 |
|   1382 |   18191 |      1.13238e+07 |          1.04069e+07 |  0        |      8.65e+06    | 2.9717e+08  |
|   1383 |   19605 |      1.374e+07   |          1.35611e+07 |  0        |      1.08e+07    | 7.73995e+08 |
|   1384 |   21199 |      1.64563e+07 |          1.48043e+07 |  0        |      1.28933e+07 | 2.16972e+08 |
|   1385 |   23036 |      1.97891e+07 |          1.79291e+07 |  0        |      1.56566e+07 | 5.59562e+08 |
|   1386 |   24087 |      2.33537e+07 |          2.16754e+07 | -1.08e+07 |      1.824e+07   | 8.6e+08     |
|   1387 |   29355 |      2.65559e+07 |          2.14045e+07 |  0        |      2.2608e+07  | 5.866e+08   |
|   1388 |   26698 |      2.96556e+07 |          2.41516e+07 |  0        |      2.4e+07     | 3.78e+08    |
|   1389 |   26971 |      3.42885e+07 |          2.80405e+07 |  0        |      3e+07       | 5.83158e+08 |
|   1390 |   25060 |      4.14638e+07 |          3.07148e+07 |  0        |      3.6e+07     | 5.79e+08    |
|   1391 |   24335 |      4.97237e+07 |          3.6761e+07  |  0        |      4.5164e+07  | 9e+08       |
|   1392 |   23759 |      6.60163e+07 |          4.71054e+07 |  0        |      6e+07       | 1.7848e+09  |
|   1393 |   23885 |      8.24599e+07 |          6.24783e+07 |  0        |      7.2e+07     | 2.292e+09   |
|   1394 |   23798 |      9.77226e+07 |          7.43578e+07 |  0        |      8.5e+07     | 1.78421e+09 |
|   1395 |   23564 |      1.11317e+08 |          8.75831e+07 |  0        |      9.6e+07     | 1.97798e+09 |
|   1396 |   23805 |      1.24857e+08 |          1.01788e+08 |  0        |      1.035e+08   | 2.42873e+09 |
|   1397 |   24482 |      1.49228e+08 |          1.2016e+08  |  0        |      1.2e+08     | 2.9425e+09  |
|   1398 |   23575 |      1.85234e+08 |          1.47063e+08 |  0        |      1.52e+08    | 3.6e+09     |
|   1399 |   23073 |      2.61396e+08 |          2.01453e+08 |  0        |      2.204e+08   | 2.99e+09    |
|   1400 |   23130 |      4.10468e+08 |          2.95174e+08 |  0        |      3.6e+08     | 5.4e+09     |
|   1401 |   22615 |      6.18849e+08 |          4.23398e+08 |  0        |      5.92e+08    | 1.44e+10    |
|   1402 |   22094 |      9.13411e+08 |          6.15691e+08 |  0        |      8.4e+08     | 1.65e+10    |


