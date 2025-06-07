# transportation

## Old to New Titles

| Years     | ADDRESS   | COL1           | COL3             | COL4         | COL5        | COL6        |
|:----------|:----------|:---------------|:-----------------|:-------------|:------------|:------------|
| 1363-1368 | ID        | Commodity_Code | Provision_Method | Expenditure  |             |             |
| 1369      | ID        | Commodity_Code | Provision_Method | Price_System | Amount      | Expenditure |
| 1370-1373 | ID        | Commodity_Code | Provision_Method | Price_System | Expenditure |             |
| 1374-1383 | ID        | Commodity_Code | Provision_Method | Expenditure  |             |             |


| Years     | ADDRESS   | DYCOL01        | DYCOL02          | DYCOL03     |
|:----------|:----------|:---------------|:-----------------|:------------|
| 1384-1402 | ID        | Commodity_Code | Provision_Method | Expenditure |


## New to Old Titles

| Years     | ID      | Commodity_Code   | Provision_Method   | Expenditure   | Price_System   | Amount   |
|:----------|:--------|:-----------------|:-------------------|:--------------|:---------------|:---------|
| 1363-1368 | ADDRESS | COL1             | COL3               | COL4          |                |          |
| 1369      | ADDRESS | COL1             | COL3               | COL6          | COL4           | COL5     |
| 1370-1373 | ADDRESS | COL1             | COL3               | COL5          | COL4           |          |
| 1374-1383 | ADDRESS | COL1             | COL3               | COL4          |                |          |
| 1384-1402 | ADDRESS | DYCOL01          | DYCOL02            | DYCOL03       |                |          |


## Columns Details

### ID

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: ADDRESS
      type: UInt64
    
    ```
#### Column Codes

| Years     | ID                                                  |
|:----------|:----------------------------------------------------|
| 1363-1402 | [ADDRESS](/HBSIR/tables/raw/transportation#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |      Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|------------:|------------:|
|   1363 |   53298 | 758866           |     491969           |  1001          | 1.04306e+06 | 1.23452e+06 |
|   1364 |   52148 | 714862           |     501111           |  1001          | 1.03218e+06 | 1.23442e+06 |
|   1365 |   10110 | 697273           |     522654           |  1001          | 1.03208e+06 | 1.23422e+06 |
|   1366 |   10964 | 686781           |     519514           |  1002          | 1.03204e+06 | 1.23421e+06 |
|   1367 |   15711 | 694762           |     515449           |  1002          | 1.03306e+06 | 1.23428e+06 |
|   1368 |   22968 | 669983           |     513283           |  1001          | 1.02202e+06 | 1.23428e+06 |
|   1369 |   36528 | 650705           |     511907           |  1001          | 1.02109e+06 | 1.23422e+06 |
|   1370 |   38134 | 647460           |     509481           |  1001          | 1.01404e+06 | 1.23422e+06 |
|   1371 |   39134 | 651054           |     508795           |  1001          | 1.01401e+06 | 1.23422e+06 |
|   1372 |   26970 | 682962           |     506578           |  1001          | 1.02203e+06 | 1.23422e+06 |
|   1373 |   47605 | 791039           |     494615           |  1001          | 1.06405e+06 | 1.24404e+06 |
|   1374 |   88377 |      7.442e+06   |          5.02835e+06 | 10001          | 1.06101e+07 | 1.24401e+07 |
|   1375 |   54891 | 691799           |     519943           |  1001          | 1.03309e+06 | 1.24404e+06 |
|   1376 |   55774 | 677972           |     521726           |  1001          | 1.03202e+06 | 1.25406e+06 |
|   1377 |   44108 |      6.62006e+07 |          5.20521e+07 | 11001          | 1.03021e+08 | 1.27074e+08 |
|   1378 |   71224 |      6.51245e+07 |          5.17462e+07 | 11001          | 1.01031e+08 | 1.27074e+08 |
|   1379 |   70993 |      6.32726e+07 |          5.15846e+07 | 11001          | 2.70721e+07 | 1.27074e+08 |
|   1380 |   75455 |      6.34632e+07 |          5.16571e+07 | 11001          | 2.70731e+07 | 1.27074e+08 |
|   1381 |   98434 |      6.44208e+07 |          5.14531e+07 | 11001          | 1.00011e+08 | 1.27074e+08 |
|   1382 |   77208 |      6.48165e+07 |          5.1389e+07  | 11001          | 1.00012e+08 | 1.27114e+08 |
|   1383 |   66296 |      6.47603e+07 |          5.13955e+07 | 11001          | 1.00012e+08 | 1.27114e+08 |
|   1384 |   73454 |      6.48239e+07 |          5.12918e+07 | 11001          | 1.00012e+08 | 1.29214e+08 |
|   1385 |   88325 |      6.29534e+07 |          5.16724e+07 | 11001          | 2.81331e+07 | 1.29214e+08 |
|   1386 |   91498 |      6.57589e+07 |          5.08982e+07 | 11001          | 1.00014e+08 | 1.29214e+08 |
|   1387 |  109349 |      1.62456e+09 |          5.03767e+08 |     1e+09      | 1.28741e+09 | 2.29786e+09 |
|   1388 |   97814 |      1.61471e+09 |          5.04195e+08 |     1e+09      | 1.28004e+09 | 2.29025e+09 |
|   1389 |  103325 |      1.62215e+09 |          5.03902e+08 |     1e+09      | 1.28007e+09 | 2.29013e+09 |
|   1390 |  100605 |      1.62709e+09 |          5.03653e+08 |     1e+09      | 1.29001e+09 | 2.30013e+09 |
|   1391 |   99877 |      1.62837e+09 |          5.0331e+08  |     1e+09      | 1.29005e+09 | 2.30013e+09 |
|   1392 |   93801 |      1.62081e+10 |          5.01971e+09 |     1.0001e+10 | 1.29016e+10 | 2.30047e+10 |
|   1393 |   93213 |      1.62372e+10 |          5.02791e+09 |     1.0001e+10 | 1.29016e+10 | 2.30047e+10 |
|   1394 |   90812 |      1.62399e+10 |          5.0275e+09  |     1.0001e+10 | 1.29016e+10 | 2.30047e+10 |
|   1395 |   89413 |      1.62152e+10 |          5.02766e+09 |     1.0001e+10 | 1.29016e+10 | 2.30047e+10 |
|   1396 |   87619 |      1.62248e+10 |          5.02268e+09 |     1.0001e+10 | 1.29016e+10 | 2.30047e+10 |
|   1397 |   87364 |      1.59522e+10 |          5.00921e+09 |     1.0001e+10 | 1.27093e+10 | 2.30067e+10 |
|   1398 |   80838 |      1.59059e+10 |          5.00668e+09 |     1.0001e+10 | 1.27083e+10 | 2.30067e+10 |
|   1399 |   69453 |      1.60697e+10 |          5.00969e+09 |     1.0001e+10 | 1.28023e+10 | 2.30067e+10 |
|   1400 |   73041 |      1.60025e+10 |          5.00251e+09 |     1.0001e+10 | 1.27133e+10 | 2.30067e+10 |
|   1401 |   73898 |      1.59336e+10 |          4.99511e+09 |     1.0001e+10 | 1.27113e+10 | 2.30067e+10 |
|   1402 |   75113 |      1.59302e+10 |          5.00326e+09 |     1.0001e+10 | 1.27143e+10 | 2.30067e+10 |


### Commodity_Code

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
    1402:
      column_code: DYCOL01
      type: UInt32
    
    ```
#### Column Codes

| Years     | Commodity_Code                                      |
|:----------|:----------------------------------------------------|
| 1363-1383 | [COL1](/HBSIR/tables/raw/transportation#col1)       |
| 1384-1402 | [DYCOL01](/HBSIR/tables/raw/transportation#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 |   53298 | 61686   |               180.84 |     61515 |    61639 |     62154 |
|   1364 |   52148 | 61668.7 |               164.21 |     61515 |    61639 |     62154 |
|   1365 |   10110 | 61657.1 |               146.15 |     61515 |    61639 |     62132 |
|   1366 |   10964 | 61673.2 |               166.99 |     61515 |    61639 |     62154 |
|   1367 |   15711 | 61670.5 |               163.17 |     61515 |    61639 |     62154 |
|   1368 |   22968 | 61675.4 |               163.23 |     61515 |    61639 |     62154 |
|   1369 |   36528 | 61666.9 |               155.47 |     61515 |    61639 |     62165 |
|   1370 |   38134 | 61701.7 |               156.07 |     61140 |    61719 |     62165 |
|   1371 |   39134 | 61699.5 |               152.7  |     61129 |    61719 |     62165 |
|   1372 |   26970 | 61700.7 |               154.31 |     61515 |    61719 |     62165 |
|   1373 |   47605 | 61715.2 |               169.72 |     61515 |    61719 |     62165 |
|   1374 |   88377 | 61720.3 |               179.18 |     61515 |    61719 |     62165 |
|   1375 |   54891 | 61722.5 |               176.82 |     61515 |    61719 |     62165 |
|   1376 |   55774 | 61729.9 |               181.18 |     61515 |    61719 |     62165 |
|   1377 |   44108 | 61733.4 |               188.17 |     61515 |    61719 |     62187 |
|   1378 |   71224 | 61743.2 |               198.81 |     61515 |    61719 |     62198 |
|   1379 |   70993 | 61749.5 |               202.4  |     61515 |    61719 |     62198 |
|   1380 |   75455 | 61754.6 |               206.73 |     61515 |    61719 |     62198 |
|   1381 |   98434 | 61764.9 |               211.43 |     61515 |    61719 |     62198 |
|   1382 |   77208 | 61765.6 |               215.74 |     61515 |    61719 |     62198 |
|   1383 |   66296 | 72926.8 |               444.23 |     72211 |    73213 |     73613 |
|   1384 |   73454 | 72899.7 |               454.75 |     72211 |    73213 |     73613 |
|   1385 |   88325 | 72906.4 |               452.46 |     72211 |    73214 |     73612 |
|   1386 |   91498 | 72908   |               452.13 |     72211 |    73213 |     73613 |
|   1387 |  109349 | 72892.9 |               457.88 |     72211 |    73213 |     73613 |
|   1388 |   97814 | 72874.9 |               464.56 |     72211 |    73213 |     73612 |
|   1389 |  103325 | 72871.8 |               466.24 |     72211 |    73213 |     73611 |
|   1390 |  100605 | 72866.2 |               467.9  |     72211 |    73213 |     73611 |
|   1391 |   99877 | 72856.8 |               469.68 |     72211 |    73213 |     73611 |
|   1392 |   93801 | 72834.8 |               476    |     72211 |    73213 |     73611 |
|   1393 |   93213 | 72835.9 |               475.78 |     72211 |    73213 |     73611 |
|   1394 |   90812 | 72825.2 |               478.36 |     72211 |    73213 |     73611 |
|   1395 |   89413 | 72812.4 |               480.46 |     72211 |    73213 |     73611 |
|   1396 |   87619 | 72803   |               483.16 |     72211 |    73213 |     73611 |
|   1397 |   87364 | 72786.1 |               485.92 |     72211 |    73212 |     73611 |
|   1398 |   80838 | 72776.9 |               487.41 |     72211 |    73212 |     73611 |
|   1399 |   69453 | 72727.5 |               491.53 |     72211 |    73113 |     73611 |
|   1400 |   73041 | 72728.8 |               490.63 |     72211 |    73113 |     73611 |
|   1401 |   73898 | 72728.6 |               490.18 |     72211 |    73113 |     73611 |
|   1402 |   75113 | 72736.4 |               489.49 |     72211 |    73211 |     73511 |


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
    1402:
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

| Years     | Provision_Method                                    |
|:----------|:----------------------------------------------------|
| 1363-1383 | [COL3](/HBSIR/tables/raw/transportation#col3)       |
| 1384-1402 | [DYCOL02](/HBSIR/tables/raw/transportation#dycol02) |


#### Summary Statistics

**category data**

|   Year | Purchase   | Instead_of_Private_Service   |   Non_Agricultural_Work |   Donation |   Instead_of_Public_Service | Purchase_Free_Price   | Purchase_Subsidised_Price   | Home_Production   | Agricultural_Work   | nan   | Instead_of_Cooperative_Service   |
|-------:|:-----------|:-----------------------------|------------------------:|-----------:|----------------------------:|:----------------------|:----------------------------|:------------------|:--------------------|:------|:---------------------------------|
|   1363 |            | 0.06                         |                    0.25 |       0.02 |                        0.43 | 55.28                 | 43.86                       | 0.1               | 0.01                |       |                                  |
|   1364 |            | 0.02                         |                    0.29 |       0.03 |                        0.42 | 58.4                  | 40.68                       | 0.15              | 0.01                |       |                                  |
|   1365 |            | 0.04                         |                    0.41 |       0.02 |                        0.4  | 52.97                 | 46.12                       | 0.05              |                     |       |                                  |
|   1366 |            |                              |                    0.39 |       0.05 |                        0.23 | 59.88                 | 39.37                       | 0.07              | 0.02                |       |                                  |
|   1367 |            | 0.03                         |                    0.23 |       0.04 |                        0.15 | 60.42                 | 39.09                       | 0.04              | 0.01                |       |                                  |
|   1368 |            | 0.02                         |                    0.31 |       0.02 |                        0.13 | 59.91                 | 39.57                       | 0.04              | 0.01                |       |                                  |
|   1369 | 99.39      | 0.02                         |                    0.31 |       0.01 |                        0.07 |                       |                             | 0.04              | 0.02                | 0.13  |                                  |
|   1370 | 99.42      | 0.04                         |                    0.33 |       0.03 |                        0.09 |                       |                             | 0.03              | 0.02                | 0.04  |                                  |
|   1371 | 99.42      | 0.04                         |                    0.34 |       0.03 |                        0.06 |                       |                             | 0.05              | 0.01                | 0.03  |                                  |
|   1372 | 99.42      | 0.05                         |                    0.36 |       0.03 |                        0.09 |                       |                             | 0.03              | 0.01                | 0.01  |                                  |
|   1373 | 99.22      | 0.03                         |                    0.49 |       0.02 |                        0.15 |                       |                             | 0.05              | 0.01                | 0.03  |                                  |
|   1374 | 99.02      | 0.08                         |                    0.5  |       0.02 |                        0.31 |                       |                             | 0.05              | 0.01                | 0.0   |                                  |
|   1375 | 98.44      | 0.17                         |                    0.65 |       0.02 |                        0.67 |                       |                             | 0.03              | 0.01                |       |                                  |
|   1376 | 98.02      | 0.27                         |                    0.77 |       0.04 |                        0.86 |                       |                             | 0.01              | 0.02                |       |                                  |
|   1377 | 98.15      | 0.21                         |                    0.8  |       0.03 |                        0.76 |                       |                             | 0.01              | 0.03                |       |                                  |
|   1378 | 98.46      | 0.2                          |                    0.67 |       0.03 |                        0.6  |                       |                             | 0.02              | 0.03                |       |                                  |
|   1379 | 98.59      | 0.23                         |                    0.61 |       0.01 |                        0.49 |                       |                             | 0.04              | 0.02                |       |                                  |
|   1380 | 98.46      | 0.31                         |                    0.64 |       0.03 |                        0.52 |                       |                             | 0.02              | 0.01                |       | 0.01                             |
|   1381 | 98.94      | 0.18                         |                    0.51 |       0.04 |                        0.29 |                       |                             | 0.03              | 0.01                |       | 0.01                             |
|   1382 | 98.77      | 0.25                         |                    0.64 |       0.01 |                        0.28 |                       |                             | 0.04              | 0.01                |       |                                  |
|   1383 | 98.89      | 0.25                         |                    0.54 |       0.09 |                        0.13 |                       |                             | 0.04              | 0.05                | 0.0   | 0.0                              |
|   1384 | 98.85      | 0.23                         |                    0.61 |       0.05 |                        0.21 |                       |                             | 0.04              | 0.01                |       | 0.0                              |
|   1385 | 99.16      | 0.17                         |                    0.46 |       0.05 |                        0.15 |                       |                             | 0.0               | 0.01                |       | 0.0                              |
|   1386 | 99.12      | 0.21                         |                    0.47 |       0.04 |                        0.14 |                       |                             | 0.0               | 0.01                |       |                                  |
|   1387 | 99.26      | 0.22                         |                    0.37 |       0.04 |                        0.11 |                       |                             |                   | 0.0                 |       | 0.0                              |
|   1388 | 99.34      | 0.22                         |                    0.29 |       0.06 |                        0.09 |                       |                             |                   | 0.0                 |       | 0.0                              |
|   1389 | 99.46      | 0.17                         |                    0.26 |       0.04 |                        0.07 |                       |                             |                   | 0.0                 |       |                                  |
|   1390 | 99.53      | 0.13                         |                    0.27 |       0.03 |                        0.04 |                       |                             | 0.01              |                     |       | 0.0                              |
|   1391 | 99.55      | 0.15                         |                    0.22 |       0.03 |                        0.05 |                       |                             | 0.01              | 0.0                 |       |                                  |
|   1392 | 99.51      | 0.15                         |                    0.29 |       0.03 |                        0.02 |                       |                             | 0.01              |                     |       |                                  |
|   1393 | 99.55      | 0.13                         |                    0.27 |       0.02 |                        0.03 |                       |                             | 0.0               | 0.0                 |       |                                  |
|   1394 | 99.58      | 0.14                         |                    0.24 |       0.02 |                        0.02 |                       |                             |                   | 0.0                 |       |                                  |
|   1395 | 99.64      | 0.12                         |                    0.19 |       0.02 |                        0.03 |                       |                             |                   | 0.0                 |       | 0.0                              |
|   1396 | 99.72      | 0.12                         |                    0.12 |       0.01 |                        0.01 |                       |                             | 0.0               | 0.0                 |       |                                  |
|   1397 | 99.7       | 0.15                         |                    0.12 |       0.01 |                        0.02 |                       |                             |                   | 0.01                |       |                                  |
|   1398 | 99.63      | 0.13                         |                    0.16 |       0.01 |                        0.02 |                       |                             | 0.01              | 0.02                |       |                                  |
|   1399 | 99.53      | 0.17                         |                    0.23 |       0.01 |                        0.01 |                       |                             | 0.02              | 0.02                |       |                                  |
|   1400 | 99.52      | 0.2                          |                    0.22 |       0.02 |                        0.01 |                       |                             | 0.0               | 0.02                |       |                                  |
|   1401 | 99.66      | 0.18                         |                    0.11 |       0.02 |                        0.01 |                       |                             | 0.0               | 0.01                |       |                                  |
|   1402 | 99.7       | 0.2                          |                    0.07 |       0.02 |                        0    |                       |                             |                   |                     |       |                                  |


#### Categories

|    | 1363-1368                  | 1369-1373                  | 1374-1378                  | 1379-1382                      | 1383-1400                      | 1401-1402                      |
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
    1402:
      column_code: DYCOL03
      type: float
    
    ```
#### Column Codes

| Years     | Expenditure                                         |
|:----------|:----------------------------------------------------|
| 1363-1368 | [COL4](/HBSIR/tables/raw/transportation#col4)       |
| 1369      | [COL6](/HBSIR/tables/raw/transportation#col6)       |
| 1370-1373 | [COL5](/HBSIR/tables/raw/transportation#col5)       |
| 1374-1383 | [COL4](/HBSIR/tables/raw/transportation#col4)       |
| 1384-1402 | [DYCOL03](/HBSIR/tables/raw/transportation#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |       Median |        Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|-------------:|---------------:|
|   1363 |   53298 |   1471.4         |       6236.48        |         2 |    600       | 808000         |
|   1364 |   52148 |   1572.66        |       5420.08        |         2 |    600       | 600000         |
|   1365 |   10110 |   1766.86        |       8695.13        |         4 |    700       | 700000         |
|   1366 |   10964 |   1883.6         |       4596.64        |         4 |    800       | 210000         |
|   1367 |   15711 |   2123.83        |       8271.23        |         2 |    900       | 800000         |
|   1368 |   22968 |   2154.17        |       5043.54        |         4 |   1000       | 200000         |
|   1369 |   36528 |   2695.09        |       7798.58        |         2 |   1050       | 513000         |
|   1370 |   38132 |   3408.9         |      15836.1         |         5 |   1500       |      2e+06     |
|   1371 |   39134 |   4064.53        |      10157.2         |        10 |   2000       | 580000         |
|   1372 |   26970 |   4948.24        |      10448.3         |        10 |   2200       | 410000         |
|   1373 |   47605 |   7568.68        |      32196           |        10 |   3000       |      5e+06     |
|   1374 |   88361 |  11003.6         |      30716           |        20 |   4800       |      2.67e+06  |
|   1375 |   54891 |  13822.1         |      37673.5         |        25 |   6000       |      2.75e+06  |
|   1376 |   55774 |  16792.8         |      72181.9         |        50 |   8000       |      1.44e+07  |
|   1377 |   44108 |  21072.3         |      57625.6         |        50 |  10000       |      7.5e+06   |
|   1378 |   71224 |  25910.5         |      87102.9         |         4 |  12000       |      1.6e+07   |
|   1379 |   70993 |  30225.7         |      82916.9         |        40 |  15000       |      8.4e+06   |
|   1380 |   75455 |  34455.9         |      76544.1         |       100 |  16800       |      1.007e+07 |
|   1381 |   98434 |  41001.2         |     106794           |        50 |  20000       |      2e+07     |
|   1382 |   77208 |  48281           |     107618           |       100 |  25000       |      1.834e+07 |
|   1383 |   66296 |  48917.3         |     106637           |         0 |  24000       |      9e+06     |
|   1384 |   73248 |  56443.6         |     137548           |       200 |  28000       |      1.2e+07   |
|   1385 |   88325 |  57433.3         |     125693           |         0 |  30000       |      1e+07     |
|   1386 |   91498 |  65460           |     159470           |       300 |  30000       |      2e+07     |
|   1387 |  109349 |  78924.3         |     189832           |       500 |  40000       |      3.12e+07  |
|   1388 |   97814 |  88065.5         |     194657           |       750 |  45000       |      2.4e+07   |
|   1389 |  103325 | 112180           |     215939           |       500 |  50000       |      1.2e+07   |
|   1390 |  100604 | 164805           |     319376           |      1000 |  92000       |      4e+07     |
|   1391 |   99877 | 190625           |     337141           |      1500 | 100000       |      4e+07     |
|   1392 |   93800 | 237928           |     403039           |      2000 | 150000       |      4.5e+07   |
|   1393 |   93213 | 292820           |     511444           |      2000 | 150000       |      5e+07     |
|   1394 |   90812 | 326568           |     555018           |      5000 | 200000       |      6e+07     |
|   1395 |   89413 | 362367           |     587817           |      5000 | 200000       |      4e+07     |
|   1396 |   87619 | 402257           |     576571           |      4950 | 210000       |      2.6e+07   |
|   1397 |   87364 | 497181           |     990084           |      5000 | 300000       |      1.5e+08   |
|   1398 |   80838 | 619608           |     985716           |      4000 | 300000       |      8.5e+07   |
|   1399 |   69453 | 832141           |          1.68705e+06 |     10000 | 500000       |      3.366e+08 |
|   1400 |   73041 |      1.09084e+06 |          1.71721e+06 |     16000 | 600000       |      1.5e+08   |
|   1401 |   73898 |      1.59387e+06 |          2.78919e+06 |     14000 | 900000       |      1.5e+08   |
|   1402 |   75113 |      2.06034e+06 |          3.99708e+06 |     15000 |      1.2e+06 |      5.6e+08   |


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

| Years     | Price_System                                  |
|:----------|:----------------------------------------------|
| 1363-1368 |                                               |
| 1369-1373 | [COL4](/HBSIR/tables/raw/transportation#col4) |
| 1374-1402 |                                               |


#### Summary Statistics

**category data**

|   Year |   Free_Price |   Subsidised_Price |   nan |
|-------:|-------------:|-------------------:|------:|
|   1369 |        74.31 |              25.5  |  0.19 |
|   1370 |        74.8  |              25.13 |  0.07 |
|   1371 |        75.1  |              24.87 |  0.04 |
|   1372 |        70.85 |              29.13 |  0.03 |
|   1373 |        62.51 |              36.93 |  0.56 |


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

| Years     | Amount                                        |
|:----------|:----------------------------------------------|
| 1363-1368 |                                               |
| 1369      | [COL5](/HBSIR/tables/raw/transportation#col5) |
| 1370-1402 |                                               |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1369 |    5727 | 209.29 |              1018.32 |         1 |       30 |     43557 |


