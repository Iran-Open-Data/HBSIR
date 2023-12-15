# cloth

## Old to New Titles

| Years     | ADDRESS   | COL1   | COL3             | COL4         | COL5        | COL6        |
|:----------|:----------|:-------|:-----------------|:-------------|:------------|:------------|
| 1363-1368 | ID        | Code   | Provision_Method | Expenditure  |             |             |
| 1369      | ID        | Code   | Provision_Method | Price_System | Amount      | Expenditure |
| 1370-1373 | ID        | Code   | Provision_Method | Price_System | Expenditure |             |
| 1374-1383 | ID        | Code   | Provision_Method | Expenditure  |             |             |


| Years     | ADDRESS   | DYCOL01   | DYCOL02          | DYCOL03     |
|:----------|:----------|:----------|:-----------------|:------------|
| 1384-1401 | ID        | Code      | Provision_Method | Expenditure |


## New to Old Titles

| Years     | ID      | Code    | Provision_Method   | Expenditure   | Price_System   | Amount   |
|:----------|:--------|:--------|:-------------------|:--------------|:---------------|:---------|
| 1363-1368 | ADDRESS | COL1    | COL3               | COL4          |                |          |
| 1369      | ADDRESS | COL1    | COL3               | COL6          | COL4           | COL5     |
| 1370-1373 | ADDRESS | COL1    | COL3               | COL5          | COL4           |          |
| 1374-1383 | ADDRESS | COL1    | COL3               | COL4          |                |          |
| 1384-1401 | ADDRESS | DYCOL01 | DYCOL02            | DYCOL03       |                |          |


## Columns Details

### ID

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: ADDRESS
      type: UInt64
    
    ```
#### Column Codes

| Years     | ID                                         |
|:----------|:-------------------------------------------|
| 1363-1401 | [ADDRESS](/HBSIR/tables/raw/cloth#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|-----------------:|------------:|
|   1363 |   84379 | 681256           |     509052           |  1001          |      1.0312e+06  | 1.23452e+06 |
|   1364 |   86535 | 643019           |     510532           |  1001          |      1.02114e+06 | 1.23442e+06 |
|   1365 |   12881 | 577117           |     531618           |  1003          | 211004           | 1.23422e+06 |
|   1366 |   15731 | 625208           |     524385           |  1002          |      1.00402e+06 | 1.23421e+06 |
|   1367 |   24314 | 606156           |     523077           |  1003          | 234004           | 1.23428e+06 |
|   1368 |   37281 | 591076           |     516096           |  1001          | 232014           | 1.23428e+06 |
|   1369 |   58530 | 583579           |     513038           |  1001          | 221033           | 1.23422e+06 |
|   1370 |   59085 | 582825           |     510010           |  1002          | 223029           | 1.23422e+06 |
|   1371 |   58257 | 591931           |     509212           |  1001          | 233001           | 1.23422e+06 |
|   1372 |   36365 | 626068           |     510603           |  1001          |      1.00311e+06 | 1.23422e+06 |
|   1373 |   54558 | 722600           |     510779           |  1001          |      1.04408e+06 | 1.24404e+06 |
|   1374 |  103217 |      6.59899e+06 |          5.10571e+06 | 10002          |      1.02401e+07 | 1.24401e+07 |
|   1375 |   59272 | 621333           |     519174           |  1001          |      1.003e+06   | 1.24404e+06 |
|   1376 |   59562 | 619869           |     516580           |  1002          |      1.00205e+06 | 1.25406e+06 |
|   1377 |   47201 |      5.7913e+07  |          5.14148e+07 | 11001          |      2.4041e+07  | 1.27074e+08 |
|   1378 |   81213 |      5.95782e+07 |          5.13257e+07 | 11002          |      2.40621e+07 | 1.27074e+08 |
|   1379 |   78548 |      5.85614e+07 |          5.10439e+07 | 11001          |      2.40531e+07 | 1.27074e+08 |
|   1380 |   79040 |      6.01952e+07 |          5.12725e+07 | 11001          |      2.60241e+07 | 1.27074e+08 |
|   1381 |  113712 |      6.04468e+07 |          5.10509e+07 | 11001          |      2.60321e+07 | 1.27074e+08 |
|   1382 |   85895 |      5.91301e+07 |          5.10587e+07 | 11001          |      2.5012e+07  | 1.27114e+08 |
|   1383 |  102352 |      5.97304e+07 |          5.10895e+07 | 11003          |      2.6012e+07  | 1.27114e+08 |
|   1384 |  106500 |      6.04739e+07 |          5.10625e+07 | 11006          |      2.7024e+07  | 1.29214e+08 |
|   1385 |  107199 |      5.85783e+07 |          5.12554e+07 | 11002          |      2.60321e+07 | 1.29214e+08 |
|   1386 |  102156 |      6.19719e+07 |          5.08229e+07 | 11006          |      2.81331e+07 | 1.29214e+08 |
|   1387 |  114423 |      1.63829e+09 |          5.04395e+08 |     1e+09      |      1.29767e+09 | 2.29786e+09 |
|   1388 |   99955 |      1.61921e+09 |          5.04822e+08 |     1e+09      |      1.29e+09    | 2.29025e+09 |
|   1389 |   94080 |      1.6417e+09  |          5.02827e+08 |     1e+09      |      1.29012e+09 | 2.29013e+09 |
|   1390 |   88637 |      1.65725e+09 |          5.02868e+08 |     1e+09      |      2.00012e+09 | 2.30013e+09 |
|   1391 |   83200 |      1.66041e+09 |          5.01306e+08 |     1e+09      |      2.00011e+09 | 2.30013e+09 |
|   1392 |   79177 |      1.63685e+10 |          5.03859e+09 |     1.0001e+10 |      1.29076e+10 | 2.30047e+10 |
|   1393 |   72069 |      1.64165e+10 |          5.01525e+09 |     1.0001e+10 |      1.30016e+10 | 2.30047e+10 |
|   1394 |   69165 |      1.63602e+10 |          5.02242e+09 |     1.0001e+10 |      1.30016e+10 | 2.30047e+10 |
|   1395 |   68676 |      1.62543e+10 |          5.00461e+09 |     1.0001e+10 |      1.29046e+10 | 2.30047e+10 |
|   1396 |   72079 |      1.62521e+10 |          5.0265e+09  |     1.0001e+10 |      1.29036e+10 | 2.30047e+10 |
|   1397 |   60862 |      1.61503e+10 |          5.0446e+09  |     1.0001e+10 |      1.28064e+10 | 2.30067e+10 |
|   1398 |   48371 |      1.61231e+10 |          5.04991e+09 |     1.0001e+10 |      1.28074e+10 | 2.30067e+10 |
|   1399 |   53795 |      1.59609e+10 |          5.03106e+09 |     1.0001e+10 |      1.28023e+10 | 2.30067e+10 |
|   1400 |   56915 |      1.59947e+10 |          4.99761e+09 |     1.0001e+10 |      1.28013e+10 | 2.30067e+10 |
|   1401 |   48035 |      1.60891e+10 |          5.012e+09   |     1.0001e+10 |      1.28074e+10 | 2.30067e+10 |


### Code

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL1
      type: UInt32
    1374:
      column_code: DYCOL01
      type: UInt32
    1375:
      column_code: DYCOL01
      type: UInt32
    1376:
      column_code: DYCOL01
      type: UInt32
    1377:
      column_code: DYCOL01
      type: UInt32
    1378:
      column_code: DYCOL01
      type: UInt32
    1379:
      column_code: DYCOL01
      type: UInt32
    1380:
      column_code: DYCOL01
      type: UInt32
    1381:
      column_code: DYCOL01
      type: UInt32
    1382:
      column_code: DYCOL01
      type: UInt32
    1383:
      column_code: DYCOL01
      type: UInt32
    1384:
      column_code: DYCOL01
      type: UInt32
    1385:
      column_code: DYCOL01
      type: UInt32
    1386:
      column_code: DYCOL01
      type: UInt32
    1387:
      column_code: DYCOL01
      type: UInt32
    1388:
      column_code: DYCOL01
      type: UInt32
    1389:
      column_code: DYCOL01
      type: UInt32
    1390:
      column_code: DYCOL01
      type: UInt32
    1391:
      column_code: DYCOL01
      type: UInt32
    1392:
      column_code: DYCOL01
      type: UInt32
    1393:
      column_code: DYCOL01
      type: UInt32
    1394:
      column_code: DYCOL01
      type: UInt32
    1395:
      column_code: DYCOL01
      type: UInt32
    1396:
      column_code: DYCOL01
      type: UInt32
    1397:
      column_code: DYCOL01
      type: UInt32
    1398:
      column_code: DYCOL01
      type: UInt32
    1399:
      column_code: DYCOL01
      type: UInt32
    1400:
      column_code: DYCOL01
      type: UInt32
    1401:
      column_code: DYCOL01
      type: UInt32
    
    ```
#### Column Codes

| Years     | Code                                       |
|:----------|:-------------------------------------------|
| 1363-1383 | [COL1](/HBSIR/tables/raw/cloth#col1)       |
| 1384-1401 | [DYCOL01](/HBSIR/tables/raw/cloth#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 |   84379 | 21744.9 |               380.32 |     21113 |    21678 |     22422 |
|   1364 |   86535 | 21733.8 |               403.87 |     21113 |    21678 |     29997 |
|   1365 |   12881 | 21716.2 |               388.9  |     21113 |    21634 |     22353 |
|   1366 |   15731 | 21751.4 |               442.23 |     21113 |    21678 |     29997 |
|   1367 |   24314 | 21757.6 |               413.22 |     21113 |    21678 |     29997 |
|   1368 |   37281 | 21773.8 |               466.03 |     21113 |    21689 |     29997 |
|   1369 |   58530 | 21742.2 |               392.23 |     21113 |    21656 |     23210 |
|   1370 |   59085 | 21626.5 |               437.18 |     21113 |    21441 |     22422 |
|   1371 |   58257 | 21620.3 |               436.68 |     21113 |    21441 |     22422 |
|   1372 |   36365 | 21625   |               438.84 |     21113 |    21441 |     22422 |
|   1373 |   54558 | 21631   |               439.72 |     21113 |    21441 |     22422 |
|   1374 |  103217 | 21661.9 |               452.2  |     21113 |    21452 |     22422 |
|   1375 |   59272 | 21651.5 |               446    |     21113 |    21452 |     22422 |
|   1376 |   59562 | 21637.3 |               439.45 |     21113 |    21452 |     22422 |
|   1377 |   47201 | 21629.8 |               433.14 |     21113 |    21452 |     22422 |
|   1378 |   81213 | 21632.8 |               433.67 |     21113 |    21452 |     22433 |
|   1379 |   78548 | 21617.6 |               429.3  |     21113 |    21452 |     22433 |
|   1380 |   79040 | 21601.6 |               420.31 |     21113 |    21452 |     22433 |
|   1381 |  113712 | 21602.2 |               422.21 |     21113 |    21452 |     22433 |
|   1382 |   85895 | 21591   |               418.15 |     21113 |    21420 |     22433 |
|   1383 |  102352 | 31479.8 |               394.59 |     31111 |    31252 |     32221 |
|   1384 |  106500 | 31488.7 |               399.72 |     31111 |    31252 |     32221 |
|   1385 |  107199 | 31481   |               395.64 |     31111 |    31251 |     32221 |
|   1386 |  102156 | 31468.1 |               388.43 |     31111 |    31251 |     32221 |
|   1387 |  114423 | 31447   |               376.29 |     31111 |    31251 |     32221 |
|   1388 |   99955 | 31450.6 |               378.22 |     31111 |    31251 |     32221 |
|   1389 |   94080 | 31450.5 |               378.16 |     31111 |    31251 |     32221 |
|   1390 |   88637 | 31449.3 |               377.13 |     31111 |    31251 |     32221 |
|   1391 |   83200 | 31448.5 |               374.95 |     31111 |    31251 |     32221 |
|   1392 |   79177 | 31437.1 |               366.67 |     31111 |    31251 |     32221 |
|   1393 |   72069 | 31433.4 |               361.92 |     31111 |    31251 |     32221 |
|   1394 |   69165 | 31430.7 |               361.71 |     31111 |    31251 |     32221 |
|   1395 |   68676 | 31423.5 |               355.18 |     31111 |    31251 |     32221 |
|   1396 |   72079 | 31423   |               355.42 |     31111 |    31251 |     32221 |
|   1397 |   60862 | 31430.5 |               360.65 |     31111 |    31251 |     32221 |
|   1398 |   48371 | 31428.2 |               358.14 |     31111 |    31251 |     32221 |
|   1399 |   53795 | 31395.1 |               313.73 |     31111 |    31261 |     32221 |
|   1400 |   56915 | 31397.5 |               318.74 |     31111 |    31255 |     32221 |
|   1401 |   48035 | 31408.8 |               341.62 |     31111 |    31251 |     32221 |


### Provision_Method

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL3
      type: category
      categories:
        1: Purchase_Subsidised_Price
        2: Purchase_Free_Price
        3: Home_Production
        4: Instead_of_Public_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1369:
      column_code: COL3
      type: category
      categories:
        2: Purchase
        3: Home_Production
        4: Instead_of_Public_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1374:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Private_Service
        5: Agricultural_Work
        6: Non_Agricultural_Work
        7: Donation
    1375:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Private_Service
        5: Agricultural_Work
        6: Non_Agricultural_Work
        7: Donation
    1376:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Private_Service
        5: Agricultural_Work
        6: Non_Agricultural_Work
        7: Donation
    1377:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Private_Service
        5: Agricultural_Work
        6: Non_Agricultural_Work
        7: Donation
    1378:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Private_Service
        5: Agricultural_Work
        6: Non_Agricultural_Work
        7: Donation
    1379:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Private_Service
        5: Agricultural_Work
        6: Non_Agricultural_Work
        7: Donation
        8: Instead_of_Cooperative_Service
    1380:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Private_Service
        5: Agricultural_Work
        6: Non_Agricultural_Work
        7: Donation
        8: Instead_of_Cooperative_Service
    1381:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Private_Service
        5: Agricultural_Work
        6: Non_Agricultural_Work
        7: Donation
        8: Instead_of_Cooperative_Service
    1382:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Private_Service
        5: Agricultural_Work
        6: Non_Agricultural_Work
        7: Donation
        8: Instead_of_Cooperative_Service
    1383:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1384:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1385:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1386:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1387:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1388:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1389:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1390:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1391:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1392:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1393:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1394:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1395:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1396:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1397:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1398:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1399:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1400:
      column_code: DYCOL02
      type: category
      categories:
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1401:
      column_code: DYCOL02
      type: category
      categories:
        0: Secondhand_Sale
        1: Purchase
        2: Home_Production
        3: Instead_of_Public_Service
        4: Instead_of_Cooperative_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    
    ```
#### Column Codes

| Years     | Provision_Method                           |
|:----------|:-------------------------------------------|
| 1363-1383 | [COL3](/HBSIR/tables/raw/cloth#col3)       |
| 1384-1401 | [DYCOL02](/HBSIR/tables/raw/cloth#dycol02) |


#### Summary Statistics

**category data**

|   Year | Purchase   |   Non_Agricultural_Work |   Home_Production |   Donation | Instead_of_Private_Service   |   Instead_of_Public_Service | Agricultural_Work   | Purchase_Free_Price   | Purchase_Subsidised_Price   | nan   | Instead_of_Cooperative_Service   |
|-------:|:-----------|------------------------:|------------------:|-----------:|:-----------------------------|----------------------------:|:--------------------|:----------------------|:----------------------------|:------|:---------------------------------|
|   1363 |            |                    0.54 |              2.54 |       0.18 | 0.01                         |                        0.09 | 0.01                | 84.63                 | 11.99                       |       |                                  |
|   1364 |            |                    0.58 |              2.26 |       0.13 | 0.02                         |                        0.05 | 0.02                | 90.83                 | 6.11                        |       |                                  |
|   1365 |            |                    0.49 |              2.05 |       0.15 |                              |                        0.06 | 0.01                | 93.43                 | 3.81                        |       |                                  |
|   1366 |            |                    0.48 |              2    |       0.14 | 0.03                         |                        0.02 |                     | 93.83                 | 3.45                        | 0.05  |                                  |
|   1367 |            |                    0.42 |              1.41 |       0.09 |                              |                        0.05 | 0.0                 | 95.51                 | 2.5                         | 0.02  |                                  |
|   1368 |            |                    0.49 |              1.35 |       0.17 | 0.0                          |                        0.07 | 0.01                | 95.81                 | 2.02                        | 0.08  |                                  |
|   1369 | 98.17      |                    0.47 |              0.96 |       0.14 | 0.01                         |                        0.05 | 0.01                |                       |                             | 0.2   |                                  |
|   1370 | 98.24      |                    0.49 |              1.01 |       0.11 | 0.02                         |                        0.04 | 0.03                |                       |                             | 0.07  |                                  |
|   1371 | 98.29      |                    0.54 |              0.87 |       0.12 | 0.02                         |                        0.03 | 0.02                |                       |                             | 0.11  |                                  |
|   1372 | 98.52      |                    0.36 |              0.86 |       0.08 | 0.01                         |                        0.02 | 0.01                |                       |                             | 0.13  |                                  |
|   1373 | 98.42      |                    0.39 |              0.97 |       0.1  | 0.01                         |                        0.04 | 0.01                |                       |                             | 0.05  |                                  |
|   1374 | 98.55      |                    0.49 |              0.77 |       0.12 | 0.02                         |                        0.04 | 0.02                |                       |                             | 0.0   |                                  |
|   1375 | 98.61      |                    0.53 |              0.63 |       0.13 | 0.04                         |                        0.05 | 0.0                 |                       |                             |       |                                  |
|   1376 | 98.46      |                    0.58 |              0.71 |       0.14 | 0.04                         |                        0.04 | 0.02                |                       |                             |       |                                  |
|   1377 | 98.54      |                    0.54 |              0.68 |       0.17 | 0.03                         |                        0.04 | 0.0                 |                       |                             |       |                                  |
|   1378 | 98.48      |                    0.5  |              0.53 |       0.44 | 0.03                         |                        0.03 | 0.01                |                       |                             |       |                                  |
|   1379 | 98.61      |                    0.53 |              0.54 |       0.25 | 0.02                         |                        0.04 | 0.0                 |                       |                             |       | 0.0                              |
|   1380 | 98.7       |                    0.56 |              0.47 |       0.23 | 0.02                         |                        0.02 | 0.0                 |                       |                             |       | 0.0                              |
|   1381 | 98.89      |                    0.53 |              0.39 |       0.14 | 0.01                         |                        0.03 | 0.0                 |                       |                             |       | 0.0                              |
|   1382 | 98.9       |                    0.54 |              0.42 |       0.09 | 0.02                         |                        0.02 | 0.01                |                       |                             |       |                                  |
|   1383 | 98.99      |                    0.51 |              0.32 |       0.14 | 0.02                         |                        0.01 | 0.01                |                       |                             |       | 0.0                              |
|   1384 | 99.01      |                    0.5  |              0.31 |       0.14 | 0.01                         |                        0.02 | 0.0                 |                       |                             |       | 0.0                              |
|   1385 | 99.05      |                    0.53 |              0.3  |       0.09 | 0.02                         |                        0.01 | 0.0                 |                       |                             |       | 0.0                              |
|   1386 | 99.05      |                    0.49 |              0.3  |       0.09 | 0.03                         |                        0.04 | 0.0                 |                       |                             |       | 0.0                              |
|   1387 | 99.39      |                    0.32 |              0.22 |       0.05 | 0.01                         |                        0.01 |                     |                       |                             |       |                                  |
|   1388 | 99.4       |                    0.32 |              0.19 |       0.07 | 0.01                         |                        0.01 | 0.0                 |                       |                             |       | 0.0                              |
|   1389 | 99.45      |                    0.31 |              0.21 |       0.03 | 0.0                          |                        0    |                     |                       |                             |       |                                  |
|   1390 | 99.49      |                    0.24 |              0.21 |       0.03 | 0.01                         |                        0    | 0.0                 |                       |                             |       | 0.0                              |
|   1391 | 99.52      |                    0.19 |              0.19 |       0.09 | 0.0                          |                        0.01 | 0.0                 |                       |                             |       | 0.0                              |
|   1392 | 99.56      |                    0.21 |              0.21 |       0.01 | 0.0                          |                        0    |                     |                       |                             |       |                                  |
|   1393 | 99.49      |                    0.25 |              0.17 |       0.06 | 0.01                         |                        0.01 | 0.0                 |                       |                             |       | 0.0                              |
|   1394 | 99.65      |                    0.21 |              0.11 |       0.02 | 0.0                          |                        0    |                     |                       |                             |       | 0.0                              |
|   1395 | 99.55      |                    0.24 |              0.14 |       0.05 | 0.0                          |                        0.01 |                     |                       |                             | 0.0   | 0.0                              |
|   1396 | 99.55      |                    0.25 |              0.1  |       0.08 | 0.01                         |                        0.01 | 0.0                 |                       |                             |       | 0.0                              |
|   1397 | 99.65      |                    0.19 |              0.1  |       0.05 | 0.01                         |                        0    |                     |                       |                             |       |                                  |
|   1398 | 99.58      |                    0.14 |              0.14 |       0.12 | 0.01                         |                        0    | 0.0                 |                       |                             |       |                                  |
|   1399 | 99.35      |                    0.18 |              0.05 |       0.28 | 0.1                          |                        0.04 |                     |                       |                             |       |                                  |
|   1400 | 99.51      |                    0.16 |              0.06 |       0.11 | 0.12                         |                        0.04 |                     |                       |                             |       |                                  |
|   1401 | 99.62      |                    0.26 |              0.06 |       0.03 | 0.02                         |                        0.01 | 0.0                 |                       |                             |       |                                  |


#### Categories

|    | 1363-1368                  | 1369-1373                  | 1374-1378                  | 1379-1382                      | 1383-1400                      | 1401                           |
|---:|:---------------------------|:---------------------------|:---------------------------|:-------------------------------|:-------------------------------|:-------------------------------|
|  0 |                            |                            |                            |                                |                                | Secondhand_Sale                |
|  1 | Purchase_Subsidised_Price  |                            | Purchase                   | Purchase                       | Purchase                       | Purchase                       |
|  2 | Purchase_Free_Price        | Purchase                   | Home_Production            | Home_Production                | Home_Production                | Home_Production                |
|  3 | Home_Production            | Home_Production            | Instead_of_Public_Service  | Instead_of_Public_Service      | Instead_of_Public_Service      | Instead_of_Public_Service      |
|  4 | Instead_of_Public_Service  | Instead_of_Public_Service  | Instead_of_Private_Service | Instead_of_Private_Service     | Instead_of_Cooperative_Service | Instead_of_Cooperative_Service |
|  5 | Instead_of_Private_Service | Instead_of_Private_Service | Agricultural_Work          | Agricultural_Work              | Instead_of_Private_Service     | Instead_of_Private_Service     |
|  6 | Agricultural_Work          | Agricultural_Work          | Non_Agricultural_Work      | Non_Agricultural_Work          | Agricultural_Work              | Agricultural_Work              |
|  7 | Non_Agricultural_Work      | Non_Agricultural_Work      | Donation                   | Donation                       | Non_Agricultural_Work          | Non_Agricultural_Work          |
|  8 | Donation                   | Donation                   |                            | Instead_of_Cooperative_Service | Donation                       | Donation                       |


### Expenditure

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL4
      type: float
    1369:
      column_code: COL6
      type: float
    1370:
      column_code: COL5
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
    
    ```
#### Column Codes

| Years     | Expenditure                                |
|:----------|:-------------------------------------------|
| 1363-1368 | [COL4](/HBSIR/tables/raw/cloth#col4)       |
| 1369      | [COL6](/HBSIR/tables/raw/cloth#col6)       |
| 1370-1373 | [COL5](/HBSIR/tables/raw/cloth#col5)       |
| 1374-1383 | [COL4](/HBSIR/tables/raw/cloth#col4)       |
| 1384-1401 | [DYCOL03](/HBSIR/tables/raw/cloth#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |       Median |       Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-------------:|--------------:|
|   1363 |   84379 |   2373.89        |       4109.63        |         5 |   1200       | 230000        |
|   1364 |   86535 |   2349.68        |       4395.79        |         5 |   1200       | 240000        |
|   1365 |   12881 |   2958.3         |       5022.14        |        50 |   1500       | 200000        |
|   1366 |   15731 |   3389.61        |       5181.41        |        20 |   1800       |  98000        |
|   1367 |   24314 |   4577.77        |       7280.07        |        20 |   2400       | 220000        |
|   1368 |   37281 |   5379.12        |       9673.46        |        20 |   2500       | 650000        |
|   1369 |   58530 |   7091.02        |      11506           |        20 |   3600       | 530000        |
|   1370 |   59084 |   8074.17        |      14100.2         |        40 |   4000       | 970000        |
|   1371 |   58257 |  10063.8         |      17332           |         0 |   4800       |      1.4e+06  |
|   1372 |   36365 |  11767.8         |      19762.7         |        80 |   5500       | 970000        |
|   1373 |   54558 |  16822.9         |      28643.6         |        85 |   7500       |      1.1e+06  |
|   1374 |  103214 |  24907.8         |      41766.1         |         1 |  12000       |      3e+06    |
|   1375 |   59272 |  33652.3         |      56110.8         |        50 |  15000       |      3e+06    |
|   1376 |   59562 |  38550.8         |      66148.6         |       120 |  18000       |      4e+06    |
|   1377 |   47201 |  42801.3         |      69194.8         |       100 |  20000       |      3e+06    |
|   1378 |   81213 |  44237           |      75806.4         |       200 |  20000       |      3e+06    |
|   1379 |   78548 |  50672.8         |      84172.4         |       100 |  24000       |      4e+06    |
|   1380 |   79040 |  51268.4         |      80284.5         |       100 |  25000       |      3e+06    |
|   1381 |  113712 |  52967.8         |      90729.6         |       200 |  25000       |      6e+06    |
|   1382 |   85895 |  55952.8         |      90382.3         |       200 |  30000       |      7.2e+06  |
|   1383 |  102352 |  61633.3         |      94784.8         |         0 |  32000       |      8e+06    |
|   1384 |  106358 |  69764.5         |     109911           |       250 |  40000       |      5.5e+06  |
|   1385 |  107199 |  84249.5         |     127651           |       500 |  50000       |      5e+06    |
|   1386 |  102156 |  99282.4         |     152368           |       500 |  60000       |      8.5e+06  |
|   1387 |  114423 | 118513           |     183288           |       500 |  75000       |      1.11e+07 |
|   1388 |   99955 | 134750           |     193212           |       300 |  85000       |      1.25e+07 |
|   1389 |   94080 | 163735           |     233034           |       500 | 100000       |      1e+07    |
|   1390 |   88637 | 201823           |     259750           |      1000 | 150000       |      8e+06    |
|   1391 |   83200 | 271270           |     366191           |      1000 | 185000       |      2.7e+07  |
|   1392 |   79177 | 364578           |     479034           |      2000 | 250000       |      2e+07    |
|   1393 |   72069 | 417121           |     645466           |      3000 | 300000       |      8.8e+07  |
|   1394 |   69165 | 435090           |     552856           |      3000 | 300000       |      3.5e+07  |
|   1395 |   68675 | 446693           |     564748           |      2500 | 300000       |      2e+07    |
|   1396 |   72079 | 496749           |     671256           |      3000 | 350000       |      6e+07    |
|   1397 |   60862 | 673760           |     863934           |      3500 | 480000       |      5.09e+07 |
|   1398 |   48371 | 912196           |          1.23903e+06 |      9000 | 600000       |      5e+07    |
|   1399 |   53795 |      1.09334e+06 |          1.51158e+06 |     10000 | 650000       |      8.5e+07  |
|   1400 |   56915 |      1.77068e+06 |          2.42264e+06 |     20000 |      1e+06   |      7e+07    |
|   1401 |   48035 |      3.0853e+06  |          3.83306e+06 |     20000 |      2.2e+06 |      1.5e+08  |


### Price_System

??? abstract "Column Metadata"
    ``` yaml
    1369:
      column_code: COL4
      type: category
      categories:
        0: Free_Price
        1: Subsidised_Price
    
    ```
#### Column Codes

| Years     | Price_System                         |
|:----------|:-------------------------------------|
| 1363-1368 |                                      |
| 1369-1373 | [COL4](/HBSIR/tables/raw/cloth#col4) |
| 1374-1401 |                                      |


#### Summary Statistics

**category data**

|   Year |   Free_Price |   nan |   Subsidised_Price |
|-------:|-------------:|------:|-------------------:|
|   1369 |        98.31 |  0.2  |               1.49 |
|   1370 |        99.45 |  0.1  |               0.45 |
|   1371 |        99.67 |  0.11 |               0.22 |
|   1372 |        99.71 |  0.12 |               0.17 |
|   1373 |        98.94 |  0.85 |               0.21 |


#### Categories

|    | 1369-1373        |
|---:|:-----------------|
|  0 | Free_Price       |
|  1 | Subsidised_Price |


### Amount

??? abstract "Column Metadata"
    ``` yaml
    1369:
      column_code: COL5
      type: float
    
    ```
#### Column Codes

| Years     | Amount                               |
|:----------|:-------------------------------------|
| 1363-1368 |                                      |
| 1369      | [COL5](/HBSIR/tables/raw/cloth#col5) |
| 1370-1401 |                                      |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1369 |   35276 |   6.29 |               161.12 |         1 |        2 |     25000 |


