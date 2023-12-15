# miscellaneous

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
| 1363-1401 | [ADDRESS](/HBSIR/tables/raw/miscellaneous#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |      Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|------------:|------------:|
|   1363 |   58929 | 726121           |     496490           |  1001          | 1.03403e+06 | 1.23452e+06 |
|   1364 |   57932 | 673384           |     505381           |  1001          | 1.02405e+06 | 1.23442e+06 |
|   1365 |    9518 | 624499           |     528784           |  1002          | 1.013e+06   | 1.23422e+06 |
|   1366 |   10955 | 623823           |     522303           |  1001          | 1.01102e+06 | 1.23421e+06 |
|   1367 |   15847 | 637381           |     519386           |  1001          | 1.02104e+06 | 1.23428e+06 |
|   1368 |   25466 | 615044           |     512775           |  1001          | 1.00208e+06 | 1.23428e+06 |
|   1369 |   40763 | 616085           |     511472           |  1003          | 1.00404e+06 | 1.23422e+06 |
|   1370 |   43344 | 622360           |     508863           |  1001          | 1.00411e+06 | 1.23422e+06 |
|   1371 |   44452 | 632533           |     507669           |  1001          | 1.01113e+06 | 1.23422e+06 |
|   1372 |   30095 | 652352           |     505126           |  1001          | 1.012e+06   | 1.23422e+06 |
|   1373 |   48512 | 748066           |     502648           |  1001          | 1.05102e+06 | 1.24404e+06 |
|   1374 |   88642 |      7.13825e+06 |          5.05589e+06 | 10001          | 1.04201e+07 | 1.24401e+07 |
|   1375 |   55887 | 642187           |     518391           |  1001          | 1.02109e+06 | 1.24404e+06 |
|   1376 |   57296 | 640802           |     518392           |  1001          | 1.02102e+06 | 1.25406e+06 |
|   1377 |   46962 |      6.14237e+07 |          5.18019e+07 | 11001          | 2.70642e+07 | 1.27074e+08 |
|   1378 |   75720 |      6.18762e+07 |          5.13821e+07 | 11001          | 2.60341e+07 | 1.27074e+08 |
|   1379 |   77246 |      6.04714e+07 |          5.12481e+07 | 11001          | 2.60311e+07 | 1.27074e+08 |
|   1380 |   83230 |      6.13998e+07 |          5.13438e+07 | 11001          | 2.60341e+07 | 1.27074e+08 |
|   1381 |  106742 |      6.31204e+07 |          5.13282e+07 | 11001          | 2.70631e+07 | 1.27074e+08 |
|   1382 |   84016 |      6.24907e+07 |          5.13434e+07 | 11001          | 2.70711e+07 | 1.27114e+08 |
|   1383 |  152425 |      6.6731e+07  |          5.13748e+07 | 11001          | 1.01093e+08 | 1.27114e+08 |
|   1384 |  141091 |      6.54357e+07 |          5.13524e+07 | 11001          | 1.01034e+08 | 1.29214e+08 |
|   1385 |  153566 |      6.20039e+07 |          5.16776e+07 | 11001          | 2.80241e+07 | 1.29214e+08 |
|   1386 |  148355 |      6.51191e+07 |          5.09588e+07 | 11001          | 1.00041e+08 | 1.29214e+08 |
|   1387 |  179795 |      1.61905e+09 |          5.03365e+08 |     1e+09      | 1.28741e+09 | 2.29786e+09 |
|   1388 |  164646 |      1.60017e+09 |          5.0259e+08  |     1e+09      | 1.28003e+09 | 2.29025e+09 |
|   1389 |  165799 |      1.62346e+09 |          5.03443e+08 |     1e+09      | 1.28012e+09 | 2.29013e+09 |
|   1390 |  167337 |      1.63427e+09 |          5.05019e+08 |     1e+09      | 1.30002e+09 | 2.30013e+09 |
|   1391 |  168300 |      1.6442e+09  |          5.04664e+08 |     1e+09      | 1.30008e+09 | 2.30013e+09 |
|   1392 |  166831 |      1.6275e+10  |          5.03587e+09 |     1.0001e+10 | 1.29076e+10 | 2.30047e+10 |
|   1393 |  164830 |      1.63101e+10 |          5.0414e+09  |     1.0001e+10 | 1.29086e+10 | 2.30047e+10 |
|   1394 |  167267 |      1.6309e+10  |          5.03941e+09 |     1.0001e+10 | 1.29115e+10 | 2.30047e+10 |
|   1395 |  163944 |      1.62925e+10 |          5.03693e+09 |     1.0001e+10 | 1.29056e+10 | 2.30047e+10 |
|   1396 |  167212 |      1.62692e+10 |          5.03595e+09 |     1.0001e+10 | 1.29016e+10 | 2.30047e+10 |
|   1397 |  164207 |      1.60775e+10 |          5.03434e+09 |     1.0001e+10 | 1.28023e+10 | 2.30067e+10 |
|   1398 |  149582 |      1.60688e+10 |          5.04045e+09 |     1.0001e+10 | 1.28024e+10 | 2.30067e+10 |
|   1399 |  141004 |      1.60997e+10 |          5.0373e+09  |     1.0001e+10 | 1.28034e+10 | 2.30067e+10 |
|   1400 |  146826 |      1.60324e+10 |          5.02424e+09 |     1.0001e+10 | 1.28023e+10 | 2.30067e+10 |
|   1401 |  138888 |      1.60286e+10 |          5.02208e+09 |     1.0001e+10 | 1.28023e+10 | 2.30067e+10 |


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
| 1363-1383 | [COL1](/HBSIR/tables/raw/miscellaneous#col1)       |
| 1384-1401 | [DYCOL01](/HBSIR/tables/raw/miscellaneous#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |     Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|---------:|---------------------:|----------:|---------:|----------:|
|   1363 |   58929 |  81312.7 |               503.84 |     81115 |    81126 |     84179 |
|   1364 |   57932 |  81270.6 |               364.12 |     81115 |    81126 |     83132 |
|   1365 |    9518 |  81253.1 |               369.5  |     81115 |    81126 |     83132 |
|   1366 |   10955 |  81251.2 |               329.9  |     81115 |    81126 |     83132 |
|   1367 |   15847 |  81242.4 |               320.98 |     81115 |    81126 |     83132 |
|   1368 |   25466 |  81254.6 |               333.31 |     81115 |    81126 |     83132 |
|   1369 |   40763 |  81234.9 |               256.68 |     81115 |    81126 |     86196 |
|   1370 |   43344 |  81221.4 |               236.62 |     81115 |    81137 |     86120 |
|   1371 |   44452 |  81221   |               224.69 |     81115 |    81137 |     83121 |
|   1372 |   30095 |  81219.2 |               199.39 |     81115 |    81137 |     83121 |
|   1373 |   48512 |  81224.2 |               212.03 |     81115 |    81217 |     83121 |
|   1374 |   88642 |  81234.8 |               229.33 |     81115 |    81217 |     83132 |
|   1375 |   55887 |  81224.6 |               192.78 |     81115 |    81217 |     83132 |
|   1376 |   57296 |  81229.7 |               198.74 |     81115 |    81217 |     83132 |
|   1377 |   46962 |  81235.1 |               202.21 |     81115 |    81217 |     83143 |
|   1378 |   75720 |  81240.5 |               209.14 |     81115 |    81217 |     83143 |
|   1379 |   77246 |  81241.1 |               198.23 |     81115 |    81217 |     83143 |
|   1380 |   83230 |  81246.5 |               207.47 |     81115 |    81217 |     83143 |
|   1381 |  106742 |  81250.9 |               215.52 |     81115 |    81228 |     83154 |
|   1382 |   84016 |  81256   |               216.28 |     81115 |    81239 |     83154 |
|   1383 |  152425 | 121904   |              1417.22 |    121111 |   121333 |    125511 |
|   1384 |  141091 | 121342   |               359.1  |    121111 |   121333 |    124116 |
|   1385 |  153566 | 121324   |               314.81 |    121111 |   121333 |    124116 |
|   1386 |  148355 | 121322   |               318.63 |    121111 |   121333 |    124116 |
|   1387 |  179795 | 121318   |               306.72 |    121111 |   121333 |    124116 |
|   1388 |  164646 | 121319   |               308.77 |    121111 |   121333 |    124116 |
|   1389 |  165799 | 121317   |               305.08 |    121111 |   121333 |    124116 |
|   1390 |  167337 | 121317   |               305.6  |    121111 |   121333 |    124116 |
|   1391 |  168300 | 121318   |               301.59 |    121111 |   121333 |    124116 |
|   1392 |  166831 | 121313   |               295.05 |    121111 |   121333 |    124116 |
|   1393 |  164830 | 121315   |               299.86 |    121111 |   121333 |    124116 |
|   1394 |  167267 | 121311   |               285.32 |    121111 |   121333 |    124116 |
|   1395 |  163944 | 121307   |               273.14 |    121111 |   121333 |    124116 |
|   1396 |  167212 | 121308   |               274.15 |    121111 |   121333 |    124116 |
|   1397 |  164207 | 121306   |               273.52 |    121111 |   121333 |    124116 |
|   1398 |  149582 | 121299   |               247.54 |    121111 |   121333 |    124116 |
|   1399 |  141004 | 121297   |               224.93 |    121111 |   121333 |    124116 |
|   1400 |  146826 | 121292   |               226    |    121111 |   121333 |    124116 |
|   1401 |  138888 | 121292   |               231.16 |    121111 |   121333 |    124114 |


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
| 1363-1383 | [COL3](/HBSIR/tables/raw/miscellaneous#col3)       |
| 1384-1401 | [DYCOL02](/HBSIR/tables/raw/miscellaneous#dycol02) |


#### Summary Statistics

**category data**

|   Year | Purchase   |   Non_Agricultural_Work |   Instead_of_Private_Service |   Donation | Home_Production   | Purchase_Free_Price   | Purchase_Subsidised_Price   | Instead_of_Public_Service   | Agricultural_Work   | nan   | Instead_of_Cooperative_Service   |
|-------:|:-----------|------------------------:|-----------------------------:|-----------:|:------------------|:----------------------|:----------------------------|:----------------------------|:--------------------|:------|:---------------------------------|
|   1363 |            |                    0.53 |                         0.04 |       0.04 | 0.09              | 85.58                 | 13.6                        | 0.07                        | 0.05                |       |                                  |
|   1364 |            |                    0.6  |                         0.04 |       0.05 | 0.05              | 87.93                 | 11.24                       | 0.06                        | 0.04                |       |                                  |
|   1365 |            |                    0.53 |                         0.03 |       0.05 |                   | 85.43                 | 13.89                       | 0.03                        | 0.04                |       |                                  |
|   1366 |            |                    0.57 |                         0.05 |       0.05 | 0.06              | 88.07                 | 11.08                       | 0.12                        | 0.01                |       |                                  |
|   1367 |            |                    0.37 |                         0.03 |       0.04 | 0.04              | 90.18                 | 9.16                        | 0.16                        | 0.02                |       |                                  |
|   1368 |            |                    0.57 |                         0.05 |       0.04 | 0.07              | 91.77                 | 7.17                        | 0.3                         | 0.03                |       |                                  |
|   1369 | 98.68      |                    0.71 |                         0.02 |       0.02 | 0.14              |                       |                             | 0.28                        | 0.03                | 0.11  |                                  |
|   1370 | 98.98      |                    0.73 |                         0.02 |       0.05 | 0.1               |                       |                             | 0.07                        | 0.01                | 0.03  |                                  |
|   1371 | 99.01      |                    0.71 |                         0.03 |       0.08 | 0.07              |                       |                             | 0.02                        | 0.02                | 0.05  |                                  |
|   1372 | 99.13      |                    0.6  |                         0.02 |       0.03 | 0.14              |                       |                             | 0.02                        | 0.01                | 0.05  |                                  |
|   1373 | 98.86      |                    0.86 |                         0.03 |       0.01 | 0.16              |                       |                             | 0.03                        | 0.02                | 0.02  |                                  |
|   1374 | 98.96      |                    0.8  |                         0.02 |       0.03 | 0.13              |                       |                             | 0.04                        | 0.01                | 0.01  |                                  |
|   1375 | 98.98      |                    0.86 |                         0.04 |       0.01 | 0.06              |                       |                             | 0.04                        | 0.01                |       |                                  |
|   1376 | 98.86      |                    0.9  |                         0.03 |       0.03 | 0.08              |                       |                             | 0.08                        | 0.03                |       |                                  |
|   1377 | 98.73      |                    0.97 |                         0.03 |       0.03 | 0.15              |                       |                             | 0.09                        | 0.0                 |       |                                  |
|   1378 | 98.64      |                    1.14 |                         0.04 |       0.04 | 0.09              |                       |                             | 0.05                        | 0.01                |       |                                  |
|   1379 | 98.84      |                    1.05 |                         0.03 |       0.01 | 0.04              |                       |                             | 0.03                        | 0.01                |       |                                  |
|   1380 | 98.8       |                    1.1  |                         0.02 |       0.01 | 0.04              |                       |                             | 0.02                        |                     |       | 0.0                              |
|   1381 | 98.9       |                    0.93 |                         0.02 |       0.03 | 0.08              |                       |                             | 0.03                        | 0.01                |       |                                  |
|   1382 | 99.02      |                    0.86 |                         0.02 |       0.03 | 0.03              |                       |                             | 0.02                        | 0.01                |       | 0.01                             |
|   1383 | 94.22      |                    0.89 |                         1.28 |       0.75 | 0.06              |                       |                             | 2.74                        | 0.02                |       | 0.05                             |
|   1384 | 98.66      |                    1.03 |                         0.03 |       0.07 | 0.08              |                       |                             | 0.12                        | 0.01                | 0.0   | 0.0                              |
|   1385 | 98.65      |                    1.2  |                         0.01 |       0.05 | 0.0               |                       |                             | 0.07                        | 0.0                 | 0.01  | 0.01                             |
|   1386 | 98.65      |                    1.21 |                         0.01 |       0.06 | 0.0               |                       |                             | 0.06                        | 0.0                 |       | 0.0                              |
|   1387 | 98.99      |                    0.93 |                         0.02 |       0.02 | 0.0               |                       |                             | 0.03                        | 0.01                |       | 0.01                             |
|   1388 | 98.88      |                    1    |                         0.01 |       0.08 | 0.0               |                       |                             | 0.03                        | 0.0                 |       | 0.0                              |
|   1389 | 99.0       |                    0.92 |                         0.02 |       0.04 | 0.0               |                       |                             | 0.01                        |                     |       |                                  |
|   1390 | 99.15      |                    0.79 |                         0.01 |       0.02 | 0.0               |                       |                             | 0.02                        | 0.0                 |       | 0.0                              |
|   1391 | 99.19      |                    0.75 |                         0.01 |       0.03 | 0.01              |                       |                             | 0.01                        | 0.0                 |       | 0.0                              |
|   1392 | 99.31      |                    0.61 |                         0.01 |       0.02 | 0.05              |                       |                             | 0.0                         | 0.0                 |       | 0.0                              |
|   1393 | 99.32      |                    0.64 |                         0.02 |       0.02 | 0.0               |                       |                             | 0.0                         | 0.0                 |       | 0.0                              |
|   1394 | 99.28      |                    0.66 |                         0.03 |       0.03 | 0.01              |                       |                             | 0.01                        |                     |       |                                  |
|   1395 | 99.2       |                    0.75 |                         0.03 |       0.01 | 0.01              |                       |                             | 0.01                        | 0.0                 |       | 0.0                              |
|   1396 | 99.15      |                    0.78 |                         0.04 |       0.03 | 0.0               |                       |                             | 0.0                         | 0.0                 |       | 0.0                              |
|   1397 | 99.24      |                    0.69 |                         0.02 |       0.04 | 0.0               |                       |                             | 0.0                         | 0.0                 |       |                                  |
|   1398 | 99.2       |                    0.72 |                         0.01 |       0.02 | 0.04              |                       |                             | 0.01                        | 0.0                 |       | 0.0                              |
|   1399 | 99.2       |                    0.55 |                         0.03 |       0.02 | 0.2               |                       |                             | 0.0                         |                     |       |                                  |
|   1400 | 99.12      |                    0.55 |                         0.02 |       0.01 | 0.29              |                       |                             | 0.0                         | 0.0                 |       | 0.0                              |
|   1401 | 99.37      |                    0.58 |                         0.03 |       0.02 | 0.0               |                       |                             |                             |                     |       |                                  |


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
| 1363-1368 | [COL4](/HBSIR/tables/raw/miscellaneous#col4)       |
| 1369      | [COL6](/HBSIR/tables/raw/miscellaneous#col6)       |
| 1370-1373 | [COL5](/HBSIR/tables/raw/miscellaneous#col5)       |
| 1374-1383 | [COL4](/HBSIR/tables/raw/miscellaneous#col4)       |
| 1384-1401 | [DYCOL03](/HBSIR/tables/raw/miscellaneous#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |      Mean |   Standard Deviation |   Minimum |   Median |          Maximum |
|-------:|--------:|----------:|---------------------:|----------:|---------:|-----------------:|
|   1363 |   58929 |    716.32 |       3786.17        |        10 |      300 | 400000           |
|   1364 |   57932 |    713.86 |       6140.56        |        10 |      300 |      1.3e+06     |
|   1365 |    9518 |    836.4  |       5795.53        |        20 |      450 | 520000           |
|   1366 |   10955 |    850.81 |       2983.07        |        20 |      500 | 150000           |
|   1367 |   15847 |    923.15 |       3164.27        |        15 |      500 | 200000           |
|   1368 |   25466 |   1095.69 |       6121.31        |         8 |      550 | 800000           |
|   1369 |   40762 |   1152    |       3354.45        |         1 |      600 | 230000           |
|   1370 |   43343 |   1277.6  |       3147.1         |        16 |      700 | 200000           |
|   1371 |   44452 |   1582.95 |       7310.98        |         2 |      800 | 940000           |
|   1372 |   30095 |   1803.83 |       8113.88        |        30 |     1000 |      1.2e+06     |
|   1373 |   48512 |   2806.39 |      14001.2         |        40 |     1500 |      1.7e+06     |
|   1374 |   88620 |   4049.55 |      18626.7         |        70 |     2000 |      2.15e+06    |
|   1375 |   55887 |   4618.06 |      23859           |        50 |     2400 |      3.5e+06     |
|   1376 |   57296 |   5272.46 |      35988.2         |         3 |     2600 |      7.5e+06     |
|   1377 |   46962 |   6079.15 |      23984.5         |        50 |     3000 |      2.5e+06     |
|   1378 |   75720 |   6838.42 |      24817.2         |       100 |     3400 |      2.4e+06     |
|   1379 |   77246 |   7880.82 |      28617.9         |       200 |     4000 |      2.5e+06     |
|   1380 |   83230 |   9149.78 |      44323.3         |       100 |     4500 |      6.58e+06    |
|   1381 |  106742 |  10318.1  |      50945.6         |       200 |     5000 |      8e+06       |
|   1382 |   84016 |  11873.3  |      56587.2         |       150 |     5000 |      6e+06       |
|   1383 |  152425 |  20909.4  |      87230.9         |       150 |     6000 |      1.09327e+07 |
|   1384 |  141030 |  12270.1  |      27310.8         |       200 |     6000 |      2.5e+06     |
|   1385 |  153566 |  14129    |      38608.4         |         0 |     7000 |      5e+06       |
|   1386 |  148355 |  17699.6  |      51330.3         |       300 |    10000 |      6e+06       |
|   1387 |  179795 |  20627.3  |      49106.6         |       300 |    12000 |      6e+06       |
|   1388 |  164646 |  24779.1  |     303640           |       500 |    15000 |      1.2e+08     |
|   1389 |  165799 |  30246.8  |     112218           |       500 |    18000 |      2.4e+07     |
|   1390 |  167337 |  36290.5  |     109974           |       500 |    20000 |      2.5e+07     |
|   1391 |  168300 |  48494.3  |     158412           |      1000 |    30000 |      3e+07       |
|   1392 |  166831 |  68273.4  |     135195           |      1000 |    45000 |      2e+07       |
|   1393 |  164830 |  77847.9  |     185121           |      1000 |    50000 |      5e+07       |
|   1394 |  167267 |  82661.5  |     275202           |      2000 |    50000 |      7e+07       |
|   1395 |  163944 |  88478.6  |     251274           |      1000 |    50000 |      5e+07       |
|   1396 |  167212 | 100426    |     353797           |       990 |    60000 |      8.316e+07   |
|   1397 |  164207 | 137574    |     366508           |      2000 |    80000 |      6.7e+07     |
|   1398 |  149582 | 179547    |     537596           |      4000 |   120000 |      1.5e+08     |
|   1399 |  141004 | 237900    |     490112           |      5000 |   150000 |      6.8e+07     |
|   1400 |  146826 | 349072    |     589008           |      5000 |   250000 |      4.3e+07     |
|   1401 |  138888 | 540320    |          1.07112e+06 |     10000 |   350000 |      1.5e+08     |


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
| 1369-1373 | [COL4](/HBSIR/tables/raw/miscellaneous#col4) |
| 1374-1401 |                                              |


#### Summary Statistics

**category data**

|   Year |   Free_Price |   Subsidised_Price |   nan |
|-------:|-------------:|-------------------:|------:|
|   1369 |        95.48 |               4.35 |  0.17 |
|   1370 |        95.75 |               4.19 |  0.06 |
|   1371 |        96.58 |               3.37 |  0.05 |
|   1372 |        95.96 |               4    |  0.05 |
|   1373 |        96.3  |               2.7  |  0.99 |


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
| 1369      | [COL5](/HBSIR/tables/raw/miscellaneous#col5) |
| 1370-1401 |                                              |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1369 |     183 |  50.13 |               332.74 |         1 |        2 |      3840 |


