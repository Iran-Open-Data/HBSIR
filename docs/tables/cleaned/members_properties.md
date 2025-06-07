# members_properties

## Old to New Titles

| Years     | ADDRESS   | COL01         | COL03        | COL04   | COL05   | COL06              | COL07           | COL08              | COL09           | COL10           | COL11           | COL12           | COL13               | COL14     | COL15               |
|:----------|:----------|:--------------|:-------------|:--------|:--------|:-------------------|:----------------|:-------------------|:----------------|:----------------|:----------------|:----------------|:--------------------|:----------|:--------------------|
| 1363      | ID        | Member_Number | Relationship | Sex     | Age     | Weeks_in_Household | Marital_Status  | Nationality        | Literacy_Status | Education_Level | Activity_Status | Occupation_Code | Work_Place          | Work_Type | Weeks_in_Employment |
| 1364-1365 | ID        | Member_Number | Relationship | Sex     | Age     | Marital_Status     | Nationality     | Weeks_in_Household | Literacy_Status | Education_Level | Activity_Status | Occupation_Code | Work_Place          | Work_Type | Weeks_in_Employment |
| 1366-1368 | ID        | Member_Number | Relationship | Sex     | Age     | Weeks_in_Household | Literacy_Status | Education_Level    | Activity_Status | Occupation_Code | Work_Place      | Work_Type       | Weeks_in_Employment |           |                     |
| 1369-1383 | ID        | Member_Number | Relationship | Sex     | Age     | Is_Literate        | Is_Student      | Education_Level    | Activity_Status | Marital_Status  |                 |                 |                     |           |                     |


| Years     | ADDRESS   | DYCOL01       | DYCOL03      | DYCOL04   | DYCOL05   | DYCOL06     | DYCOL07    | DYCOL08         | DYCOL09         | DYCOL10        |
|:----------|:----------|:--------------|:-------------|:----------|:----------|:------------|:-----------|:----------------|:----------------|:---------------|
| 1384-1402 | ID        | Member_Number | Relationship | Sex       | Age       | Is_Literate | Is_Student | Education_Level | Activity_Status | Marital_Status |


## New to Old Titles

| Years     | ID      | Member_Number   | Relationship   | Sex     | Age     | Is_Literate   | Is_Student   | Education_Level   | Activity_Status   | Marital_Status   | Weeks_in_Household   | Nationality   | Literacy_Status   | Occupation_Code   | Work_Place   | Work_Type   | Weeks_in_Employment   |
|:----------|:--------|:----------------|:---------------|:--------|:--------|:--------------|:-------------|:------------------|:------------------|:-----------------|:---------------------|:--------------|:------------------|:------------------|:-------------|:------------|:----------------------|
| 1363      | ADDRESS | COL01           | COL03          | COL04   | COL05   |               |              | COL10             | COL11             | COL07            | COL06                | COL08         | COL09             | COL12             | COL13        | COL14       | COL15                 |
| 1364-1365 | ADDRESS | COL01           | COL03          | COL04   | COL05   |               |              | COL10             | COL11             | COL06            | COL08                | COL07         | COL09             | COL12             | COL13        | COL14       | COL15                 |
| 1366-1368 | ADDRESS | COL01           | COL03          | COL04   | COL05   |               |              | COL08             | COL09             |                  | COL06                |               | COL07             | COL10             | COL11        | COL12       | COL13                 |
| 1369-1383 | ADDRESS | COL01           | COL03          | COL04   | COL05   | COL06         | COL07        | COL08             | COL09             | COL10            |                      |               |                   |                   |              |             |                       |
| 1384-1402 | ADDRESS | DYCOL01         | DYCOL03        | DYCOL04 | DYCOL05 | DYCOL06       | DYCOL07      | DYCOL08           | DYCOL09           | DYCOL10          |                      |               |                   |                   |              |             |                       |


## Columns Details

### ID

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: ADDRESS
      type: UInt64
    
    ```
#### Column Codes

| Years     | ID                                                      |
|:----------|:--------------------------------------------------------|
| 1363-1402 | [ADDRESS](/HBSIR/tables/raw/members_properties#address) |


#### Summary Statistics

**numeric data**

|   Year |   Count |             Mean |   Standard Deviation |        Minimum |           Median |     Maximum |
|-------:|--------:|-----------------:|---------------------:|---------------:|-----------------:|------------:|
|   1363 |  144063 | 618822           |     511334           |  1001          |      1.00311e+06 | 1.23452e+06 |
|   1364 |  145536 | 591642           |     509223           |  1001          | 232110           | 1.23442e+06 |
|   1365 |   30546 | 553151           |     522907           |  1001          | 184004           | 1.23422e+06 |
|   1366 |   31331 | 553153           |     519409           |  1001          | 193028           | 1.23421e+06 |
|   1367 |   45728 | 558177           |     518133           |  1001          | 194016           | 1.23428e+06 |
|   1368 |   63783 | 537683           |     513157           |  1001          | 162010           | 1.23428e+06 |
|   1369 |  101571 | 559528           |     508893           |  1001          | 194051           | 1.23422e+06 |
|   1370 |  102828 | 556809           |     508195           |  1001          | 193094           | 1.23422e+06 |
|   1371 |  100096 | 559495           |     507585           |  1001          | 194035           | 1.23422e+06 |
|   1372 |   66245 | 598828           |     511359           |  1001          |      1.001e+06   | 1.23422e+06 |
|   1373 |  104370 | 694414           |     514749           |  1001          |      1.03316e+06 | 1.24404e+06 |
|   1374 |  193671 |      6.51532e+06 |          5.12211e+06 | 10001          |      1.021e+07   | 1.24401e+07 |
|   1375 |  113827 | 577456           |     518178           |  1001          | 232231           | 1.24404e+06 |
|   1376 |  111735 | 581111           |     518986           |  1001          | 233071           | 1.25406e+06 |
|   1377 |   89035 |      5.58558e+07 |          5.14156e+07 | 11001          |      2.30841e+07 | 1.27074e+08 |
|   1378 |  139841 |      5.70616e+07 |          5.10581e+07 | 11001          |      2.30941e+07 | 1.27074e+08 |
|   1379 |  132708 |      5.55175e+07 |          5.07616e+07 | 11001          |      2.30631e+07 | 1.27074e+08 |
|   1380 |  130965 |      5.57576e+07 |          5.08053e+07 | 11001          |      2.30921e+07 | 1.27074e+08 |
|   1381 |  153114 |      5.74588e+07 |          5.0895e+07  | 11001          |      2.40511e+07 | 1.27074e+08 |
|   1382 |  108120 |      5.85296e+07 |          5.10584e+07 | 11001          |      2.50111e+07 | 1.27114e+08 |
|   1383 |  112774 |      5.82826e+07 |          5.09254e+07 | 11001          |      2.40911e+07 | 1.27114e+08 |
|   1384 |  120639 |      5.95681e+07 |          5.09354e+07 | 11001          |      2.60331e+07 | 1.29214e+08 |
|   1385 |  135270 |      5.73392e+07 |          5.09995e+07 | 11001          |      2.50141e+07 | 1.29214e+08 |
|   1386 |  133476 |      6.01405e+07 |          5.06462e+07 | 11001          |      2.70726e+07 | 1.29214e+08 |
|   1387 |  161250 |      1.67e+09    |          5.03916e+08 |     1e+09      |      2.01046e+09 | 2.29786e+09 |
|   1388 |  150470 |      1.6497e+09  |          5.03482e+08 |     1e+09      |      2.00018e+09 | 2.29025e+09 |
|   1389 |  152291 |      1.66777e+09 |          5.02293e+08 |     1e+09      |      2.01006e+09 | 2.29013e+09 |
|   1390 |  150540 |      1.67266e+09 |          5.02986e+08 |     1e+09      |      2.01006e+09 | 2.30013e+09 |
|   1391 |  146063 |      1.67121e+09 |          5.03267e+08 |     1e+09      |      2.01005e+09 | 2.30013e+09 |
|   1392 |  140359 |      1.66295e+10 |          5.02755e+09 |     1.0001e+10 |      2.0011e+10  | 2.30047e+10 |
|   1393 |  139033 |      1.66282e+10 |          5.03207e+09 |     1.0001e+10 |      2.0011e+10  | 2.30047e+10 |
|   1394 |  137616 |      1.66073e+10 |          5.03536e+09 |     1.0001e+10 |      2.0007e+10  | 2.30047e+10 |
|   1395 |  135552 |      1.66132e+10 |          5.03158e+09 |     1.0001e+10 |      2.001e+10   | 2.30047e+10 |
|   1396 |  134389 |      1.66181e+10 |          5.03417e+09 |     1.0001e+10 |      2.0009e+10  | 2.30047e+10 |
|   1397 |  135830 |      1.63155e+10 |          5.03728e+09 |     1.0001e+10 |      1.29044e+10 | 2.30067e+10 |
|   1398 |  132541 |      1.63517e+10 |          5.03661e+09 |     1.0001e+10 |      1.29074e+10 | 2.30067e+10 |
|   1399 |  128955 |      1.64175e+10 |          5.02911e+09 |     1.0001e+10 |      1.30014e+10 | 2.30067e+10 |
|   1400 |  128914 |      1.63882e+10 |          5.02475e+09 |     1.0001e+10 |      1.29114e+10 | 2.30067e+10 |
|   1401 |  126478 |      1.63849e+10 |          5.03047e+09 |     1.0001e+10 |      1.29114e+10 | 2.30067e+10 |
|   1402 |  123857 |      1.63436e+10 |          5.02704e+09 |     1.0001e+10 |      1.29064e+10 | 2.30067e+10 |


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

| Years     | Member_Number                                           |
|:----------|:--------------------------------------------------------|
| 1363-1383 | [COL01](/HBSIR/tables/raw/members_properties#col01)     |
| 1384-1402 | [DYCOL01](/HBSIR/tables/raw/members_properties#dycol01) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |  144063 |   3.77 |                 2.43 |         0 |        3 |        80 |
|   1364 |  145536 |   3.75 |                 2.38 |         1 |        3 |        52 |
|   1365 |   30546 |   3.8  |                 2.43 |         1 |        3 |        25 |
|   1366 |   31331 |   3.84 |                 2.48 |         1 |        3 |        33 |
|   1367 |   45728 |   3.86 |                 2.46 |         0 |        3 |        23 |
|   1368 |   63783 |   3.9  |                 2.51 |         0 |        3 |        32 |
|   1369 |  101571 |   3.89 |                 2.5  |         1 |        3 |        56 |
|   1370 |  102828 |   3.89 |                 2.48 |         1 |        3 |        25 |
|   1371 |  100096 |   3.81 |                 2.45 |         0 |        3 |        28 |
|   1372 |   66245 |   3.69 |                 2.33 |         1 |        3 |        21 |
|   1373 |  104370 |   3.71 |                 2.38 |         1 |        3 |        34 |
|   1374 |  193671 |   3.76 |                 2.42 |         1 |        3 |        33 |
|   1375 |  113827 |   3.68 |                 2.37 |         1 |        3 |        30 |
|   1376 |  111735 |   3.62 |                 2.34 |         1 |        3 |        40 |
|   1377 |   89035 |   3.61 |                 2.32 |         1 |        3 |        26 |
|   1378 |  139841 |   3.61 |                 2.31 |         1 |        3 |        29 |
|   1379 |  132708 |   3.51 |                 2.22 |         1 |        3 |        22 |
|   1380 |  130965 |   3.47 |                 2.21 |         1 |        3 |        25 |
|   1381 |  153114 |   3.42 |                 2.16 |         1 |        3 |        22 |
|   1382 |  108120 |   3.34 |                 2.1  |         1 |        3 |        24 |
|   1383 |  112774 |   3.3  |                 2.1  |         1 |        3 |        21 |
|   1384 |  120639 |   3.23 |                 2.05 |         1 |        3 |        24 |
|   1385 |  135270 |   3.16 |                 1.99 |         1 |        3 |        24 |
|   1386 |  133476 |   3.08 |                 1.94 |         1 |        3 |        24 |
|   1387 |  161250 |   2.99 |                 1.85 |         1 |        3 |        28 |
|   1388 |  150470 |   2.96 |                 1.84 |         1 |        3 |        26 |
|   1389 |  152291 |   2.89 |                 1.75 |         1 |        3 |        19 |
|   1390 |  150540 |   2.84 |                 1.7  |         1 |        3 |        18 |
|   1391 |  146063 |   2.79 |                 1.67 |         1 |        2 |        20 |
|   1392 |  140359 |   2.67 |                 1.57 |         1 |        2 |        19 |
|   1393 |  139033 |   2.65 |                 1.54 |         1 |        2 |        16 |
|   1394 |  137616 |   2.63 |                 1.53 |         1 |        2 |        17 |
|   1395 |  135552 |   2.61 |                 1.51 |         1 |        2 |        20 |
|   1396 |  134389 |   2.59 |                 1.49 |         1 |        2 |        16 |
|   1397 |  135829 |   2.56 |                 1.47 |         1 |        2 |        17 |
|   1398 |  132541 |   2.54 |                 1.45 |         1 |        2 |        18 |
|   1399 |  128955 |   2.52 |                 1.43 |         1 |        2 |        18 |
|   1400 |  128914 |   2.5  |                 1.41 |         1 |        2 |        16 |
|   1401 |  126478 |   2.48 |                 1.39 |         1 |        2 |        16 |
|   1402 |  123857 |   2.46 |                 1.39 |         1 |        2 |        16 |


### Relationship

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1364:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1365:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1366:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1367:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1368:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1369:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace:
        0: null
    1370:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1371:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace:
        0: null
    1372:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1373:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1374:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1375:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1376:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1377:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1378:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1379:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1380:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1381:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1382:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1383:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1384:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1385:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1386:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1387:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1388:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1389:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1390:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1391:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1392:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1393:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1394:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1395:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1396:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1397:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1398:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1399:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1400:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1401:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    1402:
      column_code: DYCOL03
      type: category
      categories:
        1: Head
        2: Spouse
        3: Child
        4: Child_in_Law
        5: Grand_Child
        6: Parent
        7: Sibling
        8: Other_Family
        9: Non_Family
      replace: null
    
    ```
#### Column Codes

| Years     | Relationship                                            |
|:----------|:--------------------------------------------------------|
| 1363-1383 | [COL03](/HBSIR/tables/raw/members_properties#col03)     |
| 1384-1402 | [DYCOL03](/HBSIR/tables/raw/members_properties#dycol03) |


#### Summary Statistics

**category data**

|   Year |   Child |   Head |   Spouse | Grand_Child   | Parent   |   Child_in_Law | Sibling   | Other_Family   | Non_Family   | nan   |
|-------:|--------:|-------:|---------:|:--------------|:---------|---------------:|:----------|:---------------|:-------------|:------|
|   1363 |   56.67 |  18.84 |    16.43 | 1.79          | 2.09     |           1.22 | 1.56      | 1.28           | 0.12         |       |
|   1364 |   57    |  18.94 |    16.77 | 1.75          | 1.85     |           1.15 | 1.4       | 1.04           | 0.1          |       |
|   1365 |   56.45 |  18.62 |    16.5  | 2.47          | 1.91     |           1.47 | 1.46      | 1.04           | 0.08         |       |
|   1366 |   57.66 |  18.4  |    16.28 |               |          |           7.65 |           |                |              |       |
|   1367 |   58.11 |  18.19 |    16.1  |               |          |           7.61 |           |                |              |       |
|   1368 |   58.61 |  18.06 |    15.95 |               |          |           7.38 |           |                |              |       |
|   1369 |   58.51 |  18.17 |    15.92 | 2.26          | 1.69     |           1.34 | 1.23      | 0.8            | 0.07         | 0.0   |
|   1370 |   58.79 |  18.16 |    15.86 | 2.27          | 1.59     |           1.36 | 1.14      | 0.78           | 0.05         |       |
|   1371 |   57.87 |  18.65 |    16.5  | 2.01          | 1.61     |           1.22 | 1.25      | 0.81           | 0.07         | 0.0   |
|   1372 |   57.89 |  19.28 |    16.92 | 1.68          | 1.48     |           1.04 | 1.03      | 0.61           | 0.08         |       |
|   1373 |   57.8  |  19.08 |    16.9  | 1.8           | 1.41     |           1.18 | 1.05      | 0.73           | 0.07         |       |
|   1374 |   58.08 |  18.89 |    16.57 | 1.93          | 1.48     |           1.16 | 1.1       | 0.72           | 0.06         |       |
|   1375 |   56.89 |  19.3  |    17.15 | 1.85          | 1.49     |           1.19 | 1.29      | 0.76           | 0.08         |       |
|   1376 |   56.52 |  19.64 |    17.47 | 1.83          | 1.45     |           1.2  | 1.11      | 0.69           | 0.08         |       |
|   1377 |   56.56 |  19.63 |    17.48 | 1.89          | 1.38     |           1.28 | 1.14      | 0.59           | 0.04         |       |
|   1378 |   56.65 |  19.64 |    17.35 | 1.73          | 1.48     |           1.27 | 1.16      | 0.65           | 0.07         |       |
|   1379 |   56.06 |  20.3  |    17.86 | 1.57          | 1.31     |           1.14 | 1.1       | 0.58           | 0.09         |       |
|   1380 |   55.57 |  20.59 |    18.03 | 1.7           | 1.23     |           1.23 | 0.99      | 0.58           | 0.08         |       |
|   1381 |   55.08 |  21    |    18.19 | 1.55          | 1.26     |           1.28 | 0.96      | 0.57           | 0.11         |       |
|   1382 |   53.61 |  21.4  |    18.91 | 1.61          | 1.4      |           1.24 | 1.22      | 0.49           | 0.12         |       |
|   1383 |   53.16 |  21.77 |    19.12 | 1.59          | 1.26     |           1.26 | 1.12      | 0.57           | 0.15         |       |
|   1384 |   52.45 |  22.29 |    19.6  | 1.45          | 1.29     |           1.18 | 1.07      | 0.53           | 0.13         |       |
|   1385 |   51.79 |  22.85 |    19.85 | 1.44          | 1.21     |           1.19 | 1.04      | 0.5            | 0.12         |       |
|   1386 |   50.84 |  23.44 |    20.37 | 1.44          | 1.15     |           1.22 | 0.93      | 0.46           | 0.14         |       |
|   1387 |   50.18 |  24.24 |    20.75 | 1.12          | 1.16     |           1.04 | 0.9       | 0.45           | 0.15         |       |
|   1388 |   49.67 |  24.5  |    20.84 | 1.23          | 1.15     |           1.2  | 0.8       | 0.45           | 0.16         |       |
|   1389 |   48.84 |  25.14 |    21.26 | 1.29          | 1.07     |           1.15 | 0.74      | 0.4            | 0.11         |       |
|   1390 |   48.44 |  25.58 |    21.56 | 1.23          | 0.95     |           1.14 | 0.64      | 0.36           | 0.1          |       |
|   1391 |   47.62 |  26.15 |    21.85 | 1.24          | 0.98     |           1.11 | 0.62      | 0.33           | 0.11         |       |
|   1392 |   46.07 |  27.3  |    23.2  | 0.96          | 0.84     |           0.81 | 0.5       | 0.26           | 0.06         |       |
|   1393 |   45.89 |  27.53 |    23.13 | 0.98          | 0.84     |           0.83 | 0.49      | 0.25           | 0.06         |       |
|   1394 |   45.59 |  27.8  |    23.13 | 1.07          | 0.84     |           0.85 | 0.43      | 0.22           | 0.06         |       |
|   1395 |   44.99 |  28.14 |    23.33 | 1.14          | 0.83     |           0.84 | 0.46      | 0.23           | 0.05         |       |
|   1396 |   44.55 |  28.25 |    23.47 | 1.28          | 0.84     |           0.84 | 0.47      | 0.25           | 0.05         |       |
|   1397 |   43.59 |  28.68 |    23.99 | 1.21          | 0.86     |           0.75 | 0.5       | 0.35           | 0.08         |       |
|   1398 |   43.61 |  28.92 |    23.92 | 1.16          | 0.85     |           0.69 | 0.49      | 0.3            | 0.05         |       |
|   1399 |   43.89 |  29.12 |    23.89 | 1.08          | 0.77     |           0.61 | 0.39      | 0.22           | 0.03         |       |
|   1400 |   43.78 |  29.47 |    23.97 | 0.98          | 0.7      |           0.54 | 0.36      | 0.19           | 0.02         |       |
|   1401 |   43.35 |  30.01 |    24.11 | 0.9           | 0.66     |           0.45 | 0.31      | 0.18           | 0.05         |       |
|   1402 |   42.83 |  30.59 |    24.23 | 0.85          | 0.57     |           0.39 | 0.32      | 0.19           | 0.04         |       |


#### Categories

|    | 1363-1402    |
|---:|:-------------|
|  1 | Head         |
|  2 | Spouse       |
|  3 | Child        |
|  4 | Child_in_Law |
|  5 | Grand_Child  |
|  6 | Parent       |
|  7 | Sibling      |
|  8 | Other_Family |
|  9 | Non_Family   |


#### Replacements

|   Year |   Value |   Replace_Value |   Frequency |
|-------:|--------:|----------------:|------------:|
|   1369 |       0 |             nan |           1 |
|   1371 |       0 |             nan |           2 |


### Sex

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1364:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1365:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1366:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1367:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1368:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1369:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace:
        0: null
        3: null
        4: null
        5: null
        6: null
        8: null
    1370:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1371:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1372:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1373:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1374:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1375:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1376:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1377:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1378:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1379:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1380:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1381:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1382:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1383:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1384:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1385:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1386:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1387:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1388:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1389:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1390:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1391:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1392:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1393:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1394:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1395:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1396:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1397:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1398:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1399:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1400:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1401:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    1402:
      column_code: DYCOL04
      type: category
      categories:
        1: Male
        2: Female
      replace: null
    
    ```
#### Column Codes

| Years     | Sex                                                     |
|:----------|:--------------------------------------------------------|
| 1363-1383 | [COL04](/HBSIR/tables/raw/members_properties#col04)     |
| 1384-1402 | [DYCOL04](/HBSIR/tables/raw/members_properties#dycol04) |


#### Summary Statistics

**category data**

|   Year |   Female |   Male | nan   |
|-------:|---------:|-------:|:------|
|   1363 |    49.72 |  50.28 |       |
|   1364 |    49.7  |  50.3  |       |
|   1365 |    49.84 |  50.16 |       |
|   1366 |    50.1  |  49.9  |       |
|   1367 |    50.14 |  49.86 |       |
|   1368 |    49.89 |  50.11 |       |
|   1369 |    50.28 |  49.68 | 0.04  |
|   1370 |    50.13 |  49.87 |       |
|   1371 |    50.15 |  49.85 | 0.0   |
|   1372 |    49.8  |  50.2  |       |
|   1373 |    49.8  |  50.2  |       |
|   1374 |    49.91 |  50.09 |       |
|   1375 |    49.61 |  50.39 |       |
|   1376 |    50.15 |  49.85 |       |
|   1377 |    49.85 |  50.15 |       |
|   1378 |    49.86 |  50.14 |       |
|   1379 |    49.68 |  50.32 |       |
|   1380 |    49.76 |  50.24 |       |
|   1381 |    50.18 |  49.82 |       |
|   1382 |    49.8  |  50.2  |       |
|   1383 |    49.57 |  50.43 |       |
|   1384 |    49.93 |  50.07 |       |
|   1385 |    50.04 |  49.96 |       |
|   1386 |    49.97 |  50.03 |       |
|   1387 |    49.66 |  50.34 |       |
|   1388 |    49.91 |  50.09 |       |
|   1389 |    49.93 |  50.07 |       |
|   1390 |    50.02 |  49.98 | 0.0   |
|   1391 |    50.01 |  49.99 |       |
|   1392 |    49.96 |  50.04 |       |
|   1393 |    50.06 |  49.94 |       |
|   1394 |    50.1  |  49.9  |       |
|   1395 |    50    |  50    |       |
|   1396 |    49.98 |  50.02 |       |
|   1397 |    49.91 |  50.09 |       |
|   1398 |    50.07 |  49.93 |       |
|   1399 |    50.05 |  49.95 |       |
|   1400 |    49.97 |  50.03 |       |
|   1401 |    50.06 |  49.94 | 0.0   |
|   1402 |    50.27 |  49.73 |       |


#### Categories

|    | 1363-1402   |
|---:|:------------|
|  1 | Male        |
|  2 | Female      |


#### Replacements

|   Year |   Value |   Replace_Value |   Frequency |
|-------:|--------:|----------------:|------------:|
|   1369 |       0 |             nan |           1 |
|   1369 |       3 |             nan |          13 |
|   1369 |       4 |             nan |           2 |
|   1369 |       5 |             nan |           4 |
|   1369 |       6 |             nan |           1 |
|   1369 |       8 |             nan |           2 |


### Age

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL05
      type: UInt8
    1364:
      column_code: DYCOL05
      type: UInt8
    1365:
      column_code: DYCOL05
      type: UInt8
    1366:
      column_code: DYCOL05
      type: UInt8
    1367:
      column_code: DYCOL05
      type: UInt8
    1368:
      column_code: DYCOL05
      type: UInt8
    1369:
      column_code: DYCOL05
      type: UInt8
    1370:
      column_code: DYCOL05
      type: UInt8
    1371:
      column_code: DYCOL05
      type: UInt8
    1372:
      column_code: DYCOL05
      type: UInt8
    1373:
      column_code: DYCOL05
      type: UInt8
    1374:
      column_code: DYCOL05
      type: UInt8
    1375:
      column_code: DYCOL05
      type: UInt8
    1376:
      column_code: DYCOL05
      type: UInt8
    1377:
      column_code: DYCOL05
      type: UInt8
    1378:
      column_code: DYCOL05
      type: UInt8
    1379:
      column_code: DYCOL05
      type: UInt8
    1380:
      column_code: DYCOL05
      type: UInt8
    1381:
      column_code: DYCOL05
      type: UInt8
    1382:
      column_code: DYCOL05
      type: UInt8
    1383:
      column_code: DYCOL05
      type: UInt8
    1384:
      column_code: DYCOL05
      type: UInt8
    1385:
      column_code: DYCOL05
      type: UInt8
    1386:
      column_code: DYCOL05
      type: UInt8
    1387:
      column_code: DYCOL05
      type: UInt8
    1388:
      column_code: DYCOL05
      type: UInt8
    1389:
      column_code: DYCOL05
      type: UInt8
    1390:
      column_code: DYCOL05
      type: UInt8
    1391:
      column_code: DYCOL05
      type: UInt8
    1392:
      column_code: DYCOL05
      type: UInt8
    1393:
      column_code: DYCOL05
      type: UInt8
    1394:
      column_code: DYCOL05
      type: UInt8
    1395:
      column_code: DYCOL05
      type: UInt8
    1396:
      column_code: DYCOL05
      type: UInt8
    1397:
      column_code: DYCOL05
      type: UInt8
    1398:
      column_code: DYCOL05
      type: UInt8
    1399:
      column_code: DYCOL05
      type: UInt8
    1400:
      column_code: DYCOL05
      type: UInt8
    1401:
      column_code: DYCOL05
      type: UInt8
    1402:
      column_code: DYCOL05
      type: UInt8
    
    ```
#### Column Codes

| Years     | Age                                                     |
|:----------|:--------------------------------------------------------|
| 1363-1383 | [COL05](/HBSIR/tables/raw/members_properties#col05)     |
| 1384-1402 | [DYCOL05](/HBSIR/tables/raw/members_properties#dycol05) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |  144063 |  23.03 |                19.96 |         0 |       17 |        99 |
|   1364 |  145536 |  22.17 |                19.5  |         0 |       16 |        99 |
|   1365 |   30546 |  22.47 |                19.71 |         0 |       16 |        99 |
|   1366 |   31331 |  21.94 |                19.38 |         0 |       16 |        99 |
|   1367 |   45728 |  22.06 |                19.44 |         0 |       16 |        99 |
|   1368 |   63783 |  22.6  |                19.59 |         0 |       16 |        99 |
|   1369 |  101569 |  22.8  |                19.67 |         0 |       16 |        99 |
|   1370 |  102828 |  23.16 |                19.79 |         0 |       16 |        99 |
|   1371 |  100094 |  22.96 |                19.45 |         0 |       16 |        99 |
|   1372 |   66245 |  23.87 |                19.67 |         0 |       17 |        99 |
|   1373 |  104370 |  23.98 |                19.18 |         0 |       18 |        99 |
|   1374 |  193671 |  24.25 |                19.43 |         0 |       17 |        99 |
|   1375 |  113827 |  24.4  |                19.11 |         0 |       18 |        99 |
|   1376 |  111735 |  24.72 |                19.08 |         0 |       18 |        99 |
|   1377 |   89035 |  25.25 |                19.15 |         0 |       19 |        99 |
|   1378 |  139841 |  25.68 |                19.26 |         0 |       19 |        99 |
|   1379 |  132708 |  25.95 |                19.12 |         0 |       20 |        99 |
|   1380 |  130965 |  26.56 |                19.19 |         0 |       21 |        99 |
|   1381 |  153114 |  27.15 |                19.28 |         0 |       21 |        99 |
|   1382 |  108120 |  26.85 |                18.88 |         0 |       22 |        99 |
|   1383 |  111327 |  27.6  |                18.76 |         1 |       23 |        99 |
|   1384 |  119062 |  28.28 |                18.99 |         1 |       23 |        99 |
|   1385 |  135270 |  28.56 |                19.31 |         0 |       24 |        99 |
|   1386 |  133472 |  28.88 |                19.48 |         0 |       24 |        99 |
|   1387 |  161250 |  29.14 |                19.41 |         0 |       25 |        99 |
|   1388 |  150469 |  29.74 |                19.71 |         0 |       25 |        99 |
|   1389 |  152291 |  30.52 |                19.94 |         0 |       27 |        99 |
|   1390 |  150476 |  31.26 |                20.12 |         0 |       27 |        99 |
|   1391 |  146063 |  32.11 |                20.38 |         0 |       29 |        99 |
|   1392 |  140359 |  30.83 |                20.18 |         0 |       28 |        99 |
|   1393 |  139033 |  31.66 |                20.53 |         0 |       29 |        99 |
|   1394 |  137616 |  32.29 |                20.75 |         0 |       30 |        99 |
|   1395 |  135552 |  32.89 |                20.97 |         0 |       31 |        99 |
|   1396 |  134389 |  33.23 |                21.12 |         0 |       31 |        99 |
|   1397 |  135830 |  32.57 |                21.08 |         0 |       31 |        99 |
|   1398 |  132541 |  33.42 |                21.33 |         0 |       32 |        99 |
|   1399 |  128955 |  33.72 |                21.25 |         0 |       33 |        99 |
|   1400 |  128914 |  34.17 |                21.24 |         0 |       33 |        99 |
|   1401 |  126478 |  34.77 |                21.38 |         0 |       34 |        99 |
|   1402 |  123857 |  35.47 |                21.57 |         0 |       35 |        99 |


### Is_Literate

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1369:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1370:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1371:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1372:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1373:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1374:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1375:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1376:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1377:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1378:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1379:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1380:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1381:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1382:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1383:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1384:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1385:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1386:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1387:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1388:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1389:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1390:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1391:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1392:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1393:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1394:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1395:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1396:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1397:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1398:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1399:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1400:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1401:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    1402:
      column_code: DYCOL06
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Is_Literate                                             |
|:----------|:--------------------------------------------------------|
| 1363-1368 |                                                         |
| 1369-1383 | [COL06](/HBSIR/tables/raw/members_properties#col06)     |
| 1384-1402 | [DYCOL06](/HBSIR/tables/raw/members_properties#dycol06) |


#### Summary Statistics

**boolean data**

|   Year |   True |   False |   Missing |
|-------:|-------:|--------:|----------:|
|   1369 |  54.34 |   45.66 |      0    |
|   1370 |  56.86 |   43.14 |      0    |
|   1371 |  57.6  |   42.4  |      0    |
|   1372 |  61.57 |   38.43 |      0    |
|   1373 |  64.67 |   35.33 |      0    |
|   1374 |  64.55 |   35.45 |      0    |
|   1375 |  65.98 |   34.02 |      0    |
|   1376 |  66.85 |   33.15 |      0    |
|   1377 |  67.68 |   32.32 |      0    |
|   1378 |  68.55 |   31.45 |      0    |
|   1379 |  69.13 |   30.87 |      0    |
|   1380 |  69.82 |   30.18 |      0    |
|   1381 |  70.72 |   29.28 |      0    |
|   1382 |  71.45 |   28.55 |      0    |
|   1383 |  71.91 |   19.34 |      8.75 |
|   1384 |  72.44 |   27.56 |      0    |
|   1385 |  72.24 |   19.42 |      8.34 |
|   1386 |  72.22 |   18.94 |      8.83 |
|   1387 |  72.7  |   18.37 |      8.93 |
|   1388 |  72.14 |   18.82 |      9.04 |
|   1389 |  72.39 |   18.79 |      8.82 |
|   1390 |  72.91 |   18.75 |      8.34 |
|   1391 |  73.41 |   18.83 |      7.77 |
|   1392 |  73.12 |   16.83 |     10.05 |
|   1393 |  73.6  |   16.86 |      9.54 |
|   1394 |  74.03 |   16.85 |      9.12 |
|   1395 |  74.14 |   16.99 |      8.87 |
|   1396 |  74.55 |   16.68 |      8.77 |
|   1397 |  75.01 |   15.03 |      9.95 |
|   1398 |  75.51 |   15.18 |      9.31 |
|   1399 |  76.96 |   14.32 |      8.72 |
|   1400 |  78.26 |   13.89 |      7.85 |
|   1401 |  78.93 |   13.96 |      7.11 |
|   1402 |  79.62 |   13.96 |      6.41 |


### Is_Student

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1369:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1370:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1371:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1372:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1373:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1374:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1375:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1376:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1377:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1378:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1379:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1380:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1381:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1382:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1383:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1384:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1385:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1386:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1387:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1388:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1389:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1390:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1391:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1392:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1393:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1394:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1395:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1396:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1397:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1398:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1399:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1400:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1401:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    1402:
      column_code: DYCOL07
      type: boolean
      true_condition: 1
    
    ```
#### Column Codes

| Years     | Is_Student                                              |
|:----------|:--------------------------------------------------------|
| 1363-1368 |                                                         |
| 1369-1383 | [COL07](/HBSIR/tables/raw/members_properties#col07)     |
| 1384-1402 | [DYCOL07](/HBSIR/tables/raw/members_properties#dycol07) |


#### Summary Statistics

**boolean data**

|   Year |   False |   True |   Missing |
|-------:|--------:|-------:|----------:|
|   1369 |   26.12 |  29.17 |     44.71 |
|   1370 |   69.48 |  30.52 |      0    |
|   1371 |   70.31 |  29.69 |      0    |
|   1372 |   68.74 |  31.26 |      0    |
|   1373 |   67.12 |  32.88 |      0    |
|   1374 |   66.38 |  33.62 |      0    |
|   1375 |   67.66 |  32.34 |      0    |
|   1376 |   68.4  |  31.6  |      0    |
|   1377 |   68.46 |  31.54 |      0    |
|   1378 |   68.31 |  31.69 |      0    |
|   1379 |   69.13 |  30.87 |      0    |
|   1380 |   70.18 |  29.82 |      0    |
|   1381 |   70.91 |  29.09 |      0    |
|   1382 |   72.19 |  27.81 |      0    |
|   1383 |   49.01 |  26.85 |     24.14 |
|   1384 |   73.41 |  26.59 |      0    |
|   1385 |   51.15 |  25.55 |     23.3  |
|   1386 |   47.37 |  24.85 |     27.78 |
|   1387 |   48.09 |  24.61 |     27.3  |
|   1388 |   48.21 |  23.93 |     27.86 |
|   1389 |   48.58 |  23.82 |     27.61 |
|   1390 |   49.38 |  23.58 |     27.04 |
|   1391 |   50.13 |  23.28 |     26.59 |
|   1392 |   50.73 |  22.39 |     26.88 |
|   1393 |   51.17 |  22.42 |     26.4  |
|   1394 |   51.83 |  22.2  |     25.97 |
|   1395 |   52.4  |  21.74 |     25.86 |
|   1396 |   53.02 |  21.53 |     25.45 |
|   1397 |   53.82 |  21.2  |     24.98 |
|   1398 |   54.3  |  21.2  |     24.49 |
|   1399 |   55.1  |  21.86 |     23.04 |
|   1400 |   55.79 |  22.47 |     21.74 |
|   1401 |   56.07 |  22.86 |     21.07 |
|   1402 |   56.69 |  22.93 |     20.38 |


### Education_Level

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1364:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1365:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1366:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1367:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1368:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1369:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1370:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1371:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1372:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1373:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1374:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1375:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1376:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1377:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1378:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1379:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1380:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1381:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1382:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1383:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1384:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1385:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1386:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1387:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1388:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1389:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1390:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1391:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1392:
      column_code: DYCOL08
      type: string
      categories: null
      replace: null
    1393:
      column_code: DYCOL08
      type: category
      categories:
        11: Primary
        21: Lower_Secondary
        31: Higher_Secondary
        41: Pre_University
        51: Short_Cycle_Tertiary
        52: Bachelors
        53: Masters
        61: Doctoral
        71: Unofficial
      replace: null
    1394:
      column_code: DYCOL08
      type: category
      categories:
        11: Primary
        21: Lower_Secondary
        31: Higher_Secondary
        41: Pre_University
        51: Short_Cycle_Tertiary
        52: Bachelors
        53: Masters
        61: Doctoral
        71: Unofficial
      replace:
        '1': null
    1395:
      column_code: DYCOL08
      type: category
      categories:
        11: Primary
        21: Lower_Secondary
        31: Higher_Secondary
        41: Pre_University
        51: Short_Cycle_Tertiary
        52: Bachelors
        53: Masters
        61: Doctoral
        71: Unofficial
      replace: null
    1396:
      column_code: DYCOL08
      type: category
      categories:
        11: Primary
        21: Lower_Secondary
        31: Higher_Secondary
        41: Pre_University
        51: Short_Cycle_Tertiary
        52: Bachelors
        53: Masters
        61: Doctoral
        71: Unofficial
      replace: null
    1397:
      column_code: DYCOL08
      type: category
      categories:
        1: Primary
        2: Lower_Secondary
        3: Higher_Secondary
        4: Pre_University
        5: Short_Cycle_Tertiary
        6: Bachelors
        7: Masters
        8: Doctoral
        9: Unofficial
      replace: null
    1398:
      column_code: DYCOL08
      type: category
      categories:
        1: Primary
        2: Lower_Secondary
        3: Higher_Secondary
        4: Pre_University
        5: Short_Cycle_Tertiary
        6: Bachelors
        7: Masters
        8: Doctoral
        9: Unofficial
      replace: null
    1399:
      column_code: DYCOL08
      type: category
      categories:
        1: Primary
        2: Lower_Secondary
        3: Higher_Secondary
        4: Pre_University
        5: Short_Cycle_Tertiary
        6: Bachelors
        7: Masters
        8: Doctoral
        9: Unofficial
      replace: null
    1400:
      column_code: DYCOL08
      type: category
      categories:
        1: Primary
        2: Lower_Secondary
        3: Higher_Secondary
        4: Pre_University
        5: Short_Cycle_Tertiary
        6: Bachelors
        7: Masters
        8: Doctoral
        9: Unofficial
      replace: null
    1401:
      column_code: DYCOL08
      type: category
      categories:
        1: Primary
        2: Lower_Secondary
        3: Higher_Secondary
        4: Pre_University
        5: Short_Cycle_Tertiary
        6: Bachelors
        7: Masters
        8: Doctoral
        9: Unofficial
      replace: null
    1402:
      column_code: DYCOL08
      type: category
      categories:
        1: Primary
        2: Lower_Secondary
        3: Higher_Secondary
        4: Pre_University
        5: Short_Cycle_Tertiary
        6: Bachelors
        7: Masters
        8: Doctoral
        9: Unofficial
      replace: null
    
    ```
#### Column Codes

| Years     | Education_Level                                         |
|:----------|:--------------------------------------------------------|
| 1363-1365 | [COL10](/HBSIR/tables/raw/members_properties#col10)     |
| 1366-1383 | [COL08](/HBSIR/tables/raw/members_properties#col08)     |
| 1384-1402 | [DYCOL08](/HBSIR/tables/raw/members_properties#dycol08) |


#### Summary Statistics

**string data**

|   Year | <NA>   | 106   | 234   | 346   | 512   | 105   | 104   | 511   | 103   | 354   | 102   | 107   | 101   | 233   | 522   | 341   | 231   | 232   | 342   | 343   | 364   | 521   | 344   | 345   | 514   | 901   | 513   | 353   | 352   | 002   |       | 362   | 363   | ---   | 108   | 517   | 510   | 602   | 905   | 520   | 516   | 515   | 310   | 109   | 601   | 605   | 001   | 604   | 606   | 603   | 907   | 05   | 04   | 02   | 01   | 03   | 11   | 06   | 13   | 12   | 34   | 26   | X1   | 33   | 31   | 23   | 32   | 47   | 53   | 46   | 65   | 25   | 45   | X2   | 22   | 44   | 21   | 24   | 61   | 95   | 89   | 62   | 73   | 96   | 63   | 97   | 64   | 51   | 74   | 52   | 93   | 41   | 81   | 82   | 42   | 83   | 71   | 84   | 91   | 85   | 86   | 43   | 88   | 00   | 92   | 72   | 15.0   | 14.0   | 12.0   | 11.0   | 13.0   | 16.0   | 23.0   | 34.0   | 21.0   | 22.0   | 91.0   | 37.0   | 31.0   | 33.0   | 32.0   | 17.0   | 26.0   | 18.0   | 64.0   | 52.0   | 36.0   | 19.0   | 25.0   | 72.0   | 62.0   | 41.0   | 61.0   | 24.0   | 63.0   | 42.0   | 73.0   | 35.0   | 87.0   | 43.0   | 51.0   | 40.0   | 70.0   | 88.0   | 50.0   | 82.0   | 93.0   | 49.0   | 81.0   | 47.0   | 89.0   | 45.0   | 60.0   | 10.0   | 71.0   | 83.0   | 84.0   | 92.0   | 30.0   | 85.0   | 38.0   | 80.0   | 20.0   | 1.0   | 28.0   | 86.0   | 29.0   | 46.0   | 39.0   | 94.0   | 2.0   | 3.0   | 4.0   | 6.0   | 5.0   | 48.0   | 44.0   | 76.0   | 75.0   | 78.0   | 77.0   | 27.0   | 16   | 15   | 14   | 48   | 39   | 49   | 35   |       | 38   | 76   | 10   | 75   | 40   | 30   | 78   | 77   | 214   | 313   | 213   | 212   | 211   | 312   | 317   | 311   | 322   | 324   | 314   | 319   | 321   | 315   | 316   | 323   | 326   | 216   | 328   | 325   | 318   | 215   | 210   | 327   | 301   | 302   | 906   | 222   | 100   | 221   | 303   | 902   | 300   | 908   | 220   | 904   | 903   | 32A   | 217   | -    | 31D   | 31C   | 31b   | --   | 112   |
|-------:|:-------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:------|:-------|:-------|:-------|:-------|:-------|:-------|:------|:------|:------|:------|:------|:-------|:-------|:-------|:-------|:-------|:-------|:-------|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:------|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:-----|:------|:------|:------|:-----|:------|
|   1363 | 54.65  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       | 6.27 | 4.47 | 4.47 | 4.0  | 3.65 | 2.83 | 2.79 | 2.56 | 2.5  | 2.46 | 1.53 | 1.41 | 0.98 | 0.95 | 0.79 | 0.77 | 0.42 | 0.4  | 0.36 | 0.3  | 0.23 | 0.21 | 0.15 | 0.14 | 0.12 | 0.1  | 0.06 | 0.06 | 0.05 | 0.04 | 0.03 | 0.03 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  |      |      |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1364 | 55.74  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       | 6.59 | 4.4  | 4.53 | 4.36 | 3.6  | 2.88 | 2.35 | 2.58 | 2.26 | 2.23 | 1.39 | 1.3  | 0.86 | 0.88 | 0.68 | 0.74 | 0.34 | 0.41 | 0.37 | 0.29 | 0.22 | 0.23 | 0.02 | 0.13 | 0.11 | 0.06 | 0.05 | 0.05 | 0.05 | 0.03 | 0.04 | 0.03 | 0.03 | 0.02 | 0.01 | 0.03 | 0.03 | 0.03 | 0.01 | 0.01 | 0.0  | 0.0  | 0.01 | 0.0  | 0.0  | 0.0  | 0.0  |      | 0.0  | 0.0  |      |      | 0.0  | 0.0  | 0.0  |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1365 | 54.31  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       | 6.95 | 4.54 | 4.57 | 4.62 | 3.61 | 2.73 | 2.51 | 2.56 | 2.31 | 2.4  | 1.46 | 1.65 | 0.89 | 0.87 | 0.72 | 0.68 | 0.26 | 0.4  | 0.25 | 0.39 | 0.21 | 0.16 | 0.07 | 0.11 | 0.06 | 0.08 | 0.04 | 0.08 | 0.04 | 0.02 | 0.09 | 0.06 | 0.03 | 0.06 | 0.01 | 0.04 | 0.02 | 0.05 | 0.01 | 0.03 |      | 0.01 | 0.01 | 0.01 | 0.0  | 0.01 | 0.01 |      | 0.01 | 0.0  |      |      |      |      | 0.0  |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1366 | 53.16  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 6.15   | 4.77   | 4.18   | 4.1    | 3.78   | 3.67   | 2.78   | 2.74   | 2.69   | 2.51   | 1.37   | 1.31   | 1.16   | 1.1    | 0.84   | 0.7    | 0.67   | 0.55   | 0.4    | 0.34   | 0.16   | 0.12   | 0.08   | 0.07   | 0.07   | 0.06   | 0.06   | 0.06   | 0.06   | 0.04   | 0.04   | 0.03   | 0.03   | 0.02   | 0.01   | 0.01   | 0.01   | 0.01   | 0.01   | 0.01   | 0.01   | 0.01   | 0.01   | 0.01   | 0.01   | 0.0    | 0.0    | 0.0    | 0.0    | 0.0    | 0.0    |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1367 | 52.17  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 5.76   | 4.53   | 4.36   | 4.03   | 3.96   | 3.55   | 3.16   | 2.79   | 2.96   | 2.44   | 1.54   | 1.31   | 1.06   | 1.09   | 0.84   | 1.13   | 0.7    | 0.56   | 0.43   | 0.49   | 0.15   | 0.12   | 0.1    | 0.06   | 0.07   | 0.12   | 0.11   | 0.03   | 0.07   | 0.07   | 0.01   | 0.05   | 0.02   | 0.02   | 0.02   | 0.01   | 0.0    | 0.01   |        | 0.0    |        | 0.02   | 0.01   | 0.01   | 0.01   | 0.01   | 0.01   | 0.01   |        | 0.01   | 0.0    | 0.01   | 0.0    |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1368 | 50.58  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 4.69   | 4.97   | 4.3    | 4.07   | 4.14   | 5.32   | 3.26   | 2.83   | 3.21   | 2.71   | 1.56   | 1.12   | 1.22   | 1.04   | 0.97   | 1.22   | 0.53   | 0.62   | 0.37   | 0.46   | 0.15   | 0.07   | 0.08   | 0.04   | 0.09   | 0.02   | 0.07   | 0.04   | 0.05   | 0.03   | 0.01   | 0.03   | 0.02   | 0.02   | 0.02   | 0.0    | 0.0    | 0.01   | 0.0    | 0.01   |        | 0.01   | 0.01   | 0.0    | 0.0    | 0.0    | 0.02   |        | 0.0    | 0.01   | 0.0    | 0.0    |        | 0.0    | 0.0    |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1369 | 45.66  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 4.35   | 5.13   | 4.53   | 4.23   | 4.3    | 6.09   | 3.75   | 3.12   | 3.47   | 2.95   | 1.63   | 1.03   | 1.41   | 1.22   | 0.98   | 1.73   | 0.41   | 2.21   | 0.39   | 0.51   | 0.15   | 0.05   | 0.08   | 0.03   | 0.06   | 0.01   | 0.08   | 0.04   | 0.05   | 0.02   | 0.01   | 0.04   | 0.03   | 0.01   | 0.01   | 0.0    | 0.0    | 0.0    | 0.02   | 0.0    | 0.0    | 0.0    | 0.0    | 0.0    | 0.01   | 0.01   | 0.11   | 0.0    | 0.0    | 0.0    | 0.0    |        | 0.0    | 0.0    |        | 0.01   | 0.0    | 0.0   |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1370 | 43.14  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 4.92   | 5.3    | 4.64   | 4.36   | 4.33   | 5.95   | 4.04   | 3.44   | 3.96   | 3.08   | 1.41   | 0.88   | 1.5    | 1.23   | 1.11   | 1.09   | 0.43   | 3.2    | 0.41   | 0.53   | 0.09   | 0.18   | 0.08   | 0.04   | 0.1    | 0.01   | 0.08   | 0.04   | 0.06   | 0.02   | 0.01   | 0.03   | 0.02   | 0.01   | 0.02   | 0.0    | 0.0    | 0.01   | 0.02   | 0.01   | 0.01   | 0.02   | 0.0    | 0.01   | 0.01   | 0.02   | 0.11   | 0.02   | 0.0    | 0.0    | 0.0    | 0.01   |        | 0.01   |        | 0.01   |        |       | 0.0    | 0.0    |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1371 | 42.4   |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 4.78   | 5.28   | 4.51   | 3.96   | 4.35   | 6.6    | 4.09   | 3.85   | 3.9    | 3.34   | 1.3    | 0.8    | 1.56   | 1.4    | 1.16   | 0.89   | 0.41   | 3.18   | 0.51   | 0.68   | 0.11   | 0.17   | 0.06   | 0.04   | 0.11   | 0.01   | 0.11   | 0.04   | 0.06   | 0.02   | 0.01   | 0.02   | 0.03   | 0.02   | 0.03   | 0.0    | 0.0    | 0.01   | 0.02   | 0.0    | 0.01   | 0.01   | 0.01   | 0.0    | 0.0    | 0.02   | 0.07   | 0.01   | 0.01   | 0.0    | 0.0    | 0.0    | 0.0    | 0.01   | 0.0    | 0.0    |        |       | 0.0    | 0.0    | 0.0    | 0.0    |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1372 | 38.43  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 4.82   | 5.43   | 4.28   | 3.67   | 4.39   | 7.43   | 4.86   | 4.46   | 4.24   | 3.77   | 1.29   | 1.0    | 1.88   | 1.63   | 1.3    | 0.84   | 0.44   | 3.23   | 0.67   | 0.71   | 0.11   | 0.11   | 0.06   | 0.06   | 0.09   | 0.02   | 0.09   | 0.05   | 0.06   | 0.03   | 0.02   | 0.03   | 0.05   | 0.02   | 0.01   | 0.0    | 0.01   | 0.02   | 0.08   | 0.0    | 0.0    | 0.01   | 0.0    |        | 0.0    | 0.0    | 0.23   | 0.0    | 0.0    | 0.0    | 0.0    | 0.0    | 0.0    | 0.01   |        | 0.02   |        |       | 0.0    | 0.0    |        |        | 0.0    |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1373 | 35.33  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 4.5    | 5.33   | 4.05   | 3.45   | 4.25   | 7.93   | 5.64   | 5.19   | 4.49   | 4.12   | 1.16   | 1.14   | 2.13   | 1.76   | 1.65   | 0.5    | 0.59   | 3.54   | 0.82   | 0.76   | 0.11   | 0.03   | 0.07   | 0.11   | 0.05   | 0.03   | 0.07   | 0.04   | 0.05   | 0.05   | 0.01   | 0.05   | 0.06   | 0.04   | 0.02   | 0.0    | 0.02   | 0.02   | 0.06   |        |        | 0.02   | 0.0    |        | 0.02   | 0.01   | 0.66   | 0.0    | 0.0    | 0.0    | 0.0    | 0.0    |        |        | 0.0    | 0.06   |        |       |        | 0.0    | 0.0    | 0.0    |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1374 | 35.45  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 4.29   | 5.42   | 4.08   | 3.46   | 4.14   | 8.18   | 5.79   | 5.07   | 4.48   | 4.23   | 1.19   | 0.96   | 2.19   | 1.81   | 1.69   | 0.48   | 0.47   | 3.46   | 0.8    | 0.83   | 0.11   | 0.02   | 0.04   | 0.09   | 0.06   | 0.02   | 0.04   | 0.03   | 0.03   | 0.03   | 0.01   | 0.02   | 0.04   | 0.02   | 0.01   | 0.01   | 0.04   | 0.01   | 0.1    | 0.0    | 0.0    | 0.0    | 0.0    |        | 0.01   | 0.02   | 0.72   | 0.01   | 0.0    | 0.0    | 0.0    | 0.01   | 0.0    | 0.0    | 0.0    | 0.03   |        |       | 0.0    | 0.0    | 0.0    | 0.0    | 0.0    | 0.0    |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1375 | 34.02  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 4.19   | 5.25   | 4.11   | 3.32   | 4.16   | 8.95   | 6.11   | 0.89   | 4.79   | 4.15   | 1.2    |        | 0.22   | 3.05   | 3.43   | 0.0    | 0.53   | 0.0    |        | 0.79   |        |        | 0.07   | 0.1    | 0.93   | 1.23   | 0.82   | 0.0    |        | 1.08   | 0.01   | 0.36   |        | 0.19   | 0.09   | 0.01   |        |        |        | 0.03   | 0.01   | 0.0    | 0.03   | 0.02   | 0.02   | 0.01   | 0.0    | 0.0    | 0.03   | 0.02   |        | 0.04   | 0.02   | 0.02   | 0.17   |        |        | 0.18  |        | 0.0    |        | 0.11   | 1.28   | 0.0    | 1.88  | 1.12  | 0.37  | 0.17  | 0.13  | 0.09   | 0.08   | 0.07   | 0.04   | 0.01   | 0.0    | 0.0    |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1376 | 33.15  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 4.27   | 5.09   | 3.74   | 3.1    | 4.0    | 9.08   | 6.54   | 0.57   | 4.72   | 4.56   | 0.96   |        | 0.16   | 3.45   | 2.56   |        | 0.52   |        |        | 0.81   |        |        | 0.11   | 0.1    | 0.99   | 1.69   | 0.89   | 0.0    |        | 1.88   | 0.02   | 0.44   |        | 0.29   | 0.09   | 0.0    |        |        |        | 0.03   | 0.0    | 0.01   | 0.02   | 0.04   | 0.01   | 0.05   |        | 0.01   | 0.05   | 0.03   |        | 0.03   | 0.02   | 0.01   | 0.11   |        |        | 0.03  |        |        |        | 0.29   | 1.12   |        | 1.74  | 1.36  | 0.4   | 0.19  | 0.13  | 0.26   | 0.17   | 0.07   | 0.04   | 0.0    | 0.0    | 0.0    |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1377 | 32.32  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 5.28   | 5.01   | 3.72   | 2.91   | 3.95   | 7.96   | 6.91   | 0.55   | 4.57   | 4.58   | 0.84   |        | 0.14   | 3.38   | 2.12   |        | 0.44   |        |        | 0.74   |        |        | 0.11   | 0.11   | 1.16   | 1.83   | 1.01   | 0.01   |        | 2.45   | 0.01   | 0.38   |        | 0.53   | 0.1    | 0.02   |        |        |        | 0.03   |        | 0.04   | 0.03   | 0.12   | 0.01   | 0.09   |        | 0.01   | 0.04   | 0.03   |        | 0.04   | 0.01   | 0.02   | 0.15   |        |        | 0.05  |        | 0.0    |        | 0.33   | 1.17   | 0.0    | 1.76  | 1.3   | 0.33  | 0.25  | 0.16  | 0.54   | 0.25   | 0.06   | 0.04   | 0.01   | 0.0    | 0.0    |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1378 | 31.45  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 5.08   | 4.84   | 3.5    | 4.37   | 3.67   | 7.91   | 7.24   | 0.3    | 4.53   | 4.59   | 0.81   |        | 0.08   | 3.57   | 1.85   |        | 0.34   |        |        | 0.79   |        |        | 0.05   | 0.11   | 1.15   | 2.05   | 0.95   | 0.0    |        | 2.94   | 0.01   | 0.43   |        | 0.75   | 0.11   | 0.02   |        |        |        | 0.02   | 0.0    | 0.11   | 0.03   | 0.16   | 0.01   | 0.12   |        | 0.01   | 0.03   | 0.02   |        | 0.03   | 0.09   | 0.02   | 0.11   |        |        | 0.05  |        | 0.0    |        | 0.41   | 0.95   |        | 1.54  | 1.09  | 0.31  | 0.15  | 0.15  | 0.77   | 0.27   | 0.05   | 0.03   | 0.0    | 0.0    | 0.0    |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1379 | 30.87  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 5.92   | 4.74   | 3.47   | 2.55   | 3.82   | 8.08   | 7.86   | 0.19   | 4.47   | 4.54   | 0.85   |        | 0.06   | 3.7    | 1.69   |        | 0.32   |        |        | 0.86   |        |        | 0.05   | 0.12   | 1.3    | 2.24   | 1.04   | 0.0    |        | 3.0    | 0.0    | 0.42   | 0.0    | 0.94   | 0.13   | 0.09   |        |        |        | 0.03   | 0.0    | 0.25   | 0.02   | 0.24   | 0.01   | 0.21   |        | 0.01   | 0.03   | 0.02   |        | 0.07   | 0.01   | 0.02   | 0.11   |        |        | 0.05  |        | 0.0    |        | 0.35   | 0.83   |        | 1.52  | 0.96  | 0.27  | 0.15  | 0.16  | 0.92   | 0.35   | 0.06   | 0.03   | 0.01   | 0.0    | 0.0    |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1380 | 30.18  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 6.08   | 4.53   | 3.24   | 2.39   | 3.6    | 7.74   | 8.16   | 0.15   | 4.54   | 4.53   | 0.85   |        | 0.04   | 3.97   | 1.63   |        | 0.32   |        |        | 0.98   |        |        | 0.04   | 0.12   | 1.42   | 2.58   | 1.08   | 0.0    |        | 2.99   |        | 0.36   |        | 1.55   | 0.14   | 0.04   |        |        |        | 0.04   | 0.0    | 0.35   | 0.04   | 0.36   | 0.02   | 0.36   |        | 0.01   | 0.02   | 0.02   |        | 0.05   | 0.0    | 0.04   | 0.08   |        |        | 0.04  |        |        |        | 0.33   | 0.76   |        | 1.44  | 0.75  | 0.21  | 0.11  | 0.19  | 1.04   | 0.37   | 0.06   | 0.02   | 0.0    | 0.0    |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1381 | 29.28  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 6.0    | 4.24   | 3.11   | 2.16   | 3.43   | 8.03   | 8.48   | 0.13   | 4.45   | 4.59   | 0.87   |        | 0.05   | 3.58   | 1.45   |        | 0.21   |        |        | 1.07   |        |        | 0.04   | 0.12   | 1.63   | 2.7    | 1.2    | 0.0    |        | 3.17   | 0.01   | 0.41   | 0.0    | 2.21   | 0.16   | 0.02   |        |        |        | 0.03   | 0.0    | 0.48   | 0.03   | 0.5    | 0.02   | 0.49   |        | 0.01   | 0.03   | 0.01   |        | 0.03   | 0.01   | 0.04   | 0.11   |        |        | 0.06  |        | 0.0    |        | 0.37   | 0.71   |        | 1.33  | 0.77  | 0.22  | 0.13  | 0.18  | 1.12   | 0.4    | 0.07   | 0.03   | 0.0    | 0.0    | 0.0    |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1382 | 28.55  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 6.18   | 4.11   | 3.12   | 2.28   | 3.32   | 7.82   | 9.14   | 0.15   | 4.44   | 4.48   | 0.79   |        | 0.06   | 3.51   | 1.21   |        | 0.13   |        |        | 1.12   |        |        | 0.02   | 0.11   | 1.71   | 2.68   | 1.25   | 0.0    |        | 3.02   |        | 0.44   |        | 2.74   | 0.26   | 0.1    |        |        |        | 0.02   |        | 0.6    | 0.02   | 0.54   | 0.01   | 0.61   |        | 0.01   | 0.03   | 0.01   |        | 0.02   | 0.01   | 0.05   | 0.13   |        |        | 0.03  |        |        |        | 0.45   | 0.68   |        | 1.25  | 0.69  | 0.2   | 0.14  | 0.17  | 0.98   | 0.49   | 0.09   | 0.03   | 0.01   | 0.0    | 0.0    |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1383 | 27.85  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       | 0.2  | 0.26 | 1.34 | 0.05 | 0.77 | 2.19 | 0.12 | 3.08 | 2.91 | 0.12 | 0.26 |      | 3.36 | 0.07 | 9.37 | 1.29 | 0.66 |      | 0.36 |      | 0.02 | 0.74 |      | 4.22 | 0.43 | 4.18 | 0.0  | 1.36 |      | 0.01 | 1.93 | 0.0  |      |      |      |      | 0.35 |      | 1.29 | 0.0  | 2.62 | 0.02 | 0.03 | 3.19 | 0.02 | 0.05 |      | 0.76 | 0.07 | 0.0  | 3.38 |      |      | 0.02 | 0.15 |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        | 7.16 | 6.51 | 3.9  | 0.97 | 0.85 | 0.57 | 0.47 | 0.24  | 0.08 | 0.06 | 0.04 | 0.02 | 0.02 | 0.01 | 0.0  | 0.0  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1384 | 27.56  |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 8.41   | 3.65   | 2.68   | 2.42   | 2.89   | 7.69   | 10.65  | 0.06   | 3.12   | 3.03   | 0.64   |        | 0.04   | 2.88   | 0.95   |        | 0.39   |        |        | 1.38   |        |        | 0.01   | 0.17   | 2.11   | 2.07   | 1.49   | 0.0    |        | 2.82   | 0.0    | 0.32   | 0.0    | 4.09   | 0.39   | 0.03   |        |        |        | 0.02   |        | 0.57   | 0.02   | 0.8    | 0.02   | 0.91   |        | 0.01   | 0.05   | 0.01   |        | 0.01   | 0.0    | 0.06   | 0.04   |        |        | 0.07  |        | 0.01   |        | 0.33   | 1.17   |        | 1.16  | 0.63  | 0.25  | 0.12  | 0.3   | 0.92   | 0.44   | 0.07   | 0.03   | 0.0    |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |
|   1385 |        | 12.06 |       |       | 2.1   | 3.91  | 3.28  | 1.71  | 2.82  |       | 2.41  | 2.77  | 2.26  |       | 1.36  |       |       |       |       |       |       | 0.57  |       |       | 0.16  | 0.57  | 0.07  |       |       | 0.08  |       |       |       |       | 0.28  | 0.04  | 0.02  | 0.02  | 0.05  | 0.02  | 0.02  | 0.01  | 0.02  | 0.06  | 0.01  | 0.01  |       | 0.0   | 0.0   |       | 0.0   |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      | 27.76 |      |      |      |      |      |      |      |      | 8.0   | 3.77  | 2.95  | 2.93  | 2.9   | 2.83  | 2.74  | 2.36  | 1.86  | 0.96  | 0.96  | 0.68  | 0.57  | 0.54  | 0.4   | 0.32  | 0.29  | 0.24  | 0.05  | 0.04  | 0.02  | 0.02  | 0.02  | 0.02  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |      |       |       |       |      |       |
|   1386 | 27.76  | 12.43 |       |       | 2.3   | 3.44  | 3.18  | 1.99  | 2.67  |       | 2.4   | 2.72  | 2.19  |       | 1.5   |       |       |       |       |       |       | 0.74  |       |       | 0.19  | 0.48  | 0.07  |       |       | 0.06  |       |       |       |       | 0.22  | 0.06  | 0.02  | 0.03  | 0.04  | 0.02  | 0.02  | 0.01  | 0.02  | 0.08  | 0.01  | 0.01  |       | 0.0   | 0.0   |       | 0.0   |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      | 0.01  |      |      |      |      |      |      |      |      | 8.49  | 4.0   | 2.86  | 2.68  | 2.49  | 2.68  | 2.77  | 2.29  | 1.89  | 1.05  | 1.02  | 0.58  | 0.61  | 0.52  | 0.22  | 0.3   | 0.24  | 0.22  | 0.02  | 0.03  | 0.01  | 0.0   | 0.01  | 0.01  | 0.22  | 0.04  | 0.0   | 0.0   | 0.01  | 0.01  | 0.0   | 0.0   | 0.01  | 0.01  |       |       | 0.0   |       | 0.0   |      |       |       |       |      |       |
|   1387 | 27.25  | 13.1  |       |       | 2.61  | 3.1   | 3.09  | 2.37  | 2.65  |       | 2.31  | 2.65  | 2.22  |       | 1.72  |       |       |       |       |       |       | 0.79  |       |       | 0.17  | 0.48  | 0.13  |       |       | 0.06  |       |       |       |       | 0.22  | 0.04  | 0.02  | 0.04  | 0.04  | 0.02  | 0.01  | 0.01  | 0.02  | 0.05  | 0.01  | 0.01  | 0.0   |       | 0.01  |       | 0.0   |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      | 9.67  | 4.24  | 2.2   | 2.19  | 2.25  | 2.6   | 2.74  | 2.23  | 1.87  | 0.96  | 1.01  | 0.67  | 0.59  | 0.48  | 0.07  | 0.27  | 0.2   | 0.23  | 0.03  | 0.03  | 0.01  | 0.01  | 0.0   | 0.0   | 0.15  | 0.05  |       | 0.0   | 0.01  | 0.0   | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   |       |       |       | 0.0   | 0.05 | 0.0   |       |       |      |       |
|   1388 | 27.69  | 13.54 |       |       | 2.63  | 2.61  | 2.93  | 2.49  | 2.6   |       | 2.4   | 2.63  | 2.19  |       | 1.71  |       |       |       |       |       |       | 0.75  |       |       | 0.16  | 0.44  | 0.12  |       |       | 0.06  |       |       |       |       | 0.16  | 0.03  | 0.02  | 0.02  | 0.04  | 0.02  | 0.02  | 0.01  | 0.02  | 0.03  | 0.01  | 0.01  | 0.0   | 0.0   | 0.0   |       |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      | 9.49  | 4.25  | 2.26  | 2.16  | 2.14  | 2.55  | 2.33  | 2.15  | 2.08  | 1.0   | 1.02  | 0.57  | 0.6   | 0.71  | 0.09  | 0.3   | 0.22  | 0.19  | 0.05  | 0.06  | 0.0   | 0.01  | 0.01  | 0.01  | 0.14  | 0.05  |       | 0.0   | 0.05  | 0.0   | 0.0   | 0.01  |       | 0.0   | 0.0   | 0.0   |       |       | 0.0   | 0.17 | 0.0   | 0.0   |       |      |       |
|   1389 | 27.41  | 13.7  |       |       | 3.16  | 2.39  | 2.92  | 2.92  | 2.53  |       | 2.29  | 2.33  | 2.11  |       | 1.72  |       |       |       |       |       |       | 0.84  |       |       | 0.23  | 0.46  | 0.17  |       |       | 0.08  |       |       |       |       | 0.12  | 0.03  | 0.03  | 0.02  | 0.05  | 0.02  | 0.03  | 0.02  | 0.01  | 0.08  | 0.02  | 0.02  | 0.0   | 0.0   | 0.01  | 0.0   | 0.0   |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      | 9.44  | 4.19  | 2.08  | 1.93  | 2.01  | 2.5   | 2.46  | 1.98  | 2.11  | 1.08  | 0.9   | 0.72  | 0.66  | 0.84  | 0.03  | 0.26  | 0.22  | 0.45  | 0.06  | 0.04  | 0.0   | 0.0   | 0.01  | 0.01  | 0.03  | 0.01  |       | 0.0   | 0.04  | 0.0   | 0.01  | 0.0   | 0.0   |       |       | 0.0   |       |       | 0.0   | 0.19 |       |       | 0.0   |      |       |
|   1390 | 26.81  | 13.48 |       |       | 3.46  | 2.52  | 2.83  | 2.97  | 2.49  |       | 2.35  | 2.21  | 2.04  |       | 1.8   |       |       |       |       |       |       | 0.89  |       |       | 0.31  | 0.45  | 0.25  |       |       | 0.13  | 0.15  |       |       |       | 0.15  | 0.04  | 0.03  | 0.02  | 0.04  | 0.03  | 0.03  | 0.02  | 0.02  | 0.07  | 0.02  | 0.01  | 0.0   | 0.0   | 0.0   |       | 0.0   |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      | 9.78  | 4.28  | 1.8   | 1.96  | 2.0   | 2.45  | 2.31  | 1.86  | 1.91  | 1.18  | 1.02  | 0.63  | 0.56  | 0.97  | 0.06  | 0.29  | 0.21  | 0.4   | 0.05  | 0.02  | 0.0   | 0.01  | 0.01  | 0.01  | 0.36  | 0.01  |       | 0.0   | 0.03  | 0.0   | 0.02  | 0.0   | 0.0   | 0.0   | 0.01  |       |       |       | 0.0   | 0.16 |       |       |       | 0.0  | 0.0   |
|   1391 | 26.04  | 13.51 |       |       | 3.85  | 2.67  | 2.9   | 3.05  | 2.51  |       | 2.37  | 2.6   | 2.11  |       | 1.8   |       |       |       |       |       |       | 0.87  |       |       | 0.35  | 0.5   | 0.32  |       |       | 0.19  | 0.39  |       |       |       | 0.13  | 0.05  | 0.04  | 0.02  | 0.05  | 0.03  | 0.03  | 0.02  | 0.02  | 0.04  | 0.02  | 0.0   |       | 0.0   | 0.0   | 0.0   |       |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      | 9.71  | 4.36  | 1.85  | 1.93  | 1.49  | 2.28  | 2.37  | 1.69  | 2.06  | 1.29  | 0.89  | 0.67  | 0.64  | 0.98  | 0.1   | 0.24  | 0.17  | 0.4   | 0.08  | 0.01  | 0.0   | 0.01  | 0.01  | 0.01  | 0.07  | 0.01  |       | 0.0   | 0.03  | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |       |       |       | 0.0   | 0.16 |       |       | 0.0   |      |       |
|   1392 | 26.63  | 12.85 | 10.08 | 7.96  | 4.22  | 3.69  | 2.82  | 2.79  | 2.52  | 2.49  | 2.34  | 2.28  | 2.23  | 2.0   | 1.9   | 1.79  | 1.49  | 1.34  | 1.27  | 1.14  | 1.1   | 0.75  | 0.7   | 0.69  | 0.49  | 0.43  | 0.3   | 0.29  | 0.27  | 0.23  | 0.17  | 0.14  | 0.14  | 0.07  | 0.07  | 0.05  | 0.05  | 0.04  | 0.03  | 0.03  | 0.03  | 0.03  | 0.02  | 0.02  | 0.02  | 0.01  | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |       |        |        |        |        |        |        |       |       |       |       |       |        |        |        |        |        |        |        |      |      |      |      |      |      |      |       |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |      |       |       |       |      |       |


**category data**

|   Year |   Primary |   nan |   Lower_Secondary |   Pre_University |   Bachelors |   Higher_Secondary |   Short_Cycle_Tertiary |   Masters |   Unofficial |   Doctoral |
|-------:|----------:|------:|------------------:|-----------------:|------------:|-------------------:|-----------------------:|----------:|-------------:|-----------:|
|   1393 |     27.78 | 26.4  |             14.09 |            12.78 |        7.07 |               5.18 |                   2.74 |      1.05 |         2.83 |       0.07 |
|   1394 |     27.97 | 25.97 |             14.48 |            13.21 |        7.09 |               4.58 |                   2.72 |      1.15 |         2.73 |       0.08 |
|   1395 |     27.66 | 25.86 |             14.55 |            13.44 |        7.02 |               4.41 |                   2.69 |      1.34 |         2.93 |       0.09 |
|   1396 |     27.78 | 25.45 |             14.64 |            13.76 |        7.09 |               4.2  |                   2.67 |      1.4  |         2.91 |       0.1  |
|   1397 |     28.72 | 24.99 |             15.38 |            14.36 |        7.41 |               3.93 |                   2.84 |      1.59 |         0.71 |       0.07 |
|   1398 |     29.24 | 24.49 |             15.35 |            14.46 |        7.39 |               4.14 |                   2.72 |      1.56 |         0.55 |       0.1  |
|   1399 |     29.46 | 23.04 |             15.79 |            14.67 |        7.74 |               4.4  |                   2.7  |      1.59 |         0.49 |       0.1  |
|   1400 |     29.87 | 21.74 |             16.03 |            15.04 |        8.12 |               4.42 |                   2.61 |      1.62 |         0.44 |       0.11 |
|   1401 |     30.06 | 21.07 |             16.18 |            15.36 |        8.02 |               4.67 |                   2.57 |      1.66 |         0.29 |       0.11 |
|   1402 |     30.29 | 20.38 |             16.45 |            15.58 |        8.07 |               4.68 |                   2.53 |      1.7  |         0.21 |       0.11 |


#### Categories

|    | 1363-1392   | 1393-1396            | 1397-1402            |
|---:|:------------|:---------------------|:---------------------|
|  1 |             |                      | Primary              |
|  2 |             |                      | Lower_Secondary      |
|  3 |             |                      | Higher_Secondary     |
|  4 |             |                      | Pre_University       |
|  5 |             |                      | Short_Cycle_Tertiary |
|  6 |             |                      | Bachelors            |
|  7 |             |                      | Masters              |
|  8 |             |                      | Doctoral             |
|  9 |             |                      | Unofficial           |
| 11 |             | Primary              |                      |
| 21 |             | Lower_Secondary      |                      |
| 31 |             | Higher_Secondary     |                      |
| 41 |             | Pre_University       |                      |
| 51 |             | Short_Cycle_Tertiary |                      |
| 52 |             | Bachelors            |                      |
| 53 |             | Masters              |                      |
| 61 |             | Doctoral             |                      |
| 71 |             | Unofficial           |                      |


#### Replacements

|   Year |   Value |   Replace_Value |   Frequency |
|-------:|--------:|----------------:|------------:|
|   1394 |       1 |             nan |           1 |


### Activity_Status

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL09
      type: UInt16
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1364:
      column_code: DYCOL09
      type: UInt16
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace:
        ٌق: null
    1365:
      column_code: DYCOL09
      type: UInt16
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1366:
      column_code: DYCOL09
      type: UInt16
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1367:
      column_code: DYCOL09
      type: UInt16
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1368:
      column_code: DYCOL09
      type: UInt16
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1369:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace:
        0: null
        9: null
    1370:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace:
        7: null
    1371:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace:
        9: null
    1372:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1373:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1374:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1375:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1376:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1377:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1378:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1379:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1380:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1381:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1382:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1383:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1384:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1385:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1386:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1387:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1388:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1389:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1390:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1391:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1392:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1393:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1394:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1395:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1396:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1397:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1398:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1399:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1400:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1401:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    1402:
      column_code: DYCOL09
      type: category
      categories:
        1: Employed
        2: Unemployed
        3: Income_without_Work
        4: Student
        5: Housekeeper
        6: Other
      replace: null
    
    ```
#### Column Codes

| Years     | Activity_Status                                         |
|:----------|:--------------------------------------------------------|
| 1363-1365 | [COL11](/HBSIR/tables/raw/members_properties#col11)     |
| 1366-1383 | [COL09](/HBSIR/tables/raw/members_properties#col09)     |
| 1384-1402 | [DYCOL09](/HBSIR/tables/raw/members_properties#dycol09) |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |  115434 |  42.71 |                23.51 |         1 |       50 |        98 |
|   1364 |  114627 |  42.98 |                23.76 |         1 |       50 |        98 |
|   1365 |   24140 |  42.11 |                22.65 |         1 |       50 |        87 |
|   1366 |   24666 |  42.55 |                22.07 |         1 |       50 |        87 |
|   1367 |   36213 |  42.63 |                21.98 |         1 |       50 |        87 |
|   1368 |   51469 |  42.08 |                21.83 |         1 |       50 |        87 |


**category data**

|   Year |   Employed |   Housekeeper |   Student |   nan |   Income_without_Work |   Unemployed |   Other |
|-------:|-----------:|--------------:|----------:|------:|----------------------:|-------------:|--------:|
|   1369 |      24.32 |          1.58 |     21.16 | 18.54 |                 27.61 |         2.07 |    4.72 |
|   1370 |      23.39 |         20.86 |     29.06 | 17.72 |                  1.9  |         2.36 |    4.71 |
|   1371 |      25.03 |         20.32 |     28.34 | 17.69 |                  1.71 |         2.23 |    4.68 |
|   1372 |      25.9  |         19.66 |     30.09 | 15.39 |                  2.3  |         2.24 |    4.42 |
|   1373 |      25.05 |         20.32 |     31.74 | 13.71 |                  2.52 |         2.27 |    4.38 |
|   1374 |      25.97 |         19.49 |     22.4  | 25.22 |                  2.59 |         2.43 |    1.89 |
|   1375 |      27.03 |         19.97 |     21.65 | 24.03 |                  2.66 |         2.66 |    2    |
|   1376 |      27.4  |         20.46 |     21.65 | 22.84 |                  2.97 |         2.77 |    1.91 |
|   1377 |      27.59 |         21.07 |     22    | 21.31 |                  3.05 |         2.98 |    1.99 |
|   1378 |      27.55 |         21.31 |     22.47 | 19.91 |                  3.49 |         3.37 |    1.91 |
|   1379 |      27.92 |         21.9  |     22.34 | 18.76 |                  3.35 |         3.69 |    2.05 |
|   1380 |      27.93 |         22.54 |     22    | 17.3  |                  3.73 |         4.02 |    2.48 |
|   1381 |      28.22 |         22.81 |     21.82 | 16.04 |                  4.23 |         4.25 |    2.62 |
|   1382 |      29.73 |         22.47 |     20.87 | 16.55 |                  3.7  |         4.21 |    2.46 |
|   1383 |      30.39 |         22.28 |     20.28 | 15.77 |                  4.09 |         4.41 |    2.8  |
|   1384 |      30.59 |         22.51 |     19.78 | 15.22 |                  4.49 |         4.61 |    2.8  |
|   1385 |      30.72 |         22.63 |     18.87 | 14.8  |                  5.34 |         4.85 |    2.8  |
|   1386 |      30.6  |         23.13 |     18.43 | 15.04 |                  5.82 |         4.47 |    2.51 |
|   1387 |      29.47 |         23.23 |     18.16 | 14.96 |                  6.37 |         5.27 |    2.54 |
|   1388 |      29.02 |         23.28 |     17.34 | 14.96 |                  7.53 |         5.61 |    2.26 |
|   1389 |      28.79 |         23.97 |     17.47 | 14.6  |                  7.57 |         5.43 |    2.17 |
|   1390 |      27.86 |         24.8  |     17.38 | 14.18 |                  7.59 |         6.03 |    2.17 |
|   1391 |      28.55 |         24.67 |     16.81 | 13.7  |                  8.1  |         6.07 |    2.11 |
|   1392 |      28.64 |         25.1  |     15.64 | 16.32 |                  7.46 |         5.08 |    1.77 |
|   1393 |      28.35 |         25.06 |     15.45 | 15.91 |                  8.19 |         5.13 |    1.91 |
|   1394 |      27.91 |         25.55 |     15.19 | 15.63 |                  8.45 |         5.38 |    1.88 |
|   1395 |      27.82 |         25.6  |     14.92 | 15.26 |                  8.83 |         5.66 |    1.92 |
|   1396 |      28.08 |         25.41 |     14.83 | 15.18 |                  9.04 |         5.44 |    2.02 |
|   1397 |      28.32 |         25.36 |     14.25 | 16.61 |                  8.82 |         4.91 |    1.75 |
|   1398 |      28.05 |         25.4  |     14.31 | 15.96 |                  9.62 |         4.82 |    1.84 |
|   1399 |      27.07 |         25.47 |     14.91 | 15.49 |                 10.2  |         4.96 |    1.9  |
|   1400 |      27.32 |         25.54 |     15.46 | 14.77 |                 10.42 |         4.58 |    1.9  |
|   1401 |      27.34 |         25.55 |     15.67 | 14.14 |                 11.01 |         4.52 |    1.78 |
|   1402 |      27.54 |         25.62 |     15.63 | 13.53 |                 11.59 |         4.26 |    1.83 |


#### Categories

|    | 1363-1402           |
|---:|:--------------------|
|  1 | Employed            |
|  2 | Unemployed          |
|  3 | Income_without_Work |
|  4 | Student             |
|  5 | Housekeeper         |
|  6 | Other               |


#### Replacements

|   Year | Value   |   Replace_Value |   Frequency |
|-------:|:--------|----------------:|------------:|
|   1364 | ٌق       |             nan |           1 |
|   1369 | 0       |             nan |           1 |
|   1369 | 9       |             nan |           2 |
|   1370 | 7       |             nan |           1 |
|   1371 | 9       |             nan |           1 |


### Marital_Status

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1364:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1365:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1369:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace:
        0: null
        5: null
        7: null
        8: null
        9: null
    1370:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1371:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1372:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1373:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1374:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1375:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1376:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1377:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1378:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1379:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1380:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1381:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1382:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1383:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1384:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1385:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1386:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1387:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1388:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1389:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1390:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1391:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1392:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1393:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1394:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1395:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1396:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1397:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1398:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1399:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1400:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1401:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    1402:
      column_code: DYCOL10
      type: category
      categories:
        1: Married
        2: Widowed
        3: Divorced
        4: Bachelor
      replace: null
    
    ```
#### Column Codes

| Years     | Marital_Status                                          |
|:----------|:--------------------------------------------------------|
| 1363      | [COL07](/HBSIR/tables/raw/members_properties#col07)     |
| 1364-1365 | [COL06](/HBSIR/tables/raw/members_properties#col06)     |
| 1366-1368 |                                                         |
| 1369-1383 | [COL10](/HBSIR/tables/raw/members_properties#col10)     |
| 1384-1402 | [DYCOL10](/HBSIR/tables/raw/members_properties#dycol10) |


#### Summary Statistics

**category data**

|   Year |   Married |   Bachelor | nan   |   Widowed |   Divorced |
|-------:|----------:|-----------:|:------|----------:|-----------:|
|   1363 |     58.84 |       0.43 |       |     37.18 |       3.55 |
|   1364 |     37.54 |      58.87 |       |      3.17 |       0.42 |
|   1365 |     37.71 |      58.55 |       |      3.38 |       0.36 |
|   1369 |     35.66 |      29.43 | 31.35 |      3.3  |       0.26 |
|   1370 |     35.71 |      30.2  | 30.55 |      3.29 |       0.25 |
|   1371 |     36.86 |      29.62 | 30.36 |      2.92 |       0.24 |
|   1372 |     37.33 |      31.22 | 28.08 |      3.1  |       0.27 |
|   1373 |     37.58 |      33.36 | 25.92 |      2.86 |       0.29 |
|   1374 |     36.92 |      34.6  | 25.23 |      2.97 |       0.28 |
|   1375 |     38.2  |      34.63 | 24.03 |      2.87 |       0.27 |
|   1376 |     38.93 |      35.08 | 22.84 |      2.88 |       0.27 |
|   1377 |     39.17 |      36.38 | 21.31 |      2.85 |       0.29 |
|   1378 |     39.03 |      37.71 | 19.91 |      3.1  |       0.26 |
|   1379 |     39.74 |      38.16 | 18.76 |      3.05 |       0.3  |
|   1380 |     40.3  |      39.01 | 17.3  |      3.11 |       0.28 |
|   1381 |     40.95 |      39.39 | 16.04 |      3.32 |       0.3  |
|   1382 |     42.23 |      37.93 | 16.55 |      2.97 |       0.32 |
|   1383 |     42.77 |      38.07 | 15.76 |      3.05 |       0.35 |
|   1384 |     43.74 |      37.51 | 15.22 |      3.17 |       0.36 |
|   1385 |     44.55 |      36.94 | 14.8  |      3.31 |       0.4  |
|   1386 |     45.43 |      35.69 | 15.04 |      3.43 |       0.41 |
|   1387 |     46.04 |      34.92 | 14.96 |      3.62 |       0.46 |
|   1388 |     46.63 |      34.05 | 14.95 |      3.83 |       0.53 |
|   1389 |     47.42 |      33.5  | 14.6  |      3.89 |       0.6  |
|   1390 |     47.96 |      33.14 | 14.18 |      4.06 |       0.67 |
|   1391 |     48.63 |      32.62 | 13.7  |      4.28 |       0.77 |
|   1392 |     50.39 |      28.72 | 16.32 |      3.88 |       0.69 |
|   1393 |     50.31 |      28.8  | 15.91 |      4.19 |       0.78 |
|   1394 |     50.2  |      28.92 | 15.62 |      4.4  |       0.85 |
|   1395 |     50.49 |      28.71 | 15.26 |      4.61 |       0.93 |
|   1396 |     50.78 |      28.44 | 15.18 |      4.6  |       1    |
|   1397 |     51.6  |      26.41 | 16.6  |      4.34 |       1.05 |
|   1398 |     51.31 |      26.98 | 15.96 |      4.6  |       1.14 |
|   1399 |     50.95 |      27.68 | 15.49 |      4.68 |       1.2  |
|   1400 |     50.93 |      28.26 | 14.77 |      4.85 |       1.19 |
|   1401 |     50.99 |      28.44 | 14.14 |      5.23 |       1.21 |
|   1402 |     50.93 |      28.7  | 13.53 |      5.49 |       1.35 |


#### Categories

|    | 1363-1402   |
|---:|:------------|
|  1 | Married     |
|  2 | Widowed     |
|  3 | Divorced    |
|  4 | Bachelor    |


#### Replacements

|   Year |   Value |   Replace_Value |   Frequency |
|-------:|--------:|----------------:|------------:|
|   1369 |       0 |             nan |          10 |
|   1369 |       5 |             nan |           1 |
|   1369 |       7 |             nan |           1 |
|   1369 |       8 |             nan |           1 |
|   1369 |       9 |             nan |          10 |


### Weeks_in_Household

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL06
      type: UInt16
    1364:
      column_code: COL08
      type: UInt16
    1366:
      column_code: COL06
      type: UInt16
    
    ```
#### Column Codes

| Years     | Weeks_in_Household                                  |
|:----------|:----------------------------------------------------|
| 1363      | [COL06](/HBSIR/tables/raw/members_properties#col06) |
| 1364-1365 | [COL08](/HBSIR/tables/raw/members_properties#col08) |
| 1366-1368 | [COL06](/HBSIR/tables/raw/members_properties#col06) |
| 1369-1402 |                                                     |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |  144063 |  50.16 |                 7.77 |         0 |       52 |        52 |
|   1364 |  145536 |  50.02 |                 8.1  |         0 |       52 |        52 |
|   1365 |   30546 |  50.11 |                 7.92 |         0 |       52 |        52 |
|   1366 |   31331 |  50.4  |                 7.28 |         0 |       52 |        52 |
|   1367 |   45728 |  50.38 |                 7.36 |         0 |       52 |        52 |
|   1368 |   63783 |  50.51 |                 7.09 |         0 |       52 |        52 |


### Nationality

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL08
      type: UInt8
    1364:
      column_code: COL07
      type: UInt8
    
    ```
#### Column Codes

| Years     | Nationality                                         |
|:----------|:----------------------------------------------------|
| 1363      | [COL08](/HBSIR/tables/raw/members_properties#col08) |
| 1364-1365 | [COL07](/HBSIR/tables/raw/members_properties#col07) |
| 1366-1402 |                                                     |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |  144063 |   1.01 |                 0.11 |         1 |        1 |         4 |
|   1364 |  145536 |   1.01 |                 0.14 |         1 |        1 |         4 |
|   1365 |   30546 |   1.01 |                 0.12 |         1 |        1 |         4 |


### Literacy_Status

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL09
      type: UInt8
    1366:
      column_code: COL07
      type: UInt8
    
    ```
#### Column Codes

| Years     | Literacy_Status                                     |
|:----------|:----------------------------------------------------|
| 1363-1365 | [COL09](/HBSIR/tables/raw/members_properties#col09) |
| 1366-1368 | [COL07](/HBSIR/tables/raw/members_properties#col07) |
| 1369-1402 |                                                     |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |  115434 |   2.56 |                 1.29 |         1 |        2 |         4 |
|   1364 |  114597 |   2.57 |                 1.29 |         1 |        2 |         4 |
|   1365 |   24129 |   2.14 |                 0.83 |         1 |        2 |         3 |
|   1366 |   24662 |   2.1  |                 0.84 |         1 |        2 |         3 |
|   1367 |   36204 |   2.08 |                 0.84 |         1 |        2 |         3 |
|   1368 |   51460 |   2.07 |                 0.84 |         1 |        2 |         3 |


### Occupation_Code

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL12
      type: string
    1366:
      column_code: COL10
      type: string
    
    ```
#### Column Codes

| Years     | Occupation_Code                                     |
|:----------|:----------------------------------------------------|
| 1363-1365 | [COL12](/HBSIR/tables/raw/members_properties#col12) |
| 1366-1368 | [COL10](/HBSIR/tables/raw/members_properties#col10) |
| 1369-1402 |                                                     |


#### Summary Statistics

**string data**

|   Year |   <NA> |   612 |   614 |   753 |   956 |   410 |   985 |   622 |   613 |   133 |   452 |   624 |   X03 |   552 |   843 |   310 |   951 |   893 |   791 |   132 |   776 |   589 |   451 |   623 |   754 |   971 |   110 |   872 |   627 | 571   | 530   |   839 |   811 |   849 |   831 |   582 |   832 |   072 |   139 |   801 |   391 | X04   | 875   |   359 | 443   | 845   |   510 |   871 |   959 |   851 |   873 |   955 |   931 |   751 |   778 |   300 |   626 |   855 |   551 |   321 |   331 |   441 |   974 | 700   | 858   |   752 | 932   |   943 |   149 |   771 |   857 |   952 |   034 | 572   | 420   |   629 |   953 |   141 |   211 | 962   |   395 |   560 |   625 |   755 |   820 |   795 |   724 |   711 |   854 |   380 |   370 |   957 |   490 |   163 |   219 |   880 |   641 |   779 |   399 | 161   | 958   |   981 |   973 |   921 | 983   |   961 |   892 |   339 |   394 |   803 | 963   |   901 |   033 | 453   |   134 | 731   |   053 |   999 |   774 |   032 |   799 |   796 |   842 |   061 |   X01 | 078   |   581 |   131 | 949   |   819 |   022 |   773 |   619 |   939 |   079 |   615 |   212 |   772 |   600 | 084   |   031 |   745 |   054 |   035 |   942 |   969 |   599 |   841 | 813   |   193 |   195 |   400 |   202 | 123   |   722 | 055   | 191   | 351   |   856 | 213   | 902   |   929 |   728 |   090 | 746   |   775 | 074   |   742 |   180 | 876   | 122   | 076   |   712 | 744   | 713   |   071 | 068   | 173   | 063   | 201   |   013 | 649   | 593   | 064   | 052   | 041   | 067   | 083   |   926 |   756 |   062 |   986 | 630   | 340   |   023 | 066   |   759 |   749 | 910   |   891 | 733   | 152   | 760   | 069   | 727   | 075   | 874   | 616   | 729   |   129 | 021   | 844   | 192   | 042   |   979 |   077 | 859   | 199   | 037   | 121   | 726   | 793   |   024 |   721 | 038   | 862   | 179   |   029 | 194   | 135   | 322   | 142   | 941   | 954   | 393   | 570   | 360   | 531   | 442   | 834   | 532   | 540   | 392   | 621   | 611   | 732   | 853   | 802   | 761   | 422   | 632   | 432   | 162   | 922   | 421   | 899   | 812   | 895   | 984   | 073   | 500   | 794   | 789   | 065   | 734   | 159   | 039   | 925   | 781   | 352   | 723   | 835   | 025   | 741   | 342   | 783   | 927   | 592   | 036   | 591   | 171   | 777   | X02   | 852   | 982   | 081   | 431   | 174   | 027   | 014   | 792   | 782   | 725   | 151   | 631   | 028   | 026   | 520   | 082   | 043   | 833   | 972   | 861   | 924   | 175   | 780   | 877   |
|-------:|-------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|:------|:------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|:------|:------|------:|:------|:------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|:------|:------|------:|:------|------:|------:|------:|------:|------:|------:|:------|:------|------:|------:|------:|------:|:------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|:------|:------|------:|------:|------:|:------|------:|------:|------:|------:|------:|:------|------:|------:|:------|------:|:------|------:|------:|------:|------:|------:|------:|------:|------:|------:|:------|------:|------:|:------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|:------|------:|------:|------:|------:|------:|------:|------:|------:|:------|------:|------:|------:|------:|:------|------:|:------|:------|:------|------:|:------|:------|------:|------:|------:|:------|------:|:------|------:|------:|:------|:------|:------|------:|:------|:------|------:|:------|:------|:------|:------|------:|:------|:------|:------|:------|:------|:------|:------|------:|------:|------:|------:|:------|:------|------:|:------|------:|------:|:------|------:|:------|:------|:------|:------|:------|:------|:------|:------|:------|------:|:------|:------|:------|:------|------:|------:|:------|:------|:------|:------|:------|:------|------:|------:|:------|:------|:------|------:|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|
|   1363 |  70.76 |  6.78 |  2.35 |  0    |  0    |  1.71 |  1.23 |  0.5  |  0.68 |  0.85 |  0.38 |  0.25 |  0.58 |  0.22 |  0.36 |  0.1  |  0.33 |  0.07 |  0.31 |  0.14 |  0.27 |  0.25 |  0.26 |  0.11 |  2.59 |  0.16 |  0.07 |  0.19 |  0.1  |       |       |  0.04 |  0.04 |  0.1  |  0.18 |  0.14 |  0.01 |  0.12 |  0.11 |  0.1  |  0.1  |       |       |  0.01 | 0.0   |       |  0.1  |  0.09 |  0.05 |  0.05 |  0.23 |  0.04 |  0.11 |  0.01 |  0.01 |  0.08 |  0.06 |  0.14 |  0.07 |  0.07 |  0.17 |  0.02 |  0.06 |       |       |  0.13 |       |  0.05 |  0.02 |  0.02 |  0.03 |  0.04 |  0.03 |       |       |  0.07 |  0.02 |  0.07 |  0.04 |       |  0.06 |  0.04 |  0.02 |  0.05 |  0.03 |  0.02 |  0.02 |  0.05 |  0.03 |  0.05 |  0.05 |  0.03 |  0    |  0.02 |  0.04 |  0.03 |  0.06 |  0.01 |  0.08 | 0.0   |       |  0.06 |  0.02 |  0    | 0.0   |  0.01 |  0.08 |  0.09 |  0.01 |  0.01 |       |  0.02 |  0.05 |       |  0.02 | 0.0   |  0.01 |  1.98 |  0    |  0.01 |  0.01 |  0.04 |  0.03 |  0.03 |  0.07 |       |  0.01 |  0.01 | 0.01  |  0.02 |  0.01 |  0.03 |  0.01 |  0.06 |  0.03 |  0.03 |  0.02 |  0.01 |  0.01 | 0.01  |  0.02 |  0.01 |  0.01 |  0.02 |  0.04 |  0.05 |  0.08 |  0.01 |       |  0.01 |  0.01 |  0.01 |  0.02 |       |  0    |       | 0.01  | 0.0   |  0.01 |       | 0.02  |  0.01 |  0.01 |  0    |       |  0.01 | 0.0   |  0.01 |  0.01 |       | 0.0   | 0.0   |  0.01 | 0.0   | 0.01  |  0.01 | 0.02  | 0.0   | 0.0   | 0.0   |  0    | 0.0   |       | 0.0   | 0.01  | 0.0   | 0.0   | 0.0   |  0.01 |  0.02 |  0.03 |  0.04 |       |       |  0.01 | 0.01  |  0.01 |  0.01 | 0.01  |  0    |       |       |       | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |  0.01 | 0.0   | 0.0   | 0.0   | 0.01  |  0.01 |  0.01 | 0.01  | 0.0   | 0.0   |       | 0.0   | 0.0   |  0    |  0    | 0.0   | 0.0   | 0.0   |  0    |       |       |       |       |       | 0.16  | 0.15  | 0.15  | 0.14  | 0.11  | 0.09  | 0.08  | 0.07  | 0.05  | 0.05  | 0.04  | 0.02  | 0.02  | 0.02  | 0.02  | 0.02  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |       |       |       |       |       |       |       |       |       |       |       |       |       |
|   1364 |  71.66 |  7.02 |  2.26 |  0.01 |  0    |  1.42 |  1.16 |  0.58 |  0.66 |  0.77 |  0.35 |  0.3  |  0.42 |  0.23 |  0.3  |  0.08 |  0.36 |  0.07 |  0.29 |  0.17 |  0.26 |  0.25 |  0.22 |  0.12 |  2.33 |  0.15 |  0.07 |  0.21 |  0.11 |       |       |  0.05 |  0.03 |  0.09 |  0.17 |  0.15 |  0.01 |  0.11 |  0.11 |  0.08 |  0.09 |       |       |  0.02 | 0.0   |       |  0.09 |  0.08 |  0.05 |  0.05 |  0.17 |  0.05 |  0.09 |  0.01 |  0.01 |  0.08 |  0.08 |  0.11 |  0.08 |  0.07 |  0.15 |  0.02 |  0.07 |       |       |  0.12 |       |  0.07 |  0.02 |  0.02 |  0.03 |  0.05 |  0.04 |       |       |  0.05 |  0.03 |  0.06 |  0.03 |       |  0.05 |  0.03 |  0.02 |  0.03 |  0.04 |  0.02 |  0.01 |  0.04 |  0.03 |  0.05 |  0.05 |  0.03 |  0    |  0.03 |  0.04 |  0.02 |  0.08 |  0.01 |  0.07 | 0.0   |       |  0.05 |  0.02 |  0    | 0.0   |  0.02 |  0.08 |  0.1  |  0.02 |  0.01 |       |  0.02 |  0.04 |       |  0.02 |       |  0.01 |  2.22 |  0.01 |  0.01 |  0.02 |  0.04 |  0.02 |  0.02 |  0    |       |  0.01 |  0.01 | 0.01  |  0.01 |  0.01 |  0.04 |  0.02 |  0.05 |  0.03 |  0.02 |  0.02 |  0.01 |  0.01 | 0.01  |  0.02 |  0.01 |  0.02 |  0.02 |  0.03 |  0.06 |  0.08 |  0.02 |       |  0.01 |  0    |  0.01 |  0.02 |       |  0    |       | 0.0   | 0.0   |  0.02 |       | 0.03  |  0.01 |  0    |  0    |       |  0.01 | 0.0   |  0.01 |  0.01 |       | 0.0   | 0.0   |  0.01 | 0.01  | 0.01  |  0.01 | 0.01  |       | 0.0   |       |  0    | 0.0   |       | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |  0    |  0.01 |  0.04 |  0.02 |       |       |  0.01 | 0.01  |  0.02 |  0.01 | 0.0   |  0    | 0.0   |       |       | 0.0   | 0.0   | 0.0   |       |       | 0.0   |  0.01 | 0.0   | 0.01  | 0.0   | 0.0   |  0.01 |  0    | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |  0    |  0    | 0.0   | 0.0   | 0.0   |  0    | 0.0   | 0.0   | 0.0   |       |       | 0.14  | 0.11  | 0.13  | 0.1   | 0.1   | 0.06  | 0.08  | 0.06  | 0.04  | 0.03  | 0.1   | 0.02  | 0.01  | 0.01  | 0.01  | 0.0   | 0.02  | 0.0   | 0.01  | 0.02  | 0.0   | 0.01  | 0.0   | 0.01  | 0.0   | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.01  | 0.0   | 0.0   | 0.0   | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   |       | 0.0   | 0.0   | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   |       |       | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |       | 0.0   |       | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |       |       |       |       |       |
|   1365 |  70.81 |  8.29 |  2.31 |  0.01 |  0    |  1.33 |  1.24 |  0.62 |  0.72 |  0.67 |  0.26 |  0.29 |  0.47 |  0.19 |  0.21 |  0.09 |  0.32 |  0.03 |  0.27 |  0.14 |  0.31 |  0.27 |  0.27 |  0.11 |  2.59 |  0.15 |  0.09 |  0.23 |  0.09 |       |       |  0.04 |  0.03 |  0.14 |  0.15 |  0.09 |  0.02 |  0.12 |  0.11 |  0.09 |  0.07 |       |       |  0.02 |       |       |  0.09 |  0.09 |  0.06 |  0.03 |  0.18 |  0.04 |  0.09 |  0.01 |  0.01 |  0.08 |  0.05 |  0.12 |  0.06 |  0.09 |  0.11 |  0.03 |  0.06 |       |       |  0.1  |       |  0.05 |  0.01 |  0.02 |  0.02 |  0.04 |  0.04 |       |       |  0.06 |  0.03 |  0.05 |  0.02 |       |  0.06 |  0.02 |  0.01 |  0.05 |  0.03 |  0.02 |  0.02 |  0.04 |  0.04 |  0.04 |  0.06 |  0.03 |  0    |  0    |  0.06 |  0    |  0.07 |  0.01 |  0.11 |       |       |  0.03 |  0.02 |  0.01 |       |  0.01 |  0.05 |  0.14 |  0.01 |  0.02 |       |  0.05 |  0.03 |       |  0.02 |       |  0.01 |  1.72 |  0    |  0    |  0.02 |  0.03 |  0.03 |  0.02 |  0.01 |       |  0.01 |  0.01 | 0.01  |  0.03 |  0.02 |  0.02 |  0.02 |  0.04 |  0.02 |  0.01 |  0.02 |  0    |  0.02 |       |  0.01 |  0    |  0.02 |  0.02 |  0.05 |  0.04 |  0.1  |  0.01 |       |  0.01 |  0.01 |  0.01 |  0.02 |       |  0    |       |       |       |  0.01 |       | 0.04  |  0    |  0.02 |  0.01 |       |  0.01 |       |  0.01 |  0.02 |       |       |       |  0.01 | 0.0   | 0.02  |  0.01 | 0.03  |       |       |       |  0    |       |       |       | 0.0   |       |       |       |  0.01 |  0.02 |  0.04 |  0.03 |       |       |  0    | 0.01  |  0.01 |  0.01 | 0.0   |  0    |       |       |       | 0.0   |       |       |       | 0.01  | 0.0   |  0.02 |       | 0.0   |       | 0.0   |  0.01 |  0.01 | 0.01  | 0.0   | 0.0   | 0.01  |       |       |  0.01 |  0    |       | 0.0   |       |  0.01 |       | 0.0   |       |       |       | 0.17  | 0.08  | 0.14  | 0.12  | 0.08  | 0.07  | 0.09  | 0.06  | 0.06  | 0.02  | 0.12  | 0.01  | 0.02  | 0.03  | 0.06  | 0.0   | 0.02  | 0.0   | 0.0   | 0.02  | 0.01  | 0.03  |       | 0.0   | 0.01  | 0.01  | 0.01  | 0.0   | 0.0   |       |       |       |       | 0.0   |       | 0.01  |       | 0.0   |       | 0.01  |       |       |       | 0.0   |       | 0.01  | 0.0   |       | 0.0   |       |       |       |       |       |       | 0.0   | 0.0   | 0.0   |       |       |       | 0.0   | 0.0   |       |       |       |       | 0.0   |       | 0.0   | 0.0   | 0.0   |       |       |
|   1366 |  72.56 |  7.69 |  2.13 |  1.86 |  1.61 |  1.42 |  1.26 |  0.63 |  0.56 |  0.53 |  0.28 |  0.4  |  0.42 |  0.47 |  0.19 |  0.37 |  0.3  |  0.17 |  0.28 |  0.23 |  0.2  |  0.24 |  0.31 |  0.14 |  0.02 |  0.2  |  0.15 |  0.2  |  0.09 | 0.13  | 0.1   |  0.13 |  0.11 |  0.14 |  0.14 |  0.08 |  0.06 |  0.1  |  0.09 |  0.13 |  0.08 | 0.07  | 0.06  |  0.08 | 0.05  | 0.04  |  0.08 |  0.09 |  0.04 |  0.04 |  0.05 |  0.04 |  0.05 |  0.13 |  0.06 |  0.05 |  0.09 |  0.06 |  0.05 |  0.04 |  0.04 |  0.04 |  0.07 | 0.03  | 0.04  |  0.08 | 0.03  |  0.05 |  0.08 |  0.03 |  0.04 |  0.06 |  0.02 | 0.08  | 0.03  |  0.07 |  0.01 |  0.01 |  0.03 | 0.02  |  0.02 |  0.02 |  0.04 |  0.04 |  0.05 |  0.03 |  0.02 |  0.03 |  0.03 |  0.06 |  0.04 |  0.02 |  0.01 |  0.02 |  0.03 |  0.01 |  0.04 |  0.02 |  0.02 | 0.0   | 0.01  |  0.04 |  0.02 |  0.01 | 0.02  |  0.02 |  0.02 |  0.02 |  0.01 |  0.01 | 0.03  |  0.01 |  0.01 | 0.01  |  0.02 | 0.03  |  0    |  0.01 |  0.02 |  0    |  0.03 |  0.01 |  0.01 |  0.02 |  0.01 | 0.02  |  0.02 |  0.01 | 0.01  |  0.03 |  0.02 |  0.01 |  0.03 |  0.02 |  0    |  0    |  0.03 |  0.02 |  0.01 | 0.0   |  0.03 |  0.01 |  0.01 |  0.02 |  0.05 |  0.01 |  0    |  0.01 |       |  0.01 |  0    |  0    |  0.01 | 0.0   |  0.02 | 0.01  | 0.01  | 0.01  |  0.01 | 0.0   |       |  0    |  0    |  0.01 |       |  0    |       |  0.01 |  0.02 | 0.0   | 0.01  |       |  0    |       | 0.02  |  0.01 | 0.0   |       | 0.02  |       |  0.01 |       | 0.01  |       |       | 0.0   | 0.0   | 0.01  |  0    |  0.02 |  0    |  0    | 0.0   | 0.0   |  0.01 | 0.01  |  0.02 |  0.01 |       |  0.01 |       | 0.01  | 0.0   |       | 0.01  | 0.0   | 0.01  | 0.01  |       |  0.01 |       | 0.01  | 0.0   |       |  0.01 |  0.01 |       |       |       |       |       |       |  0.01 |  0.01 |       |       | 0.01  |  0    | 0.01  |       | 0.0   |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       | 0.0   |       |       |       | 0.0   |       |       |       |       |       |       |       |       | 0.0   |       |       |       |       |       | 0.01  |       |       | 0.0   | 0.01  |       |       |       |       |       |       |       |       |       |       | 0.0   |       |       |       |       |       |       |       |       |       |       |       | 0.0   |       |
|   1367 |  73.14 |  7.06 |  2.54 |  1.81 |  1.53 |  1.42 |  1.14 |  0.66 |  0.51 |  0.53 |  0.32 |  0.35 |  0.36 |  0.42 |  0.25 |  0.34 |  0.3  |  0.14 |  0.22 |  0.3  |  0.21 |  0.23 |  0.21 |  0.13 |  0.02 |  0.17 |  0.18 |  0.15 |  0.1  | 0.1   | 0.09  |  0.14 |  0.13 |  0.14 |  0.11 |  0.11 |  0.09 |  0.1  |  0.12 |  0.14 |  0.1  | 0.06  | 0.09  |  0.1  | 0.06  | 0.06  |  0.09 |  0.06 |  0.04 |  0.08 |  0.07 |  0.05 |  0.05 |  0.09 |  0.03 |  0.05 |  0.08 |  0.04 |  0.06 |  0.05 |  0.04 |  0.05 |  0.04 | 0.04  | 0.04  |  0.07 | 0.04  |  0.03 |  0.06 |  0.02 |  0.05 |  0.07 |  0.02 | 0.04  | 0.03  |  0.07 |  0.02 |  0.03 |  0.03 | 0.02  |  0.03 |  0.02 |  0.01 |  0.03 |  0.02 |  0.02 |  0.03 |  0.03 |  0.03 |  0.06 |  0.03 |  0.05 |  0.02 |  0.03 |  0.02 |  0.02 |  0.1  |  0.02 |  0.03 | 0.01  | 0.03  |  0.06 |  0.01 |  0.01 | 0.01  |  0.02 |  0.01 |  0.03 |  0.02 |  0.02 | 0.03  |  0.02 |  0.01 | 0.02  |  0.02 | 0.01  |  0    |  0.07 |  0.01 |  0.02 |  0.02 |  0.02 |  0.01 |  0.02 |  0.01 | 0.01  |  0.02 |  0.02 |       |  0.03 |  0.02 |  0    |  0    |  0.02 |  0.01 |  0.01 |  0.03 |  0.01 |  0    | 0.0   |  0.01 |  0.01 |  0.02 |  0.02 |  0.05 |  0    |  0.02 |  0.01 | 0.0   |  0.01 |  0.01 |  0.01 |  0.01 |       |  0    | 0.0   | 0.0   | 0.0   |  0.02 | 0.01  | 0.01  |  0.01 |  0.01 |  0.01 | 0.01  |  0.01 | 0.0   |  0.01 |  0.01 | 0.01  | 0.01  | 0.01  |  0    | 0.0   |       |  0.02 |       | 0.0   | 0.0   |       |  0    | 0.01  | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.01  |  0    |  0.01 |  0.02 |  0.01 | 0.01  |       |  0.01 |       |  0.01 |  0    | 0.01  |  0.01 |       | 0.0   | 0.0   |       | 0.0   |       | 0.0   | 0.0   | 0.0   |  0    | 0.0   |       |       | 0.0   |  0    |  0.01 | 0.01  |       |       | 0.01  |       |       |  0    |  0.01 |       |       |       |  0    | 0.01  |       | 0.0   |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       | 0.01  |       |       |       | 0.0   |       |       | 0.0   |       |       |       |       |       | 0.0   |       |       |       |       | 0.0   | 0.0   |       | 0.0   | 0.0   |       | 0.01  |       | 0.0   |       |       | 0.0   | 0.0   |       |       |       | 0.0   |       |       | 0.0   |       |       |       |       |       |       |       |       | 0.0   | 0.0   |
|   1368 |  71.76 |  7.65 |  3.35 |  2.16 |  1.57 |  1.47 |  1.08 |  0.66 |  0.54 |  0.53 |  0.42 |  0.41 |  0.39 |  0.36 |  0.3  |  0.3  |  0.27 |  0.27 |  0.26 |  0.26 |  0.21 |  0.21 |  0.2  |  0.18 |  0.17 |  0.16 |  0.15 |  0.12 |  0.11 | 0.1   | 0.1   |  0.1  |  0.09 |  0.09 |  0.09 |  0.08 |  0.08 |  0.08 |  0.08 |  0.08 |  0.07 | 0.07  | 0.07  |  0.07 | 0.07  | 0.06  |  0.06 |  0.06 |  0.06 |  0.06 |  0.06 |  0.06 |  0.06 |  0.06 |  0.05 |  0.05 |  0.05 |  0.05 |  0.05 |  0.05 |  0.05 |  0.05 |  0.05 | 0.05  | 0.04  |  0.04 | 0.04  |  0.04 |  0.04 |  0.04 |  0.04 |  0.04 |  0.04 | 0.04  | 0.04  |  0.04 |  0.03 |  0.03 |  0.03 | 0.03  |  0.03 |  0.03 |  0.03 |  0.03 |  0.03 |  0.03 |  0.03 |  0.03 |  0.03 |  0.03 |  0.03 |  0.02 |  0.02 |  0.02 |  0.02 |  0.02 |  0.02 |  0.02 |  0.02 | 0.02  | 0.02  |  0.02 |  0.02 |  0.02 | 0.02  |  0.02 |  0.02 |  0.02 |  0.02 |  0.02 | 0.02  |  0.02 |  0.02 | 0.02  |  0.02 | 0.02  |  0.02 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 | 0.01  |  0.01 |  0.01 | 0.01  |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 | 0.01  |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 |  0.01 | 0.01  |  0.01 |  0.01 |  0.01 |  0.01 | 0.01  |  0.01 | 0.01  | 0.01  | 0.01  |  0.01 | 0.01  | 0.01  |  0.01 |  0.01 |  0.01 | 0.01  |  0.01 | 0.01  |  0.01 |  0.01 | 0.01  | 0.01  | 0.01  |  0.01 | 0.0   | 0.0   |  0    | 0.0   | 0.0   | 0.0   | 0.0   |  0    | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |  0    |  0    |  0    |  0    | 0.0   | 0.0   |  0    | 0.0   |  0    |  0    | 0.0   |  0    | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |  0    | 0.0   | 0.0   | 0.0   | 0.0   |  0    |  0    | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |  0    |  0    | 0.0   | 0.0   | 0.0   |  0    | 0.0   | 0.0   | 0.0   | 0.0   | 0.0   |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |


### Work_Place

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL13
      type: UInt32
    1366:
      column_code: COL11
      type: UInt32
    
    ```
#### Column Codes

| Years     | Work_Place                                          |
|:----------|:----------------------------------------------------|
| 1363-1365 | [COL13](/HBSIR/tables/raw/members_properties#col13) |
| 1366-1368 | [COL11](/HBSIR/tables/raw/members_properties#col11) |
| 1369-1402 |                                                     |


#### Summary Statistics

**numeric data**

|   Year |   Count |    Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|--------:|---------------------:|----------:|---------:|----------:|
|   1363 |   42121 | 4089.02 |              3032.63 |         0 |     3214 |      9600 |
|   1364 |   41248 | 3978.68 |              2990.03 |         0 |     3214 |      9600 |
|   1365 |    8917 | 3747.96 |              2930.17 |      1110 |     3214 |      9599 |
|   1366 |    8597 | 3909.85 |              3015.96 |       110 |     3214 |      9599 |
|   1367 |   12282 | 3969.97 |              3058.28 |       110 |     3214 |      9600 |
|   1368 |   18013 | 3748.77 |              2991.9  |       110 |     3214 |      9599 |


### Work_Type

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL14
      type: UInt32
    1366:
      column_code: COL12
      type: UInt32
    
    ```
#### Column Codes

| Years     | Work_Type                                           |
|:----------|:----------------------------------------------------|
| 1363-1365 | [COL14](/HBSIR/tables/raw/members_properties#col14) |
| 1366-1368 | [COL12](/HBSIR/tables/raw/members_properties#col12) |
| 1369-1402 |                                                     |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |   42121 |   3.28 |                 1.24 |         1 |        3 |         5 |
|   1364 |   41248 |   3.27 |                 1.23 |         1 |        3 |         5 |
|   1365 |    8917 |   3.3  |                 1.27 |         1 |        3 |         5 |
|   1366 |    8597 |   3.25 |                 1.31 |         1 |        3 |         5 |
|   1367 |   12282 |   3.26 |                 1.26 |         1 |        3 |         5 |
|   1368 |   18013 |   3.35 |                 1.28 |         1 |        3 |         5 |


### Weeks_in_Employment

??? abstract "Column Metadata"
    ``` yaml
    1363:
      column_code: COL15
      type: UInt32
    1366:
      column_code: COL13
      type: UInt32
    
    ```
#### Column Codes

| Years     | Weeks_in_Employment                                 |
|:----------|:----------------------------------------------------|
| 1363-1365 | [COL15](/HBSIR/tables/raw/members_properties#col15) |
| 1366-1368 | [COL13](/HBSIR/tables/raw/members_properties#col13) |
| 1369-1402 |                                                     |


#### Summary Statistics

**numeric data**

|   Year |   Count |   Mean |   Standard Deviation |   Minimum |   Median |   Maximum |
|-------:|--------:|-------:|---------------------:|----------:|---------:|----------:|
|   1363 |  144063 |  12.71 |                21.41 |         0 |        0 |        52 |
|   1364 |  145536 |  12.37 |                21.17 |         0 |        0 |        52 |
|   1365 |   30546 |  12.83 |                21.47 |         0 |        0 |        52 |
|   1366 |    6876 |  45.74 |                13.1  |         0 |       52 |        52 |
|   1367 |   10020 |  45.59 |                13.15 |         0 |       52 |        52 |
|   1368 |   14009 |  45.86 |                13.04 |         0 |       52 |        52 |


