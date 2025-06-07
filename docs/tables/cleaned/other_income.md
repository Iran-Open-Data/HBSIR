# other_income

## Old to New Titles

| Years     | ADDRESS   | COL01         | COL03      | COL04   | COL05    | COL06   | COL07           | COL08    | TAX   |
|:----------|:----------|:--------------|:-----------|:--------|:---------|:--------|:----------------|:---------|:------|
| 1369-1377 | ID        | Member_Number | Retirement | Rent    | Interest | Aid     | Home_Production |          |       |
| 1378-1380 | ID        | Member_Number | Retirement | Rent    | Interest | Aid     | Home_Production | Transfer | drop  |
| 1381-1383 | ID        | Member_Number | Retirement | Rent    | Interest | Aid     | Home_Production | Transfer |       |


| Years     | ADDRESS   | DYCOL01       | DYCOL03    | DYCOL04   | DYCOL05   | DYCOL06   | DYCOL07         | DYCOL08   |
|:----------|:----------|:--------------|:-----------|:----------|:----------|:----------|:----------------|:----------|
| 1384-1402 | ID        | Member_Number | Retirement | Rent      | Interest  | Aid       | Home_Production | Transfer  |


## New to Old Titles

| Years     | ID      | Member_Number   | Retirement   | Rent    | Interest   | Aid     | Home_Production   | Transfer   |
|:----------|:--------|:----------------|:-------------|:--------|:-----------|:--------|:------------------|:-----------|
| 1369-1377 | ADDRESS | COL01           | COL03        | COL04   | COL05      | COL06   | COL07             |            |
| 1378-1383 | ADDRESS | COL01           | COL03        | COL04   | COL05      | COL06   | COL07             | COL08      |
| 1384-1402 | ADDRESS | DYCOL01         | DYCOL03      | DYCOL04 | DYCOL05    | DYCOL06 | DYCOL07           | DYCOL08    |


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

| Years     | ID                                                |
|:----------|:--------------------------------------------------|
| 1369-1402 | [ADDRESS](/HBSIR/tables/raw/other_income#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |      Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|------------:|------------:|
|   1369 |    4128 | 646750           |     509627           |  1008          | 1.01213e+06 | 1.23422e+06 |
|   1370 |    4790 | 676047           |     499413           |  1008          | 1.01409e+06 | 1.23422e+06 |
|   1371 |    4886 | 713023           |     490081           |  1001          | 1.02204e+06 | 1.23422e+06 |
|   1372 |    3139 | 701251           |     499109           |  1002          | 1.02207e+06 | 1.23422e+06 |
|   1373 |    5554 | 798328           |     493416           |  1004          | 1.07213e+06 | 1.24404e+06 |
|   1374 |   11663 |      7.01654e+06 |          5.07465e+06 | 10008          | 1.04102e+07 | 1.24401e+07 |
|   1375 |    6517 | 667529           |     518631           |  1002          | 1.02405e+06 | 1.24402e+06 |
|   1376 |    6915 | 674803           |     521310           |  1013          | 1.03111e+06 | 1.25406e+06 |
|   1377 |    5596 |      6.37199e+07 |          5.19435e+07 | 11001          | 1.01031e+08 | 1.27074e+08 |
|   1378 |   12202 |      6.17186e+07 |          5.17057e+07 | 11004          | 2.60311e+07 | 1.27074e+08 |
|   1379 |   10670 |      5.85916e+07 |          5.11624e+07 | 11004          | 2.40341e+07 | 1.27074e+08 |
|   1380 |   12391 |      5.80528e+07 |          5.12864e+07 | 11002          | 2.40431e+07 | 1.27074e+08 |
|   1381 |   15277 |      6.04451e+07 |          5.11985e+07 | 11002          | 2.6014e+07  | 1.27074e+08 |
|   1382 |   10014 |      6.35454e+07 |          5.13845e+07 | 11008          | 2.70721e+07 | 1.27113e+08 |
|   1383 |   12311 |      6.01601e+07 |          5.11441e+07 | 11003          | 2.5012e+07  | 1.27114e+08 |
|   1384 |   14464 |      6.24029e+07 |          5.09528e+07 | 11002          | 2.8091e+07  | 1.29213e+08 |
|   1385 |   17173 |      6.10525e+07 |          5.12822e+07 | 11002          | 2.8023e+07  | 1.29214e+08 |
|   1386 |   17413 |      6.26306e+07 |          5.05195e+07 | 11004          | 2.9034e+07  | 1.29214e+08 |
|   1387 |   21578 |      1.66868e+09 |          5.10571e+08 |     1e+09      | 2.00028e+09 | 2.29786e+09 |
|   1388 |   26045 |      1.70091e+09 |          5.06265e+08 |     1e+09      | 2.02018e+09 | 2.29025e+09 |
|   1389 |   28341 |      1.67277e+09 |          5.06058e+08 |     1e+09      | 2.01005e+09 | 2.29013e+09 |
|   1390 |   20153 |      1.6351e+09  |          5.07837e+08 |     1e+09      | 1.2901e+09  | 2.30013e+09 |
|   1391 |   20375 |      1.63013e+09 |          5.07172e+08 |     1e+09      | 1.29007e+09 | 2.30013e+09 |
|   1392 |   18595 |      1.63417e+10 |          5.04167e+09 |     1.0001e+10 | 1.30016e+10 | 2.30047e+10 |
|   1393 |   20023 |      1.64406e+10 |          5.05659e+09 |     1.0001e+10 | 1.30017e+10 | 2.30047e+10 |
|   1394 |   21266 |      1.64372e+10 |          5.04681e+09 |     1.0001e+10 | 1.30017e+10 | 2.30047e+10 |
|   1395 |   21647 |      1.63904e+10 |          5.0526e+09  |     1.0001e+10 | 1.30016e+10 | 2.30047e+10 |
|   1396 |   25316 |      1.66087e+10 |          5.04805e+09 |     1.0001e+10 | 2.0007e+10  | 2.30047e+10 |
|   1397 |   35009 |      1.65026e+10 |          5.08208e+09 |     1.0001e+10 | 1.30014e+10 | 2.30067e+10 |
|   1398 |   37964 |      1.64711e+10 |          5.06485e+09 |     1.0001e+10 | 1.30014e+10 | 2.30067e+10 |
|   1399 |   47622 |      1.65662e+10 |          5.05155e+09 |     1.0001e+10 | 2.00034e+10 | 2.30067e+10 |
|   1400 |   49442 |      1.65929e+10 |          5.04207e+09 |     1.0001e+10 | 2.00064e+10 | 2.30067e+10 |
|   1401 |   53724 |      1.64881e+10 |          5.04685e+09 |     1.0001e+10 | 2.00014e+10 | 2.30067e+10 |
|   1402 |   47606 |      1.65631e+10 |          5.04158e+09 |     1.0001e+10 | 2.00064e+10 | 2.30067e+10 |


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

| Years     | Member_Number                                     |
|:----------|:--------------------------------------------------|
| 1369-1383 | [COL01](/HBSIR/tables/raw/other_income#col01)     |
| 1384-1402 | [DYCOL01](/HBSIR/tables/raw/other_income#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1369 |    4128 |   1.54 |                 1.97 |         1 |        1 |        81 |
|   1370 |    4790 |   1.47 |                 1.46 |         0 |        1 |        15 |
|   1371 |    4886 |   1.41 |                 1.32 |         0 |        1 |        12 |
|   1372 |    3139 |   1.44 |                 1.42 |         0 |        1 |        14 |
|   1373 |    5554 |   1.4  |                 1.26 |         0 |        1 |        20 |
|   1374 |   11663 |   1.54 |                 1.48 |         1 |        1 |        19 |
|   1375 |    6517 |   1.5  |                 1.44 |         1 |        1 |        17 |
|   1376 |    6915 |   1.53 |                 1.52 |         1 |        1 |        17 |
|   1377 |    5596 |   1.56 |                 1.6  |         1 |        1 |        20 |
|   1378 |   12202 |   1.57 |                 1.57 |         1 |        1 |        25 |
|   1379 |   10670 |   1.54 |                 1.52 |         1 |        1 |        19 |
|   1380 |   12391 |   1.5  |                 1.38 |         1 |        1 |        16 |
|   1381 |   15277 |   1.5  |                 1.36 |         1 |        1 |        13 |
|   1382 |   10014 |   1.53 |                 1.38 |         1 |        1 |        13 |
|   1383 |   12311 |   1.58 |                 1.43 |         1 |        1 |        16 |
|   1384 |   14464 |   1.58 |                 1.36 |         1 |        1 |        15 |
|   1385 |   17173 |   1.58 |                 1.35 |         1 |        1 |        13 |
|   1386 |   17413 |   1.62 |                 1.4  |         1 |        1 |        14 |
|   1387 |   21578 |   1.57 |                 1.27 |         1 |        1 |        19 |
|   1388 |   26043 |   1.66 |                 1.33 |         1 |        1 |        17 |
|   1389 |   28341 |   1.4  |                 1.09 |         1 |        1 |        15 |
|   1390 |   20147 |   1.43 |                 1.12 |         1 |        1 |        14 |
|   1391 |   20365 |   1.5  |                 1.2  |         1 |        1 |        20 |
|   1392 |   18590 |   1.5  |                 1.18 |         1 |        1 |        13 |
|   1393 |   20023 |   1.53 |                 1.21 |         1 |        1 |        14 |
|   1394 |   21264 |   1.54 |                 1.24 |         1 |        1 |        14 |
|   1395 |   21647 |   1.48 |                 1.15 |         1 |        1 |        13 |
|   1396 |   25316 |   1.55 |                 1.15 |         1 |        1 |        11 |
|   1397 |   35008 |   1.64 |                 1.14 |         1 |        1 |        14 |
|   1398 |   37964 |   1.58 |                 1.07 |         1 |        1 |        13 |
|   1399 |   47620 |   1.5  |                 1.01 |         1 |        1 |        12 |
|   1400 |   49441 |   1.53 |                 1    |         1 |        1 |        11 |
|   1401 |   53724 |   1.56 |                 0.99 |         1 |        1 |        14 |
|   1402 |   47606 |   1.6  |                 0.97 |         1 |        1 |        12 |


### Retirement

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL03
      type: float
    1364:
      column_code: DYCOL03
      type: float
    1365:
      column_code: DYCOL03
      type: float
    1366:
      column_code: DYCOL03
      type: float
    1367:
      column_code: DYCOL03
      type: float
    1368:
      column_code: DYCOL03
      type: float
    1369:
      column_code: DYCOL03
      type: float
    1370:
      column_code: DYCOL03
      type: float
    1371:
      column_code: DYCOL03
      type: float
    1372:
      column_code: DYCOL03
      type: float
    1373:
      column_code: DYCOL03
      type: float
    1374:
      column_code: DYCOL03
      type: float
    1375:
      column_code: DYCOL03
      type: float
    1376:
      column_code: DYCOL03
      type: float
    1377:
      column_code: DYCOL03
      type: float
    1378:
      column_code: DYCOL03
      type: float
    1379:
      column_code: DYCOL03
      type: float
    1380:
      column_code: DYCOL03
      type: float
    1381:
      column_code: DYCOL03
      type: float
    1382:
      column_code: DYCOL03
      type: float
    1383:
      column_code: DYCOL03
      type: float
    1384:
      column_code: DYCOL03
      type: float
    1385:
      column_code: DYCOL03
      type: float
    1386:
      column_code: DYCOL03
      type: float
    1387:
      column_code: DYCOL03
      type: float
    1388:
      column_code: DYCOL03
      type: float
    1389:
      column_code: DYCOL03
      type: float
    1390:
      column_code: DYCOL03
      type: float
    1391:
      column_code: DYCOL03
      type: float
    1392:
      column_code: DYCOL03
      type: float
    1393:
      column_code: DYCOL03
      type: float
    1394:
      column_code: DYCOL03
      type: float
    1395:
      column_code: DYCOL03
      type: float
    1396:
      column_code: DYCOL03
      type: float
    1397:
      column_code: DYCOL03
      type: float
    1398:
      column_code: DYCOL03
      type: float
    1399:
      column_code: DYCOL03
      type: float
    1400:
      column_code: DYCOL03
      type: float
    1401:
      column_code: DYCOL03
      type: float
    1402:
      column_code: DYCOL03
      type: float
    
    ```
#### Column Codes

| Years     | Retirement                                        |
|:----------|:--------------------------------------------------|
| 1369-1383 | [COL03](/HBSIR/tables/raw/other_income#col03)     |
| 1384-1402 | [DYCOL03](/HBSIR/tables/raw/other_income#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |    Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|----------:|------------:|
|   1369 |    4128 | 134914           |     352111           |         0 | 0         | 9.96e+06    |
|   1370 |    4790 | 170016           |     388577           |         0 | 0         | 8.35e+06    |
|   1371 |    4886 | 200742           |     500449           |         0 | 0         | 1.4978e+07  |
|   1372 |    3139 | 378741           |          1.40473e+06 |         0 | 0         | 6.42e+07    |
|   1373 |    5554 | 549392           |          1.29791e+06 |         0 | 0         | 3.33e+07    |
|   1374 |   11663 | 611140           |          1.4189e+06  |         0 | 0         | 5.057e+07   |
|   1375 |    6517 | 875150           |          1.78332e+06 |         0 | 0         | 3.4e+07     |
|   1376 |    6915 |      1.13586e+06 |          2.08358e+06 |         0 | 0         | 4.186e+07   |
|   1377 |    5596 |      1.38838e+06 |          2.85297e+06 |         0 | 0         | 9.8e+07     |
|   1378 |   12202 |      1.26314e+06 |          4.27432e+06 |         0 | 0         | 3.2375e+08  |
|   1379 |   10670 |      1.55553e+06 |          3.73119e+06 |         0 | 0         | 8.87e+07    |
|   1380 |   12391 |      1.92893e+06 |          5.06964e+06 |         0 | 0         | 1.9035e+08  |
|   1381 |   15277 |      2.59174e+06 |          6.4987e+06  |         0 | 0         | 1.748e+08   |
|   1382 |   10014 |      3.50724e+06 |          1.85265e+07 |         0 | 0         | 1.27613e+09 |
|   1383 |   12311 |      3.90761e+06 |          9.61456e+06 |         0 | 0         | 2.63408e+08 |
|   1384 |    4879 |      1.34465e+07 |          1.64758e+07 |         0 | 1.444e+07 | 3.2e+08     |
|   1385 |    6863 |      1.435e+07   |          2.09372e+07 |         0 | 1.32e+07  | 7.86548e+08 |
|   1386 |    8655 |      1.48584e+07 |          2.14967e+07 |         0 | 0         | 3.9058e+08  |
|   1387 |   11793 |      1.7144e+07  |          2.68203e+07 |         0 | 0         | 8e+08       |
|   1388 |   14218 |      1.85416e+07 |          2.99458e+07 |         0 | 0         | 5.05e+08    |
|   1389 |   16391 |      2.12025e+07 |          3.50276e+07 |         0 | 0         | 9.25e+08    |
|   1390 |   12724 |      3.20268e+07 |          4.2909e+07  |         0 | 0         | 1.36e+09    |
|   1391 |   13105 |      3.72645e+07 |          4.80269e+07 |         0 | 6e+06     | 1.115e+09   |
|   1392 |   11051 |      4.63308e+07 |          5.76533e+07 |         0 | 2.16e+07  | 1.2402e+09  |
|   1393 |   11449 |      5.93561e+07 |          6.87925e+07 |         0 | 4.7e+07   | 1.60025e+09 |
|   1394 |   11621 |      7.08271e+07 |          7.69894e+07 |         0 | 6.54e+07  | 1.08003e+09 |
|   1395 |   11296 |      8.7321e+07  |          9.72422e+07 |         0 | 9.6e+07   | 3.0004e+09  |
|   1396 |   12753 |      9.39124e+07 |          1.04803e+08 |         0 | 7.2e+07   | 1.532e+09   |
|   1397 |   13795 |      1.04699e+08 |          1.29026e+08 |         0 | 5.58e+07  | 3.14852e+09 |
|   1398 |   15107 |      1.26229e+08 |          1.52518e+08 |         0 | 5.16e+07  | 2.03e+09    |
|   1399 |   18346 |      1.54745e+08 |          2.13587e+08 |         0 | 0         | 2.98e+09    |
|   1400 |   17388 |      2.71736e+08 |          3.40684e+08 |         0 | 5.89e+07  | 7.2e+09     |
|   1401 |   53724 |      1.2083e+08  |          3.07203e+08 |         0 | 0         | 7.5e+09     |
|   1402 |   47606 |      1.95916e+08 |          4.50825e+08 |         0 | 0         | 9.703e+09   |


### Rent

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL04
      type: float
    1364:
      column_code: DYCOL04
      type: float
    1365:
      column_code: DYCOL04
      type: float
    1366:
      column_code: DYCOL04
      type: float
    1367:
      column_code: DYCOL04
      type: float
    1368:
      column_code: DYCOL04
      type: float
    1369:
      column_code: DYCOL04
      type: float
    1370:
      column_code: DYCOL04
      type: float
    1371:
      column_code: DYCOL04
      type: float
    1372:
      column_code: DYCOL04
      type: float
    1373:
      column_code: DYCOL04
      type: float
    1374:
      column_code: DYCOL04
      type: float
    1375:
      column_code: DYCOL04
      type: float
    1376:
      column_code: DYCOL04
      type: float
    1377:
      column_code: DYCOL04
      type: float
    1378:
      column_code: DYCOL04
      type: float
    1379:
      column_code: DYCOL04
      type: float
    1380:
      column_code: DYCOL04
      type: float
    1381:
      column_code: DYCOL04
      type: float
    1382:
      column_code: DYCOL04
      type: float
    1383:
      column_code: DYCOL04
      type: float
    1384:
      column_code: DYCOL04
      type: float
    1385:
      column_code: DYCOL04
      type: float
    1386:
      column_code: DYCOL04
      type: float
    1387:
      column_code: DYCOL04
      type: float
    1388:
      column_code: DYCOL04
      type: float
    1389:
      column_code: DYCOL04
      type: float
    1390:
      column_code: DYCOL04
      type: float
    1391:
      column_code: DYCOL04
      type: float
    1392:
      column_code: DYCOL04
      type: float
    1393:
      column_code: DYCOL04
      type: float
    1394:
      column_code: DYCOL04
      type: float
    1395:
      column_code: DYCOL04
      type: float
    1396:
      column_code: DYCOL04
      type: float
    1397:
      column_code: DYCOL04
      type: float
    1398:
      column_code: DYCOL04
      type: float
    1399:
      column_code: DYCOL04
      type: float
    1400:
      column_code: DYCOL04
      type: float
    1401:
      column_code: DYCOL04
      type: float
    1402:
      column_code: DYCOL04
      type: float
    
    ```
#### Column Codes

| Years     | Rent                                              |
|:----------|:--------------------------------------------------|
| 1369-1383 | [COL04](/HBSIR/tables/raw/other_income#col04)     |
| 1384-1402 | [DYCOL04](/HBSIR/tables/raw/other_income#dycol04) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |   Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------:|------------:|
|   1369 |    4128 | 134949           |     828364           |         0 |  0       | 4e+07       |
|   1370 |    4790 | 149720           |     575517           |         0 |  0       | 1.8e+07     |
|   1371 |    4886 | 195786           |          1.24855e+06 |         0 |  0       | 7e+07       |
|   1372 |    3139 | 233421           |     634781           |         0 |  0       | 1.02e+07    |
|   1373 |    5554 | 377320           |          1.61617e+06 |         0 |  0       | 8.4e+07     |
|   1374 |   11663 | 395877           |          1.69105e+06 |         0 |  0       | 7.2e+07     |
|   1375 |    6517 | 605059           |          2.39749e+06 |         0 |  0       | 1.002e+08   |
|   1376 |    6915 | 580002           |          1.76463e+06 |         0 |  0       | 3.6e+07     |
|   1377 |    5596 | 831486           |          2.84038e+06 |         0 |  0       | 8.006e+07   |
|   1378 |   12202 | 805134           |          3.57748e+06 |         0 |  0       | 2e+08       |
|   1379 |   10670 |      1.05394e+06 |          5.22885e+06 |         0 |  0       | 2.5e+08     |
|   1380 |   12391 |      1.15994e+06 |          7.07667e+06 |         0 |  0       | 5.10001e+08 |
|   1381 |   15277 |      1.4633e+06  |          8.04302e+06 |         0 |  0       | 5.118e+08   |
|   1382 |   10014 |      1.90769e+06 |          1.00844e+07 |         0 |  0       | 4.5e+08     |
|   1383 |   12311 |      2.08442e+06 |          9.11826e+06 |         0 |  0       | 4e+08       |
|   1384 |    4734 |      7.08304e+06 |          1.69277e+07 |         0 |  2.4e+06 | 4.5e+08     |
|   1385 |    6842 |      6.32871e+06 |          1.81295e+07 |         0 |  0       | 7.4e+08     |
|   1386 |    8236 |      6.41888e+06 |          1.98585e+07 |         0 |  0       | 7.896e+08   |
|   1387 |   10593 |      6.35313e+06 |          4.55981e+07 |         0 |  0       | 4.248e+09   |
|   1388 |   13074 |      4.78725e+06 |          1.9516e+07  |         0 |  0       | 1.2e+09     |
|   1389 |   15163 |      4.9138e+06  |          1.84235e+07 |         0 |  0       | 7.68e+08    |
|   1390 |   10780 |      6.76639e+06 |          1.94072e+07 |         0 |  0       | 4.2e+08     |
|   1391 |   10886 |      8.3983e+06  |          2.77687e+07 |         0 |  0       | 9.6e+08     |
|   1392 |    8772 |      1.05275e+07 |          3.46994e+07 |         0 |  0       | 1.2e+09     |
|   1393 |    8783 |      1.51869e+07 |          5.84715e+07 |         0 |  0       | 3.6e+09     |
|   1394 |    9039 |      1.73337e+07 |          4.30256e+07 |         0 |  0       | 1e+09       |
|   1395 |    8939 |      1.94529e+07 |          5.157e+07   |         0 |  0       | 1.75e+09    |
|   1396 |    9917 |      2.08612e+07 |          5.86814e+07 |         0 |  0       | 1.24e+09    |
|   1397 |   10480 |      2.18951e+07 |          8.51715e+07 |         0 |  0       | 4.395e+09   |
|   1398 |   11552 |      2.33984e+07 |          7.47954e+07 |         0 |  0       | 1.5e+09     |
|   1399 |   14099 |      2.23364e+07 |          9.62399e+07 |         0 |  0       | 3.48e+09    |
|   1400 |   12438 |      3.66557e+07 |          1.59152e+08 |         0 |  0       | 7.2e+09     |
|   1401 |   53724 |      1.23729e+07 |          1.06114e+08 |         0 |  0       | 8e+09       |
|   1402 |   47606 |      2.19683e+07 |          1.56895e+08 |         0 |  0       | 9.6e+09     |


### Interest

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL05
      type: float
    1364:
      column_code: DYCOL05
      type: float
    1365:
      column_code: DYCOL05
      type: float
    1366:
      column_code: DYCOL05
      type: float
    1367:
      column_code: DYCOL05
      type: float
    1368:
      column_code: DYCOL05
      type: float
    1369:
      column_code: DYCOL05
      type: float
    1370:
      column_code: DYCOL05
      type: float
    1371:
      column_code: DYCOL05
      type: float
    1372:
      column_code: DYCOL05
      type: float
    1373:
      column_code: DYCOL05
      type: float
    1374:
      column_code: DYCOL05
      type: float
    1375:
      column_code: DYCOL05
      type: float
    1376:
      column_code: DYCOL05
      type: float
    1377:
      column_code: DYCOL05
      type: float
    1378:
      column_code: DYCOL05
      type: float
    1379:
      column_code: DYCOL05
      type: float
    1380:
      column_code: DYCOL05
      type: float
    1381:
      column_code: DYCOL05
      type: float
    1382:
      column_code: DYCOL05
      type: float
    1383:
      column_code: DYCOL05
      type: float
    1384:
      column_code: DYCOL05
      type: float
    1385:
      column_code: DYCOL05
      type: float
    1386:
      column_code: DYCOL05
      type: float
    1387:
      column_code: DYCOL05
      type: float
    1388:
      column_code: DYCOL05
      type: float
    1389:
      column_code: DYCOL05
      type: float
    1390:
      column_code: DYCOL05
      type: float
    1391:
      column_code: DYCOL05
      type: float
    1392:
      column_code: DYCOL05
      type: float
    1393:
      column_code: DYCOL05
      type: float
    1394:
      column_code: DYCOL05
      type: float
    1395:
      column_code: DYCOL05
      type: float
    1396:
      column_code: DYCOL05
      type: float
    1397:
      column_code: DYCOL05
      type: float
    1398:
      column_code: DYCOL05
      type: float
    1399:
      column_code: DYCOL05
      type: float
    1400:
      column_code: DYCOL05
      type: float
    1401:
      column_code: DYCOL05
      type: float
    1402:
      column_code: DYCOL05
      type: float
    
    ```
#### Column Codes

| Years     | Interest                                          |
|:----------|:--------------------------------------------------|
| 1369-1383 | [COL05](/HBSIR/tables/raw/other_income#col05)     |
| 1384-1402 | [DYCOL05](/HBSIR/tables/raw/other_income#dycol05) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |       Median |    Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-------------:|-----------:|
|   1369 |    4128 |  18251.5         |     424918           |         0 |      0       | 2.5e+07    |
|   1370 |    4790 |  18514.3         |     283256           |         0 |      0       | 1.68e+07   |
|   1371 |    4886 |  20738.1         |     486096           |         0 |      0       | 3.258e+07  |
|   1372 |    3139 |  36137.8         |     416271           |         0 |      0       | 1.92e+07   |
|   1373 |    5554 |  39701.6         |     345393           |         0 |      0       | 1.2e+07    |
|   1374 |   11663 |  57375           |          1.01354e+06 |         0 |      0       | 1e+08      |
|   1375 |    6517 |  80842.9         |     745783           |         0 |      0       | 2e+07      |
|   1376 |    6915 | 113232           |          1.22489e+06 |         0 |      0       | 6e+07      |
|   1377 |    5596 | 127765           |          1.28645e+06 |         0 |      0       | 4.17e+07   |
|   1378 |   12202 | 126188           |          1.65983e+06 |         0 |      0       | 9.6e+07    |
|   1379 |   10670 | 165702           |          1.8357e+06  |         0 |      0       | 1e+08      |
|   1380 |   12391 | 196577           |          2.10839e+06 |         0 |      0       | 1e+08      |
|   1381 |   15277 | 250245           |          3.4933e+06  |         0 |      0       | 3e+08      |
|   1382 |   10014 | 319370           |          3.82298e+06 |         0 |      0       | 1.85e+08   |
|   1383 |   12311 | 370305           |          3.81492e+06 |         0 |      0       | 1.392e+08  |
|   1384 |    2815 |      2.24364e+06 |          1.0794e+07  |         0 |      0       | 2.7e+08    |
|   1385 |    4711 |      1.61692e+06 |          1.0285e+07  |         0 |      0       | 4.8e+08    |
|   1386 |    6692 |      1.46268e+06 |          1.01199e+07 |         0 |      0       | 3.5e+08    |
|   1387 |   10796 |      1.56143e+06 |          2.91469e+07 |         0 |      0       | 2.9e+09    |
|   1388 |   17776 |      1.94136e+06 |          1.38805e+07 |         0 | 800000       | 1.405e+09  |
|   1389 |   16845 |      1.90963e+06 |          7.71942e+06 |         0 |      0       | 4.5e+08    |
|   1390 |    9650 |      1.85786e+06 |          1.34172e+07 |         0 |      0       | 6.0272e+08 |
|   1391 |    9720 |      1.90495e+06 |          1.40812e+07 |         0 |      0       | 6.6e+08    |
|   1392 |    7846 |      3.262e+06   |          3.48486e+07 |         0 |      0       | 2.4e+09    |
|   1393 |    7625 |      5.35533e+06 |          3.10764e+07 |         0 |      0       | 1.5e+09    |
|   1394 |    7886 |      9.26755e+06 |          4.25378e+07 |         0 |      0       | 1.8e+09    |
|   1395 |    7735 |      1.07451e+07 |          4.53798e+07 |         0 |      0       | 1.835e+09  |
|   1396 |   11361 |      9.22736e+06 |          4.85534e+07 |         0 |      0       | 1.8e+09    |
|   1397 |   24798 |      5.27838e+06 |          3.82483e+07 |         0 | 750000       | 2e+09      |
|   1398 |   25122 |      5.78184e+06 |          4.22595e+07 |         0 | 850000       | 2.06e+09   |
|   1399 |   30065 |      6.68392e+06 |          5.66956e+07 |         0 | 980000       | 4e+09      |
|   1400 |   33590 |      7.85421e+06 |          6.72649e+07 |         0 |      1e+06   | 6.009e+09  |
|   1401 |   53724 |      1.09719e+07 |          7.67498e+07 |         0 |      5e+06   | 8.4e+09    |
|   1402 |   47606 |      1.97121e+07 |          9.57905e+07 |         0 |      1.1e+07 | 8.012e+09  |


### Aid

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL06
      type: float
    1364:
      column_code: DYCOL06
      type: float
    1365:
      column_code: DYCOL06
      type: float
    1366:
      column_code: DYCOL06
      type: float
    1367:
      column_code: DYCOL06
      type: float
    1368:
      column_code: DYCOL06
      type: float
    1369:
      column_code: DYCOL06
      type: float
    1370:
      column_code: DYCOL06
      type: float
    1371:
      column_code: DYCOL06
      type: float
    1372:
      column_code: DYCOL06
      type: float
    1373:
      column_code: DYCOL06
      type: float
    1374:
      column_code: DYCOL06
      type: float
    1375:
      column_code: DYCOL06
      type: float
    1376:
      column_code: DYCOL06
      type: float
    1377:
      column_code: DYCOL06
      type: float
    1378:
      column_code: DYCOL06
      type: float
    1379:
      column_code: DYCOL06
      type: float
    1380:
      column_code: DYCOL06
      type: float
    1381:
      column_code: DYCOL06
      type: float
    1382:
      column_code: DYCOL06
      type: float
    1383:
      column_code: DYCOL06
      type: float
    1384:
      column_code: DYCOL06
      type: float
    1385:
      column_code: DYCOL06
      type: float
    1386:
      column_code: DYCOL06
      type: float
    1387:
      column_code: DYCOL06
      type: float
    1388:
      column_code: DYCOL06
      type: float
    1389:
      column_code: DYCOL06
      type: float
    1390:
      column_code: DYCOL06
      type: float
    1391:
      column_code: DYCOL06
      type: float
    1392:
      column_code: DYCOL06
      type: float
    1393:
      column_code: DYCOL06
      type: float
    1394:
      column_code: DYCOL06
      type: float
    1395:
      column_code: DYCOL06
      type: float
    1396:
      column_code: DYCOL06
      type: float
    1397:
      column_code: DYCOL06
      type: float
    1398:
      column_code: DYCOL06
      type: float
    1399:
      column_code: DYCOL06
      type: float
    1400:
      column_code: DYCOL06
      type: float
    1401:
      column_code: DYCOL06
      type: float
    1402:
      column_code: DYCOL06
      type: float
    
    ```
#### Column Codes

| Years     | Aid                                               |
|:----------|:--------------------------------------------------|
| 1369-1383 | [COL06](/HBSIR/tables/raw/other_income#col06)     |
| 1384-1402 | [DYCOL06](/HBSIR/tables/raw/other_income#dycol06) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |         Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------------:|------------:|
|   1369 |    4128 |   8894.23        |     391142           |         0 |      0         | 2.51e+07    |
|   1370 |    4790 |  55756.3         |     167235           |         0 |      0         | 3.75e+06    |
|   1371 |    4886 |  64846.3         |     263004           |         0 |      0         | 1.13848e+07 |
|   1372 |    3139 | 101473           |     271912           |         0 |      0         | 6e+06       |
|   1373 |    5554 | 134440           |     397814           |         0 |      0         | 9.5e+06     |
|   1374 |   11663 | 155511           |     404269           |         0 |      0         | 1.68e+07    |
|   1375 |    6517 | 189778           |     653753           |         0 |      0         | 2.6e+07     |
|   1376 |    6915 | 240409           |     612486           |         0 |      0         | 9.9e+06     |
|   1377 |    5596 | 338741           |     948056           |         0 |      0         | 3.51184e+07 |
|   1378 |   12202 | 345050           |          1.1099e+06  |         0 |      0         | 7.6e+07     |
|   1379 |   10670 | 493682           |          1.66108e+06 |         0 |      0         | 1.2e+08     |
|   1380 |   12391 | 513197           |          1.71182e+06 |         0 |      0         | 8.5e+07     |
|   1381 |   15277 | 591360           |          1.68985e+06 |         0 |      0         | 8e+07       |
|   1382 |   10014 | 686643           |          2.05539e+06 |         0 |      0         | 4.3e+07     |
|   1383 |   12311 | 740844           |          3.29981e+06 |         0 |      0         | 2.4e+08     |
|   1384 |    5435 |      2.75092e+06 |          6.95376e+06 |         0 |      2e+06     | 4.16e+08    |
|   1385 |    8100 |      3.19618e+06 |          5.93133e+06 |         0 |      2.4e+06   | 3.0205e+08  |
|   1386 |    9931 |      2.82046e+06 |          5.26072e+06 |         0 |      1.28e+06  | 1.46e+08    |
|   1387 |   12802 |      2.59199e+06 |          4.9382e+06  |         0 | 960000         | 9.6e+07     |
|   1388 |   15807 |      2.54677e+06 |          5.42452e+06 |         0 |      0         | 1.536e+08   |
|   1389 |   19203 |      2.85659e+06 |          6.53489e+06 |         0 |      0         | 1.92e+08    |
|   1390 |   12649 |      3.22552e+06 |          1.00088e+07 |         0 |      0         | 7e+08       |
|   1391 |   13084 |      3.38721e+06 |          9.54593e+06 |         0 |      0         | 3e+08       |
|   1392 |   11382 |      4.18745e+06 |          1.28342e+07 |         0 |      0         | 6e+08       |
|   1393 |   10733 |      4.86805e+06 |          1.26958e+07 |         0 |      2e+06     | 2.2e+08     |
|   1394 |   10797 |      5.60422e+06 |          1.47561e+07 |         0 |      3.6e+06   | 3.42e+08    |
|   1395 |   10812 |      6.31122e+06 |          1.79339e+07 |         0 |      4.8e+06   | 4.86e+08    |
|   1396 |   11865 |      7.41738e+06 |          1.92248e+07 |         0 |      0         | 5e+08       |
|   1397 |   12905 |      1.0476e+07  |          2.43959e+07 |         0 |      0         | 5.4e+08     |
|   1398 |   19480 |      1.05287e+07 |          2.54027e+07 |         0 |      2.74e+06  | 1.25e+09    |
|   1399 |   37173 |      2.37203e+07 |          5.18463e+07 |         0 |      2.064e+07 | 8.6e+09     |
|   1400 |   35732 |      2.84796e+07 |          3.8429e+07  |         0 |      2.064e+07 | 2.064e+09   |
|   1401 |   53724 |      5.01588e+07 |          5.94429e+07 |         0 |      3.456e+07 | 1.08475e+09 |
|   1402 |   47606 |      1.9865e+07  |          5.81125e+07 |         0 |      0         | 1.665e+09   |


### Home_Production

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL07
      type: float
    1364:
      column_code: DYCOL07
      type: float
    1365:
      column_code: DYCOL07
      type: float
    1366:
      column_code: DYCOL07
      type: float
    1367:
      column_code: DYCOL07
      type: float
    1368:
      column_code: DYCOL07
      type: float
    1369:
      column_code: DYCOL07
      type: float
    1370:
      column_code: DYCOL07
      type: float
    1371:
      column_code: DYCOL07
      type: float
    1372:
      column_code: DYCOL07
      type: float
    1373:
      column_code: DYCOL07
      type: float
    1374:
      column_code: DYCOL07
      type: float
    1375:
      column_code: DYCOL07
      type: float
    1376:
      column_code: DYCOL07
      type: float
    1377:
      column_code: DYCOL07
      type: float
    1378:
      column_code: DYCOL07
      type: float
    1379:
      column_code: DYCOL07
      type: float
    1380:
      column_code: DYCOL07
      type: float
    1381:
      column_code: DYCOL07
      type: float
    1382:
      column_code: DYCOL07
      type: float
    1383:
      column_code: DYCOL07
      type: float
    1384:
      column_code: DYCOL07
      type: float
    1385:
      column_code: DYCOL07
      type: float
    1386:
      column_code: DYCOL07
      type: float
    1387:
      column_code: DYCOL07
      type: float
    1388:
      column_code: DYCOL07
      type: float
    1389:
      column_code: DYCOL07
      type: float
    1390:
      column_code: DYCOL07
      type: float
    1391:
      column_code: DYCOL07
      type: float
    1392:
      column_code: DYCOL07
      type: float
    1393:
      column_code: DYCOL07
      type: float
    1394:
      column_code: DYCOL07
      type: float
    1395:
      column_code: DYCOL07
      type: float
    1396:
      column_code: DYCOL07
      type: float
    1397:
      column_code: DYCOL07
      type: float
    1398:
      column_code: DYCOL07
      type: float
    1399:
      column_code: DYCOL07
      type: float
    1400:
      column_code: DYCOL07
      type: float
    1401:
      column_code: DYCOL07
      type: float
    1402:
      column_code: DYCOL07
      type: float
    
    ```
#### Column Codes

| Years     | Home_Production                                   |
|:----------|:--------------------------------------------------|
| 1369-1383 | [COL07](/HBSIR/tables/raw/other_income#col07)     |
| 1384-1402 | [DYCOL07](/HBSIR/tables/raw/other_income#dycol07) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |   Median |    Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------:|-----------:|
|   1369 |    4128 |  68340.7         |     163260           |         0 |        0 | 4.25e+06   |
|   1370 |    4790 |  26027.3         |     154405           |         0 |        0 | 6e+06      |
|   1371 |    4886 |  29744.4         |     159849           |         0 |        0 | 3.6e+06    |
|   1372 |    3139 |  27841           |     151605           |         0 |        0 | 2.4e+06    |
|   1373 |    5554 |  71428.2         |     374713           |         0 |        0 | 1.2e+07    |
|   1374 |   11663 |  94488.9         |     442727           |         0 |        0 | 1.5e+07    |
|   1375 |    6517 | 123448           |     579626           |         0 |        0 | 1.5e+07    |
|   1376 |    6915 | 138413           |     807324           |         0 |        0 | 3.05e+07   |
|   1377 |    5596 | 111407           |     636993           |         0 |        0 | 2e+07      |
|   1378 |   12202 | 106659           |     709649           |         0 |        0 | 3.6e+07    |
|   1379 |   10670 | 155761           |     907520           |         0 |        0 | 3e+07      |
|   1380 |   12391 | 125718           |     946064           |         0 |        0 | 6e+07      |
|   1381 |   15277 | 134760           |          1.11694e+06 |         0 |        0 | 7e+07      |
|   1382 |   10014 | 226937           |          2.74782e+06 |         0 |        0 | 2e+08      |
|   1383 |   12311 | 369256           |          4.8953e+06  |         0 |        0 | 3.05e+08   |
|   1384 |    3558 |      1.3503e+06  |          4.77922e+06 |         0 |        0 | 1.35e+08   |
|   1385 |    5525 |      1.23555e+06 |          6.84718e+06 |         0 |        0 | 2.5e+08    |
|   1386 |    7138 |      1.09594e+06 |          5.42395e+06 |         0 |        0 | 1.8e+08    |
|   1387 |    9318 | 742078           |          4.58543e+06 |         0 |        0 | 3e+08      |
|   1388 |   11895 | 518237           |          2.84188e+06 |         0 |        0 | 6e+07      |
|   1389 |   16252 |      2.1465e+06  |          4.54982e+06 |         0 |        0 | 2e+08      |
|   1390 |    9472 | 717521           |          6.37705e+06 |         0 |        0 | 3.3038e+08 |
|   1391 |    9757 | 660723           |          4.61698e+06 |         0 |        0 | 1.5e+08    |
|   1392 |    7849 |      1.13729e+06 |          7.4247e+06  |         0 |        0 | 2.4e+08    |
|   1393 |    7424 |      2.12276e+06 |          1.3396e+07  |         0 |        0 | 5e+08      |
|   1394 |    7225 |      2.98098e+06 |          3.84949e+07 |         0 |        0 | 3e+09      |
|   1395 |    7054 |      2.83129e+06 |          1.72144e+07 |         0 |        0 | 3.6e+08    |
|   1396 |    8360 |      2.69738e+06 |          1.20505e+07 |         0 |        0 | 3e+08      |
|   1397 |    8960 |      2.54044e+06 |          1.39011e+07 |         0 |        0 | 5e+08      |
|   1398 |   10073 |      2.69082e+06 |          1.55466e+07 |         0 |        0 | 4.8e+08    |
|   1399 |   12960 |      2.64307e+06 |          2.11466e+07 |         0 |        0 | 9.6e+08    |
|   1400 |   11416 |      4.42904e+06 |          2.90069e+07 |         0 |        0 | 8.4e+08    |
|   1401 |   53724 |      1.50563e+06 |          3.52124e+07 |         0 |        0 | 6e+09      |
|   1402 |   47606 |      1.41878e+06 |          2.04907e+07 |         0 |        0 | 1e+09      |


### Transfer

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL08
      type: float
    1364:
      column_code: DYCOL08
      type: float
    1365:
      column_code: DYCOL08
      type: float
    1366:
      column_code: DYCOL08
      type: float
    1367:
      column_code: DYCOL08
      type: float
    1368:
      column_code: DYCOL08
      type: float
    1369:
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

| Years     | Transfer                                          |
|:----------|:--------------------------------------------------|
| 1369-1377 |                                                   |
| 1378-1383 | [COL08](/HBSIR/tables/raw/other_income#col08)     |
| 1384-1402 | [DYCOL08](/HBSIR/tables/raw/other_income#dycol08) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |       Median |   Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-------------:|----------:|
|   1378 |   12202 | 423405           |          1.7957e+06  |         0 |      0       | 8e+07     |
|   1379 |   10670 | 350525           |          1.96592e+06 |         0 |      0       | 1.17e+08  |
|   1380 |   12391 | 779748           |          3.47177e+06 |         0 |      0       | 2.4e+08   |
|   1381 |   15277 | 949932           |          3.09717e+06 |         0 |      0       | 1e+08     |
|   1382 |   10014 |      1.17352e+06 |          5.48608e+06 |         0 |      0       | 3e+08     |
|   1383 |   12311 |      1.45591e+06 |          4.97613e+06 |         0 |      0       | 1.785e+08 |
|   1384 |    7224 |      3.39557e+06 |          8.77973e+06 |         0 | 600000       | 3.5e+08   |
|   1385 |    9299 |      3.38782e+06 |          8.23371e+06 |         0 | 500000       | 2.5e+08   |
|   1386 |    9570 |      3.50667e+06 |          9.2009e+06  |         0 | 300000       | 3e+08     |
|   1387 |   12484 |      3.62595e+06 |          1.03771e+07 |         0 | 250000       | 3e+08     |
|   1388 |   15019 |      3.47128e+06 |          1.02923e+07 |         0 |      0       | 3.2e+08   |
|   1389 |   16930 |      3.47003e+06 |          1.07415e+07 |         0 |      0       | 5e+08     |
|   1390 |   12146 |      4.89451e+06 |          1.37973e+07 |         0 | 200000       | 5e+08     |
|   1391 |   12648 |      5.57036e+06 |          1.84495e+07 |         0 | 250000       | 8e+08     |
|   1392 |   11426 |      7.55419e+06 |          1.97084e+07 |         0 | 500000       | 4.5e+08   |
|   1393 |   11912 |      9.77257e+06 |          2.39319e+07 |         0 | 800000       | 8e+08     |
|   1394 |   12284 |      1.2343e+07  |          3.0277e+07  |         0 |      1e+06   | 8.5e+08   |
|   1395 |   12792 |      1.42262e+07 |          4.87012e+07 |         0 |      1.7e+06 | 4e+09     |
|   1396 |   14258 |      1.52958e+07 |          3.76479e+07 |         0 |      2e+06   | 8.5e+08   |
|   1397 |   15885 |      1.59064e+07 |          4.56361e+07 |         0 |      1.8e+06 | 2e+09     |
|   1398 |   16671 |      1.81822e+07 |          6.9429e+07  |         0 |      1.5e+06 | 5e+09     |
|   1399 |   18602 |      1.64944e+07 |          7.62405e+07 |         0 |      0       | 7e+09     |
|   1400 |   17125 |      2.44055e+07 |          9.70291e+07 |         0 |      0       | 4.5e+09   |
|   1401 |   53724 |      1.13665e+07 |          6.99661e+07 |         0 |      0       | 3.8e+09   |
|   1402 |   47606 |      1.97368e+07 |          1.1272e+08  |         0 |      0       | 6.01e+09  |


