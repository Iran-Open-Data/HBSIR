# entertainment

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

| Years     | ID                                                 |
|:----------|:---------------------------------------------------|
| 1363-1401 | [ADDRESS](/HBSIR/tables/raw/entertainment#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |      Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|------------:|------------:|
|   1363 |   45098 | 734849           |     497626           |  1001          | 1.03415e+06 | 1.23452e+06 |
|   1364 |   43776 | 688201           |     505612           |  1001          | 1.02418e+06 | 1.23442e+06 |
|   1365 |    5783 | 668622           |     529764           |  1003          | 1.03102e+06 | 1.23422e+06 |
|   1366 |    7742 | 681041           |     522824           |  1002          | 1.03202e+06 | 1.23421e+06 |
|   1367 |   11482 | 646259           |     519919           |  1002          | 1.02204e+06 | 1.23428e+06 |
|   1368 |   16485 | 657383           |     512219           |  1004          | 1.02101e+06 | 1.23428e+06 |
|   1369 |   24090 | 638057           |     512843           |  1001          | 1.01305e+06 | 1.23422e+06 |
|   1370 |   30851 | 628978           |     508263           |  1001          | 1.01102e+06 | 1.23422e+06 |
|   1371 |   29581 | 641482           |     505842           |  1002          | 1.01301e+06 | 1.23422e+06 |
|   1372 |   21412 | 673681           |     503756           |  1001          | 1.02106e+06 | 1.23422e+06 |
|   1373 |   34852 | 770444           |     497974           |  1001          | 1.06207e+06 | 1.24404e+06 |
|   1374 |   68849 |      7.26269e+06 |          5.01709e+06 | 10001          | 1.052e+07   | 1.24401e+07 |
|   1375 |   37446 | 661723           |     515542           |  1001          | 1.02407e+06 | 1.24404e+06 |
|   1376 |   38697 | 664372           |     515285           |  1001          | 1.02405e+06 | 1.25406e+06 |
|   1377 |   29980 |      6.55837e+07 |          5.13341e+07 | 11001          | 1.02161e+08 | 1.27074e+08 |
|   1378 |   50266 |      6.55855e+07 |          5.15434e+07 | 11001          | 1.01054e+08 | 1.27074e+08 |
|   1379 |   48059 |      6.45965e+07 |          5.14345e+07 | 11005          | 1.00063e+08 | 1.27074e+08 |
|   1380 |   48145 |      6.51567e+07 |          5.13029e+07 | 11003          | 1.01033e+08 | 1.27074e+08 |
|   1381 |   62407 |      6.68381e+07 |          5.11265e+07 | 11002          | 1.01053e+08 | 1.27074e+08 |
|   1382 |   50294 |      6.70445e+07 |          5.12957e+07 | 11002          | 1.02023e+08 | 1.27114e+08 |
|   1383 |   62005 |      6.73303e+07 |          5.13509e+07 | 11001          | 1.02021e+08 | 1.27114e+08 |
|   1384 |   61274 |      6.73411e+07 |          5.108e+07   | 11003          | 1.02013e+08 | 1.29214e+08 |
|   1385 |   58358 |      6.44563e+07 |          5.16534e+07 | 11001          | 1.00014e+08 | 1.29214e+08 |
|   1386 |   55736 |      6.88507e+07 |          5.05613e+07 | 11006          | 1.02024e+08 | 1.29214e+08 |
|   1387 |   59976 |      1.57926e+09 |          5.00566e+08 |     1e+09      | 1.27706e+09 | 2.29786e+09 |
|   1388 |   49025 |      1.55107e+09 |          4.96542e+08 |     1e+09      | 1.25009e+09 | 2.29025e+09 |
|   1389 |   43905 |      1.56014e+09 |          4.95898e+08 |     1e+09      | 1.25006e+09 | 2.29013e+09 |
|   1390 |   40874 |      1.58165e+09 |          4.98886e+08 |     1e+09      | 1.27011e+09 | 2.30013e+09 |
|   1391 |   39622 |      1.59294e+09 |          4.99514e+08 |     1e+09      | 1.28007e+09 | 2.30013e+09 |
|   1392 |   36880 |      1.57833e+10 |          4.98836e+09 |     1.0001e+10 | 1.28026e+10 | 2.30047e+10 |
|   1393 |   35939 |      1.59009e+10 |          4.99175e+09 |     1.0001e+10 | 1.28046e+10 | 2.30047e+10 |
|   1394 |   34513 |      1.59703e+10 |          4.98738e+09 |     1.0001e+10 | 1.29016e+10 | 2.30047e+10 |
|   1395 |   33051 |      1.59883e+10 |          4.99936e+09 |     1.0001e+10 | 1.28026e+10 | 2.30047e+10 |
|   1396 |   34009 |      1.59733e+10 |          5.01621e+09 |     1.0001e+10 | 1.28016e+10 | 2.30047e+10 |
|   1397 |   31961 |      1.581e+10   |          5.01475e+09 |     1.0001e+10 | 1.27073e+10 | 2.30067e+10 |
|   1398 |   25499 |      1.57721e+10 |          4.97913e+09 |     1.0001e+10 | 1.27083e+10 | 2.30067e+10 |
|   1399 |   17725 |      1.60111e+10 |          4.99668e+09 |     1.0001e+10 | 1.27123e+10 | 2.30067e+10 |
|   1400 |   20441 |      1.60984e+10 |          4.97592e+09 |     1.0001e+10 | 1.28034e+10 | 2.30067e+10 |
|   1401 |   23632 |      1.61102e+10 |          5.00165e+09 |     1.0001e+10 | 1.28054e+10 | 2.30067e+10 |


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

| Years     | Code                                               |
|:----------|:---------------------------------------------------|
| 1363-1383 | [COL1](/HBSIR/tables/raw/entertainment#col1)       |
| 1384-1401 | [DYCOL01](/HBSIR/tables/raw/entertainment#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 |   45098 | 72156.8 |               333.76 |     71417 |    72329 |     72395 |
|   1364 |   43776 | 72148.6 |               346.28 |     71417 |    72329 |     79995 |
|   1365 |    5783 | 72161.8 |               324.3  |     71417 |    72318 |     72340 |
|   1366 |    7742 | 72177.9 |               319.06 |     71417 |    72329 |     72395 |
|   1367 |   11482 | 72230   |               268.05 |     71417 |    72329 |     72395 |
|   1368 |   16485 | 72210.8 |               289.14 |     71417 |    72329 |     72395 |
|   1369 |   24090 | 72222.3 |               273.32 |     71417 |    72329 |     72395 |
|   1370 |   30851 | 72205.3 |               296.46 |     71417 |    72329 |     72395 |
|   1371 |   29581 | 72195   |               306.74 |     71360 |    72329 |     72395 |
|   1372 |   21412 | 72215.5 |               286.04 |     71417 |    72329 |     72395 |
|   1373 |   34852 | 72200.9 |               295.8  |     71417 |    72329 |     72395 |
|   1374 |   68849 | 72227.5 |               269.97 |     71417 |    72330 |     72395 |
|   1375 |   37446 | 72224.4 |               271.17 |     71417 |    72330 |     72395 |
|   1376 |   38697 | 72215.2 |               279.17 |     71417 |    72329 |     72395 |
|   1377 |   29980 | 72211   |               283.46 |     71417 |    72329 |     72395 |
|   1378 |   50266 | 72186.6 |               310.37 |     71417 |    72329 |     72395 |
|   1379 |   48059 | 72173.6 |               321.46 |     71417 |    72329 |     72395 |
|   1380 |   48145 | 72155.7 |               334.04 |     71417 |    72318 |     72395 |
|   1381 |   62407 | 72111.1 |               365.08 |     71417 |    72318 |     72395 |
|   1382 |   50294 | 72071.6 |               385.37 |     71417 |    72318 |     72395 |
|   1383 |   62005 | 94502.1 |              1445    |     91216 |    95411 |     95428 |
|   1384 |   61274 | 94526.5 |              1414.63 |     91216 |    95411 |     95435 |
|   1385 |   58358 | 94537   |              1403.67 |     91216 |    95411 |     95435 |
|   1386 |   55736 | 94681.3 |              1281.91 |     91216 |    95411 |     95435 |
|   1387 |   59976 | 94746.4 |              1229.2  |     91216 |    95411 |     95435 |
|   1388 |   49025 | 94780.4 |              1181.14 |     91211 |    95411 |     95435 |
|   1389 |   43905 | 94754.3 |              1186.4  |     91216 |    95411 |     95435 |
|   1390 |   40874 | 94786.5 |              1137.23 |     91216 |    95411 |     95435 |
|   1391 |   39622 | 94891.7 |              1035.53 |     91216 |    95411 |     95435 |
|   1392 |   36880 | 94884.6 |              1003.01 |     91216 |    95411 |     95435 |
|   1393 |   35939 | 94896.8 |               988.19 |     91216 |    95412 |     95435 |
|   1394 |   34513 | 94958.2 |               921.73 |     91216 |    95413 |     95435 |
|   1395 |   33051 | 94958.1 |               899.98 |     91216 |    95413 |     95435 |
|   1396 |   34009 | 94946.6 |               914.56 |     91216 |    95413 |     95435 |
|   1397 |   31961 | 94961.6 |               863.46 |     91216 |    95413 |     95435 |
|   1398 |   25499 | 95029.2 |               786.79 |     91216 |    95413 |     95435 |
|   1399 |   17725 | 95090.5 |               783.21 |     91216 |    95413 |     95435 |
|   1400 |   20441 | 95100.4 |               746.83 |     91216 |    95413 |     95435 |
|   1401 |   23632 | 95117.3 |               707.16 |     91216 |    95413 |     95435 |


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

| Years     | Provision_Method                                   |
|:----------|:---------------------------------------------------|
| 1363-1383 | [COL3](/HBSIR/tables/raw/entertainment#col3)       |
| 1384-1401 | [DYCOL02](/HBSIR/tables/raw/entertainment#dycol02) |


#### Summary Statistics

**category data**

|   Year | Purchase   |   Non_Agricultural_Work |   Donation | Instead_of_Private_Service   | Instead_of_Public_Service   | Agricultural_Work   | Home_Production   | Purchase_Free_Price   | Purchase_Subsidised_Price   | nan   | Instead_of_Cooperative_Service   |
|-------:|:-----------|------------------------:|-----------:|:-----------------------------|:----------------------------|:--------------------|:------------------|:----------------------|:----------------------------|:------|:---------------------------------|
|   1363 |            |                    1.47 |       0.46 | 0.0                          | 0.06                        | 0.06                | 0.0               | 78.74                 | 19.2                        |       |                                  |
|   1364 |            |                    1.41 |       0.27 | 0.01                         | 0.02                        | 0.0                 | 0.01              | 82.1                  | 16.18                       |       |                                  |
|   1365 |            |                    0.76 |       0.16 | 0.02                         | 0.03                        | 0.03                |                   | 72.54                 | 26.46                       |       |                                  |
|   1366 |            |                    0.58 |       0.52 |                              | 0.1                         |                     |                   | 68.25                 | 30.55                       |       |                                  |
|   1367 |            |                    0.48 |       0.33 | 0.02                         | 0.21                        |                     |                   | 75.07                 | 23.89                       |       |                                  |
|   1368 |            |                    0.83 |       0.15 | 0.03                         | 0.05                        |                     | 0.02              | 77.85                 | 21.07                       |       |                                  |
|   1369 | 98.24      |                    1.15 |       0.24 | 0.01                         | 0.07                        | 0.01                | 0.01              |                       |                             | 0.27  |                                  |
|   1370 | 98.55      |                    1.14 |       0.12 | 0.03                         | 0.07                        | 0.02                | 0.02              |                       |                             | 0.06  |                                  |
|   1371 | 98.53      |                    1.24 |       0.13 | 0.01                         | 0.01                        | 0.01                | 0.01              |                       |                             | 0.06  |                                  |
|   1372 | 98.74      |                    0.98 |       0.16 |                              | 0.02                        |                     | 0.02              |                       |                             | 0.07  |                                  |
|   1373 | 98.37      |                    1.26 |       0.2  | 0.02                         | 0.05                        | 0.01                | 0.05              |                       |                             | 0.05  |                                  |
|   1374 | 98.5       |                    1.19 |       0.17 | 0.02                         | 0.06                        | 0.02                | 0.03              |                       |                             | 0.0   |                                  |
|   1375 | 98.54      |                    1.2  |       0.15 | 0.02                         | 0.06                        |                     | 0.03              |                       |                             |       |                                  |
|   1376 | 98.66      |                    1.05 |       0.12 | 0.02                         | 0.09                        | 0.04                | 0.02              |                       |                             |       |                                  |
|   1377 | 98.33      |                    1.26 |       0.25 | 0.05                         | 0.1                         | 0.01                | 0.01              |                       |                             |       |                                  |
|   1378 | 98.18      |                    1.21 |       0.44 | 0.02                         | 0.12                        | 0.01                | 0.01              |                       |                             |       |                                  |
|   1379 | 98.51      |                    1.1  |       0.28 | 0.02                         | 0.07                        | 0.01                | 0.01              |                       |                             |       |                                  |
|   1380 | 98.62      |                    1.02 |       0.25 | 0.01                         | 0.07                        |                     | 0.02              |                       |                             |       | 0.01                             |
|   1381 | 98.6       |                    1.1  |       0.21 | 0.01                         | 0.06                        | 0.0                 | 0.01              |                       |                             |       | 0.0                              |
|   1382 | 98.8       |                    0.89 |       0.19 | 0.02                         | 0.07                        | 0.02                | 0.02              |                       |                             |       |                                  |
|   1383 | 98.93      |                    0.76 |       0.17 | 0.03                         | 0.09                        | 0.02                | 0.01              |                       |                             |       | 0.0                              |
|   1384 | 98.82      |                    0.81 |       0.17 | 0.04                         | 0.15                        | 0.01                | 0.01              |                       |                             |       | 0.0                              |
|   1385 | 98.67      |                    1.04 |       0.16 | 0.02                         | 0.1                         | 0.01                | 0.0               |                       |                             |       | 0.0                              |
|   1386 | 98.92      |                    0.85 |       0.13 | 0.01                         | 0.08                        | 0.01                |                   |                       |                             |       | 0.0                              |
|   1387 | 99.25      |                    0.59 |       0.1  | 0.01                         | 0.05                        | 0.0                 |                   |                       |                             |       | 0.01                             |
|   1388 | 99.42      |                    0.41 |       0.09 | 0.02                         | 0.05                        | 0.01                |                   |                       |                             |       |                                  |
|   1389 | 99.45      |                    0.38 |       0.09 | 0.04                         | 0.04                        |                     |                   |                       |                             |       |                                  |
|   1390 | 99.44      |                    0.39 |       0.07 | 0.0                          | 0.09                        |                     | 0.01              |                       |                             |       |                                  |
|   1391 | 99.53      |                    0.29 |       0.11 | 0.01                         | 0.06                        |                     | 0.01              |                       |                             |       |                                  |
|   1392 | 99.63      |                    0.27 |       0.06 | 0.01                         | 0.02                        |                     | 0.01              |                       |                             |       |                                  |
|   1393 | 99.61      |                    0.29 |       0.06 | 0.01                         | 0.03                        |                     |                   |                       |                             |       |                                  |
|   1394 | 99.68      |                    0.27 |       0.03 | 0.0                          | 0.02                        | 0.0                 |                   |                       |                             |       |                                  |
|   1395 | 99.41      |                    0.35 |       0.14 | 0.05                         | 0.04                        | 0.0                 |                   |                       |                             |       |                                  |
|   1396 | 99.31      |                    0.49 |       0.15 | 0.0                          | 0.04                        |                     | 0.0               |                       |                             |       |                                  |
|   1397 | 99.52      |                    0.22 |       0.18 | 0.04                         | 0.03                        | 0.0                 |                   |                       |                             |       | 0.0                              |
|   1398 | 99.39      |                    0.36 |       0.2  | 0.03                         | 0.02                        | 0.0                 |                   |                       |                             |       |                                  |
|   1399 | 99.48      |                    0.39 |       0.08 | 0.05                         |                             | 0.01                |                   |                       |                             |       |                                  |
|   1400 | 99.54      |                    0.33 |       0.07 | 0.05                         |                             | 0.0                 |                   |                       |                             |       |                                  |
|   1401 | 99.46      |                    0.33 |       0.16 | 0.03                         | 0.01                        | 0.01                | 0.0               |                       |                             |       |                                  |


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

| Years     | Expenditure                                        |
|:----------|:---------------------------------------------------|
| 1363-1368 | [COL4](/HBSIR/tables/raw/entertainment#col4)       |
| 1369      | [COL6](/HBSIR/tables/raw/entertainment#col6)       |
| 1370-1373 | [COL5](/HBSIR/tables/raw/entertainment#col5)       |
| 1374-1383 | [COL4](/HBSIR/tables/raw/entertainment#col4)       |
| 1384-1401 | [DYCOL03](/HBSIR/tables/raw/entertainment#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |      Mean |   Standard Deviation |   Minimum |   Median |       Maximum |
|-------:|--------:|----------:|---------------------:|----------:|---------:|--------------:|
|   1363 |   45098 |    354.57 |       1242.79        |         5 |      150 |  85000        |
|   1364 |   43776 |    376.06 |       1371.39        |         5 |      150 | 162400        |
|   1365 |    5783 |    585.64 |       1322.88        |        10 |      300 |  38000        |
|   1366 |    7742 |    538.58 |       1221.41        |         5 |      280 |  40000        |
|   1367 |   11482 |    638.93 |       1501.89        |        10 |      300 |  80000        |
|   1368 |   16485 |    716.56 |       2333.58        |        10 |      350 | 170000        |
|   1369 |   24090 |    836.92 |       5793.58        |         1 |      400 | 851272        |
|   1370 |   30849 |    992.88 |       3233.37        |        10 |      500 | 250000        |
|   1371 |   29581 |   1247.07 |       4073.2         |        20 |      550 | 300000        |
|   1372 |   21412 |   1477.92 |       4346.28        |        25 |      750 | 300000        |
|   1373 |   34852 |   2895.61 |      11282.1         |        40 |     1200 |      1.5e+06  |
|   1374 |   68846 |   3664.52 |      16096.9         |        30 |     1500 |      3e+06    |
|   1375 |   37446 |   4051.77 |       9939.25        |         8 |     2000 | 550000        |
|   1376 |   38697 |   4703.38 |      11413.9         |       100 |     2000 | 560000        |
|   1377 |   29980 |   5577.62 |      14058.7         |        50 |     2400 | 680000        |
|   1378 |   50266 |   7008.96 |      34098.7         |        50 |     3000 |      5e+06    |
|   1379 |   48059 |   8056.04 |      25921           |       100 |     3000 |      2.35e+06 |
|   1380 |   48145 |   9257.34 |      45274.6         |        60 |     3500 |      8e+06    |
|   1381 |   62407 |  10490.2  |      55439.8         |       100 |     4000 |      1e+07    |
|   1382 |   50294 |  12231.1  |      51661.7         |       100 |     5000 |      5e+06    |
|   1383 |   62005 |  13236    |      35928.9         |       100 |     5000 |      2.2e+06  |
|   1384 |   61187 |  16193.9  |      56720.2         |       100 |     6000 |      5e+06    |
|   1385 |   58358 |  18486.1  |      75388.4         |         0 |     7500 |      3.7e+06  |
|   1386 |   55735 |  20544.3  |      83822.2         |       200 |    10000 |      7.5e+06  |
|   1387 |   59976 |  23934.6  |      78590.5         |       200 |    10000 |      7.09e+06 |
|   1388 |   49025 |  28857.2  |     159904           |       500 |    12000 |      2.15e+07 |
|   1389 |   43905 |  39336.2  |     161848           |       500 |    17000 |      1e+07    |
|   1390 |   40874 |  45703.1  |     136724           |       350 |    20000 |      1.5e+07  |
|   1391 |   39622 |  64119.9  |     242810           |      1000 |    30000 |      1.6e+07  |
|   1392 |   36880 |  90148.1  |     250484           |       500 |    50000 |      1.8e+07  |
|   1393 |   35939 |  96789.1  |     263294           |      1000 |    50000 |      1.7e+07  |
|   1394 |   34513 | 100328    |     342226           |      2000 |    50000 |      3e+07    |
|   1395 |   33051 | 111694    |     317793           |       500 |    50000 |      2e+07    |
|   1396 |   34009 | 145936    |     629792           |      1980 |    50000 |      6e+07    |
|   1397 |   31961 | 199026    |     952036           |      1000 |   100000 |      1e+08    |
|   1398 |   25499 | 248741    |     632053           |      5000 |   120000 |      6e+07    |
|   1399 |   17725 | 309532    |          1.07681e+06 |      6000 |   150000 |      8e+07    |
|   1400 |   20441 | 449158    |          1.48492e+06 |      8000 |   200000 |      1.4e+08  |
|   1401 |   23632 | 754834    |          1.61434e+06 |     10000 |   380000 |      8e+07    |


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

| Years     | Price_System                                 |
|:----------|:---------------------------------------------|
| 1363-1368 |                                              |
| 1369-1373 | [COL4](/HBSIR/tables/raw/entertainment#col4) |
| 1374-1401 |                                              |


#### Summary Statistics

**category data**

|   Year |   Free_Price |   Subsidised_Price |   nan |
|-------:|-------------:|-------------------:|------:|
|   1369 |        84.9  |              14.79 |  0.32 |
|   1370 |        88.77 |              11.15 |  0.08 |
|   1371 |        94.01 |               5.91 |  0.08 |
|   1372 |        95.54 |               4.39 |  0.07 |
|   1373 |        91.18 |               8.4  |  0.42 |


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

| Years     | Amount                                       |
|:----------|:---------------------------------------------|
| 1363-1368 |                                              |
| 1369      | [COL5](/HBSIR/tables/raw/entertainment#col5) |
| 1370-1401 |                                              |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1369 |    1928 |  11.52 |                 19.5 |         1 |        5 |       400 |


