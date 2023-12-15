# food

## Old to New Titles

| Years     | ADDRESS   | COL1   | COL3             | COL4         | COL4_5   | COL5   | COL5_6   | COL6        | COL7        | COL8        |
|:----------|:----------|:-------|:-----------------|:-------------|:---------|:-------|:---------|:------------|:------------|:------------|
| 1363-1368 | ID        | Code   | Provision_Method |              | Kilos    |        |          | Expenditure |             |             |
| 1369      | ID        | Code   | Provision_Method | Price_System |          |        | Kilos    |             | Price       | Expenditure |
| 1370-1371 | ID        | Code   | Provision_Method | Price_System |          |        | Kilos    |             |             | Expenditure |
| 1372-1373 | ID        | Code   | Provision_Method | Price_System |          |        | Kilos    |             | Price       | Expenditure |
| 1374-1382 | ID        | Code   | Provision_Method |              | Kilos    |        |          | Price       | Expenditure |             |
| 1383      | ID        | Code   | Provision_Method | Grams        |          | Kilos  |          | Price       | Expenditure |             |


| Years     | ADDRESS   | DYCOL01   | DYCOL02          | DYCOL03   | DYCOL04   | DYCOL05   | DYCOL06     | DYCOL07   |
|:----------|:----------|:----------|:-----------------|:----------|:----------|:----------|:------------|:----------|
| 1384      | ID        | Code      | Provision_Method | Grams     | Kilos     | Price     | Expenditure | drop      |
| 1385-1401 | ID        | Code      | Provision_Method | Grams     | Kilos     | Price     | Expenditure |           |


## New to Old Titles

| Years     | ID      | Code    | Provision_Method   | Grams   | Kilos   | Price   | Expenditure   | Price_System   |
|:----------|:--------|:--------|:-------------------|:--------|:--------|:--------|:--------------|:---------------|
| 1363-1368 | ADDRESS | COL1    | COL3               |         | COL4_5  |         | COL6          |                |
| 1369      | ADDRESS | COL1    | COL3               |         | COL5_6  | COL7    | COL8          | COL4           |
| 1370-1371 | ADDRESS | COL1    | COL3               |         | COL5_6  |         | COL8          | COL4           |
| 1372-1373 | ADDRESS | COL1    | COL3               |         | COL5_6  | COL7    | COL8          | COL4           |
| 1374-1382 | ADDRESS | COL1    | COL3               |         | COL4_5  | COL6    | COL7          |                |
| 1383      | ADDRESS | COL1    | COL3               | COL4    | COL5    | COL6    | COL7          |                |
| 1384-1401 | ADDRESS | DYCOL01 | DYCOL02            | DYCOL03 | DYCOL04 | DYCOL05 | DYCOL06       |                |


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
| 1363-1401 | [ADDRESS](/HBSIR/tables/raw/food#address) |


#### Summary Statistics

**numeric data**

|   Year |            Count |             Mean |   Standard Deviation |        Minimum |           Median |     Maximum |
|-------:|-----------------:|-----------------:|---------------------:|---------------:|-----------------:|------------:|
|   1363 | 295773           | 655589           |     510647           |  1001          |      1.0212e+06  | 1.23452e+06 |
|   1364 | 311002           | 616338           |     510168           |  1001          |      1.003e+06   | 1.23442e+06 |
|   1365 |  51809           | 618757           |     530772           |  1001          |      1.003e+06   | 1.23422e+06 |
|   1366 |  63183           | 594800           |     524784           |  1002          | 233009           | 1.23421e+06 |
|   1367 |  92676           | 596936           |     522183           |  1001          | 233014           | 1.23428e+06 |
|   1368 | 136402           | 591400           |     518808           |  1001          | 233026           | 1.23428e+06 |
|   1369 | 402492           | 650278           |     509928           |  1001          |      1.01307e+06 | 1.23422e+06 |
|   1370 | 407241           | 645464           |     508434           |  1001          |      1.01301e+06 | 1.23422e+06 |
|   1371 | 409859           | 655803           |     507026           |  1001          |      1.01308e+06 | 1.23422e+06 |
|   1372 | 292306           | 687494           |     503539           |  1001          |      1.021e+06   | 1.23422e+06 |
|   1373 | 470756           | 786477           |     495479           |  1001          |      1.06305e+06 | 1.24404e+06 |
|   1374 | 874879           |      7.52742e+06 |          4.9994e+06  | 10001          |      1.06201e+07 | 1.24401e+07 |
|   1375 | 503808           | 687928           |     517467           |  1001          |      1.03305e+06 | 1.24404e+06 |
|   1376 | 523101           | 681347           |     518352           |  1001          |      1.03115e+06 | 1.25406e+06 |
|   1377 | 422342           |      6.61192e+07 |          5.19257e+07 | 11001          |      1.02073e+08 | 1.27074e+08 |
|   1378 | 706456           |      6.57591e+07 |          5.16321e+07 | 11001          |      1.01053e+08 | 1.27074e+08 |
|   1379 | 720008           |      6.49278e+07 |          5.15297e+07 | 11001          |      1.01041e+08 | 1.27074e+08 |
|   1380 | 765426           |      6.43029e+07 |          5.15303e+07 | 11001          |      1.00053e+08 | 1.27074e+08 |
|   1381 |      1.03796e+06 |      6.58284e+07 |          5.13225e+07 | 11001          |      1.01051e+08 | 1.27074e+08 |
|   1382 | 793904           |      6.56269e+07 |          5.13564e+07 | 11001          |      1.01023e+08 | 1.27114e+08 |
|   1383 | 907142           |      6.54822e+07 |          5.13077e+07 | 11001          |      1.00073e+08 | 1.27114e+08 |
|   1384 | 970821           |      6.62478e+07 |          5.12074e+07 | 11001          |      1.01043e+08 | 1.29214e+08 |
|   1385 |      1.03836e+06 |      6.37213e+07 |          5.16294e+07 | 11001          |      2.91211e+07 | 1.29214e+08 |
|   1386 |      1.07582e+06 |      6.63875e+07 |          5.08253e+07 | 11001          |      1.01034e+08 | 1.29214e+08 |
|   1387 |      1.27233e+06 |      1.61649e+09 |          5.0367e+08  |     1e+09      |      1.28736e+09 | 2.29786e+09 |
|   1388 |      1.17969e+06 |      1.60265e+09 |          5.03748e+08 |     1e+09      |      1.27015e+09 | 2.29025e+09 |
|   1389 |      1.21819e+06 |      1.61937e+09 |          5.03397e+08 |     1e+09      |      1.28007e+09 | 2.29013e+09 |
|   1390 |      1.24789e+06 |      1.63043e+09 |          5.04709e+08 |     1e+09      |      1.29008e+09 | 2.30013e+09 |
|   1391 |      1.22517e+06 |      1.63268e+09 |          5.0416e+08  |     1e+09      |      1.2901e+09  | 2.30013e+09 |
|   1392 |      1.18932e+06 |      1.62697e+10 |          5.03444e+09 |     1.0001e+10 |      1.29056e+10 | 2.30047e+10 |
|   1393 |      1.20728e+06 |      1.62719e+10 |          5.03361e+09 |     1.0001e+10 |      1.29056e+10 | 2.30047e+10 |
|   1394 |      1.21571e+06 |      1.62899e+10 |          5.03489e+09 |     1.0001e+10 |      1.29076e+10 | 2.30047e+10 |
|   1395 |      1.23181e+06 |      1.62797e+10 |          5.02959e+09 |     1.0001e+10 |      1.29056e+10 | 2.30047e+10 |
|   1396 |      1.25768e+06 |      1.6276e+10  |          5.03246e+09 |     1.0001e+10 |      1.29046e+10 | 2.30047e+10 |
|   1397 |      1.22093e+06 |      1.60087e+10 |          5.02974e+09 |     1.0001e+10 |      1.27113e+10 | 2.30067e+10 |
|   1398 |      1.14916e+06 |      1.60189e+10 |          5.03294e+09 |     1.0001e+10 |      1.27133e+10 | 2.30067e+10 |
|   1399 |      1.10205e+06 |      1.60515e+10 |          5.02293e+09 |     1.0001e+10 |      1.28013e+10 | 2.30067e+10 |
|   1400 |      1.12713e+06 |      1.60245e+10 |          5.01687e+09 |     1.0001e+10 |      1.27143e+10 | 2.30067e+10 |
|   1401 |      1.08138e+06 |      1.60503e+10 |          5.02503e+09 |     1.0001e+10 |      1.28013e+10 | 2.30067e+10 |


### Code

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL01
      type: UInt32
    1364:
      column_code: DYCOL01
      type: UInt32
    1365:
      column_code: DYCOL01
      type: UInt32
    1366:
      column_code: DYCOL01
      type: UInt32
    1367:
      column_code: DYCOL01
      type: UInt32
    1368:
      column_code: DYCOL01
      type: UInt32
    1369:
      column_code: DYCOL01
      type: UInt32
    1370:
      column_code: DYCOL01
      type: UInt32
    1371:
      column_code: DYCOL01
      type: UInt32
    1372:
      column_code: DYCOL01
      type: UInt32
    1373:
      column_code: DYCOL01
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

| Years     | Code                                      |
|:----------|:------------------------------------------|
| 1363-1383 | [COL1](/HBSIR/tables/raw/food#col1)       |
| 1384-1401 | [DYCOL01](/HBSIR/tables/raw/food#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |            Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|-----------------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 | 295773           | 15153.6 |              2506.21 |     11110 |    15540 |     19778 |
|   1364 | 311002           | 15213.4 |              2514.74 |     11110 |    15540 |     19993 |
|   1365 |  51809           | 14950.5 |              2469.76 |     11110 |    15449 |     19756 |
|   1366 |  63183           | 15185.5 |              2683.91 |     11110 |    15540 |     91197 |
|   1367 |  92676           | 15196.8 |              2472.59 |     11110 |    15540 |     19778 |
|   1368 | 136402           | 15204   |              2456.87 |     11110 |    15540 |     19778 |
|   1369 | 402492           | 14979.2 |              2233.25 |     11110 |    15438 |     19778 |
|   1370 | 407241           | 14999.4 |              2322.04 |     11110 |    15416 |     19552 |
|   1371 | 409859           | 15019.9 |              2304.5  |     11110 |    15427 |     19552 |
|   1372 | 292306           | 14998.9 |              2263.65 |     11110 |    15416 |     19552 |
|   1373 | 470756           | 14992.4 |              2311.92 |     11110 |    15427 |     19552 |
|   1374 | 874879           | 15023.2 |              2316.13 |     11110 |    15438 |     19563 |
|   1375 | 503808           | 15074.4 |              2347.97 |     11110 |    15427 |     19563 |
|   1376 | 523101           | 15095.3 |              2369.31 |     11110 |    15427 |     19563 |
|   1377 | 422342           | 15128.4 |              2355.82 |     11110 |    15518 |     19563 |
|   1378 | 706456           | 15120.1 |              2390.34 |     11110 |    15518 |     19563 |
|   1379 | 720008           | 15155.9 |              2381.55 |     11110 |    15518 |     19563 |
|   1380 | 765426           | 15172.3 |              2387.01 |     11110 |    15518 |     19563 |
|   1381 |      1.03796e+06 | 15186.4 |              2354.02 |     11110 |    15518 |     19563 |
|   1382 | 793904           | 15200.1 |              2366.23 |     11110 |    15518 |     19563 |
|   1383 | 907142           | 11614.2 |               280.81 |     11111 |    11711 |     12218 |
|   1384 | 970821           | 11612   |               281.73 |     11111 |    11665 |     12218 |
|   1385 |      1.03836e+06 | 11608.2 |               281.98 |     11111 |    11665 |     12218 |
|   1386 |      1.07582e+06 | 11604.4 |               283.51 |     11111 |    11662 |     12218 |
|   1387 |      1.27233e+06 | 11606.1 |               283.19 |     11111 |    11663 |     12218 |
|   1388 |      1.17969e+06 | 11606.4 |               283.71 |     11111 |    11665 |     12218 |
|   1389 |      1.21819e+06 | 11606.3 |               283.93 |     11111 |    11662 |     12218 |
|   1390 |      1.24789e+06 | 11609.8 |               285.34 |     11111 |    11665 |     12218 |
|   1391 |      1.22517e+06 | 11611.1 |               286.3  |     11111 |    11665 |     12218 |
|   1392 |      1.18932e+06 | 11610   |               285.74 |     11111 |    11665 |     12218 |
|   1393 |      1.20728e+06 | 11611.1 |               284.43 |     11111 |    11665 |     12218 |
|   1394 |      1.21571e+06 | 11611.2 |               282.97 |     11111 |    11665 |     12218 |
|   1395 |      1.23181e+06 | 11611.2 |               280.64 |     11111 |    11665 |     12218 |
|   1396 |      1.25768e+06 | 11613.5 |               280.69 |     11111 |    11665 |     12218 |
|   1397 |      1.22093e+06 | 11610.3 |               280.53 |     11111 |    11665 |     12218 |
|   1398 |      1.14916e+06 | 11605.2 |               280.19 |     11111 |    11661 |     12218 |
|   1399 |      1.10205e+06 | 11604.9 |               281.96 |     11111 |    11664 |     12218 |
|   1400 |      1.12713e+06 | 11604.4 |               281.57 |     11111 |    11661 |     12218 |
|   1401 |      1.08138e+06 | 11606.6 |               281.31 |     11111 |    11663 |     12218 |


### Provision_Method

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL02
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
    1364:
      column_code: DYCOL02
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
    1365:
      column_code: DYCOL02
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
    1366:
      column_code: DYCOL02
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
    1367:
      column_code: DYCOL02
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
    1368:
      column_code: DYCOL02
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
      column_code: DYCOL02
      type: category
      categories:
        2: Purchase
        3: Home_Production
        4: Instead_of_Public_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1370:
      column_code: DYCOL02
      type: category
      categories:
        2: Purchase
        3: Home_Production
        4: Instead_of_Public_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1371:
      column_code: DYCOL02
      type: category
      categories:
        2: Purchase
        3: Home_Production
        4: Instead_of_Public_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1372:
      column_code: DYCOL02
      type: category
      categories:
        2: Purchase
        3: Home_Production
        4: Instead_of_Public_Service
        5: Instead_of_Private_Service
        6: Agricultural_Work
        7: Non_Agricultural_Work
        8: Donation
    1373:
      column_code: DYCOL02
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

| Years     | Provision_Method                          |
|:----------|:------------------------------------------|
| 1363-1383 | [COL3](/HBSIR/tables/raw/food#col3)       |
| 1384-1401 | [DYCOL02](/HBSIR/tables/raw/food#dycol02) |


#### Summary Statistics

**category data**

|   Year | Purchase   |   Home_Production |   Non_Agricultural_Work |   Agricultural_Work |   Donation |   Instead_of_Private_Service |   Instead_of_Public_Service | Instead_of_Cooperative_Service   | Purchase_Free_Price   | Purchase_Subsidised_Price   | nan   |
|-------:|:-----------|------------------:|------------------------:|--------------------:|-----------:|-----------------------------:|----------------------------:|:---------------------------------|:----------------------|:----------------------------|:------|
|   1363 |            |              1.67 |                    0.86 |                5.46 |       1.23 |                         0.14 |                        0.13 |                                  | 49.29                 | 41.23                       |       |
|   1364 |            |              1.57 |                    0.88 |                5.61 |       1.37 |                         0.12 |                        0.14 |                                  | 55.55                 | 34.76                       |       |
|   1365 |            |              1.79 |                    0.93 |                6.8  |       1.38 |                         0.16 |                        0.24 |                                  | 51.35                 | 37.35                       | 0.0   |
|   1366 |            |              1.74 |                    0.82 |                6.01 |       1.08 |                         0.12 |                        0.21 |                                  | 56.12                 | 33.88                       | 0.03  |
|   1367 |            |              1.69 |                    0.85 |                5.66 |       1    |                         0.17 |                        0.23 |                                  | 59.37                 | 31.02                       |       |
|   1368 |            |              1.88 |                    0.84 |                6.43 |       0.95 |                         0.11 |                        0.17 |                                  | 61.48                 | 28.15                       |       |
|   1369 | 93.51      |              2.48 |                    1.06 |                2.56 |       0.18 |                         0.06 |                        0.16 |                                  |                       |                             | 0.0   |
|   1370 | 93.74      |              2.36 |                    1.21 |                2.25 |       0.13 |                         0.06 |                        0.18 |                                  |                       |                             | 0.07  |
|   1371 | 93.84      |              2.36 |                    1.16 |                2.24 |       0.13 |                         0.07 |                        0.12 |                                  |                       |                             | 0.08  |
|   1372 | 94.3       |              2.28 |                    1.07 |                1.96 |       0.07 |                         0.1  |                        0.15 |                                  |                       |                             | 0.07  |
|   1373 | 95.38      |              1.7  |                    1.4  |                1.11 |       0.09 |                         0.08 |                        0.18 |                                  |                       |                             | 0.07  |
|   1374 | 95.21      |              1.91 |                    1.18 |                1.24 |       0.12 |                         0.1  |                        0.23 |                                  |                       |                             | 0.01  |
|   1375 | 95.29      |              1.75 |                    1.23 |                1.12 |       0.13 |                         0.16 |                        0.32 |                                  |                       |                             |       |
|   1376 | 95.32      |              1.68 |                    1.32 |                1.04 |       0.14 |                         0.17 |                        0.34 |                                  |                       |                             |       |
|   1377 | 95.23      |              1.7  |                    1.34 |                1.06 |       0.14 |                         0.17 |                        0.37 |                                  |                       |                             |       |
|   1378 | 95.05      |              1.7  |                    1.38 |                1.16 |       0.13 |                         0.18 |                        0.4  |                                  |                       |                             |       |
|   1379 | 95.2       |              1.67 |                    1.36 |                1.12 |       0.15 |                         0.18 |                        0.33 | 0.0                              |                       |                             |       |
|   1380 | 95.06      |              1.84 |                    1.41 |                1.01 |       0.2  |                         0.2  |                        0.26 | 0.02                             |                       |                             |       |
|   1381 | 95.11      |              1.85 |                    1.43 |                0.88 |       0.35 |                         0.16 |                        0.2  | 0.01                             |                       |                             |       |
|   1382 | 95.32      |              1.61 |                    1.38 |                0.81 |       0.42 |                         0.21 |                        0.24 | 0.0                              |                       |                             |       |
|   1383 | 95.14      |              1.8  |                    1.41 |                0.89 |       0.53 |                         0.11 |                        0.11 | 0.01                             |                       |                             |       |
|   1384 | 94.88      |              2.03 |                    1.42 |                0.88 |       0.56 |                         0.11 |                        0.12 | 0.01                             |                       |                             |       |
|   1385 | 95.24      |              1.67 |                    1.63 |                0.71 |       0.57 |                         0.08 |                        0.09 | 0.01                             |                       |                             |       |
|   1386 | 95.31      |              1.54 |                    1.56 |                0.61 |       0.78 |                         0.07 |                        0.12 | 0.0                              |                       |                             |       |
|   1387 | 95.9       |              1.58 |                    1.25 |                0.55 |       0.55 |                         0.06 |                        0.1  | 0.01                             |                       |                             |       |
|   1388 | 95.85      |              1.61 |                    1.23 |                0.49 |       0.72 |                         0.07 |                        0.04 | 0.0                              |                       |                             |       |
|   1389 | 96.39      |              1.5  |                    1.2  |                0.4  |       0.43 |                         0.07 |                        0.02 | 0.0                              |                       |                             |       |
|   1390 | 97.08      |              1.32 |                    1.09 |                0.35 |       0.07 |                         0.06 |                        0.02 | 0.0                              |                       |                             |       |
|   1391 | 96.99      |              1.4  |                    1.07 |                0.4  |       0.07 |                         0.06 |                        0.02 | 0.0                              |                       |                             |       |
|   1392 | 96.52      |              1.41 |                    0.88 |                0.36 |       0.76 |                         0.06 |                        0.01 | 0.0                              |                       |                             |       |
|   1393 | 97.13      |              1.34 |                    0.91 |                0.33 |       0.21 |                         0.07 |                        0.01 | 0.0                              |                       |                             | 0.0   |
|   1394 | 97.24      |              1.18 |                    0.97 |                0.34 |       0.16 |                         0.09 |                        0.02 | 0.0                              |                       |                             |       |
|   1395 | 97.33      |              1.08 |                    1.03 |                0.31 |       0.15 |                         0.08 |                        0.01 | 0.0                              |                       |                             |       |
|   1396 | 97.26      |              1.12 |                    1.04 |                0.31 |       0.16 |                         0.09 |                        0.01 | 0.0                              |                       |                             |       |
|   1397 | 97.31      |              1.06 |                    0.9  |                0.28 |       0.33 |                         0.1  |                        0.01 | 0.0                              |                       |                             |       |
|   1398 | 97.32      |              1.14 |                    0.94 |                0.3  |       0.2  |                         0.09 |                        0.01 | 0.0                              |                       |                             |       |
|   1399 | 97.52      |              1.04 |                    0.74 |                0.26 |       0.33 |                         0.11 |                        0    | 0.0                              |                       |                             |       |
|   1400 | 97.7       |              0.95 |                    0.74 |                0.24 |       0.26 |                         0.1  |                        0.01 | 0.0                              |                       |                             |       |
|   1401 | 97.78      |              0.93 |                    0.75 |                0.23 |       0.2  |                         0.1  |                        0    | 0.0                              |                       |                             |       |


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


### Grams

??? abstract "Column Metadata"
    ``` yaml
    1363:
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

| Years     | Grams                                     |
|:----------|:------------------------------------------|
| 1363-1382 |                                           |
| 1383      | [COL4](/HBSIR/tables/raw/food#col4)       |
| 1384-1401 | [DYCOL03](/HBSIR/tables/raw/food#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1383 |  212771 | 462.71 |               184.83 |         1 |      500 |       999 |
|   1384 |  227804 | 462.56 |               188.21 |         0 |      500 |       999 |
|   1385 |  243790 | 467.91 |               185.35 |         0 |      500 |       999 |
|   1386 |  262984 | 473.95 |               186.74 |         0 |      500 |       999 |
|   1387 |  297892 | 475.73 |               186.12 |         0 |      500 |       998 |
|   1388 |  319756 | 401.89 |               243.58 |         0 |      500 |       999 |
|   1389 |  329299 | 377.62 |               255.45 |         0 |      500 |      1000 |
|   1390 |  328988 | 372.89 |               257.91 |         0 |      500 |       999 |
|   1391 |  290551 | 402.16 |               241.81 |         0 |      500 |       999 |
|   1392 |  259084 | 442.95 |               216.94 |         0 |      500 |       999 |
|   1393 |  270544 | 448.7  |               206.11 |         0 |      500 |       999 |
|   1394 |  280745 | 451.25 |               199.87 |         0 |      500 |       999 |
|   1395 |  286653 | 448.82 |               199.34 |         0 |      500 |       999 |
|   1396 |  291840 | 455.41 |               193.77 |         0 |      500 |       999 |
|   1397 |  285437 | 468.92 |               185    |         0 |      500 |       999 |
|   1398 |  276574 | 465.7  |               188.13 |         0 |      500 |       998 |
|   1399 |  272005 | 459.84 |               191    |         0 |      500 |       996 |
|   1400 |  293963 | 440.77 |               206.38 |         0 |      500 |       999 |
|   1401 |  295824 | 427.5  |               220.46 |         0 |      500 |       999 |


### Kilos

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
    
    ```
#### Column Codes

| Years     | Kilos                                     |
|:----------|:------------------------------------------|
| 1363-1368 | [COL4_5](/HBSIR/tables/raw/food#col4_5)   |
| 1369-1373 | [COL5_6](/HBSIR/tables/raw/food#col5_6)   |
| 1374-1382 | [COL4_5](/HBSIR/tables/raw/food#col4_5)   |
| 1383      | [COL5](/HBSIR/tables/raw/food#col5)       |
| 1384-1401 | [DYCOL04](/HBSIR/tables/raw/food#dycol04) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |  278196 |   3.4  |                14.95 |      0    |      1   |       999 |
|   1364 |  297774 |   3.22 |                11.89 |      0    |      1   |       999 |
|   1365 |   50429 |   3.42 |                11.14 |      0    |      1   |       900 |
|   1366 |   60884 |   3    |                 9.89 |      0    |      1   |       900 |
|   1367 |   89136 |   2.92 |                 9.9  |      0    |      1   |       900 |
|   1368 |  131725 |   2.71 |                 9.26 |      0    |      1   |       999 |
|   1369 |  393588 |  17.17 |                67.27 |      0    |      4   |      1000 |
|   1370 |  391019 |  29.22 |              1852.95 |      0    |      4   |    600600 |
|   1371 |  409859 |  16.71 |               103.09 |      0    |      3.6 |     30000 |
|   1372 |  281175 |  15.88 |                74.38 |      0    |      3.6 |      6000 |
|   1373 |  438857 |  15.63 |                70.15 |      0    |      4   |      6000 |
|   1374 |  816874 |  15.57 |                78.63 |      0    |      4   |     22000 |
|   1375 |  440220 |  16.41 |                77.62 |      0.02 |      4   |     12000 |
|   1376 |  453457 |  16.45 |                75.94 |      0.02 |      4   |     11000 |
|   1377 |  366306 |  16.24 |                78.82 |      0.05 |      4   |     12000 |
|   1378 |  604040 |  16.04 |                71.59 |      0    |      4   |      9000 |
|   1379 |  612735 |  14.95 |                67.63 |      0.03 |      4   |      6000 |
|   1380 |  646896 |  14.44 |                66.88 |      0.02 |      3.6 |      8000 |
|   1381 |  876685 |  12.77 |                60.81 |      0    |      3   |      6000 |
|   1382 |  662289 |  12.2  |                60.01 |      0.05 |      3   |      8000 |
|   1383 |  705711 |   8.21 |                28.78 |      1    |      3   |      5169 |
|   1384 |  756252 |   8    |                21.84 |      0    |      3   |      9000 |
|   1385 |  808897 |   7.6  |                19.12 |      0    |      3   |      7000 |
|   1386 |  828606 |   7.38 |                17.14 |      0    |      3   |      2000 |
|   1387 |  984080 |   7.04 |                15.68 |      0    |      3   |      1650 |
|   1388 |  922597 |   6.96 |                15.21 |      0    |      3   |      1200 |
|   1389 |  963316 |   6.84 |                16.64 |      0    |      3   |      7500 |
|   1390 |  995036 |   6.4  |                12.52 |      0    |      3   |      1000 |
|   1391 |  971779 |   6.28 |                12.76 |      0    |      3   |      2500 |
|   1392 |  934106 |   5.96 |                11.67 |      0    |      3   |      1500 |
|   1393 |  937731 |   5.79 |                35.3  |      0    |      3   |     32000 |
|   1394 |  934617 |   5.48 |                10.59 |      0    |      3   |      1820 |
|   1395 |  945238 |   5.32 |                18.51 |      0    |      3   |     15000 |
|   1396 |  961587 |   5.26 |                 9.99 |      0    |      3   |      1200 |
|   1397 |  928302 |   5.15 |                 9.59 |      0    |      3   |       800 |
|   1398 |  873469 |   5.23 |                10    |      0    |      3   |       555 |
|   1399 |  832695 |   5.08 |                 9.33 |      0    |      2   |      1000 |
|   1400 |  853008 |   4.87 |                 8.84 |      0    |      2   |       500 |
|   1401 |  817479 |   4.8  |                 9.1  |      0    |      2   |       500 |


### Price

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL05
      type: float
    1369:
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
    
    ```
#### Column Codes

| Years     | Price                                     |
|:----------|:------------------------------------------|
| 1363-1368 |                                           |
| 1369      | [COL7](/HBSIR/tables/raw/food#col7)       |
| 1370-1371 |                                           |
| 1372-1373 | [COL7](/HBSIR/tables/raw/food#col7)       |
| 1374-1383 | [COL6](/HBSIR/tables/raw/food#col6)       |
| 1384-1401 | [DYCOL05](/HBSIR/tables/raw/food#dycol05) |


#### Summary Statistics

**numeric data**

|   Year |            Count |      Mean |   Standard Deviation |   Minimum |   Median |          Maximum |
|-------:|-----------------:|----------:|---------------------:|----------:|---------:|-----------------:|
|   1369 | 392966           |    626.39 |              1078.68 |         1 |      200 |  99999           |
|   1372 | 281149           |   1601.58 |             54110.5  |         1 |      500 |      2.66661e+07 |
|   1373 | 438856           |   2146.24 |             26177.8  |         1 |      800 |      1.06667e+07 |
|   1374 | 816867           |   3668.82 |             42656.7  |         1 |     1142 |      1.16667e+07 |
|   1375 | 440215           |   3149.62 |              4709.75 |         2 |     1350 |  80000           |
|   1376 | 453457           |   3668.09 |              5557.76 |         2 |     1574 |  72000           |
|   1377 | 366306           |   4535.02 |              6655.92 |         4 |     2000 | 200000           |
|   1378 | 604040           |   5355.15 |              7763.79 |         2 |     2200 | 120000           |
|   1379 | 612735           |   5981.21 |              8287.59 |        10 |     2500 | 220000           |
|   1380 | 646896           |   6304.74 |              8551.17 |         6 |     3000 | 140000           |
|   1381 | 876685           |   7085.75 |              9223.35 |        10 |     3500 | 300000           |
|   1382 | 662300           |   8169.57 |             10489.6  |        15 |     4365 | 500000           |
|   1383 | 823470           |   9456.71 |             11388.1  |         4 |     5000 | 400000           |
|   1384 | 884644           |  10478.2  |             18608    |         0 |     6000 |      2.5e+06     |
|   1385 | 945705           |  11845.2  |             17975.2  |         0 |     7143 |      3.6e+06     |
|   1386 | 976920           |  13906.3  |             18578.9  |         0 |     9000 |      3e+06       |
|   1387 |      1.15759e+06 |  17059.1  |             20899.1  |        50 |    10000 |      2.5e+06     |
|   1388 |      1.07297e+06 |  18681.6  |             23368.6  |        63 |    12000 |      2e+06       |
|   1389 |      1.11096e+06 |  21703.7  |             27362.7  |        80 |    13000 |      3e+06       |
|   1390 |      1.13342e+06 |  26735    |             30858    |       200 |    16000 | 800000           |
|   1391 |      1.10746e+06 |  38752.4  |             48466.8  |       800 |    20000 |      2e+06       |
|   1392 |      1.07194e+06 |  54167.5  |             68569.7  |       400 |    30000 |      6.8e+06     |
|   1393 |      1.08662e+06 |  58146.3  |             72945.4  |       500 |    32000 |      7e+06       |
|   1394 |      1.0979e+06  |  62121.6  |             77893.4  |       500 |    35000 |      2e+06       |
|   1395 |      1.11432e+06 |  66428.6  |             83732.8  |         3 |    40000 |      3e+06       |
|   1396 |      1.13662e+06 |  73554.7  |             94416.5  |      1000 |    40000 |      3e+06       |
|   1397 |      1.10576e+06 |  98903.3  |            136700    |      1000 |    55000 |      1.5e+07     |
|   1398 |      1.04465e+06 | 138114    |            200029    |       700 |    75000 |      1.1e+07     |
|   1399 |      1.00042e+06 | 200589    |            288502    |      1000 |   110000 |      1e+07       |
|   1400 |      1.02434e+06 | 307030    |            407958    |        40 |   170000 |      1.8e+07     |
|   1401 |      1.08138e+06 | 458806    |            606480    |         0 |   250000 |      3e+07       |


### Expenditure

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
    
    ```
#### Column Codes

| Years     | Expenditure                               |
|:----------|:------------------------------------------|
| 1363-1368 | [COL6](/HBSIR/tables/raw/food#col6)       |
| 1369-1373 | [COL8](/HBSIR/tables/raw/food#col8)       |
| 1374-1383 | [COL7](/HBSIR/tables/raw/food#col7)       |
| 1384-1401 | [DYCOL06](/HBSIR/tables/raw/food#dycol06) |


#### Summary Statistics

**numeric data**

|   Year |            Count |      Mean |   Standard Deviation |   Minimum |   Median |          Maximum |
|-------:|-----------------:|----------:|---------------------:|----------:|---------:|-----------------:|
|   1363 | 284777           |    411.47 |       1746.01        |         1 |      120 | 159000           |
|   1364 | 298727           |    451.07 |       1865.68        |         1 |      120 | 135000           |
|   1365 |  51627           |    598.6  |       2842.67        |         1 |      120 | 159600           |
|   1366 |  60706           |    579    |       2833.31        |         1 |      130 | 236250           |
|   1367 |  89079           |    732.07 |       3136.84        |         1 |      150 | 180000           |
|   1368 | 131496           |    820.59 |       4811.07        |         1 |      180 |      1.05e+06    |
|   1369 | 402059           |   2903.86 |       8612.34        |         1 |     1100 |      1.54e+06    |
|   1370 | 407202           |   3480.28 |       9292.44        |         1 |     1500 |      1.56202e+06 |
|   1371 | 409859           |   4226.07 |       9708.54        |         0 |     1800 | 900000           |
|   1372 | 292306           |   5014.51 |      11688.5         |         5 |     2100 |      1e+06       |
|   1373 | 470756           |   7029.2  |      16227           |        11 |     3000 |      2.56e+06    |
|   1374 | 874833           |  10603.2  |      26211           |         6 |     4760 |      6.48e+06    |
|   1375 | 503808           |  12101.6  |      30624.2         |         1 |     5400 |      4.5e+06     |
|   1376 | 523101           |  13746.6  |      41309.1         |         2 |     6000 |      1.4e+07     |
|   1377 | 422342           |  17756.8  |      63568.1         |        16 |     8000 |      9e+06       |
|   1378 | 706456           |  19859.3  |      61319.8         |        30 |     9000 |      1.03992e+07 |
|   1379 | 720008           |  20851.6  |      53452.4         |       100 |    10000 |      9.1e+06     |
|   1380 | 765426           |  21323.6  |      52495.5         |        60 |    10000 |      6e+06       |
|   1381 |      1.03796e+06 |  23325.9  |      61889.1         |        50 |    10400 |      2e+07       |
|   1382 | 793904           |  26006.9  |      61459.6         |       100 |    12000 |      9.8e+06     |
|   1383 | 907142           |  28181.4  |      71313.1         |         0 |    12500 |      8.5e+06     |
|   1384 | 970430           |  30997.4  |      78285.1         |       100 |    15000 |      2.04e+07    |
|   1385 |      1.03836e+06 |  35654.3  |      89698.8         |       100 |    17000 |      1.6e+07     |
|   1386 |      1.07582e+06 |  41261.9  |     100033           |       100 |    20000 |      1.245e+07   |
|   1387 |      1.27233e+06 |  50109.4  |     138416           |       150 |    24000 |      3.01e+07    |
|   1388 |      1.17969e+06 |  53819.9  |     130704           |       100 |    25000 |      1.863e+07   |
|   1389 |      1.21819e+06 |  64764.2  |     166725           |         0 |    30000 |      5.625e+07   |
|   1390 |      1.24789e+06 |  81204.4  |     174501           |       350 |    40000 |      2.4e+07     |
|   1391 |      1.22517e+06 | 111428    |     256317           |       600 |    50000 |      8e+07       |
|   1392 |      1.18932e+06 | 142847    |     287474           |      1000 |    75000 |      4.5e+07     |
|   1393 |      1.20728e+06 | 144548    |     292238           |      1000 |    75000 |      5.6e+07     |
|   1394 |      1.21571e+06 | 146790    |     305397           |       750 |    75000 |      4.55e+07    |
|   1395 |      1.23181e+06 | 150941    |     325466           |       500 |    80000 |      6.6e+07     |
|   1396 |      1.25768e+06 | 165915    |     386696           |      1000 |    88000 |      6.6e+07     |
|   1397 |      1.22093e+06 | 216154    |     513150           |      1500 |   110000 |      9.18e+07    |
|   1398 |      1.14916e+06 | 284890    |     700473           |      1000 |   150000 |      1.2e+08     |
|   1399 |      1.10205e+06 | 397307    |     892634           |      2500 |   200000 |      1.2e+08     |
|   1400 |      1.12713e+06 | 593368    |          1.20152e+06 |      5000 |   320000 |      1.59e+08    |
|   1401 |      1.08138e+06 | 963649    |          2.08837e+06 |      4000 |   500000 |      4e+08       |


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
| 1369-1373 | [COL4](/HBSIR/tables/raw/food#col4) |
| 1374-1401 |                                     |


#### Summary Statistics

**category data**

|   Year |   Free_Price |   Subsidised_Price |   nan |
|-------:|-------------:|-------------------:|------:|
|   1369 |        78.72 |              21.28 |  0    |
|   1370 |        81.58 |              18.15 |  0.27 |
|   1371 |        86.05 |              13.76 |  0.19 |
|   1372 |        87.39 |              12.47 |  0.14 |
|   1373 |        87.05 |              11.79 |  1.16 |


#### Categories

|    | 1369-1373        |
|---:|:-----------------|
|  0 | Free_Price       |
|  1 | Subsidised_Price |


