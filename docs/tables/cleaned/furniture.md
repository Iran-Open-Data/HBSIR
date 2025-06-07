# furniture

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

| Years     | ID                                             |
|:----------|:-----------------------------------------------|
| 1363-1402 | [ADDRESS](/HBSIR/tables/raw/furniture#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |      Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|------------:|------------:|
|   1363 |  140285 | 714044           |     501068           |  1001          | 1.0332e+06  | 1.23452e+06 |
|   1364 |  129986 | 672424           |     505972           |  1001          | 1.02305e+06 | 1.23442e+06 |
|   1365 |   19794 | 648539           |     531311           |  1001          | 1.02203e+06 | 1.23422e+06 |
|   1366 |   25933 | 658046           |     524724           |  1001          | 1.02303e+06 | 1.23421e+06 |
|   1367 |   35949 | 658122           |     520986           |  1001          | 1.02402e+06 | 1.23428e+06 |
|   1368 |   54679 | 640789           |     516546           |  1001          | 1.00403e+06 | 1.23428e+06 |
|   1369 |   93959 | 615165           |     512692           |  1001          | 1.00403e+06 | 1.23422e+06 |
|   1370 |  102553 | 609291           |     510552           |  1001          | 1.00304e+06 | 1.23422e+06 |
|   1371 |   99264 | 621823           |     510041           |  1001          | 1.00408e+06 | 1.23422e+06 |
|   1372 |   69356 | 655803           |     508032           |  1001          | 1.01213e+06 | 1.23422e+06 |
|   1373 |  112092 | 750240           |     505512           |  1001          | 1.05307e+06 | 1.24404e+06 |
|   1374 |  203063 |      7.16114e+06 |          5.07827e+06 | 10001          | 1.044e+07   | 1.24401e+07 |
|   1375 |  122378 | 646583           |     520645           |  1001          | 1.02109e+06 | 1.24404e+06 |
|   1376 |  124613 | 643171           |     519870           |  1001          | 1.01405e+06 | 1.25406e+06 |
|   1377 |  100565 |      6.17454e+07 |          5.18767e+07 | 11001          | 2.70642e+07 | 1.27074e+08 |
|   1378 |  167718 |      6.18855e+07 |          5.15433e+07 | 11001          | 2.60331e+07 | 1.27074e+08 |
|   1379 |  167927 |      6.0659e+07  |          5.12909e+07 | 11001          | 2.60241e+07 | 1.27074e+08 |
|   1380 |  181241 |      6.05686e+07 |          5.13014e+07 | 11001          | 2.60321e+07 | 1.27074e+08 |
|   1381 |  231860 |      6.17937e+07 |          5.1259e+07  | 11001          | 2.7034e+07  | 1.27074e+08 |
|   1382 |  177606 |      6.12928e+07 |          5.12757e+07 | 11001          | 2.60431e+07 | 1.27114e+08 |
|   1383 |  220236 |      6.20457e+07 |          5.13272e+07 | 11002          | 2.7034e+07  | 1.27114e+08 |
|   1384 |  224538 |      6.24167e+07 |          5.1138e+07  | 11001          | 2.8024e+07  | 1.29214e+08 |
|   1385 |  229205 |      5.93617e+07 |          5.14069e+07 | 11001          | 2.7034e+07  | 1.29214e+08 |
|   1386 |  229663 |      6.22584e+07 |          5.08426e+07 | 11001          | 2.82521e+07 | 1.29214e+08 |
|   1387 |  258180 |      1.64753e+09 |          5.04939e+08 |     1e+09      | 2.00017e+09 | 2.29786e+09 |
|   1388 |  229173 |      1.63035e+09 |          5.05014e+08 |     1e+09      | 1.29003e+09 | 2.29025e+09 |
|   1389 |  229333 |      1.65091e+09 |          5.04698e+08 |     1e+09      | 2.0001e+09  | 2.29013e+09 |
|   1390 |  222368 |      1.66053e+09 |          5.06163e+08 |     1e+09      | 2.00014e+09 | 2.30013e+09 |
|   1391 |  219072 |      1.6651e+09  |          5.04485e+08 |     1e+09      | 2.00016e+09 | 2.30013e+09 |
|   1392 |  208271 |      1.65368e+10 |          5.04025e+09 |     1.0001e+10 | 2.0003e+10  | 2.30047e+10 |
|   1393 |  203190 |      1.65503e+10 |          5.039e+09   |     1.0001e+10 | 2.0004e+10  | 2.30047e+10 |
|   1394 |  209442 |      1.65406e+10 |          5.03733e+09 |     1.0001e+10 | 2.0004e+10  | 2.30047e+10 |
|   1395 |  204035 |      1.6531e+10  |          5.04574e+09 |     1.0001e+10 | 2.0004e+10  | 2.30047e+10 |
|   1396 |  208478 |      1.65185e+10 |          5.04733e+09 |     1.0001e+10 | 2.00015e+10 | 2.30047e+10 |
|   1397 |  198686 |      1.62874e+10 |          5.05661e+09 |     1.0001e+10 | 1.29034e+10 | 2.30067e+10 |
|   1398 |  183177 |      1.62685e+10 |          5.0535e+09  |     1.0001e+10 | 1.29024e+10 | 2.30067e+10 |
|   1399 |  188779 |      1.62152e+10 |          5.04932e+09 |     1.0001e+10 | 1.28074e+10 | 2.30067e+10 |
|   1400 |  184265 |      1.62343e+10 |          5.03971e+09 |     1.0001e+10 | 1.29024e+10 | 2.30067e+10 |
|   1401 |  171054 |      1.62293e+10 |          5.04215e+09 |     1.0001e+10 | 1.29014e+10 | 2.30067e+10 |
|   1402 |  167022 |      1.61634e+10 |          5.04419e+09 |     1.0001e+10 | 1.28044e+10 | 2.30067e+10 |


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

| Years     | Commodity_Code                                 |
|:----------|:-----------------------------------------------|
| 1363-1383 | [COL1](/HBSIR/tables/raw/furniture#col1)       |
| 1384-1402 | [DYCOL01](/HBSIR/tables/raw/furniture#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 |  140285 | 44908.3 |               771.13 |     42113 |    45122 |     46250 |
|   1364 |  129986 | 44919   |               733.15 |     42113 |    45122 |     49994 |
|   1365 |   19794 | 45008.4 |               641.8  |     42113 |    45122 |     49994 |
|   1366 |   25933 | 44982.4 |               641.56 |     42113 |    45122 |     49994 |
|   1367 |   35949 | 44992.5 |               613.55 |     42113 |    45122 |     49994 |
|   1368 |   54679 | 44940.4 |               667.38 |     42113 |    45122 |     49994 |
|   1369 |   93959 | 44950.5 |               640.72 |     42113 |    45133 |     46250 |
|   1370 |  102553 | 44937.2 |               652.43 |     41121 |    45133 |     46227 |
|   1371 |   99264 | 44951.6 |               641.2  |     41132 |    45133 |     46227 |
|   1372 |   69356 | 44972.7 |               618.29 |     42113 |    45133 |     46227 |
|   1373 |  112092 | 44995.4 |               614.96 |     42113 |    45133 |     46227 |
|   1374 |  203063 | 44981.7 |               610.41 |     42113 |    45133 |     46227 |
|   1375 |  122378 | 45000.6 |               584.11 |     42113 |    45133 |     46227 |
|   1376 |  124613 | 45003.4 |               576.65 |     42113 |    45133 |     46227 |
|   1377 |  100565 | 45004.2 |               578.16 |     42113 |    45133 |     46227 |
|   1378 |  167718 | 44976.2 |               605.57 |     42113 |    45133 |     46238 |
|   1379 |  167927 | 44977.4 |               604.64 |     42113 |    45133 |     46238 |
|   1380 |  181241 | 44951.1 |               632.95 |     42113 |    45133 |     46238 |
|   1381 |  231860 | 44933.2 |               657.94 |     42113 |    45133 |     46261 |
|   1382 |  177606 | 44918.2 |               688.95 |     42113 |    45133 |     46261 |
|   1383 |  220236 | 55752.2 |               896.01 |     52111 |    56116 |     56219 |
|   1384 |  224538 | 55778.2 |               864.34 |     52111 |    56116 |     56219 |
|   1385 |  229205 | 55817   |               821.85 |     52111 |    56116 |     56219 |
|   1386 |  229663 | 55827.8 |               816.36 |     52111 |    56116 |     56215 |
|   1387 |  258180 | 55850.9 |               782.06 |     52111 |    56116 |     56215 |
|   1388 |  229173 | 55871.6 |               761.23 |     52111 |    56116 |     56215 |
|   1389 |  229333 | 55924.8 |               682.14 |     52111 |    56116 |     56215 |
|   1390 |  222368 | 55911.7 |               711.37 |     52111 |    56116 |     56215 |
|   1391 |  219072 | 55931   |               679.24 |     52111 |    56116 |     56215 |
|   1392 |  208271 | 55940.4 |               657.47 |     52111 |    56116 |     56215 |
|   1393 |  203190 | 55939.5 |               651.95 |     52111 |    56116 |     56215 |
|   1394 |  209442 | 55942.4 |               650.38 |     52111 |    56116 |     56215 |
|   1395 |  204035 | 55944.7 |               637.78 |     52111 |    56116 |     56215 |
|   1396 |  208478 | 55951.1 |               623.1  |     52111 |    56116 |     56215 |
|   1397 |  198686 | 55976.7 |               570.38 |     52111 |    56116 |     56215 |
|   1398 |  183177 | 56002.1 |               514.13 |     52111 |    56116 |     56215 |
|   1399 |  188779 | 56008.8 |               498.47 |     52111 |    56116 |     56215 |
|   1400 |  184265 | 56004.4 |               507.06 |     52111 |    56116 |     56215 |
|   1401 |  171054 | 56009.7 |               501.99 |     52111 |    56116 |     56215 |
|   1402 |  167022 | 56013.7 |               488.56 |     52111 |    56116 |     56215 |


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

| Years     | Provision_Method                               |
|:----------|:-----------------------------------------------|
| 1363-1383 | [COL3](/HBSIR/tables/raw/furniture#col3)       |
| 1384-1402 | [DYCOL02](/HBSIR/tables/raw/furniture#dycol02) |


#### Summary Statistics

**category data**

|   Year | Purchase   |   Non_Agricultural_Work |   Donation |   Instead_of_Private_Service | Instead_of_Public_Service   |   Home_Production | Purchase_Free_Price   | Purchase_Subsidised_Price   | Agricultural_Work   | nan   | Instead_of_Cooperative_Service   |
|-------:|:-----------|------------------------:|-----------:|-----------------------------:|:----------------------------|------------------:|:----------------------|:----------------------------|:--------------------|:------|:---------------------------------|
|   1363 |            |                    0.95 |       0.1  |                         0.01 | 0.03                        |              0.3  | 53.18                 | 45.41                       | 0.02                |       |                                  |
|   1364 |            |                    1.26 |       0.07 |                         0.02 | 0.02                        |              0.3  | 68.61                 | 29.69                       | 0.03                |       |                                  |
|   1365 |            |                    1.11 |       0.04 |                         0.05 | 0.01                        |              0.34 | 68.17                 | 30.18                       | 0.07                | 0.05  |                                  |
|   1366 |            |                    0.73 |       0.03 |                         0.01 | 0.12                        |              0.24 | 64.75                 | 34.08                       | 0.0                 | 0.04  |                                  |
|   1367 |            |                    0.85 |       0.06 |                         0.05 | 0.27                        |              0.29 | 61.29                 | 37.16                       | 0.01                | 0.01  |                                  |
|   1368 |            |                    0.85 |       0.03 |                         0.03 | 0.21                        |              0.2  | 63.34                 | 35.25                       | 0.05                | 0.03  |                                  |
|   1369 | 98.44      |                    1.07 |       0.08 |                         0.01 | 0.16                        |              0.09 |                       |                             | 0.03                | 0.12  |                                  |
|   1370 | 98.22      |                    1.37 |       0.03 |                         0.03 | 0.07                        |              0.18 |                       |                             | 0.05                | 0.06  |                                  |
|   1371 | 98.09      |                    1.57 |       0.03 |                         0.01 | 0.02                        |              0.2  |                       |                             | 0.04                | 0.03  |                                  |
|   1372 | 98.15      |                    1.51 |       0.03 |                         0.01 | 0.03                        |              0.17 |                       |                             | 0.03                | 0.06  |                                  |
|   1373 | 97.72      |                    1.93 |       0.04 |                         0.02 | 0.02                        |              0.19 |                       |                             | 0.03                | 0.05  |                                  |
|   1374 | 98.06      |                    1.66 |       0.03 |                         0.03 | 0.07                        |              0.1  |                       |                             | 0.04                | 0.0   |                                  |
|   1375 | 98.01      |                    1.76 |       0.03 |                         0.04 | 0.05                        |              0.08 |                       |                             | 0.02                | 0.0   |                                  |
|   1376 | 97.9       |                    1.83 |       0.05 |                         0.04 | 0.04                        |              0.09 |                       |                             | 0.06                |       |                                  |
|   1377 | 97.94      |                    1.86 |       0.04 |                         0.02 | 0.04                        |              0.07 |                       |                             | 0.02                |       |                                  |
|   1378 | 97.82      |                    1.98 |       0.04 |                         0.03 | 0.04                        |              0.07 |                       |                             | 0.02                |       |                                  |
|   1379 | 97.84      |                    1.98 |       0.02 |                         0.02 | 0.02                        |              0.08 |                       |                             | 0.03                |       | 0.0                              |
|   1380 | 97.85      |                    1.95 |       0.03 |                         0.04 | 0.02                        |              0.09 |                       |                             | 0.01                |       | 0.01                             |
|   1381 | 97.92      |                    1.86 |       0.06 |                         0.02 | 0.05                        |              0.07 |                       |                             | 0.03                |       | 0.0                              |
|   1382 | 98.01      |                    1.75 |       0.04 |                         0.03 | 0.05                        |              0.09 |                       |                             | 0.03                |       | 0.0                              |
|   1383 | 97.9       |                    1.72 |       0.1  |                         0.04 | 0.09                        |              0.07 |                       |                             | 0.07                |       | 0.0                              |
|   1384 | 97.72      |                    1.78 |       0.09 |                         0.06 | 0.23                        |              0.09 |                       |                             | 0.03                |       | 0.01                             |
|   1385 | 97.54      |                    2.13 |       0.09 |                         0.03 | 0.15                        |              0.04 |                       |                             | 0.02                |       | 0.01                             |
|   1386 | 97.54      |                    1.98 |       0.3  |                         0.02 | 0.1                         |              0.05 |                       |                             | 0.0                 |       | 0.0                              |
|   1387 | 98.17      |                    1.6  |       0.09 |                         0.03 | 0.05                        |              0.05 |                       |                             | 0.01                |       | 0.01                             |
|   1388 | 97.84      |                    1.68 |       0.36 |                         0.02 | 0.04                        |              0.04 |                       |                             | 0.01                |       | 0.0                              |
|   1389 | 98.07      |                    1.67 |       0.17 |                         0.04 | 0.02                        |              0.04 |                       |                             | 0.0                 |       |                                  |
|   1390 | 98.36      |                    1.51 |       0.04 |                         0.03 | 0.02                        |              0.03 |                       |                             | 0.01                |       |                                  |
|   1391 | 98.47      |                    1.41 |       0.04 |                         0.03 | 0.01                        |              0.03 |                       |                             | 0.01                |       |                                  |
|   1392 | 98.83      |                    1.11 |       0.02 |                         0.02 | 0.0                         |              0.01 |                       |                             | 0.0                 |       |                                  |
|   1393 | 98.7       |                    1.18 |       0.07 |                         0.04 | 0.0                         |              0.01 |                       |                             | 0.0                 |       | 0.0                              |
|   1394 | 98.65      |                    1.22 |       0.07 |                         0.05 | 0.01                        |              0    |                       |                             | 0.0                 |       | 0.0                              |
|   1395 | 98.54      |                    1.33 |       0.08 |                         0.04 | 0.01                        |              0.01 |                       |                             | 0.0                 |       | 0.0                              |
|   1396 | 98.54      |                    1.32 |       0.08 |                         0.07 | 0.0                         |              0    |                       |                             | 0.0                 |       |                                  |
|   1397 | 98.53      |                    1.16 |       0.25 |                         0.04 | 0.0                         |              0    |                       |                             | 0.01                |       | 0.0                              |
|   1398 | 98.63      |                    1.25 |       0.08 |                         0.02 | 0.01                        |              0    |                       |                             |                     |       | 0.0                              |
|   1399 | 98.93      |                    0.94 |       0.08 |                         0.05 | 0.0                         |              0.01 |                       |                             | 0.0                 |       | 0.0                              |
|   1400 | 99.0       |                    0.92 |       0.02 |                         0.03 | 0.02                        |              0    |                       |                             |                     |       |                                  |
|   1401 | 98.93      |                    1.02 |       0.02 |                         0.02 |                             |              0    |                       |                             |                     |       | 0.0                              |
|   1402 | 98.56      |                    1.08 |       0.32 |                         0.04 | 0.01                        |              0    |                       |                             |                     |       |                                  |


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

| Years     | Expenditure                                    |
|:----------|:-----------------------------------------------|
| 1363-1368 | [COL4](/HBSIR/tables/raw/furniture#col4)       |
| 1369      | [COL6](/HBSIR/tables/raw/furniture#col6)       |
| 1370-1373 | [COL5](/HBSIR/tables/raw/furniture#col5)       |
| 1374-1383 | [COL4](/HBSIR/tables/raw/furniture#col4)       |
| 1384-1402 | [DYCOL03](/HBSIR/tables/raw/furniture#dycol03) |


#### Summary Statistics

**numeric data**

|   Year |   Count |      Mean |   Standard Deviation |   Minimum |   Median |        Maximum |
|-------:|--------:|----------:|---------------------:|----------:|---------:|---------------:|
|   1363 |  140285 |    561.13 |       1966.75        |         3 |      200 | 100000         |
|   1364 |  129986 |    613.18 |       2443.39        |         3 |      200 | 318000         |
|   1365 |   19794 |    721.49 |       3445.53        |         5 |      250 | 350000         |
|   1366 |   25933 |    815.73 |       2405.89        |         6 |      325 | 153000         |
|   1367 |   35949 |    816.76 |       3350.28        |        10 |      320 | 268000         |
|   1368 |   54679 |   1155.55 |       6607.43        |         5 |      400 |      1e+06     |
|   1369 |   93959 |   1220.77 |       5629.33        |         2 |      450 | 750000         |
|   1370 |  102548 |   1444.1  |       7393.94        |         7 |      500 | 900000         |
|   1371 |   99264 |   1762.58 |       7212.75        |         0 |      700 |      1e+06     |
|   1372 |   69356 |   2184.12 |       6860.37        |         1 |     1000 | 500000         |
|   1373 |  112092 |   3146.29 |      12457.5         |        20 |     1400 |      1.2e+06   |
|   1374 |  203052 |   4912.78 |      22580.6         |         1 |     2000 |      4e+06     |
|   1375 |  122377 |   5478.51 |      31618.5         |        15 |     2400 |      8.2e+06   |
|   1376 |  124613 |   6049.78 |      25027.7         |        50 |     2800 |      2e+06     |
|   1377 |  100565 |   7074.3  |      28887.1         |        50 |     3000 |      3e+06     |
|   1378 |  167718 |   8039.67 |      32050.2         |        50 |     3500 |      2.5e+06   |
|   1379 |  167927 |   9352.58 |      36508           |        40 |     4000 |      3e+06     |
|   1380 |  181241 |  10801.2  |      46421.5         |       100 |     4500 |      6e+06     |
|   1381 |  231860 |  11863.7  |      45830.3         |        85 |     5000 |      6e+06     |
|   1382 |  177606 |  13029.2  |      50768.2         |       100 |     5500 |      6.9e+06   |
|   1383 |  220236 |  14337.1  |      68953.6         |       100 |     5000 |      1.5e+07   |
|   1384 |  224457 |  16961.9  |      82773.7         |       100 |     6000 |      1.37e+07  |
|   1385 |  229205 |  19102.9  |      93830.9         |         0 |     7000 |      1e+07     |
|   1386 |  229663 |  21371.5  |     127444           |       100 |     8000 |      3.6e+07   |
|   1387 |  258180 |  26029.5  |     133423           |       150 |    10000 |      2.5e+07   |
|   1388 |  229173 |  28716.8  |     127148           |       250 |    12000 |      1.2e+07   |
|   1389 |  229333 |  31624.1  |     144878           |       250 |    15000 |      1.25e+07  |
|   1390 |  222368 |  36973.1  |     165469           |       250 |    17000 |      1.5e+07   |
|   1391 |  219072 |  49626.3  |     228590           |       500 |    24000 |      2.915e+07 |
|   1392 |  208271 |  68015.3  |     300837           |       500 |    35000 |      4.65e+07  |
|   1393 |  203190 |  73154.7  |     329216           |      1000 |    40000 |      4.5e+07   |
|   1394 |  209442 |  75192    |     449193           |       500 |    40000 |      7.2e+07   |
|   1395 |  204035 |  76126.1  |     389679           |      1000 |    40000 |      1e+08     |
|   1396 |  208478 |  83695.4  |     431917           |      1000 |    49500 |      7e+07     |
|   1397 |  198686 | 113258    |     526233           |      1500 |    60000 |      9e+07     |
|   1398 |  183177 | 152759    |     531434           |      2000 |   100000 |      6e+07     |
|   1399 |  188779 | 219938    |     799294           |      3500 |   150000 |      6e+07     |
|   1400 |  184265 | 318544    |     980230           |      5000 |   200000 |      1e+08     |
|   1401 |  171054 | 483610    |          1.79521e+06 |     10000 |   300000 |      2e+08     |
|   1402 |  167022 | 635412    |          2.41339e+06 |      7500 |   400000 |      5e+08     |


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

| Years     | Price_System                             |
|:----------|:-----------------------------------------|
| 1363-1368 |                                          |
| 1369-1373 | [COL4](/HBSIR/tables/raw/furniture#col4) |
| 1374-1402 |                                          |


#### Summary Statistics

**category data**

|   Year |   Free_Price |   Subsidised_Price |   nan |
|-------:|-------------:|-------------------:|------:|
|   1369 |        69.5  |              30.35 |  0.15 |
|   1370 |        82.83 |              17.09 |  0.08 |
|   1371 |        93.95 |               6.01 |  0.03 |
|   1372 |        98.94 |               0.99 |  0.07 |
|   1373 |        97.45 |               1.44 |  1.11 |


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

| Years     | Amount                                   |
|:----------|:-----------------------------------------|
| 1363-1368 |                                          |
| 1369      | [COL5](/HBSIR/tables/raw/furniture#col5) |
| 1370-1402 |                                          |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1369 |   28692 | 1252.08 |              2130.96 |         1 |      480 |    192020 |


