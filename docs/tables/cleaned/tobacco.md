# tobacco

## Old to New Titles

|   Years | ADDRESS   | COL1           | COL3             | COL4   | COL5   | COL6   | COL7        |
|--------:|:----------|:---------------|:-----------------|:-------|:-------|:-------|:------------|
|    1383 | ID        | Commodity_Code | Provision_Method | drop   | Amount | Price  | Expenditure |


| Years     | ADDRESS   | DYCOL01        | DYCOL02          | DYCOL03   | DYCOL04   | DYCOL05   | DYCOL06     | DYCOL07   |
|:----------|:----------|:---------------|:-----------------|:----------|:----------|:----------|:------------|:----------|
| 1384      | ID        | Commodity_Code | Provision_Method | drop      | Amount    | Price     | Expenditure | drop      |
| 1385-1402 | ID        | Commodity_Code | Provision_Method | drop      | Amount    | Price     | Expenditure |           |


## New to Old Titles

| Years     | ID      | Commodity_Code   | Provision_Method   | Amount   | Price   | Expenditure   |
|:----------|:--------|:-----------------|:-------------------|:---------|:--------|:--------------|
| 1383      | ADDRESS | COL1             | COL3               | COL5     | COL6    | COL7          |
| 1384-1402 | ADDRESS | DYCOL01          | DYCOL02            | DYCOL04  | DYCOL05 | DYCOL06       |


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
| 1383-1402 | [ADDRESS](/HBSIR/tables/raw/tobacco#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |        Mean |   Standard Deviation |        Minimum |      Median |     Maximum |
|-------:|--------:|------------:|---------------------:|---------------:|------------:|------------:|
|   1383 |    8733 | 5.67004e+07 |          5.07417e+07 | 11001          | 2.4031e+07  | 1.27114e+08 |
|   1384 |    9195 | 5.8328e+07  |          5.08854e+07 | 11001          | 2.50121e+07 | 1.29214e+08 |
|   1385 |    9852 | 5.42459e+07 |          5.05789e+07 | 11001          | 2.30821e+07 | 1.29214e+08 |
|   1386 |    9377 | 5.63187e+07 |          5.01002e+07 | 11003          | 2.50121e+07 | 1.29214e+08 |
|   1387 |   10716 | 1.69128e+09 |          5.03149e+08 |     1e+09      | 2.02077e+09 | 2.29786e+09 |
|   1388 |    9582 | 1.66299e+09 |          5.04746e+08 |     1e+09      | 2.01018e+09 | 2.29024e+09 |
|   1389 |    9414 | 1.67946e+09 |          5.01428e+08 |     1e+09      | 2.02002e+09 | 2.29011e+09 |
|   1390 |    8952 | 1.6841e+09  |          5.01886e+08 |     1e+09      | 2.02e+09    | 2.30013e+09 |
|   1391 |    8804 | 1.70334e+09 |          4.99579e+08 |     1e+09      | 2.03002e+09 | 2.30013e+09 |
|   1392 |    7928 | 1.68625e+10 |          4.99191e+09 |     1.0001e+10 | 2.0116e+10  | 2.30047e+10 |
|   1393 |    7842 | 1.69167e+10 |          4.9926e+09  |     1.0001e+10 | 2.0114e+10  | 2.30047e+10 |
|   1394 |    7729 | 1.70029e+10 |          5.00994e+09 |     1.0001e+10 | 2.02071e+10 | 2.30047e+10 |
|   1395 |    7634 | 1.70507e+10 |          5.00157e+09 |     1.0001e+10 | 2.02191e+10 | 2.30047e+10 |
|   1396 |    8080 | 1.70167e+10 |          4.9994e+09  |     1.0001e+10 | 2.02101e+10 | 2.30047e+10 |
|   1397 |    8220 | 1.67706e+10 |          5.03964e+09 |     1.0001e+10 | 2.01094e+10 | 2.30067e+10 |
|   1398 |    7921 | 1.66681e+10 |          5.02807e+09 |     1.0001e+10 | 2.00124e+10 | 2.30067e+10 |
|   1399 |    6814 | 1.67569e+10 |          5.0256e+09  |     1.0001e+10 | 2.01034e+10 | 2.30067e+10 |
|   1400 |    6828 | 1.66982e+10 |          5.02842e+09 |     1.0001e+10 | 2.00124e+10 | 2.30067e+10 |
|   1401 |    6762 | 1.68044e+10 |          5.02249e+09 |     1.0001e+10 | 2.01039e+10 | 2.30067e+10 |
|   1402 |    6862 | 1.69361e+10 |          5.02042e+09 |     1.0001e+10 | 2.02144e+10 | 2.30067e+10 |


### Commodity_Code

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
    1402:
      column_code: DYCOL01
      type: UInt32
    
    ```
#### Column Codes

| Years     | Commodity_Code                               |
|:----------|:---------------------------------------------|
| 1383      | [COL1](/HBSIR/tables/raw/tobacco#col1)       |
| 1384-1402 | [DYCOL01](/HBSIR/tables/raw/tobacco#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1383 |    8733 | 21680.2 |              3040.69 |       231 |    22113 |     22115 |
|   1384 |    9195 | 22155.3 |               220.24 |     21111 |    22113 |     23111 |
|   1385 |    9852 | 22164.7 |               227.01 |     21111 |    22113 |     23111 |
|   1386 |    9377 | 22170.9 |               235.6  |     21111 |    22113 |     23111 |
|   1387 |   10716 | 22169   |               233.25 |     21111 |    22113 |     23111 |
|   1388 |    9582 | 22165.6 |               225.1  |     21111 |    22113 |     23111 |
|   1389 |    9414 | 22165.2 |               226.37 |     21111 |    22113 |     23111 |
|   1390 |    8952 | 22168.8 |               233.52 |     21111 |    22111 |     23111 |
|   1391 |    8804 | 22180.7 |               255.85 |     21111 |    22111 |     23111 |
|   1392 |    7928 | 22176   |               248.25 |     21111 |    22111 |     23111 |
|   1393 |    7842 | 22184.3 |               259.21 |     21111 |    22113 |     23111 |
|   1394 |    7729 | 22197.2 |               279.23 |     21111 |    22113 |     23111 |
|   1395 |    7634 | 22202.1 |               289.03 |     21111 |    22113 |     23111 |
|   1396 |    8080 | 22216.5 |               310.14 |     21111 |    22113 |     23111 |
|   1397 |    8220 | 22211   |               308.03 |     21111 |    22113 |     23111 |
|   1398 |    7921 | 22211.4 |               303.64 |     21111 |    22113 |     23111 |
|   1399 |    6814 | 22197.7 |               286.66 |     21111 |    22113 |     23111 |
|   1400 |    6828 | 22205.2 |               293.83 |     21111 |    22113 |     23111 |
|   1401 |    6762 | 22210.9 |               302.21 |     21111 |    22113 |     23111 |
|   1402 |    6862 | 22230.8 |               327.86 |     21111 |    22111 |     23111 |


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
| 1383      | [COL3](/HBSIR/tables/raw/tobacco#col3)       |
| 1384-1402 | [DYCOL02](/HBSIR/tables/raw/tobacco#dycol02) |


#### Summary Statistics

**category data**

|   Year |   Purchase |   Non_Agricultural_Work | Instead_of_Private_Service   | Donation   | nan   | Agricultural_Work   | Home_Production   | Instead_of_Public_Service   | Instead_of_Cooperative_Service   |
|-------:|-----------:|------------------------:|:-----------------------------|:-----------|:------|:--------------------|:------------------|:----------------------------|:---------------------------------|
|   1383 |      96.51 |                    1.26 | 0.03                         |            | 1.97  | 0.14                | 0.07              | 0.02                        |                                  |
|   1384 |      98.85 |                    1    | 0.03                         |            |       | 0.05                | 0.04              | 0.01                        | 0.01                             |
|   1385 |      98.69 |                    1.27 | 0.01                         |            |       | 0.01                |                   | 0.02                        |                                  |
|   1386 |      98.69 |                    1.22 | 0.04                         |            |       | 0.04                |                   | 0.01                        |                                  |
|   1387 |      98.96 |                    0.94 | 0.03                         |            |       | 0.02                | 0.02              | 0.03                        |                                  |
|   1388 |      98.82 |                    1.07 | 0.03                         | 0.02       |       | 0.02                | 0.01              |                             | 0.02                             |
|   1389 |      99.04 |                    0.8  | 0.03                         | 0.01       |       | 0.06                | 0.05              |                             |                                  |
|   1390 |      99.17 |                    0.74 | 0.02                         |            |       | 0.04                | 0.02              |                             |                                  |
|   1391 |      99.22 |                    0.73 |                              | 0.01       |       | 0.01                | 0.02              |                             | 0.01                             |
|   1392 |      99.53 |                    0.45 |                              |            |       | 0.01                |                   |                             |                                  |
|   1393 |      99.23 |                    0.69 | 0.03                         |            |       | 0.01                | 0.04              |                             |                                  |
|   1394 |      99.24 |                    0.66 | 0.06                         |            |       | 0.03                |                   | 0.01                        |                                  |
|   1395 |      99.19 |                    0.75 | 0.01                         |            |       | 0.04                |                   | 0.01                        |                                  |
|   1396 |      99.33 |                    0.64 | 0.01                         | 0.01       |       |                     |                   |                             |                                  |
|   1397 |      99.31 |                    0.66 | 0.01                         | 0.01       |       |                     | 0.01              |                             |                                  |
|   1398 |      99.33 |                    0.59 | 0.01                         | 0.03       |       | 0.03                |                   | 0.01                        |                                  |
|   1399 |      99.25 |                    0.65 | 0.04                         | 0.04       |       |                     | 0.01              |                             |                                  |
|   1400 |      99.34 |                    0.51 | 0.04                         | 0.09       |       |                     |                   | 0.01                        |                                  |
|   1401 |      99.48 |                    0.49 | 0.01                         |            |       | 0.01                |                   |                             |                                  |
|   1402 |      99.48 |                    0.48 | 0.03                         | 0.01       |       |                     |                   |                             |                                  |


#### Categories

|    | 1383-1400                      | 1401-1402                      |
|---:|:-------------------------------|:-------------------------------|
|  0 |                                | Secondhand_Sale                |
|  1 | Purchase                       | Purchase                       |
|  2 | Home_Production                | Home_Production                |
|  3 | Instead_of_Public_Service      | Instead_of_Public_Service      |
|  4 | Instead_of_Cooperative_Service | Instead_of_Cooperative_Service |
|  5 | Instead_of_Private_Service     | Instead_of_Private_Service     |
|  6 | Agricultural_Work              | Agricultural_Work              |
|  7 | Non_Agricultural_Work          | Non_Agricultural_Work          |
|  8 | Donation                       | Donation                       |


### Amount

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

| Years     | Amount                                       |
|:----------|:---------------------------------------------|
| 1383      | [COL5](/HBSIR/tables/raw/tobacco#col5)       |
| 1384-1402 | [DYCOL04](/HBSIR/tables/raw/tobacco#dycol04) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1383 |    7297 | 489.24 |               390.19 |         1 |      600 |     12000 |
|   1384 |    7746 | 489.72 |               334.67 |         1 |      600 |      7200 |
|   1385 |    8188 | 500.36 |               393.2  |         1 |      600 |     16801 |
|   1386 |    7881 | 499.15 |               311.53 |         1 |      600 |      3100 |
|   1387 |    9018 | 501.17 |               326.06 |         1 |      600 |      6200 |
|   1388 |    8209 | 513.9  |               333.13 |         3 |      600 |      3500 |
|   1389 |    8033 | 525.28 |               360.75 |         1 |      600 |     12000 |
|   1390 |    7631 | 531.13 |               335.34 |         4 |      600 |      6000 |
|   1391 |    7341 | 529.11 |               346.96 |         4 |      600 |      6000 |
|   1392 |    6796 | 508.6  |               316.95 |         7 |      600 |      3600 |
|   1393 |    6801 | 519.15 |               310.01 |         1 |      600 |      3200 |
|   1394 |    6495 | 519.34 |               319.63 |         2 |      600 |      3600 |
|   1395 |    6347 | 512.4  |               329.93 |         3 |      600 |      7000 |
|   1396 |    6516 | 512.96 |               321.28 |         5 |      600 |      6000 |
|   1397 |    6540 | 488.31 |               322.47 |         1 |      600 |      4000 |
|   1398 |    6381 | 482.83 |               315.78 |         1 |      600 |      4340 |
|   1399 |    5562 | 450.95 |               290.17 |         1 |      500 |      3000 |
|   1400 |    5505 | 453.75 |               284.18 |         1 |      560 |      3500 |
|   1401 |    5462 | 486.43 |               334.37 |         2 |      600 |      6000 |
|   1402 |    5458 | 497.2  |               315.35 |         4 |      600 |      3600 |


### Price

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

| Years     | Price                                        |
|:----------|:---------------------------------------------|
| 1383      | [COL6](/HBSIR/tables/raw/tobacco#col6)       |
| 1384-1402 | [DYCOL05](/HBSIR/tables/raw/tobacco#dycol05) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1383 |    7298 |  266.25 |              2721.69 |        25 |      150 |    140000 |
|   1384 |    7750 |  352.3  |              2956.58 |        20 |      165 |    100000 |
|   1385 |    8188 |  299.88 |              2621.52 |         0 |      200 |    100000 |
|   1386 |    7881 |  262.32 |               775.41 |        10 |      225 |     50000 |
|   1387 |    9018 |  293.51 |               228.93 |        25 |      250 |      5000 |
|   1388 |    8209 |  329.6  |               233.34 |        30 |      250 |      4250 |
|   1389 |    8033 |  343.42 |               235.4  |        50 |      250 |      5000 |
|   1390 |    7631 |  405.96 |               339.55 |        40 |      300 |      9500 |
|   1391 |    7342 |  644.49 |               517.6  |        50 |      500 |     12000 |
|   1392 |    6796 |  964.02 |               667.08 |       100 |      750 |     15000 |
|   1393 |    6801 |  970.6  |              1245.05 |        50 |      800 |     80000 |
|   1394 |    6495 | 1008.1  |               758.75 |       150 |      870 |     20000 |
|   1395 |    6347 | 1107.37 |               859.1  |       200 |     1000 |     30000 |
|   1396 |    6516 | 1165.94 |               854.13 |       200 |     1000 |     35000 |
|   1397 |    6540 | 2442.36 |             15753.6  |       100 |     2000 |    900000 |
|   1398 |    6381 | 2834.38 |              6385.6  |       200 |     2500 |    500000 |
|   1399 |    5562 | 3767.9  |              3298.37 |       200 |     3000 |    120000 |
|   1400 |    5505 | 5156.22 |              5316.37 |       250 |     4000 |    100000 |
|   1401 |    6762 | 5710.75 |              8791.54 |         0 |     5000 |    170000 |
|   1402 |    6862 | 6856.43 |              5512.61 |         0 |     7000 |    100000 |


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
    1402:
      column_code: DYCOL06
      type: float
    
    ```
#### Column Codes

| Years     | Expenditure                                  |
|:----------|:---------------------------------------------|
| 1383      | [COL7](/HBSIR/tables/raw/tobacco#col7)       |
| 1384-1402 | [DYCOL06](/HBSIR/tables/raw/tobacco#dycol06) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |   Minimum |         Median |   Maximum |
|-------:|--------:|-----------------:|---------------------:|----------:|---------------:|----------:|
|   1383 |    8733 |  74788.1         |      94821           |       600 |  60000         |  4.2e+06  |
|   1384 |    9188 |  85764.6         |      97571.6         |       400 |  62000         |  2e+06    |
|   1385 |    9852 |  98100.3         |     141284           |         0 |  75000         |  9.9e+06  |
|   1386 |    9377 | 116656           |     131570           |       600 |  90000         |  4e+06    |
|   1387 |   10716 | 138664           |     157120           |       500 | 100000         |  3e+06    |
|   1388 |    9582 | 158338           |     182299           |       600 | 120000         |  4.5e+06  |
|   1389 |    9414 | 178470           |     233393           |      1000 | 135000         |  6.2e+06  |
|   1390 |    8952 | 214039           |     270294           |      1200 | 150000         |  6e+06    |
|   1391 |    8804 | 339534           |     419558           |      1920 | 240000         |  1.2e+07  |
|   1392 |    7927 | 487096           |     520898           |      5000 | 390000         |  1.5e+07  |
|   1393 |    7842 | 504727           |     477301           |      7500 | 450000         |  7.5e+06  |
|   1394 |    7729 | 518405           |     507510           |      5000 | 450000         |  9.3e+06  |
|   1395 |    7634 | 570229           |     587379           |      3000 | 450000         |  1.2e+07  |
|   1396 |    8080 | 625937           |     697291           |      7000 | 450000         |  2.02e+07 |
|   1397 |    8220 |      1.007e+06   |     991471           |      9000 | 750000         |  2.1e+07  |
|   1398 |    7921 |      1.25049e+06 |          1.07356e+06 |      2000 |      1.085e+06 |  1.7e+07  |
|   1399 |    6814 |      1.55012e+06 |          1.49873e+06 |      6000 |      1.24e+06  |  3.1e+07  |
|   1400 |    6828 |      2.14038e+06 |          2.03606e+06 |     12000 |      1.8e+06   |  3e+07    |
|   1401 |    6762 |      3.1471e+06  |          3.64006e+06 |     16000 |      2.4e+06   |  1.2e+08  |
|   1402 |    6862 |      4.85862e+06 |          5.69519e+06 |     20000 |      3.6e+06   |  1.2e+08  |


