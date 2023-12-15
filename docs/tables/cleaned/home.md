# home

## Old to New Titles

| Years     | ADDRESS   | COL1   | COL3             | COL4         | COL5        | COL6        |
|:----------|:----------|:-------|:-----------------|:-------------|:------------|:------------|
| 1363-1368 | ID        | Code   | Provision_Method | Expenditure  |             |             |
| 1369      | ID        | Code   | Provision_Method | Price_System | Amount      | Expenditure |
| 1370-1373 | ID        | Code   | Provision_Method | Price_System | Expenditure |             |
| 1374-1383 | ID        | Code   | Provision_Method | Expenditure  |             |             |


| Years     | ADDRESS   | DYCOL01   | DYCOL02          | DYCOL03          | DYCOL04     |
|:----------|:----------|:----------|:-----------------|:-----------------|:------------|
| 1384-1401 | ID        | Code      | Security_Deposit | Provision_Method | Expenditure |


## New to Old Titles

| Years     | ID      | Code    | Security_Deposit   | Provision_Method   | Expenditure   | Price_System   | Amount   |
|:----------|:--------|:--------|:-------------------|:-------------------|:--------------|:---------------|:---------|
| 1363-1368 | ADDRESS | COL1    |                    | COL3               | COL4          |                |          |
| 1369      | ADDRESS | COL1    |                    | COL3               | COL6          | COL4           | COL5     |
| 1370-1373 | ADDRESS | COL1    |                    | COL3               | COL5          | COL4           |          |
| 1374-1383 | ADDRESS | COL1    |                    | COL3               | COL4          |                |          |
| 1384-1401 | ADDRESS | DYCOL01 | DYCOL02            | DYCOL03            | DYCOL04       |                |          |


## Columns Details

### ID

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: ADDRESS
      type: UInt64
    
    ```
#### Column Codes

| Years     | ID                                        |
|:----------|:------------------------------------------|
| 1363-1401 | [ADDRESS](/HBSIR/tables/raw/home#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|-----------------:|------------:|
|   1363 |  105011 | 704122           |     502267           |  1001          |      1.03212e+06 | 1.23452e+06 |
|   1364 |   86711 | 629622           |     508933           |  1001          |      1.01201e+06 | 1.23442e+06 |
|   1365 |   17467 | 610272           |     526381           |  1001          |      1.002e+06   | 1.23422e+06 |
|   1366 |   18705 | 594505           |     523481           |  1001          | 233001           | 1.23421e+06 |
|   1367 |   27304 | 602979           |     521059           |  1001          | 233038           | 1.23428e+06 |
|   1368 |   37722 | 588504           |     515417           |  1001          | 232018           | 1.23428e+06 |
|   1369 |   57020 | 600996           |     510573           |  1001          |      1.00107e+06 | 1.23422e+06 |
|   1370 |   63056 | 600017           |     509440           |  1001          |      1.00105e+06 | 1.23422e+06 |
|   1371 |   60504 | 597029           |     508370           |  1001          | 234014           | 1.23422e+06 |
|   1372 |   40270 | 625846           |     509077           |  1001          |      1.00307e+06 | 1.23422e+06 |
|   1373 |   65382 | 722200           |     511009           |  1001          |      1.0421e+06  | 1.24404e+06 |
|   1374 |  123617 |      6.76036e+06 |          5.09974e+06 | 10001          |      1.03101e+07 | 1.24401e+07 |
|   1375 |   75902 | 611039           |     519119           |  1001          | 243045           | 1.24404e+06 |
|   1376 |   77940 | 608890           |     519128           |  1001          | 243055           | 1.25406e+06 |
|   1377 |   61337 |      5.85681e+07 |          5.16179e+07 | 11001          |      2.4041e+07  | 1.27074e+08 |
|   1378 |   99772 |      5.9134e+07  |          5.12154e+07 | 11001          |      2.5011e+07  | 1.27074e+08 |
|   1379 |   98895 |      5.71527e+07 |          5.0902e+07  | 11001          |      2.4011e+07  | 1.27074e+08 |
|   1380 |  100542 |      5.73471e+07 |          5.10999e+07 | 11001          |      2.4012e+07  | 1.27074e+08 |
|   1381 |  123064 |      5.95927e+07 |          5.11323e+07 | 11001          |      2.6011e+07  | 1.27074e+08 |
|   1382 |   89237 |      5.98937e+07 |          5.11265e+07 | 11001          |      2.50141e+07 | 1.27114e+08 |
|   1383 |   96406 |      6.05962e+07 |          5.11241e+07 | 11001          |      2.6022e+07  | 1.27114e+08 |
|   1384 |  104925 |      6.3125e+07  |          5.12588e+07 | 11001          |      2.81321e+07 | 1.29214e+08 |
|   1385 |  118899 |      6.04777e+07 |          5.14103e+07 | 11001          |      2.70821e+07 | 1.29214e+08 |
|   1386 |  119605 |      6.34366e+07 |          5.08735e+07 | 11001          |      2.90331e+07 | 1.29214e+08 |
|   1387 |  148744 |      1.64015e+09 |          5.04955e+08 |     1e+09      |      1.29764e+09 | 2.29786e+09 |
|   1388 |  136573 |      1.62711e+09 |          5.04437e+08 |     1e+09      |      1.28015e+09 | 2.29025e+09 |
|   1389 |  141226 |      1.64502e+09 |          5.03014e+08 |     1e+09      |      2e+09       | 2.29013e+09 |
|   1390 |  151724 |      1.65104e+09 |          5.04186e+08 |     1e+09      |      2.00002e+09 | 2.30013e+09 |
|   1391 |  150797 |      1.64885e+09 |          5.049e+08   |     1e+09      |      2e+09       | 2.30013e+09 |
|   1392 |  151348 |      1.63405e+10 |          5.04582e+09 |     1.0001e+10 |      1.29115e+10 | 2.30047e+10 |
|   1393 |  151657 |      1.62975e+10 |          5.04971e+09 |     1.0001e+10 |      1.29056e+10 | 2.30047e+10 |
|   1394 |  154268 |      1.62683e+10 |          5.04103e+09 |     1.0001e+10 |      1.29056e+10 | 2.30047e+10 |
|   1395 |  154517 |      1.62651e+10 |          5.04131e+09 |     1.0001e+10 |      1.29046e+10 | 2.30047e+10 |
|   1396 |  155522 |      1.6234e+10  |          5.03708e+09 |     1.0001e+10 |      1.29036e+10 | 2.30047e+10 |
|   1397 |  160332 |      1.5911e+10  |          5.01493e+09 |     1.0001e+10 |      1.27093e+10 | 2.30067e+10 |
|   1398 |  155017 |      1.59335e+10 |          5.01705e+09 |     1.0001e+10 |      1.27103e+10 | 2.30067e+10 |
|   1399 |  151683 |      1.59903e+10 |          5.01087e+09 |     1.0001e+10 |      1.27143e+10 | 2.30067e+10 |
|   1400 |  155386 |      1.59778e+10 |          5.00692e+09 |     1.0001e+10 |      1.27133e+10 | 2.30067e+10 |
|   1401 |  156872 |      1.59632e+10 |          5.00555e+09 |     1.0001e+10 |      1.27113e+10 | 2.30067e+10 |


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
    
    ```
#### Column Codes

| Years     | Code                                      |
|:----------|:------------------------------------------|
| 1363-1383 | [COL1](/HBSIR/tables/raw/home#col1)       |
| 1384-1401 | [DYCOL01](/HBSIR/tables/raw/home#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 |  105011 | 31866.5 |               449.22 |     31117 |    32120 |     32197 |
|   1364 |   86711 | 31809.8 |               480.28 |     31117 |    32120 |     39990 |
|   1365 |   17467 | 31800.1 |               481.74 |     31117 |    32120 |     32197 |
|   1366 |   18705 | 31817.8 |               475.57 |     31117 |    32120 |     32197 |
|   1367 |   27304 | 31822.5 |               474.42 |     31117 |    32120 |     32197 |
|   1368 |   37722 | 31822.3 |               475.74 |     31117 |    32120 |     39990 |
|   1369 |   57020 | 31804.8 |               482.08 |     31117 |    32120 |     32255 |
|   1370 |   63056 | 31830.8 |               470.22 |     31117 |    32120 |     33189 |
|   1371 |   60504 | 31819   |               474.62 |     31117 |    32120 |     32244 |
|   1372 |   40270 | 31806.4 |               476.91 |     31117 |    32120 |     32244 |
|   1373 |   65382 | 31815.1 |               471.4  |     31117 |    32120 |     32266 |
|   1374 |  123617 | 31823.2 |               469.01 |     31117 |    32120 |     32244 |
|   1375 |   75902 | 31829.7 |               465.29 |     31117 |    32120 |     32244 |
|   1376 |   77940 | 31833.2 |               462.65 |     31117 |    32120 |     32244 |
|   1377 |   61337 | 31830   |               463.06 |     31117 |    32120 |     32244 |
|   1378 |   99772 | 31843.3 |               458.14 |     31117 |    32120 |     32266 |
|   1379 |   98895 | 31844.5 |               457.39 |     31117 |    32120 |     32266 |
|   1380 |  100542 | 31848.3 |               454.82 |     31117 |    32120 |     32266 |
|   1381 |  123064 | 31855.9 |               450.26 |     31117 |    32120 |     32266 |
|   1382 |   89237 | 31857.2 |               448.93 |     31117 |    32120 |     32266 |
|   1383 |   96406 | 44109   |              1356.19 |     41111 |    45111 |     45414 |
|   1384 |  104925 | 44088.5 |              1359.73 |     41111 |    45111 |     45414 |
|   1385 |  118899 | 44072.7 |              1363.55 |     41111 |    45111 |     45414 |
|   1386 |  119605 | 44054.2 |              1372.41 |     41111 |    44418 |     45414 |
|   1387 |  148744 | 44042.1 |              1365.32 |     41111 |    44413 |     45414 |
|   1388 |  136573 | 44027.4 |              1367.56 |     41111 |    44411 |     45419 |
|   1389 |  141226 | 44010.6 |              1368.57 |     41111 |    44411 |     45414 |
|   1390 |  151724 | 44051.7 |              1341.21 |     41111 |    44411 |     45414 |
|   1391 |  150797 | 44056.7 |              1334.35 |     41111 |    44411 |     45414 |
|   1392 |  151348 | 44045.9 |              1340.05 |     41111 |    44312 |     45414 |
|   1393 |  151657 | 44051.1 |              1329.88 |     41111 |    44311 |     45414 |
|   1394 |  154268 | 44062.6 |              1318.15 |     41111 |    44311 |     45414 |
|   1395 |  154517 | 44061.4 |              1313.93 |     41111 |    44311 |     45414 |
|   1396 |  155522 | 44060.3 |              1306.67 |     41111 |    44311 |     45414 |
|   1397 |  160332 | 44048.3 |              1312.23 |     41111 |    44311 |     45414 |
|   1398 |  155017 | 44039.3 |              1310.68 |     41111 |    44311 |     45414 |
|   1399 |  151683 | 44034.4 |              1310.88 |     41111 |    44311 |     45414 |
|   1400 |  155386 | 44042.4 |              1305.75 |     41111 |    44311 |     45414 |
|   1401 |  156872 | 44047.4 |              1300.16 |     41111 |    44311 |     45414 |


### Security_Deposit

??? abstract "Column Metadata"
    ``` yaml
    1384:
      column_code: DYCOL02
      type: float
    
    ```
#### Column Codes

| Years     | Security_Deposit                          |
|:----------|:------------------------------------------|
| 1363-1383 |                                           |
| 1384-1401 | [DYCOL02](/HBSIR/tables/raw/home#dycol02) |


#### Summary Statistics

**numeric data**

|   Year |   Count |        Mean |   Standard Deviation |    Minimum |   Median |   Maximum |
|-------:|--------:|------------:|---------------------:|-----------:|---------:|----------:|
|   1384 |    2212 | 1.59614e+07 |          1.9655e+07  |   5000     | 1e+07    |   2.5e+08 |
|   1385 |    2503 | 1.86729e+07 |          2.53651e+07 |      1     | 1e+07    |   3.5e+08 |
|   1386 |    2737 | 2.27065e+07 |          3.23838e+07 |   1500     | 1e+07    |   6.5e+08 |
|   1387 |    3545 | 2.93628e+07 |          5.08962e+07 |      1     | 1.5e+07  |   2e+09   |
|   1388 |    3132 | 2.78778e+07 |          4.4196e+07  |      1     | 1.5e+07  |   1.4e+09 |
|   1389 |    3520 | 3.45354e+07 |          5.31677e+07 | 400000     | 2e+07    |   1.5e+09 |
|   1390 |    3628 | 4.02371e+07 |          5.01013e+07 |      5     | 2e+07    |   5.8e+08 |
|   1391 |    3512 | 4.84033e+07 |          6.60999e+07 |  20000     | 3e+07    |   1.5e+09 |
|   1392 |    3962 | 6.56312e+07 |          9.48748e+07 |  20000     | 4e+07    |   1.9e+09 |
|   1393 |    3760 | 7.8684e+07  |          1.3348e+08  |      1     | 4e+07    |   5e+09   |
|   1394 |    3609 | 9.12682e+07 |          1.26464e+08 |      0     | 5e+07    |   1.6e+09 |
|   1395 |    3692 | 1.07533e+08 |          1.66358e+08 | 130000     | 5e+07    |   3.5e+09 |
|   1396 |    3822 | 1.18252e+08 |          1.68101e+08 |      1     | 6e+07    |   2.5e+09 |
|   1397 |    4529 | 1.42431e+08 |          2.09164e+08 |      1     | 7.5e+07  |   4e+09   |
|   1398 |    4103 | 1.81707e+08 |          2.93969e+08 | 500000     | 1e+08    |   6.5e+09 |
|   1399 |    3948 | 2.36824e+08 |          3.33195e+08 | 300000     | 1.25e+08 |   7e+09   |
|   1400 |    3919 | 3.43947e+08 |          4.65096e+08 | 100000     | 2e+08    |   8e+09   |
|   1401 |    3969 | 5.57088e+08 |          7.33714e+08 |      5e+06 | 3e+08    |   9.5e+09 |


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
      column_code: DYCOL03
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
      column_code: DYCOL03
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

| Years     | Provision_Method                          |
|:----------|:------------------------------------------|
| 1363-1383 | [COL3](/HBSIR/tables/raw/home#col3)       |
| 1384-1401 | [DYCOL03](/HBSIR/tables/raw/home#dycol03) |


#### Summary Statistics

**category data**

|   Year | Purchase   | nan   |   Donation |   Instead_of_Private_Service |   Home_Production |   Instead_of_Public_Service |   Agricultural_Work |   Non_Agricultural_Work | Purchase_Subsidised_Price   | Purchase_Free_Price   | Instead_of_Cooperative_Service   |
|-------:|:-----------|:------|-----------:|-----------------------------:|------------------:|----------------------------:|--------------------:|------------------------:|:----------------------------|:----------------------|:---------------------------------|
|   1363 |            |       |       2.37 |                         0.13 |              4.36 |                        0.53 |                0.84 |                    0.04 | 61.38                       | 30.34                 |                                  |
|   1364 |            |       |       3.42 |                         0.21 |              4.59 |                        0.64 |                1.5  |                    0.08 | 51.6                        | 37.97                 |                                  |
|   1365 |            |       |       3.18 |                         0.15 |              4.85 |                        0.42 |                1.13 |                    0.06 | 49.99                       | 40.22                 |                                  |
|   1366 |            |       |       2.72 |                         0.14 |              4.87 |                        0.59 |                1.14 |                    0.05 | 50.32                       | 40.17                 |                                  |
|   1367 |            |       |       2.59 |                         0.12 |              4.83 |                        0.47 |                1.3  |                    0.06 | 49.87                       | 40.76                 |                                  |
|   1368 |            | 0.0   |       2.43 |                         0.14 |              3.14 |                        0.54 |                1.97 |                    0.06 | 50.06                       | 41.67                 |                                  |
|   1369 | 93.31      | 0.18  |       1.82 |                         0.12 |              2.44 |                        0.84 |                1.24 |                    0.06 |                             |                       |                                  |
|   1370 | 93.62      | 0.04  |       1.73 |                         0.14 |              2.22 |                        0.84 |                1.34 |                    0.07 |                             |                       |                                  |
|   1371 | 93.19      | 0.06  |       2.19 |                         0.2  |              2.17 |                        0.63 |                1.49 |                    0.07 |                             |                       |                                  |
|   1372 | 94.34      | 0.04  |       2.1  |                         0.15 |              2.14 |                        0.45 |                0.75 |                    0.02 |                             |                       |                                  |
|   1373 | 94.51      | 0.02  |       1.98 |                         0.14 |              1.77 |                        0.8  |                0.74 |                    0.03 |                             |                       |                                  |
|   1374 | 93.77      | 0.0   |       1.95 |                         0.15 |              2.56 |                        0.58 |                0.92 |                    0.07 |                             |                       |                                  |
|   1375 | 93.94      | 0.0   |       1.98 |                         0.21 |              2.44 |                        0.56 |                0.83 |                    0.05 |                             |                       |                                  |
|   1376 | 93.63      |       |       2.36 |                         0.17 |              2.46 |                        0.69 |                0.64 |                    0.04 |                             |                       |                                  |
|   1377 | 71.18      | 23.11 |       2.4  |                         0.15 |              1.89 |                        0.78 |                0.45 |                    0.04 |                             |                       |                                  |
|   1378 | 71.64      | 22.43 |       2.2  |                         0.18 |              2.32 |                        0.66 |                0.53 |                    0.04 |                             |                       |                                  |
|   1379 | 72.12      | 21.61 |       2.28 |                         0.2  |              2.54 |                        0.67 |                0.52 |                    0.04 |                             |                       | 0.01                             |
|   1380 | 73.2       | 21.3  |       1.97 |                         0.21 |              2.34 |                        0.58 |                0.36 |                    0.03 |                             |                       | 0.01                             |
|   1381 | 74.63      | 20.77 |       1.88 |                         0.2  |              1.75 |                        0.46 |                0.27 |                    0.03 |                             |                       | 0.01                             |
|   1382 | 74.68      | 20.49 |       2.1  |                         0.25 |              1.8  |                        0.48 |                0.16 |                    0.02 |                             |                       | 0.01                             |
|   1383 | 75.68      | 20.1  |       1.81 |                         0.24 |              1.39 |                        0.51 |                0.23 |                    0.03 |                             |                       | 0.01                             |
|   1384 | 75.81      | 19.99 |       1.82 |                         0.34 |              1.37 |                        0.49 |                0.15 |                    0.03 |                             |                       | 0.01                             |
|   1385 | 75.26      | 20.28 |       1.97 |                         0.37 |              1.47 |                        0.43 |                0.17 |                    0.03 |                             |                       | 0.01                             |
|   1386 | 75.55      | 20.1  |       2    |                         0.43 |              1.41 |                        0.39 |                0.09 |                    0.03 |                             |                       | 0.01                             |
|   1387 | 75.38      | 19.98 |       2.38 |                         0.34 |              1.43 |                        0.4  |                0.06 |                    0.02 |                             |                       | 0.01                             |
|   1388 | 74.69      | 20.8  |       2.53 |                         0.31 |              1.19 |                        0.39 |                0.07 |                    0.02 |                             |                       | 0.01                             |
|   1389 | 74.91      | 20.97 |       2.32 |                         0.28 |              1.07 |                        0.36 |                0.06 |                    0.01 |                             |                       | 0.01                             |
|   1390 | 76.67      | 19.86 |       1.9  |                         0.3  |              0.85 |                        0.32 |                0.05 |                    0.01 |                             |                       | 0.02                             |
|   1391 | 76.61      | 20.17 |       1.76 |                         0.27 |              0.85 |                        0.27 |                0.04 |                    0.01 |                             |                       | 0.02                             |
|   1392 | 77.21      | 19.46 |       2.24 |                         0.17 |              0.68 |                        0.22 |                0.02 |                    0.01 |                             |                       |                                  |
|   1393 | 77.2       | 19.64 |       2.23 |                         0.14 |              0.55 |                        0.19 |                0.02 |                    0.02 |                             |                       | 0.0                              |
|   1394 | 77.6       | 19.62 |       1.96 |                         0.14 |              0.48 |                        0.17 |                0.02 |                    0.01 |                             |                       | 0.0                              |
|   1395 | 77.75      | 19.52 |       1.88 |                         0.14 |              0.5  |                        0.2  |                0.02 |                    0.01 |                             |                       | 0.0                              |
|   1396 | 78.23      | 19.34 |       1.87 |                         0.14 |              0.25 |                        0.16 |                0    |                    0.01 |                             |                       | 0.0                              |
|   1397 | 78.82      | 18.51 |       2.05 |                         0.2  |              0.22 |                        0.19 |                0    |                    0    |                             |                       | 0.0                              |
|   1398 | 78.16      | 19.34 |       1.97 |                         0.16 |              0.19 |                        0.17 |                0    |                    0.01 |                             |                       | 0.0                              |
|   1399 | 78.04      | 19.45 |       1.97 |                         0.16 |              0.21 |                        0.15 |                0    |                    0.01 |                             |                       | 0.0                              |
|   1400 | 78.25      | 19.32 |       1.87 |                         0.19 |              0.22 |                        0.13 |                0    |                    0.01 |                             |                       | 0.0                              |
|   1401 | 78.34      | 19.33 |       1.84 |                         0.19 |              0.18 |                        0.12 |                0.01 |                    0.01 |                             |                       |                                  |


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
      column_code: DYCOL04
      type: float
    
    ```
#### Column Codes

| Years     | Expenditure                               |
|:----------|:------------------------------------------|
| 1363-1368 | [COL4](/HBSIR/tables/raw/home#col4)       |
| 1369      | [COL6](/HBSIR/tables/raw/home#col6)       |
| 1370-1373 | [COL5](/HBSIR/tables/raw/home#col5)       |
| 1374-1383 | [COL4](/HBSIR/tables/raw/home#col4)       |
| 1384-1401 | [DYCOL04](/HBSIR/tables/raw/home#dycol04) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |   Median |          Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------:|-----------------:|
|   1363 |  105011 |   3861.43        |       9261.95        |         6 |    450   | 190000           |
|   1364 |   86711 |   4971.58        |      10492.8         |        10 |    900   | 314620           |
|   1365 |   17467 |   5898.41        |      12398.5         |        15 |   1000   | 200000           |
|   1366 |   18705 |   6258.08        |      15550.6         |        20 |   1200   |      1.3e+06     |
|   1367 |   27304 |   7126.33        |      15007.8         |        11 |   1399.5 | 300000           |
|   1368 |   37722 |   7959.17        |      18762.8         |        10 |   1500   |      1e+06       |
|   1369 |   57020 |  10244.4         |      27263.1         |        16 |   1606.5 |      2e+06       |
|   1370 |   63050 |  13677           |     178382           |         6 |   2200   |      3.00003e+07 |
|   1371 |   60504 |  16651.8         |      40088.9         |         0 |   3570   |      4e+06       |
|   1372 |   40270 |  22633.9         |      54905.8         |        17 |   4200   |      2.5e+06     |
|   1373 |   65382 |  34344.7         |      83795.2         |        75 |   5000   |      7.5e+06     |
|   1374 |  123499 |  38679.4         |      91468.8         |         1 |   6500   |      5.5e+06     |
|   1375 |   75901 |  52651.8         |     146434           |         1 |   9000   |      9.6e+06     |
|   1376 |   77939 |  63641.4         |     161471           |         1 |  12000   |      7.5e+06     |
|   1377 |   61337 |  77681.7         |     198869           |         1 |  15000   |      1.5e+07     |
|   1378 |   99772 |  83204.1         |     194684           |         1 |  20000   |      8e+06       |
|   1379 |   98895 |  93435.8         |     229409           |         1 |  25000   |      1.6e+07     |
|   1380 |  100542 | 107735           |     261155           |         1 |  28000   |      1.5e+07     |
|   1381 |  123064 | 125131           |     333926           |         1 |  30000   |      2.25e+07    |
|   1382 |   89237 | 153151           |     454711           |       400 |  37500   |      5e+07       |
|   1383 |   96406 | 174765           |     508463           |       125 |  43000   |      8.1e+07     |
|   1384 |  104742 | 192372           |     426735           |       213 |  45000   |      1.5e+07     |
|   1385 |  118899 | 219743           |     546043           |       400 |  49000   |      3.5e+07     |
|   1386 |  119605 | 280016           |     704794           |         1 |  50000   |      3.5e+07     |
|   1387 |  148744 | 334949           |     801196           |       300 |  58000   |      6e+07       |
|   1388 |  136573 | 330017           |     679674           |       750 |  60000   |      3e+07       |
|   1389 |  141226 | 416925           |          1.42554e+06 |         0 |  78000   |      4.0007e+08  |
|   1390 |  151724 | 506839           |          1.18738e+06 |         0 | 150000   |      2e+08       |
|   1391 |  150797 | 586593           |          1.38385e+06 |      1000 | 150000   |      5.5e+07     |
|   1392 |  151348 | 679568           |          1.57652e+06 |      1930 | 170000   |      4.5e+07     |
|   1393 |  151657 | 800080           |          1.80239e+06 |      1000 | 205000   |      8e+07       |
|   1394 |  154268 | 879444           |          1.9704e+06  |      1500 | 240000   |      6.25e+07    |
|   1395 |  154517 | 958001           |          2.25612e+06 |      5000 | 259000   |      1.05e+08    |
|   1396 |  155522 |      1.03832e+06 |          2.44633e+06 |      4000 | 280000   |      1.1e+08     |
|   1397 |  160332 |      1.26183e+06 |          3.20283e+06 |      5000 | 300000   |      3e+08       |
|   1398 |  155017 |      1.61447e+06 |          4.17007e+06 |      4000 | 320000   |      2e+08       |
|   1399 |  151683 |      2.19349e+06 |          5.99911e+06 |      7000 | 390000   |      8e+08       |
|   1400 |  155386 |      3.20409e+06 |          8.19e+06    |      2000 | 420000   |      3e+08       |
|   1401 |  156872 |      5.00148e+06 |          1.29402e+07 |      4000 | 500000   |      5e+08       |


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

| Years     | Price_System                        |
|:----------|:------------------------------------|
| 1363-1368 |                                     |
| 1369-1373 | [COL4](/HBSIR/tables/raw/home#col4) |
| 1374-1401 |                                     |


#### Summary Statistics

**category data**

|   Year |   Free_Price |   Subsidised_Price |   nan |
|-------:|-------------:|-------------------:|------:|
|   1369 |        56.2  |              43.49 |  0.31 |
|   1370 |        57.16 |              42.76 |  0.08 |
|   1371 |        62.13 |              37.79 |  0.08 |
|   1372 |        61.51 |              38.45 |  0.04 |
|   1373 |        54.99 |              44.45 |  0.57 |


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

| Years     | Amount                              |
|:----------|:------------------------------------|
| 1363-1368 |                                     |
| 1369      | [COL5](/HBSIR/tables/raw/home#col5) |
| 1370-1401 |                                     |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1369 |   35119 | 229.82 |              1332.16 |         1 |       70 |    150200 |


