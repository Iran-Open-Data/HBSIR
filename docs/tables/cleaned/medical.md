# medical

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

| Years     | ID                                           |
|:----------|:---------------------------------------------|
| 1363-1402 | [ADDRESS](/HBSIR/tables/raw/medical#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |      Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|------------:|------------:|
|   1363 |   55723 | 740470           |     497369           |  1001          | 1.04215e+06 | 1.23452e+06 |
|   1364 |   56403 | 698408           |     504307           |  1001          | 1.0321e+06  | 1.23442e+06 |
|   1365 |    9622 | 683182           |     527306           |  1003          | 1.03202e+06 | 1.23422e+06 |
|   1366 |   11429 | 658358           |     523359           |  1002          | 1.02401e+06 | 1.23421e+06 |
|   1367 |   15899 | 656184           |     519148           |  1004          | 1.02401e+06 | 1.23428e+06 |
|   1368 |   25651 | 669459           |     509815           |  1001          | 1.02202e+06 | 1.23428e+06 |
|   1369 |   37913 | 654016           |     509644           |  1001          | 1.01411e+06 | 1.23422e+06 |
|   1370 |   37096 | 652451           |     507619           |  1001          | 1.01403e+06 | 1.23422e+06 |
|   1371 |   36535 | 659351           |     505846           |  1002          | 1.021e+06   | 1.23422e+06 |
|   1372 |   24384 | 697908           |     500636           |  1001          | 1.02208e+06 | 1.23422e+06 |
|   1373 |   40926 | 798106           |     490611           |  1002          | 1.07102e+06 | 1.24404e+06 |
|   1374 |   78103 |      7.53344e+06 |          4.9885e+06  | 10004          | 1.06202e+07 | 1.24401e+07 |
|   1375 |   45560 | 681629           |     518074           |  1002          | 1.03208e+06 | 1.24404e+06 |
|   1376 |   46928 | 681053           |     517827           |  1002          | 1.03202e+06 | 1.25406e+06 |
|   1377 |   36749 |      6.72473e+07 |          5.16185e+07 | 11001          | 1.03031e+08 | 1.27074e+08 |
|   1378 |   61686 |      6.73641e+07 |          5.14909e+07 | 11001          | 1.02063e+08 | 1.27074e+08 |
|   1379 |   60174 |      6.4601e+07  |          5.14832e+07 | 11002          | 1.00061e+08 | 1.27074e+08 |
|   1380 |   60967 |      6.45408e+07 |          5.16196e+07 | 11004          | 1.00061e+08 | 1.27074e+08 |
|   1381 |   86185 |      6.68339e+07 |          5.13713e+07 | 11001          | 1.01081e+08 | 1.27074e+08 |
|   1382 |   64678 |      6.77158e+07 |          5.13984e+07 | 11001          | 1.02074e+08 | 1.27114e+08 |
|   1383 |   55706 |      6.26388e+07 |          5.14507e+07 | 11001          | 2.7034e+07  | 1.27114e+08 |
|   1384 |   59858 |      6.27754e+07 |          5.12011e+07 | 11001          | 2.71141e+07 | 1.29214e+08 |
|   1385 |   65024 |      5.91264e+07 |          5.14441e+07 | 11003          | 2.60321e+07 | 1.29214e+08 |
|   1386 |   62517 |      6.21465e+07 |          5.07234e+07 | 11001          | 2.82541e+07 | 1.29214e+08 |
|   1387 |   76921 |      1.63836e+09 |          5.05501e+08 |     1e+09      | 1.29763e+09 | 2.29786e+09 |
|   1388 |   75327 |      1.61598e+09 |          5.03686e+08 |     1e+09      | 1.28008e+09 | 2.29025e+09 |
|   1389 |   76201 |      1.62807e+09 |          5.03804e+08 |     1e+09      | 1.29006e+09 | 2.29013e+09 |
|   1390 |   71223 |      1.64591e+09 |          5.04376e+08 |     1e+09      | 2.00006e+09 | 2.30013e+09 |
|   1391 |   71346 |      1.64773e+09 |          5.04606e+08 |     1e+09      | 2.00006e+09 | 2.30013e+09 |
|   1392 |   69561 |      1.63643e+10 |          5.06079e+09 |     1.0001e+10 | 1.30016e+10 | 2.30047e+10 |
|   1393 |   68217 |      1.64347e+10 |          5.0468e+09  |     1.0001e+10 | 1.30017e+10 | 2.30047e+10 |
|   1394 |   69161 |      1.65106e+10 |          5.0589e+09  |     1.0001e+10 | 2.0003e+10  | 2.30047e+10 |
|   1395 |   62074 |      1.6462e+10  |          5.0378e+09  |     1.0001e+10 | 1.30017e+10 | 2.30047e+10 |
|   1396 |   66883 |      1.6435e+10  |          5.03674e+09 |     1.0001e+10 | 1.30017e+10 | 2.30047e+10 |
|   1397 |   67540 |      1.62625e+10 |          5.02476e+09 |     1.0001e+10 | 1.29014e+10 | 2.30067e+10 |
|   1398 |   65033 |      1.62074e+10 |          5.02558e+09 |     1.0001e+10 | 1.28044e+10 | 2.30067e+10 |
|   1399 |   62951 |      1.60766e+10 |          5.01279e+09 |     1.0001e+10 | 1.27133e+10 | 2.30067e+10 |
|   1400 |   63546 |      1.60745e+10 |          5.00598e+09 |     1.0001e+10 | 1.27123e+10 | 2.30067e+10 |
|   1401 |   59386 |      1.62647e+10 |          5.02542e+09 |     1.0001e+10 | 1.29014e+10 | 2.30067e+10 |
|   1402 |   58985 |      1.62793e+10 |          5.03229e+09 |     1.0001e+10 | 1.28074e+10 | 2.30067e+10 |


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

| Years     | Commodity_Code                               |
|:----------|:---------------------------------------------|
| 1363-1383 | [COL1](/HBSIR/tables/raw/medical#col1)       |
| 1384-1402 | [DYCOL01](/HBSIR/tables/raw/medical#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 |   55723 | 51397.5 |               323.09 |     51114 |    51318 |     52139 |
|   1364 |   56403 | 51394.5 |               323.39 |     51114 |    51318 |     59998 |
|   1365 |    9622 | 51410.7 |               330.57 |     51114 |    51318 |     52128 |
|   1366 |   11429 | 51401   |               320.1  |     51114 |    51318 |     52139 |
|   1367 |   15899 | 51395.3 |               326.83 |     51114 |    51318 |     52139 |
|   1368 |   25651 | 51406.9 |               336.87 |     51114 |    51318 |     52139 |
|   1369 |   37913 | 51385.3 |               316.74 |     51114 |    51318 |     52172 |
|   1370 |   37096 | 51375.2 |               319.64 |     51114 |    51318 |     52140 |
|   1371 |   36535 | 51386.1 |               328.1  |     51114 |    51318 |     52139 |
|   1372 |   24384 | 51394.4 |               339.39 |     51114 |    51318 |     52139 |
|   1373 |   40926 | 51416.6 |               355.12 |     51114 |    51318 |     52172 |
|   1374 |   78103 | 51431.9 |               360.53 |     51114 |    51329 |     52139 |
|   1375 |   45560 | 51422.2 |               353.49 |     51114 |    51329 |     52140 |
|   1376 |   46928 | 51438.3 |               363.08 |     51114 |    51329 |     52140 |
|   1377 |   36749 | 51433   |               359.45 |     51114 |    51329 |     52140 |
|   1378 |   61686 | 51478.7 |               392.97 |     51114 |    51318 |     52162 |
|   1379 |   60174 | 51474.1 |               391.87 |     51114 |    51318 |     52162 |
|   1380 |   60967 | 51467.1 |               390.35 |     51114 |    51318 |     52162 |
|   1381 |   86185 | 51468.2 |               389.61 |     51114 |    51329 |     52173 |
|   1382 |   64678 | 51473.8 |               391.27 |     51114 |    51329 |     52173 |
|   1383 |   55706 | 61848.3 |               686.63 |     61111 |    62111 |     63445 |
|   1384 |   59858 | 61856.3 |               678.98 |     61111 |    62111 |     64111 |
|   1385 |   65024 | 61868.5 |               682.5  |     61111 |    62111 |     64111 |
|   1386 |   62517 | 61834.4 |               642.98 |     61111 |    62111 |     64111 |
|   1387 |   76921 | 61854.9 |               668.76 |     61111 |    62111 |     64111 |
|   1388 |   75327 | 61846.1 |               649.96 |     61111 |    62111 |     64111 |
|   1389 |   76201 | 61837.3 |               655.28 |     61111 |    62111 |     64111 |
|   1390 |   71223 | 61782.7 |               620.31 |     61111 |    62111 |     64111 |
|   1391 |   71346 | 61786.4 |               632.6  |     61111 |    62111 |     64111 |
|   1392 |   69561 | 61774.6 |               620.92 |     61111 |    62111 |     64111 |
|   1393 |   68217 | 61772.2 |               631.81 |     61111 |    62111 |     64111 |
|   1394 |   69161 | 61785.1 |               655.12 |     61111 |    62111 |     64111 |
|   1395 |   62074 | 61656.3 |               537.69 |     61116 |    61336 |     64114 |
|   1396 |   66883 | 61672.4 |               538.87 |     61116 |    62119 |     64114 |
|   1397 |   67540 | 61675.3 |               538.35 |     61116 |    62119 |     64113 |
|   1398 |   65033 | 61651.7 |               537.43 |     61116 |    61312 |     64114 |
|   1399 |   62951 | 61534.6 |               511.21 |     61116 |    61221 |     64114 |
|   1400 |   63546 | 61575.6 |               524.27 |     61116 |    61221 |     64113 |
|   1401 |   59386 | 61608.6 |               536.68 |     61116 |    61123 |     64114 |
|   1402 |   58985 | 61626.5 |               537.83 |     61116 |    61221 |     64113 |


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

| Years     | Provision_Method                             |
|:----------|:---------------------------------------------|
| 1363-1383 | [COL3](/HBSIR/tables/raw/medical#col3)       |
| 1384-1402 | [DYCOL02](/HBSIR/tables/raw/medical#dycol02) |


#### Summary Statistics

**category data**

|   Year | Purchase   |   Donation | Instead_of_Private_Service   |   Instead_of_Public_Service |   Non_Agricultural_Work |   Home_Production | Agricultural_Work   | Purchase_Subsidised_Price   | Purchase_Free_Price   | nan   | Instead_of_Cooperative_Service   |
|-------:|:-----------|-----------:|:-----------------------------|----------------------------:|------------------------:|------------------:|:--------------------|:----------------------------|:----------------------|:------|:---------------------------------|
|   1363 |            |       0.3  | 0.02                         |                        0.27 |                    0.18 |              0.04 | 0.0                 | 76.7                        | 22.49                 |       |                                  |
|   1364 |            |       0.17 | 0.01                         |                        0.33 |                    0.14 |              0.06 | 0.0                 | 78.14                       | 21.15                 |       |                                  |
|   1365 |            |       0.05 | 0.01                         |                        0.24 |                    0.05 |              0.04 |                     | 85.22                       | 14.38                 |       |                                  |
|   1366 |            |       0.15 | 0.02                         |                        0.15 |                    0.04 |              0.11 |                     | 82.91                       | 16.62                 |       |                                  |
|   1367 |            |       0.36 |                              |                        0.13 |                    0.08 |              0.04 |                     | 79.74                       | 19.65                 |       |                                  |
|   1368 |            |       0.35 |                              |                        0.18 |                    0.15 |              0.05 | 0.01                | 70.43                       | 24.11                 | 4.72  |                                  |
|   1369 | 98.48      |       0.45 | 0.01                         |                        0.63 |                    0.13 |              0.07 |                     |                             |                       | 0.22  |                                  |
|   1370 | 98.43      |       0.29 | 0.06                         |                        0.91 |                    0.16 |              0.09 | 0.02                |                             |                       | 0.04  |                                  |
|   1371 | 99.14      |       0.32 | 0.01                         |                        0.32 |                    0.1  |              0.07 | 0.01                |                             |                       | 0.03  |                                  |
|   1372 | 99.29      |       0.32 | 0.01                         |                        0.14 |                    0.04 |              0.05 |                     |                             |                       | 0.15  |                                  |
|   1373 | 98.84      |       0.47 | 0.02                         |                        0.4  |                    0.04 |              0.1  | 0.0                 |                             |                       | 0.13  |                                  |
|   1374 | 98.84      |       0.5  | 0.07                         |                        0.44 |                    0.07 |              0.06 | 0.01                |                             |                       | 0.01  |                                  |
|   1375 | 99.23      |       0.35 | 0.05                         |                        0.26 |                    0.04 |              0.05 | 0.01                |                             |                       | 0.0   |                                  |
|   1376 | 99.17      |       0.49 | 0.07                         |                        0.19 |                    0.04 |              0.04 | 0.01                |                             |                       |       |                                  |
|   1377 | 99.13      |       0.5  | 0.05                         |                        0.24 |                    0.03 |              0.05 | 0.0                 |                             |                       |       |                                  |
|   1378 | 93.56      |       1.64 | 2.2                          |                        2.39 |                    0.12 |              0.08 | 0.02                |                             |                       |       |                                  |
|   1379 | 92.25      |       2.35 | 2.59                         |                        2.63 |                    0.07 |              0.06 | 0.02                |                             |                       |       | 0.04                             |
|   1380 | 91.93      |       2.69 | 2.56                         |                        2.66 |                    0.06 |              0.06 | 0.02                |                             |                       |       | 0.03                             |
|   1381 | 92.17      |       2.49 | 2.55                         |                        2.58 |                    0.04 |              0.11 | 0.0                 |                             |                       |       | 0.05                             |
|   1382 | 91.2       |       3.04 | 2.99                         |                        2.54 |                    0.07 |              0.1  | 0.01                |                             |                       |       | 0.05                             |
|   1383 | 95.72      |       2.79 | 0.34                         |                        0.91 |                    0.07 |              0.15 | 0.01                |                             |                       |       | 0.01                             |
|   1384 | 95.92      |       2.53 | 0.47                         |                        0.82 |                    0.07 |              0.16 | 0.0                 |                             |                       |       | 0.02                             |
|   1385 | 95.26      |       3.3  | 0.53                         |                        0.67 |                    0.16 |              0.05 | 0.01                |                             |                       | 0.0   | 0.03                             |
|   1386 | 97.42      |       1.74 | 0.2                          |                        0.54 |                    0.05 |              0.01 | 0.0                 |                             |                       | 0.0   | 0.03                             |
|   1387 | 98.06      |       1.68 | 0.03                         |                        0.18 |                    0.03 |              0.01 | 0.01                |                             |                       |       | 0.0                              |
|   1388 | 95.83      |       3.82 | 0.08                         |                        0.23 |                    0.02 |              0.01 | 0.0                 |                             |                       |       |                                  |
|   1389 | 93.66      |       5.81 | 0.23                         |                        0.26 |                    0.03 |              0.01 | 0.0                 |                             |                       |       |                                  |
|   1390 | 94.11      |       5.01 | 0.45                         |                        0.4  |                    0.02 |              0.01 | 0.0                 |                             |                       |       |                                  |
|   1391 | 93.25      |       6.06 | 0.29                         |                        0.34 |                    0.03 |              0.03 |                     |                             |                       |       |                                  |
|   1392 | 94.5       |       5.02 | 0.23                         |                        0.21 |                    0.02 |              0.02 |                     |                             |                       |       |                                  |
|   1393 | 93.7       |       5.95 | 0.15                         |                        0.17 |                    0.01 |              0.01 | 0.0                 |                             |                       |       |                                  |
|   1394 | 91.71      |       7.96 | 0.15                         |                        0.17 |                    0.01 |              0    |                     |                             |                       |       |                                  |
|   1395 | 90.93      |       8.89 | 0.08                         |                        0.08 |                    0.01 |              0    | 0.0                 |                             |                       |       |                                  |
|   1396 | 88.4       |      10.7  | 0.55                         |                        0.33 |                    0.01 |              0    |                     |                             |                       |       |                                  |
|   1397 | 86.94      |      12.14 | 0.55                         |                        0.37 |                    0    |              0    | 0.0                 |                             |                       |       |                                  |
|   1398 | 87.98      |      11.1  | 0.53                         |                        0.37 |                    0.01 |              0.01 | 0.0                 |                             |                       |       |                                  |
|   1399 | 91.44      |       7.79 | 0.48                         |                        0.26 |                    0.02 |              0.01 | 0.0                 |                             |                       |       | 0.0                              |
|   1400 | 91.71      |       7.49 | 0.51                         |                        0.24 |                    0.04 |              0.01 | 0.0                 |                             |                       |       |                                  |
|   1401 | 90.84      |       8.34 | 0.47                         |                        0.32 |                    0.01 |              0.01 |                     |                             |                       |       | 0.01                             |
|   1402 | 88.82      |      10.37 | 0.45                         |                        0.34 |                    0.02 |              0.01 | 0.0                 |                             |                       |       |                                  |


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

| Years     | Expenditure                                  |
|:----------|:---------------------------------------------|
| 1363-1368 | [COL4](/HBSIR/tables/raw/medical#col4)       |
| 1369      | [COL6](/HBSIR/tables/raw/medical#col6)       |
| 1370-1373 | [COL5](/HBSIR/tables/raw/medical#col5)       |
| 1374-1383 | [COL4](/HBSIR/tables/raw/medical#col4)       |
| 1384-1402 | [DYCOL03](/HBSIR/tables/raw/medical#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |        Median |         Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|--------------:|----------------:|
|   1363 |   55723 |   1599.37        |      11171.9         |         5 |    500        |      1.1e+06    |
|   1364 |   56403 |   1609.19        |       9472.09        |         3 |    500        | 700000          |
|   1365 |    9622 |   1931.04        |       8785.96        |        20 |    750        | 400000          |
|   1366 |   11429 |   2071.4         |      15097           |        10 |    630        | 800000          |
|   1367 |   15899 |   2381           |      18274.5         |        10 |    600        |      1e+06      |
|   1368 |   25633 |   2272.35        |      19581.4         |         1 |    600        |      1.65e+06   |
|   1369 |   37908 |   2807.73        |      16171.8         |         1 |    950        |      1.1e+06    |
|   1370 |   37095 |   4126.45        |      32910.9         |         8 |   1100        |      2e+06      |
|   1371 |   36535 |   5853.43        |      58710.2         |        15 |   1500        |      7.5e+06    |
|   1372 |   24384 |   6845.85        |      43061.9         |        30 |   2000        |      3.54e+06   |
|   1373 |   40926 |  11145.9         |      82035.7         |        30 |   3000        |      1e+07      |
|   1374 |   77856 |  14357.4         |     100703           |         4 |   4000        |      1.11e+07   |
|   1375 |   45559 |  18234.8         |     122544           |         3 |   5000        |      8.5e+06    |
|   1376 |   46928 |  21990.9         |     180625           |         1 |   6000        |      2.2e+07    |
|   1377 |   36749 |  27183.2         |     142219           |        78 |   7600        |      8e+06      |
|   1378 |   61686 |  36192.6         |     257436           |        44 |  11000        |      3e+07      |
|   1379 |   60174 |  43744.1         |     300656           |        10 |  15000        |      3e+07      |
|   1380 |   60967 |  52001.9         |     542802           |       100 |  17300        |      1.13e+08   |
|   1381 |   86185 |  56612.3         |     349158           |       150 |  20000        |      3.5e+07    |
|   1382 |   64678 |  61827.2         |     344032           |       150 |  22000        |      4.5e+07    |
|   1383 |   55706 |  84835.1         |     643498           |       200 |  25000        |      6.9137e+07 |
|   1384 |   59658 |  99151.5         |     640920           |       200 |  30000        |      6.5e+07    |
|   1385 |   65024 | 116747           |     709052           |         0 |  35000        |      7e+07      |
|   1386 |   62516 | 147164           |          1.3082e+06  |       300 |  40000        |      1.4e+08    |
|   1387 |   76921 | 185820           |          1.31019e+06 |       500 |  50000        |      1.5e+08    |
|   1388 |   75327 | 208974           |          2.06434e+06 |       500 |  60000        |      4.74e+08   |
|   1389 |   76201 | 262927           |          1.57121e+06 |       500 |  80000        |      1.2e+08    |
|   1390 |   71223 | 228812           |     795417           |       750 | 100000        |      8e+07      |
|   1391 |   71346 | 271782           |          1.14905e+06 |      1000 | 120000        |      1.7e+08    |
|   1392 |   69436 | 364895           |          1.38313e+06 |      1000 | 150000        |      1.5e+08    |
|   1393 |   68217 | 422367           |          1.51826e+06 |      1500 | 180000        |      1.417e+08  |
|   1394 |   69161 | 466857           |          1.9012e+06  |      1000 | 200000        |      3e+08      |
|   1395 |   62072 | 516957           |          1.67771e+06 |      2000 | 200000        |      1.2e+08    |
|   1396 |   66883 | 573390           |          1.84029e+06 |      1000 | 245000        |      1.656e+08  |
|   1397 |   67540 | 749890           |          3.2878e+06  |      1000 | 300000        |      4e+08      |
|   1398 |   65033 | 867854           |          3.54903e+06 |      2000 | 350000        |      5e+08      |
|   1399 |   62951 |      1.03845e+06 |          4.17541e+06 |      5000 | 400000        |      5e+08      |
|   1400 |   63546 |      1.64406e+06 |          6.43191e+06 |      5000 | 600000        |      8e+08      |
|   1401 |   59386 |      2.52089e+06 |          8.25663e+06 |      5000 |      1e+06    |      5e+08      |
|   1402 |   58985 |      3.58871e+06 |          1.30966e+07 |     10000 |      1.39e+06 |      1.1e+09    |


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

| Years     | Price_System                           |
|:----------|:---------------------------------------|
| 1363-1368 |                                        |
| 1369-1373 | [COL4](/HBSIR/tables/raw/medical#col4) |
| 1374-1402 |                                        |


#### Summary Statistics

**category data**

|   Year |   Subsidised_Price |   Free_Price |   nan |
|-------:|-------------------:|-------------:|------:|
|   1369 |              59.44 |        40.32 |  0.24 |
|   1370 |              59.03 |        40.91 |  0.06 |
|   1371 |              60.77 |        39.18 |  0.05 |
|   1372 |              62.07 |        37.77 |  0.16 |
|   1373 |              66.62 |        32.99 |  0.39 |


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

| Years     | Amount                                 |
|:----------|:---------------------------------------|
| 1363-1368 |                                        |
| 1369      | [COL5](/HBSIR/tables/raw/medical#col5) |
| 1370-1402 |                                        |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1369 |   12673 |   3.51 |                62.57 |         1 |        2 |      6000 |


