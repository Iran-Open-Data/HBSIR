# members_properties

## Old to New Titles

| Years     | ADDRESS   | COL01         | COL03        | COL04   | COL05   | COL06              | COL07           | COL08              | COL09           | COL10           | COL11          | COL12     | COL13               | COL14     | COL15               |
|:----------|:----------|:--------------|:-------------|:--------|:--------|:-------------------|:----------------|:-------------------|:----------------|:----------------|:---------------|:----------|:--------------------|:----------|:--------------------|
| 1363      | ID        | Member_Number | Relationship | Sex     | Age     | Weeks_in_Household | Marrital_State  | Nationality        | Literacy_Status | Education_Level | Activity_State | Job_Code  | Work_Place          | Work_Type | Weeks_in_Employment |
| 1364-1365 | ID        | Member_Number | Relationship | Sex     | Age     | Marrital_State     | Nationality     | Weeks_in_Household | Literacy_Status | Education_Level | Activity_State | Job_Code  | Work_Place          | Work_Type | Weeks_in_Employment |
| 1366-1368 | ID        | Member_Number | Relationship | Sex     | Age     | Weeks_in_Household | Literacy_Status | Education_Level    | Activity_State  | Job_Code        | Work_Place     | Work_Type | Weeks_in_Employment |           |                     |
| 1369-1383 | ID        | Member_Number | Relationship | Sex     | Age     | Is_Literate        | Is_Student      | Education_Level    | Activity_State  | Marrital_State  |                |           |                     |           |                     |


| Years     | ADDRESS   | DYCOL01       | DYCOL03      | DYCOL04   | DYCOL05   | DYCOL06     | DYCOL07    | DYCOL08         | DYCOL09        | DYCOL10        |
|:----------|:----------|:--------------|:-------------|:----------|:----------|:------------|:-----------|:----------------|:---------------|:---------------|
| 1384-1401 | ID        | Member_Number | Relationship | Sex       | Age       | Is_Literate | Is_Student | Education_Level | Activity_State | Marrital_State |


## New to Old Titles

| Years     | ID      | Member_Number   | Relationship   | Sex     | Age     | Is_Literate   | Is_Student   | Education_Level   | Activity_State   | Marrital_State   | Weeks_in_Household   | Nationality   | Literacy_Status   | Job_Code   | Work_Place   | Work_Type   | Weeks_in_Employment   |
|:----------|:--------|:----------------|:---------------|:--------|:--------|:--------------|:-------------|:------------------|:-----------------|:-----------------|:---------------------|:--------------|:------------------|:-----------|:-------------|:------------|:----------------------|
| 1363      | ADDRESS | COL01           | COL03          | COL04   | COL05   |               |              | COL10             | COL11            | COL07            | COL06                | COL08         | COL09             | COL12      | COL13        | COL14       | COL15                 |
| 1364-1365 | ADDRESS | COL01           | COL03          | COL04   | COL05   |               |              | COL10             | COL11            | COL06            | COL08                | COL07         | COL09             | COL12      | COL13        | COL14       | COL15                 |
| 1366-1368 | ADDRESS | COL01           | COL03          | COL04   | COL05   |               |              | COL08             | COL09            |                  | COL06                |               | COL07             | COL10      | COL11        | COL12       | COL13                 |
| 1369-1383 | ADDRESS | COL01           | COL03          | COL04   | COL05   | COL06         | COL07        | COL08             | COL09            | COL10            |                      |               |                   |            |              |             |                       |
| 1384-1401 | ADDRESS | DYCOL01         | DYCOL03        | DYCOL04 | DYCOL05 | DYCOL06       | DYCOL07      | DYCOL08           | DYCOL09          | DYCOL10          |                      |               |                   |            |              |             |                       |


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
| 1363-1401 | [ADDRESS](/HBSIR/tables/raw/members_properties#address) |


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
    
    ```
#### Column Codes

| Years     | Member_Number                                           |
|:----------|:--------------------------------------------------------|
| 1363-1383 | [COL01](/HBSIR/tables/raw/members_properties#col01)     |
| 1384-1401 | [DYCOL01](/HBSIR/tables/raw/members_properties#dycol01) |


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
    
    ```
#### Column Codes

| Years     | Relationship                                            |
|:----------|:--------------------------------------------------------|
| 1363-1383 | [COL03](/HBSIR/tables/raw/members_properties#col03)     |
| 1384-1401 | [DYCOL03](/HBSIR/tables/raw/members_properties#dycol03) |


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


#### Categories

|    | 1363-1401    |
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
    
    ```
#### Column Codes

| Years     | Sex                                                     |
|:----------|:--------------------------------------------------------|
| 1363-1383 | [COL04](/HBSIR/tables/raw/members_properties#col04)     |
| 1384-1401 | [DYCOL04](/HBSIR/tables/raw/members_properties#dycol04) |


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


#### Categories

|    | 1363-1401   |
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
    
    ```
#### Column Codes

| Years     | Age                                                     |
|:----------|:--------------------------------------------------------|
| 1363-1383 | [COL05](/HBSIR/tables/raw/members_properties#col05)     |
| 1384-1401 | [DYCOL05](/HBSIR/tables/raw/members_properties#dycol05) |


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
    
    ```
#### Column Codes

| Years     | Is_Literate                                             |
|:----------|:--------------------------------------------------------|
| 1363-1368 |                                                         |
| 1369-1383 | [COL06](/HBSIR/tables/raw/members_properties#col06)     |
| 1384-1401 | [DYCOL06](/HBSIR/tables/raw/members_properties#dycol06) |


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
    
    ```
#### Column Codes

| Years     | Is_Student                                              |
|:----------|:--------------------------------------------------------|
| 1363-1368 |                                                         |
| 1369-1383 | [COL07](/HBSIR/tables/raw/members_properties#col07)     |
| 1384-1401 | [DYCOL07](/HBSIR/tables/raw/members_properties#dycol07) |


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
        21: Secondary
        31: Tertiary
        41: Pre_University
        51: College
        52: Bachelors
        53: Masters
        61: PhD
        71: Unofficial
      replace: null
    1394:
      column_code: DYCOL08
      type: category
      categories:
        11: Primary
        21: Secondary
        31: Tertiary
        41: Pre_University
        51: College
        52: Bachelors
        53: Masters
        61: PhD
        71: Unofficial
      replace:
        '1': null
    1395:
      column_code: DYCOL08
      type: category
      categories:
        11: Primary
        21: Secondary
        31: Tertiary
        41: Pre_University
        51: College
        52: Bachelors
        53: Masters
        61: PhD
        71: Unofficial
      replace: null
    1396:
      column_code: DYCOL08
      type: category
      categories:
        11: Primary
        21: Secondary
        31: Tertiary
        41: Pre_University
        51: College
        52: Bachelors
        53: Masters
        61: PhD
        71: Unofficial
      replace: null
    1397:
      column_code: DYCOL08
      type: category
      categories:
        1: Primar
        2: Secondary
        3: Tertiary
        4: Pre_University
        5: College
        6: Bachelors
        7: Masters
        8: PhD
        9: Unofficial
      replace: null
    1398:
      column_code: DYCOL08
      type: category
      categories:
        1: Primar
        2: Secondary
        3: Tertiary
        4: Pre_University
        5: College
        6: Bachelors
        7: Masters
        8: PhD
        9: Unofficial
      replace: null
    1399:
      column_code: DYCOL08
      type: category
      categories:
        1: Primar
        2: Secondary
        3: Tertiary
        4: Pre_University
        5: College
        6: Bachelors
        7: Masters
        8: PhD
        9: Unofficial
      replace: null
    1400:
      column_code: DYCOL08
      type: category
      categories:
        1: Primar
        2: Secondary
        3: Tertiary
        4: Pre_University
        5: College
        6: Bachelors
        7: Masters
        8: PhD
        9: Unofficial
      replace: null
    1401:
      column_code: DYCOL08
      type: category
      categories:
        1: Primar
        2: Secondary
        3: Tertiary
        4: Pre_University
        5: College
        6: Bachelors
        7: Masters
        8: PhD
        9: Unofficial
      replace: null
    
    ```
#### Column Codes

| Years     | Education_Level                                         |
|:----------|:--------------------------------------------------------|
| 1363-1365 | [COL10](/HBSIR/tables/raw/members_properties#col10)     |
| 1366-1383 | [COL08](/HBSIR/tables/raw/members_properties#col08)     |
| 1384-1401 | [DYCOL08](/HBSIR/tables/raw/members_properties#dycol08) |


#### Summary Statistics

**string data**

|   Year | <NA>               | 106                | 234                | 346               | 512               | 105                | 104                | 511                | 103               | 354                | 102                | 107                | 101                | 233                | 522                | 341               | 231                | 232                | 342                | 343                | 364                | 521                | 344                | 345                | 514                 | 901                | 513                 | 353                | 352                | 2.0                 | 362               | 363                 | 108                 | 517                 | 510                  | 602                  | 905                 | 516                  | 520                  | 515                  | 310                  | 601                  | 109                  | 605                  | 1.0                   | 604                   | 606                   | 907                   | 603                   | 05                 | 04                | 02                | 01                | 03                 | 11                 | 06                 | 13                 | 12                | 34                 | 26                 | X1                 | 33                 | 31                 | 23                 | 32                 | 47                  | 53                 | 46                  | 65                  | 25                  | 45                  | X2                   | 22                  | 44                  | 21                  | 24                  | 61                  | 95                   | 89                   | 62                   | 73                   | 96                  | 63                  | 97                   | 64                  | 51                   | 52                   | 74                   | 93                   | 41                   | 81                    | 82                    | 42                    | 83                    | 71                    | 84                    | 91                    | 85                    | 86                    | 43                    | 88                    | 00                    | 92                    | 72                    | nan                | 15.0               | 14.0               | 12.0               | 11.0               | 13.0               | 16.0               | 23.0               | 34.0                | 21.0               | 22.0               | 91.0               | 37.0               | 31.0                | 33.0               | 32.0               | 17.0                  | 26.0                | 18.0                  | 64.0                | 52.0                | 36.0                | 19.0                 | 25.0                 | 72.0                 | 62.0                 | 61.0                | 41.0                 | 24.0                  | 63.0                 | 42.0                 | 73.0                  | 35.0                 | 87.0                  | 43.0                 | 40.0                  | 51.0                 | 70.0                  | 50.0                 | 88.0                  | 82.0                  | 49.0                  | 93.0                  | 47.0                  | 81.0                  | 89.0                  | 83.0                  | 71.0                  | 60.0                  | 10.0                  | 45.0                  | 84.0                  | 92.0                  | 30.0                  | 85.0                  | 38.0                  | 80.0                 | 20.0                 | 28.0                  | 86.0                  | 29.0                  | 46.0                  | 39.0                  | 94.0                  | 3.0                | 4.0                 | 6.0                 | 5.0                 | 48.0               | 44.0                | 76.0                 | 75.0                 | 78.0                  | 27.0                  | 77.0                  | 106                | 214               | 105                | 313                | 104                | 213                | 212                | 211                | 312                | 103                | 107               | 317                | 102                | 311                | 101                | 512                | 322                | 511                | 522                | 324                | 314                | 319                | 321                | 521                | 901                 | 315                 | 316                  | 323                 | 326                 | 108                 | 216                 | 514                 | 002                  | 513                 | 109                  | 905                 | 328                  | 517                  | 325                   | 602                  | 510                  | 318                   | 215                  | 310                  | 516                  | 520                  | 210                  | 327                   | 301                 | 302                  | 906                 | 515                  | 222                   | 221                   | 100                  | 303                   | 601                  | 605                  | 606                   | 902                   | 908                   | 300                   | 220                   | 907                   | 904                   | 604                   | 903                   | 32A                   | 217                   | 214               | 313               | 213                | 317                | 212                | 312                | 211               | 311               | 322                | 324                | 314                | 321                | 319                | 315                | 323                 | 326                 | 301                 | 316                 | 216                 | 302                   | 325                  | 328                  | 100                  | 318                  | 908                   | 327                  | 300                   | 210                   | 221                   | 222                   | 215                  | 902                   | 303                   | 217                   | 903                   | 906                   | 31D                   | 001                  | 31C                   | 603                   | 31b                   | 220                  | 112                   |
|-------:|:-------------------|:-------------------|:-------------------|:------------------|:------------------|:-------------------|:-------------------|:-------------------|:------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-------------------|:--------------------|:-------------------|:-------------------|:--------------------|:------------------|:--------------------|:--------------------|:--------------------|:---------------------|:---------------------|:--------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:-------------------|:------------------|:------------------|:------------------|:-------------------|:-------------------|:-------------------|:-------------------|:------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-------------------|:--------------------|:--------------------|:--------------------|:--------------------|:---------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------------------|:---------------------|:---------------------|:---------------------|:---------------------|:--------------------|:--------------------|:---------------------|:--------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-------------------|:-------------------|:----------------------|:--------------------|:----------------------|:--------------------|:--------------------|:--------------------|:---------------------|:---------------------|:---------------------|:---------------------|:--------------------|:---------------------|:----------------------|:---------------------|:---------------------|:----------------------|:---------------------|:----------------------|:---------------------|:----------------------|:---------------------|:----------------------|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:---------------------|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:-------------------|:--------------------|:--------------------|:--------------------|:-------------------|:--------------------|:---------------------|:---------------------|:----------------------|:----------------------|:----------------------|:-------------------|:------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:--------------------|:---------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------------------|:---------------------|:--------------------|:---------------------|:--------------------|:---------------------|:---------------------|:----------------------|:---------------------|:---------------------|:----------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:----------------------|:--------------------|:---------------------|:--------------------|:---------------------|:----------------------|:----------------------|:---------------------|:----------------------|:---------------------|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:------------------|:------------------|:-------------------|:-------------------|:-------------------|:-------------------|:------------------|:------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------------------|:----------------------|:---------------------|:---------------------|:---------------------|:---------------------|:----------------------|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:---------------------|:----------------------|:----------------------|:----------------------|:---------------------|:----------------------|
|   1363 | 54.64900772578664  |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       | 6.2736441695647045 | 4.469572339879081 | 4.468878199121217 | 4.0017214690795   | 3.6484038233272944 | 2.8300118698069596 | 2.7876692835773236 | 2.556520411208985  | 2.498906728306366 | 2.4614231273817704 | 1.5347452156348262 | 1.4070233161880565 | 0.9801267501023858 | 0.9495845567564191 | 0.7913204639636826 | 0.765637255922756  | 0.41648445471772766 | 0.403295780318333  | 0.35609420878365716 | 0.30472779270180406 | 0.23253715388406462 | 0.21448949417962973 | 0.1478519814247933   | 0.1422988553618903  | 0.11800392883668949 | 0.10273283216370614 | 0.06455509048124779 | 0.06177852744979627 | 0.054142979113304596 | 0.03748360092459549  | 0.03262461561955533  | 0.031930474861692454 | 0.02845977107237806 | 0.02498906728306366 | 0.02498906728306366  | 0.02429492652520078 | 0.021518363493749262 | 0.018741800462297745 | 0.018741800462297745 | 0.010412111367943191 | 0.006941407578628794 | 0.006247266820765915  | 0.0055531260629030355 | 0.003470703789314397  | 0.0027765630314515177 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0006941407578628794 | 0.0006941407578628794 | 0.0006941407578628794 |                       |                       |                       |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1364 | 55.7415347405453   |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       | 6.587373570800352  | 4.404408531222515 | 4.528776385224274 | 4.356310466138962 | 3.5997966138962183 | 2.8838225593667546 | 2.347872691292876  | 2.5787434036939314 | 2.257173482849604 | 2.2269404133685136 | 1.3893469656992083 | 1.297273526824978  | 0.8630167106420404 | 0.8836301671064204 | 0.6843667546174143 | 0.7427715479331574 | 0.34493183817062445 | 0.4088335532102023 | 0.37172933157431837 | 0.29271108179419525 | 0.21644129287598945 | 0.22537379067722077 | 0.019926341248900616 | 0.12711631486367633 | 0.10581574318381706 | 0.06252748460861918 | 0.05359498680738786 | 0.05290787159190853 | 0.04672383465259455  | 0.030920184696569923 | 0.043288258575197885 | 0.03023306948109059  | 0.03366864555848725 | 0.01786499560246262 | 0.014429419525065964 | 0.02679749340369393 | 0.02542326297273527  | 0.01236807387862797  | 0.02542326297273527  | 0.008245382585751979 | 0.004809806508355321 | 0.0027484608619173265 | 0.006184036939313985  | 0.0006871152154793316 | 0.0020613456464379947 | 0.003435576077396658  | 0.0013742304309586632 |                       | 0.003435576077396658  | 0.0027484608619173265 |                       |                       | 0.0006871152154793316 | 0.0006871152154793316 | 0.0006871152154793316 |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1365 | 54.31480390231127  |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       | 6.95017350880639   | 4.543966476789104 | 4.570156485300858 | 4.622536502324364 | 3.6109474235579126 | 2.733582138414195  | 2.5076933150003273 | 2.560073332023833  | 2.311268251162182 | 2.3996595298893473 | 1.4633667255941858 | 1.6499705362404242 | 0.8871865383356249 | 0.8740915340797486 | 0.720225234073201  | 0.6842139723695411 | 0.25535258298958946 | 0.4026713808681988 | 0.25207883192562036 | 0.38957637661232236 | 0.21279381915799123 | 0.1604138021344857  | 0.06547502127938191  | 0.10803378511098016 | 0.05892751915144372 | 0.0785700255352583  | 0.03928501276762915 | 0.0785700255352583  | 0.03601126170366005  | 0.02291625744778367  | 0.09166502979113468  | 0.05892751915144372  | 0.02619000851175277 | 0.05565376808747463 | 0.009821253191907287 | 0.04255876383159824 | 0.01636875531984548  | 0.013095004255876385 | 0.04583251489556734  | 0.02619000851175277  |                      | 0.006547502127938192  | 0.006547502127938192  | 0.006547502127938192  | 0.003273751063969096  | 0.006547502127938192  | 0.006547502127938192  |                       | 0.006547502127938192  | 0.003273751063969096  |                       |                       |                       |                       | 0.003273751063969096  |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1366 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 53.161405636589954 | 6.150458012830743  | 4.76844020299384   | 4.1843541540327465 | 4.09817752385816   | 3.7790048195078354 | 3.6704861000287257 | 2.7799942548913217 | 2.741693530369283   | 2.6938176247167345 | 2.505505729150043  | 1.3724426287063929 | 1.305416360792825  | 1.1554051897481727  | 1.104337557052121  | 0.8426159394848552 | 0.7021799495707127    | 0.6702626791356804  | 0.5457853244390539    | 0.40215760748140816 | 0.3415147936548466  | 0.15639462513165875 | 0.12447735469662635  | 0.08298490313108423  | 0.07340972200057451  | 0.06702626791356803  | 0.0638345408700648  | 0.0638345408700648   | 0.06064281382656155   | 0.05745108678305831  | 0.04149245156554211  | 0.03830072452203887   | 0.0319172704350324   | 0.028725543391529156  | 0.0159586352175162   | 0.012766908174012957  | 0.012766908174012957 | 0.012766908174012957  | 0.009575181130509718 | 0.009575181130509718  | 0.009575181130509718  | 0.006383454087006479  | 0.006383454087006479  | 0.006383454087006479  | 0.006383454087006479  | 0.006383454087006479  | 0.0031917270435032393 | 0.0031917270435032393 | 0.0031917270435032393 | 0.0031917270435032393 | 0.0031917270435032393 | 0.0031917270435032393 |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1367 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 52.173722883135056 | 5.764520643806858  | 4.528953813855844  | 4.3627536738978305 | 4.02816655003499   | 3.9603743876836948 | 3.5470608817354794 | 3.1578026592022392 | 2.7904128761371587  | 2.9631735479356194 | 2.4405178446466063 | 1.5351644506648006 | 1.312106368089573  | 1.0628061581525543  | 1.0912351294611617 | 0.8375612316305108 | 1.1327851644506648    | 0.7041637508747376  | 0.5576452064380686    | 0.4286214135759272  | 0.4920398880335899  | 0.14870538838348496 | 0.12465010496850945  | 0.09622113365990202  | 0.05685794261721484  | 0.06779216235129461  | 0.11152904128761372 | 0.12027641707487755  | 0.03280265920223933   | 0.06560531840447865  | 0.07435269419174248  | 0.00874737578726382   | 0.05029741077676697  | 0.024055283414975506  | 0.024055283414975506 | 0.0065605318404478655 | 0.01749475157452764  | 0.00437368789363191   |                      | 0.010934219734079776  | 0.00437368789363191   | 0.015307907627711687  |                       | 0.0065605318404478655 | 0.00874737578726382   | 0.0065605318404478655 | 0.00874737578726382   |                       | 0.0065605318404478655 | 0.0065605318404478655 | 0.00874737578726382   | 0.002186843946815955  | 0.0065605318404478655 | 0.002186843946815955  |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1368 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 50.58244359782387  | 4.69404073185645   | 4.969976325980277  | 4.298951131179154  | 4.066914381575028  | 4.143737359484502  | 5.316463634510763  | 3.257921389711992  | 2.8252042080178104  | 3.2077512816894784 | 2.713889280842858  | 1.558408980449336  | 1.122556167003747  | 1.2166251195459605  | 1.0363262938400515 | 0.9689102111847984 | 1.2244641989244784    | 0.5314895818635059  | 0.6239907185300159    | 0.3668689149146324  | 0.46250568333254943 | 0.1473746923161344  | 0.06898389853095653  | 0.07995860966088143  | 0.03605976514118182  | 0.0877976890393992   | 0.07055171440666008 | 0.017245974632739133 | 0.04076321276829249   | 0.053305739773920946 | 0.03292413338977471  | 0.009406895254221346  | 0.026652869886960473 | 0.01881379050844269   | 0.015678158757035574 | 0.0015678158757035576 | 0.01881379050844269  | 0.004703447627110673  | 0.003135631751407115 | 0.00627126350281423   | 0.009406895254221346  | 0.009406895254221346  |                       | 0.0015678158757035576 | 0.009406895254221346  | 0.003135631751407115  | 0.009406895254221346  | 0.0015678158757035576 | 0.015678158757035574  |                       | 0.004703447627110673  | 0.0015678158757035576 | 0.0015678158757035576 |                       | 0.0015678158757035576 | 0.0015678158757035576 |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1369 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.000984532986777722  |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 45.6557481958433   | 4.347697669610421  | 5.125478729164821  | 4.529836272164299  | 4.2305382441838715 | 4.304378218192201  | 6.0853983912731    | 3.754024278583454  | 3.1180159691250453  | 3.474416910338581  | 2.9486762953992773 | 1.626448494156797  | 1.0298215041694971 | 1.409851237065698   | 1.2208209036043753 | 0.9825639208041667 | 1.727855391794902     | 0.4144883874334209  | 2.213230154276319     | 0.3888905297772002  | 0.5149107520847486  | 0.14866448100343602 | 0.049226649338886104 | 0.0758090399818846   | 0.03052052259010938  | 0.06301011115377421  | 0.08270077088932865 | 0.014767994801665829 | 0.03839678648433116   | 0.04725758336533066  | 0.022644258695887605 | 0.013783461814888107  | 0.040365852457886604 | 0.03248958856366482   | 0.014767994801665829 | 0.000984532986777722  | 0.013783461814888107 | 0.001969065973555444  | 0.016737060775221274 | 0.00492266493388861   | 0.003938131947110888  | 0.00492266493388861   | 0.001969065973555444  | 0.003938131947110888  | 0.0029535989603331663 | 0.00984532986777722   | 0.001969065973555444  | 0.000984532986777722  | 0.11420582646621574   | 0.00492266493388861   | 0.007876263894221776  | 0.0029535989603331663 |                       | 0.001969065973555444  | 0.003938131947110888  |                       | 0.014767994801665829 | 0.001969065973555444 |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1370 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 43.14097327576147  | 4.9169486910180105 | 5.301085307503793  | 4.6388143307270395 | 4.356789979383048  | 4.325670050958882  | 5.951686311121485  | 4.043645699614891  | 3.436807095343681   | 3.959038394211693  | 3.0847629050453182 | 1.4081767611934493 | 0.87524798692963   | 1.5025090442291982  | 1.225347181701482  | 1.1144824366903956 | 1.0882249970825066    | 0.4269265180690085  | 3.19660014781966      | 0.4142840471466916  | 0.531956276500564   | 0.09433228303574902 | 0.1769945929124363   | 0.08266230987668728  | 0.03695491500369549  | 0.09627727856225932  | 0.07682732329715641 | 0.012642470922316879 | 0.03695491500369549   | 0.06223985684832925  | 0.022367448554868326 | 0.009724977632551446  | 0.030147430660909483 | 0.022367448554868326  | 0.01069747539580659  | 0.001944995526510289  | 0.02139495079161318  | 0.0009724977632551445 | 0.01653246197533746  | 0.007779982106041156  | 0.007779982106041156  | 0.0175049597385926    | 0.005834986579530867  | 0.005834986579530867  | 0.003889991053020578  | 0.0087524798692963    | 0.004862488816275723  | 0.0029174932897654336 | 0.10989224724783132   | 0.02139495079161318   | 0.019449955265102892  | 0.0029174932897654336 | 0.014587466448827167  |                       | 0.005834986579530867  |                       | 0.005834986579530867 |                      | 0.001944995526510289  | 0.0009724977632551445 |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1371 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 42.404291879795394 | 4.778412723785166  | 5.279931265984654  | 4.51266783887468   | 3.9621962915601023 | 4.348825127877238  | 6.6046595268542205 | 4.0860773657289    | 3.8503037084398977  | 3.897258631713555  | 3.3407928388746804 | 1.295756074168798  | 0.798233695652174  | 1.5595028772378516  | 1.402653452685422  | 1.1578884271099745 | 0.8931425831202047    | 0.4136029411764706  | 3.179947250639386     | 0.5125079923273658  | 0.6833439897698209  | 0.10789641943734014 | 0.16883791560102301  | 0.060941496163682864 | 0.044956841432225066 | 0.10589833759590793  | 0.10689737851662404 | 0.013986572890025575 | 0.040960677749360616  | 0.05694533248081842  | 0.0239769820971867   | 0.009990409207161126  | 0.022977941176470586 | 0.033967391304347824  | 0.0159846547314578   | 0.0009990409207161126 | 0.02597506393861893  | 0.001998081841432225  | 0.016983695652173912 | 0.0069932864450127875 | 0.0029971227621483376 | 0.0069932864450127875 | 0.0069932864450127875 | 0.0009990409207161126 | 0.005994245524296675  | 0.00399616368286445   | 0.004995204603580563  | 0.005994245524296675  | 0.0719309462915601    | 0.0079923273657289    | 0.021978900255754476  | 0.00399616368286445   | 0.00399616368286445   | 0.0009990409207161126 | 0.005994245524296675  | 0.0009990409207161126 | 0.00399616368286445  |                      | 0.001998081841432225  | 0.004995204603580563  | 0.001998081841432225  | 0.0009990409207161126 |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1372 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 38.43157974186731  | 4.8154577703977655 | 5.425315118122122  | 4.281077817193751  | 3.669710921578987  | 4.392784361083855  | 7.431504264472791  | 4.862253755000377  | 4.457694920371349   | 4.2448486678239865 | 3.7693410823458375 | 1.289153898407427  | 0.9963016076685033 | 1.8778775756660882  | 1.6318212695297758 | 1.3027398294210883 | 0.8393086270661937    | 0.443807079779606   | 3.2349611291418223    | 0.673258359121443   | 0.7140161521624273  | 0.10868744810929128 | 0.11472563967091856  | 0.06038191561627292  | 0.06340101139708657  | 0.09057287342440938  | 0.09057287342440938 | 0.018114574684881878 | 0.046795984602611515  | 0.06340101139708657  | 0.02717186202732282  | 0.021133670465695524  | 0.02868140991772964  | 0.04528643671220469   | 0.01509547890406823  | 0.0030190957808136462 | 0.010566835232847762 | 0.010566835232847762  | 0.07698694241074798  | 0.018114574684881878  | 0.0015095478904068231 | 0.0060381915616272925 | 0.0030190957808136462 |                       | 0.0015095478904068231 | 0.0045286436712204696 | 0.0030190957808136462 | 0.0015095478904068231 | 0.23247037512265076   | 0.0015095478904068231 | 0.0015095478904068231 | 0.0030190957808136462 | 0.0045286436712204696 | 0.0015095478904068231 | 0.0060381915616272925 |                       | 0.022643218356102345 |                      | 0.0015095478904068231 | 0.0045286436712204696 |                       |                       | 0.0015095478904068231 |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1373 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 35.3252850435949   | 4.497460956213471  | 5.332950081441027  | 4.049056242215196  | 3.452141419948261  | 4.252179745137492  | 7.930439781546421  | 5.638593465555236  | 5.189230621826195   | 4.488837788636581  | 4.118999712561081  | 1.160295103957076  | 1.1372999904187027 | 2.1270480022995115  | 1.764874964070135  | 1.653731915301332  | 0.5011018491903804    | 0.5930823033438728  | 3.5412474849094564    | 0.8192009198045416  | 0.7617131359586088  | 0.11401743796109994 | 0.03257641084602855  | 0.0689853406151193   | 0.10635240011497556  | 0.05365526492287055  | 0.0651528216920571  | 0.028743891922966367 | 0.041199578422918465  | 0.05078087573057392  | 0.0546133946536361   | 0.014371945961483184  | 0.04503209734598065  | 0.055571524384401653  | 0.03832518923062182  | 0.0038325189230621823 | 0.015330075692248729 | 0.02395324326913864   | 0.05844591357669829  | 0.018204464884545368  |                       | 0.015330075692248729  |                       |                       | 0.0019162594615310911 | 0.015330075692248729  | 0.0009581297307655456 | 0.002874389192296637  | 0.6591932547666954    | 0.0019162594615310911 | 0.013413816230717638  | 0.0038325189230621823 | 0.0009581297307655456 |                       |                       | 0.0009581297307655456 | 0.056529654115167194 |                      |                       | 0.0009581297307655456 | 0.0009581297307655456 | 0.0009581297307655456 |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1374 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 35.447743854268325 | 4.286134733646235  | 5.421565438294841  | 4.07701720959772   | 3.460507768328764  | 4.142075994857257  | 8.180367737038587  | 5.787133850705578  | 5.073552571112867   | 4.477180372900434  | 4.2267556836077675 | 1.1855156425071385 | 0.9619406106231703 | 2.1887634183744598  | 1.8087374981282691 | 1.69152841674799   | 0.481744814659913     | 0.46831998595556384 | 3.4620567870254195    | 0.7951629309499099  | 0.8266596444485751  | 0.1089476483314487  | 0.024784299146490697 | 0.04027448611304739  | 0.0893267448404769   | 0.057830031341811625 | 0.04492154220301439 | 0.024784299146490697 | 0.026849657408698255  | 0.031496713498665264 | 0.030464034367561482 | 0.010326791311037791  | 0.019620903490971803 | 0.04027448611304739   | 0.02271894088428314  | 0.0051633956555188956 | 0.006712414352174564 | 0.035111090457528485  | 0.09655549875820335  | 0.013941168269901019  | 0.0005163395655518895 | 0.004130716524415116  | 0.0005163395655518895 |                       | 0.0015490186966556686 | 0.010326791311037791  | 0.0005163395655518895 | 0.0015490186966556686 | 0.7218427126415415    | 0.009810451745485902  | 0.02116992218762747   | 0.0005163395655518895 | 0.006196074786622674  | 0.001032679131103779  | 0.001032679131103779  | 0.0005163395655518895 | 0.03201305306421715  |                      | 0.0005163395655518895 | 0.0015490186966556686 | 0.002065358262207558  | 0.0005163395655518895 | 0.001032679131103779  | 0.0005163395655518895 |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1375 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.8756534038497017  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.17658376307905857   |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 34.02004796752967  | 4.190569899935868  | 5.2474368998568    | 4.108866964779885  | 3.3243430820455604 | 4.1642141144016795 | 8.946910662672302  | 6.112785191562634  | 0.8917040772400221  | 4.787089179192986  | 4.146643590712221  | 1.1991882418055468 |                    | 0.2169959675648133  | 3.049364386305534  | 3.4306447503667847 | 0.0008785261844729283 | 0.5315083416061216  | 0.0008785261844729283 |                     | 0.7933091445790541  |                     |                      | 0.07291767331125304  | 0.10366608976780554  | 0.9259665984344664   | 0.8152722991908773  | 1.2290581320776266   | 0.004392630922364641  |                      | 1.0841013116395934   | 0.007906735660256355  | 0.36283131418731934  |                       | 0.18800460347720663  | 0.007028209475783426  | 0.09312377555413039  |                       |                      |                       | 0.027234311718660774  | 0.0017570523689458566 | 0.006149683291310498  | 0.023720206980769064  | 0.027234311718660774  | 0.01581347132051271   | 0.023720206980769064  | 0.032505468825498346  | 0.0017570523689458566 | 0.0017570523689458566 | 0.011420840398148066  |                       | 0.040412204485754694  | 0.01932757605840442   | 0.020206102242877347  | 0.16867702741880222   |                      |                      |                       | 0.0017570523689458566 |                       | 0.11157282542806188   | 1.2764985460391647    | 0.0008785261844729283 | 1.1192423590185105 | 0.3698595236631028  | 0.1660414488653834  | 0.1282648229330475  | 0.0869740922628199 | 0.08433851370940111 | 0.06940356857336133  | 0.04129073067022763  | 0.007028209475783426  | 0.0026355785534187847 | 0.0026355785534187847 |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1376 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.7425157739293866  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.030429140376784354  |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 33.154338389940484 | 4.270819349353381  | 5.089721215375666  | 3.7400993421935826 | 3.0975074954132547 | 3.9960621112453576 | 9.075938604734416  | 6.536895332706851  | 0.5656240211214033  | 4.716516758401576  | 4.559896182932832  | 0.9620978207365642 |                    | 0.15930549961963575 | 3.45281245804806   | 2.559627690517743  |                       | 0.5155054369714055  |                       |                     | 0.8099521188526424  |                     |                      | 0.10560701660178101  | 0.10292209245088826  | 0.9916319863963843   | 0.8887098939454959  | 1.6879223161945673   | 0.0044748735848212295 |                      | 1.8830268044927732   | 0.02326934264107039   | 0.44032756074640894  |                       | 0.2890768335794514   | 0.0017899494339284915 | 0.08502259811160334  |                       |                      |                       | 0.03400903924464134   | 0.010739696603570948  | 0.002684924150892737  | 0.043853761131248045  | 0.024164317358034634  | 0.00805477245267821   | 0.02505929207499888   | 0.05101355886696201   |                       | 0.005369848301785474  | 0.04832863471606927   |                       | 0.030429140376784354  | 0.01610954490535642   | 0.008949747169642459  | 0.10560701660178101   |                      |                      |                       |                       |                       | 0.2872868841455229    | 1.1214033203562       |                       | 1.3612565445026177 | 0.40273862263391064 | 0.1897346399964201  | 0.13424620754463684 | 0.258647693202667  | 0.17452006980802792 | 0.06712310377231842  | 0.043853761131248045 | 0.0017899494339284915 | 0.0008949747169642458 | 0.002684924150892737  |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1377 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.7554894142752848  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.046049306452518673  |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 32.31650474532487  | 5.275453473353176  | 5.0126354804290445 | 3.7153928230471167 | 2.913460998483742  | 3.954624585837031  | 7.95754478575841   | 6.906272814061885  | 0.551468523614309   | 4.571236030774414  | 4.584713876565396  | 0.8356264390408267 |                    | 0.14151738080530127 | 3.3762003706407593 | 2.1160217891840287 |                       | 0.4369068343909699  |                       |                     | 0.7435278261357893  |                     |                      | 0.1066996125119335   | 0.1066996125119335   | 1.1647105071039479   | 1.0108384343235806  | 1.8262481046779355   | 0.008985230527320717  |                      | 2.44510585724715     | 0.010108384343235806  | 0.3818722974111305   |                       | 0.526759139664177    | 0.021339922502386702  | 0.09546807435278262  |                       |                      |                       | 0.02807884539787724   | 0.044926152636603586  |                       | 0.1179311506710844    | 0.031448306845622505  | 0.006738922895490537  | 0.02807884539787724   | 0.04155669118885831   |                       | 0.005615769079575448  | 0.09322176672095243   |                       | 0.037064075925197955  | 0.013477845790981074  | 0.022463076318301793  | 0.15387207278036727   |                      |                      |                       | 0.0011231538159150896 |                       | 0.3324535295108665    | 1.1748188914471835    | 0.0011231538159150896 | 1.2983658111978436 | 0.3346998371426967  | 0.25158645476498004 | 0.162857303307688   | 0.5402369854551581 | 0.25158645476498004 | 0.06289661369124501  | 0.03818722974111304  | 0.006738922895490537  | 0.0022463076318301792 | 0.0011231538159150896 |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1378 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.5374604014559392  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.045766263113107025  |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 31.446428443732525 | 5.079340107693739  | 4.8426427156556375 | 3.4989738345692607 | 4.3685328337182945 | 3.6713124191045545 | 7.911842735678378  | 7.244656431232614  | 0.30391659098547635 | 4.534435537503307  | 4.590213170672406  | 0.805915289507369  |                    | 0.08152115617022189 | 3.5683383271000637 | 1.8478128731916965 |                       | 0.3375261904591643  |                       |                     | 0.7944737237290923  |                     |                      | 0.0543474374468146   | 0.1086948748936292   | 1.1455867735499603   | 0.945359372430117   | 2.048755372172682    | 0.0035754893057114868 |                      | 2.9404824050171268   | 0.008581174333707569  | 0.4269134231019515   |                       | 0.7537131456439814   | 0.015017055083988245  | 0.10511938558791772  |                       |                      |                       | 0.022168033695411215  | 0.11370055992162527   | 0.0007150978611422973 | 0.1566064315901631    | 0.031464305890261085  | 0.005720782889138378  | 0.01644725080627284   | 0.030749208029118784  |                       | 0.009296272194849865  | 0.12442702783875972   |                       | 0.03003411016797649   | 0.09010233050392946   | 0.015732152945130543  | 0.10654958131020231   |                      |                      |                       | 0.0007150978611422973 |                       | 0.41475675946253243   | 0.9467895681524017    |                       | 1.0862336510751498 | 0.3082071781523301  | 0.14587996367302866 | 0.14945545297874013 | 0.7730207878948234 | 0.26816169792836153 | 0.045766263113107025 | 0.034324697334830276 | 0.0014301957222845945 | 0.002860391444569189  | 0.0014301957222845945 |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1379 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.5206317629683215  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.046719112638273504  |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 30.870030442776624 | 5.924284896163004  | 4.743497000934383  | 3.470777948578835  | 2.551466377309582  | 3.816650088917021  | 8.07562467974802   | 7.8593604002773    | 0.18687645055309401 | 4.472224734002472  | 4.539289266660639  | 0.8545076408355186 |                    | 0.06480393043373421 | 3.704373511770202  | 1.69394460017482   |                       | 0.31799137957018414 |                       |                     | 0.8643035838080598  |                     |                      | 0.045965578563462645 | 0.11604424752087289  | 1.3043674834976038   | 1.0353558187901257  | 2.238749736263074    | 0.003014136299243452  |                      | 2.999819151822045    | 0.004521204448865178  | 0.41595080929559636  | 0.001507068149621726  | 0.944931729812822    | 0.08967055490249269   | 0.12734725864303584  |                       |                      |                       | 0.02863429484281279   | 0.24866624468758478   | 0.001507068149621726  | 0.24113090393947612   | 0.02260602224432589   | 0.009795942972541218  | 0.015070681496217257  | 0.032401965216867105  |                       | 0.012056545196973807  | 0.20797540464779818   |                       | 0.06781806673297766   | 0.006781806673297767  | 0.021852488169515027  | 0.10549477047352082   |                      |                      |                       | 0.0037676703740543143 |                       | 0.35265394701148384   | 0.825119811917895     |                       | 0.9562347409349852 | 0.27353286915634323 | 0.14618561051330742 | 0.15522801941103775 | 0.9200651053440636 | 0.3451186062633752  | 0.058022123760436445 | 0.029387828917623652 | 0.005274738523676041  | 0.002260602224432589  | 0.000753534074810863  |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1380 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.4408429733134807  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.0374145764135456    |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 30.184400412323903 | 6.0764326346733855 | 4.534799373878517  | 3.241324017867369  | 2.3899515137632195 | 3.598671400755927  | 7.736418126980491  | 8.161722597640592  | 0.15423968235788188 | 4.537090062230367  | 4.531745122742717  | 0.8475546901844004 |                    | 0.03894170198144543 | 3.9651815370518837 | 1.6347879204367577 |                       | 0.3245141831787119  |                       |                     | 0.9758332378879853  |                     |                      | 0.041232390333295156 | 0.12064291986408583  | 1.4240445920665827   | 1.081968464857023   | 2.5838964608864963   | 0.0030542511357996415 |                      | 2.9916389875157487   |                       | 0.3642194479441072   |                       | 1.548505325850418    | 0.041232390333295156  | 0.13896842667888368  |                       |                      |                       | 0.0366510136295957    | 0.3481846294811591    | 0.002290688351849731  | 0.3649830107280571    | 0.03512388806169587   | 0.017561944030847935  | 0.01832550681479785   | 0.019852632382697667  |                       | 0.006108502271599283  | 0.36269232237620735   |                       | 0.05421295766044363   | 0.0015271255678998208 | 0.039705264765395334  | 0.08475546901844004   |                      |                      |                       |                       |                       | 0.3283319970984614    | 0.7605085328141107    |                       | 0.7475279654869622 | 0.21456114228992476 | 0.11224372924063682 | 0.1931813843393273  | 1.0384453861718779 | 0.37032795021570647 | 0.06337571106784255  | 0.023670446302447218 | 0.0038178139197495515 |                       | 0.0007635627839499104 |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1381 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.3316875008163853  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.061392165314732815  |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 29.284715963269196 | 6.00402314615254   | 4.239978055566441  | 3.1114071868019906 | 2.1644003814151547 | 3.434042608775161  | 8.034536358530245  | 8.483221651841113  | 0.1267029794793422  | 4.4470133364682525 | 4.588737803205454  | 0.871246260955889  |                    | 0.05486108389827187 | 3.5770732917956556 | 1.449900074454328  |                       | 0.20638217276016563 |                       |                     | 1.0665255953080712  |                     |                      | 0.03788027221547344  | 0.12474365505440392  | 1.6295048134070038   | 1.2017189806288127  | 2.7006021657065977   | 0.003918648849876563  |                      | 3.1727993521167237   | 0.005224865133168751  | 0.41472366994526955  | 0.0013062162832921877 | 2.206852410622151    | 0.024165001240905468  | 0.15935838656164686  |                       |                      |                       | 0.028083650090782033  | 0.4813407003931711    | 0.0006531081416460938 | 0.4970152957926774    | 0.027430541949135936  | 0.023511893099259377  | 0.012409054691275782  | 0.02612432566584375   |                       | 0.006531081416460937  | 0.48852488995127813   |                       | 0.026777433807489846  | 0.005877973274814844  | 0.042452029206996096  | 0.10515041080502109   |                      |                      |                       | 0.0019593244249382813 |                       | 0.37096542445498126   | 0.7138471988191805    |                       | 0.7739331478506211 | 0.2194443355930875  | 0.1280091957626344  | 0.1776454145277375  | 1.121386679206343  | 0.4016615071123476  | 0.06922946301448593  | 0.025471217524197655 | 0.0013062162832921877 | 0.0013062162832921877 | 0.0013062162832921877 |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1382 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.2458379578246392  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.03237143914169441   |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 28.545135035146135 | 6.1773954864964855 | 4.109322974472808  | 3.1206067332593417 | 2.2770995190529044 | 3.3194598594154643 | 7.815390307066222  | 9.135220125786162  | 0.15353311135775066 | 4.440436551979282  | 4.475582685904551  | 0.7944876063633    |                    | 0.06474287828338882 | 3.510913799482057  | 1.2088420273769886 |                       | 0.13411024787273398 |                       |                     | 1.1191268960414356  |                     |                      | 0.023122456529781725 | 0.11468738438771735  | 1.7138364779874213   | 1.2495375508694042  | 2.6803551609322978   | 0.002774694783573807  |                      | 3.0197928227894932   |                       | 0.4365519792822789   |                       | 2.7358490566037736   | 0.09988901220865706   | 0.258046614872364    |                       |                      |                       | 0.022197558268590455  | 0.6030336662967073    |                       | 0.5438401775804662    | 0.019422863485016647  | 0.011098779134295227  | 0.006474287828338883  | 0.02774694783573807   |                       | 0.012023677395486496  | 0.6076581576026637    |                       | 0.024047354790972992  | 0.007399186089530152  | 0.04532001479837218   | 0.12948575656677763   |                      |                      |                       |                       |                       | 0.44580096189419166   | 0.6798002219755828    |                       | 0.6899741028486867 | 0.20440251572327045 | 0.13688494265630782 | 0.16925638179800223 | 0.9840917499075101 | 0.49204587495375507 | 0.08601553829078801  | 0.030521642619311874 | 0.005549389567147614  | 0.000924898261191269  | 0.000924898261191269  |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1383 | 28.090694663663612 |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.3371876496355544  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.0469966481635838    |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                    | 6.513912781314842  | 3.902495255998723  | 2.9120187277209286 | 2.1919946086863993 | 3.084044194583858  | 7.155018000602976  | 9.372727756397751  | 0.11970844343554365 | 4.178268040505791  | 4.220831042616205  | 0.7590402043024101 |                    | 0.07448525369322716 | 3.355383333037757  | 1.2875308138400696 |                       | 0.26335857555819603 |                       |                     | 1.2901910014719706  |                     |                      | 0.015961125791405822 | 0.14631031975455336  | 1.934843137602639    | 1.3629027967439304  | 2.620284817422456    | 0.004433646053168283  |                      | 3.1851313245960946   | 0.003546916842534627  | 0.46730629400393703  |                       | 3.378438292514232    | 0.015074396580772165  | 0.3484845797790271   |                       |                      |                       | 0.031922251582811645  | 0.5719403408587086    | 0.0008867292106336567 | 0.6606132619220743    | 0.02394168868710873   | 0.014187667370138508  | 0.017734584212673134  | 0.0469966481635838    |                       | 0.03812935605724724   | 0.7359852448259351    |                       | 0.016847855002039478  | 0.005320375263801941  | 0.06827814921879156   | 0.08069235816766276   |                      |                      |                       | 0.0017734584212673135 |                       | 0.35646514267473      | 0.8539202298402114    |                       | 0.7714544132512814 | 0.25537801266249316 | 0.12325536027807826 | 0.19596715555003813 | 0.9727419440651215 | 0.4282902087360562  | 0.06384450316562329  | 0.021281501055207763 | 0.0026601876319009704 |                       | 0.0008867292106336567 |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1384 |                    |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    | 1.1596581536650667  |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      | 0.0729449017316125    |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 27.557423387130196 | 8.409386682581918  | 3.6489029252563436 | 2.6790672999610408 | 2.4221023052246786 | 2.8871260537637085 | 7.689884697320104  | 10.65492916884258  | 0.06465570835302017 | 3.1192234683642934 | 3.0305290992133553 | 0.6382678901516093 |                    | 0.04393272490653934 | 2.8771790217093973 | 0.9507704805245402 |                       | 0.39124992746955795 |                       |                     | 1.3776639395220451  |                     |                      | 0.010775951392170028 | 0.1740730609504389   | 2.1079418761760293   | 1.4945415661601968  | 2.07478510266166     | 0.002486758013577699  |                      | 2.815010071369955    | 0.0033156773514369316 | 0.3249363804408193   | 0.0008289193378592329 | 4.086572335646018    | 0.027354338149354687  | 0.387934250118121    |                       |                      |                       | 0.015749467419325425  | 0.5736121817985892    |                       | 0.7990782416963006    | 0.024867580135776987  | 0.02072298344648082   | 0.009118112716451562  | 0.04890624093369474   |                       | 0.014920548081466192  | 0.910982352307297     |                       | 0.01409162874360696   | 0.004973516027155398  | 0.0629978696773017    | 0.04393272490653934   |                      |                      |                       | 0.006631354702873863  |                       | 0.32825205779225625   | 1.174578701746533     |                       | 0.6258341000837209 | 0.2544782367227845  | 0.11604870730029261 | 0.30255555831862    | 0.9242450617130447 | 0.4434718457546896  | 0.06714246636659786  | 0.026525418811495453 | 0.0008289193378592329 |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1385 | 27.75855696015377  |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       | 12.058845272418127 | 8.002513491535447 | 3.9114363864862867 | 3.7650624676572777 | 3.2764101426776078 | 2.9489169808531086 | 2.9304354254454057 | 2.904561247874621  | 2.834331337325349  | 2.820285355215495  | 2.766319213425002 | 2.738966511421601  | 2.4122126118134104 | 2.3575072078066093 | 2.256228284172396  | 2.100243956531382  | 1.8622015228801656 | 1.7062171952391514 | 1.3572854291417165 | 0.9647371922821024 | 0.9551267834700968 | 0.6808605012197827 | 0.5714496932061802 | 0.5714496932061802 | 0.5662748576920233  | 0.5426184667701635  | 0.4014193834553116   | 0.3186220152288016  | 0.2897907887927848  | 0.2809196421970873  | 0.24321726916537298 | 0.16041990093886302 | 0.0754047460634287   | 0.06801212390034746 | 0.06283728838619058  | 0.04583425741110372 | 0.045094995194795595 | 0.042137946329563095 | 0.0391808974643306    | 0.02439565313816811  | 0.02143860427293561  | 0.02143860427293561   | 0.020699342056627486 | 0.020699342056627486 | 0.017003030975086864 | 0.01626376875877874  | 0.01626376875877874  | 0.015524506542470614  | 0.01478524432616249 | 0.01478524432616249  | 0.01478524432616249 | 0.012567457677238117 | 0.011088933244621867  | 0.009610408812005618  | 0.009610408812005618 | 0.008871146595697493  | 0.005174835514156872 | 0.005174835514156872 | 0.0044355732978487465 | 0.0044355732978487465 | 0.0036963110815406226 | 0.0036963110815406226 | 0.002957048865232498  | 0.001478524432616249  | 0.001478524432616249  | 0.001478524432616249  | 0.0007392622163081245 | 0.0007392622163081245 | 0.0007392622163081245 |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |
|   1386 | 27.77503071713267  | 12.432197548622973 |                    |                   | 2.298540561599089 | 3.441817255536576  | 3.1795978303215557 | 1.9936168299919086 | 2.670892145404417 |                    | 2.3981839431807965 | 2.7210884353741496 | 2.1854116095777516 |                    | 1.5036411040186999 |                   |                    |                    |                    |                    |                    | 0.7424555725373849 |                    |                    | 0.18729958943929995 | 0.4802361473223651 | 0.06667865384039078 |                    |                    | 0.05618987683178999 |                   |                     | 0.21876592046510235 | 0.06368186040936198 | 0.024723545805987596 | 0.029967934310287995 | 0.04195510803440319 | 0.016482363870658396 | 0.016482363870658396 | 0.014983967155143997 | 0.017231562228415594 | 0.009739578650843597 | 0.07791662920674877  | 0.009739578650843597 |                       | 0.0014983967155143996 | 0.0022475950732715995 | 0.0007491983577571998 |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 8.486918996673559 | 4.000719230423447 | 2.8574425364859604 | 2.7735323204171536 | 2.6828793191285323 | 2.676885732266475  | 2.494081332973718 | 2.285054991159459 | 1.8887290599059008 | 1.050376097575594  | 1.0174113698342773 | 0.6120950582876322 | 0.577631933830801  | 0.5244388504300398 | 0.29818094638736553 | 0.23674668105127514 | 0.22475950732715996 | 0.22475950732715996 | 0.22251191225388833 | 0.04195510803440319   | 0.029967934310287995 | 0.024723545805987596 | 0.014983967155143997 | 0.014983967155143997 | 0.009739578650843597  | 0.009739578650843597 | 0.007491983577571999  | 0.0059935868620575984 | 0.005244388504300398  | 0.004495190146543199  | 0.004495190146543199 | 0.0037459917887859994 | 0.0029967934310287992 | 0.0029967934310287992 | 0.0014983967155143996 | 0.0007491983577571998 |                       |                      |                       |                       |                       |                      |                       |
|   1387 | 27.297984496124034 |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       | 13.101395348837208 | 9.665116279069768 | 3.0951937984496123 | 4.24124031007752   | 3.085891472868217  | 2.203410852713178  | 2.1866666666666665 | 2.2493023255813953 | 2.6003100775193797 | 2.645581395348837  | 2.647441860465116 | 2.738604651162791  | 2.3131782945736434 | 2.2269767441860466 | 2.223255813953488  | 2.6127131782945736 | 1.8691472868217054 | 2.3702325581395347 | 1.7196899224806204 | 0.9612403100775194 | 1.0089922480620155 | 0.667906976744186  | 0.5872868217054263 | 0.7925581395348837 | 0.47503875968992243 | 0.48496124031007753 | 0.06635658914728683  | 0.26852713178294574 | 0.20217054263565892 | 0.2158139534883721  | 0.22511627906976744 | 0.16930232558139535 | 0.060155038759689916 | 0.12837209302325583 | 0.046511627906976744 | 0.03968992248062016 | 0.03472868217054263  | 0.03658914728682171  | 0.029147286821705427  | 0.03782945736434109  | 0.02108527131782946  | 0.007441860465116279  | 0.00806201550387597  | 0.017984496124031007 | 0.013643410852713178 | 0.018604651162790697 | 0.00248062015503876  | 0.0037209302325581393 | 0.15131782945736436 | 0.04961240310077519  |                     | 0.008682170542635658 | 0.00124031007751938   | 0.00248062015503876   | 0.011162790697674419 | 0.006201550387596899  | 0.013023255813953487 | 0.009302325581395349 | 0.006821705426356589  | 0.0031007751937984496 | 0.00248062015503876   | 0.0037209302325581393 | 0.00124031007751938   | 0.00124031007751938   |                       |                       |                       |                       | 0.00124031007751938   |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       | 0.00124031007751938   | 0.00124031007751938  |                       |                       |                       |                      |                       |
|   1388 | 27.85870937728451  |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       | 13.544892669635145 | 9.492257592875657 | 2.60849338738619   | 4.25201036751512   | 2.931481358410314  | 2.262909550076427  | 2.156576061673423  | 2.14195520701801   | 2.5480162158569812 | 2.5985246228484082 | 2.634412175184422 | 2.330697148933342  | 2.3971555791852195 | 2.1505948029507542 | 2.1858177709842495 | 2.628430916461753  | 2.0834717883963583 | 2.4855452914202165 | 1.706652488868213  | 1.0035222968033495 | 1.0194723200638    | 0.571542500166146  | 0.6001196251744534 | 0.751644846148734  | 0.4412839768724663  | 0.7077822821824948  | 0.08838971223499702  | 0.29574001462085464 | 0.22130657273875193 | 0.15750647969694956 | 0.19472320063800092 | 0.1588356483019871  | 0.06313550873928359  | 0.11696683724330431 | 0.030570877915863628 | 0.03987505815112647 | 0.04984382268890809  | 0.028577125008307305 | 0.055160497109058286  | 0.015285438957931814 | 0.024589619193194658 | 0.003987505815112647  | 0.005981258722668971 | 0.016614607562969362 | 0.015285438957931814 | 0.016614607562969362 | 0.006645843025187745 | 0.005981258722668971  | 0.13557519771383    | 0.05050840699142686  |                     | 0.010633348840300393 | 0.0006645843025187745 | 0.0033229215125938727 | 0.052502159898983186 | 0.003987505815112647  | 0.006645843025187745 | 0.011962517445337943 | 0.004652090117631421  | 0.005981258722668971  | 0.0006645843025187745 |                       | 0.001329168605037549  |                       | 0.0006645843025187745 | 0.0006645843025187745 |                       |                       | 0.0006645843025187745 |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       | 0.0006645843025187745 | 0.002658337210075098 | 0.0006645843025187745 |                       |                       |                      |                       |
|   1389 | 27.60438896586141  |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       | 13.69614750707527  | 9.444418908536946 | 2.3947574052307754 | 4.1886913868843205 | 2.9194108647260837 | 2.076944796475169  | 1.9331411573894717 | 2.011937671956977  | 2.4965362365471364 | 2.528054842374139  | 2.325810454984208 | 2.4571379792633836 | 2.2949484867786016 | 1.9810757037513707 | 2.111746590409151  | 3.1571136836713922 | 2.114373140894734  | 2.918754227104688  | 1.7203905680572062 | 1.0775423367106396 | 0.9009068165551477 | 0.7223013835354682 | 0.6566376213958802 | 0.8411527930081226 | 0.46030297259851205 | 0.8391828801439349  | 0.030205330584210495 | 0.25937186045137267 | 0.2166904150606405  | 0.1168814966084667  | 0.45045340827757385 | 0.23179308035274573 | 0.08339297791727679  | 0.16809923107734534 | 0.07879651456750562  | 0.05121773446887866 | 0.06172393641121274  | 0.029548692962814614 | 0.042024807769336335  | 0.02495222961304345  | 0.03086196820560637  | 0.0019699128641876406 | 0.003939825728375281 | 0.013789390049313486 | 0.028235417720022853 | 0.02298231674885581  | 0.009192926699542324 | 0.007223013835354683  | 0.03480179393398165 | 0.009192926699542324 |                     | 0.017729215777688767 | 0.0032831881069794013 | 0.002626550485583521  | 0.03939825728375281  | 0.006566376213958803  | 0.017072578156292886 | 0.016415940534897006 | 0.005909738592562923  | 0.0006566376213958802 |                       | 0.0006566376213958802 |                       | 0.0006566376213958802 | 0.0006566376213958802 | 0.002626550485583521  |                       |                       | 0.0006566376213958802 |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       | 0.002626550485583521 |                       | 0.0006566376213958802 | 0.0006566376213958802 |                      |                       |
|   1390 | 27.1197024046765   | 13.482795270360038 |                    |                   | 3.460874186262787 | 2.521588946459413  | 2.8291483990965856 | 2.9719675833665473 | 2.494353660156769 |                    | 2.348213099508436  | 2.2133652185465658 | 2.0373322704928922 |                    | 1.7955360701474692 |                   |                    |                    |                    |                    |                    | 0.8874717683007839 |                    |                    | 0.3062309020858244  | 0.4503786369071343 | 0.2504317789291883  |                    |                    | 0.1262123023781055  |                   |                     | 0.1481333864753554  | 0.04184934236747708 | 0.027899561578318056 | 0.01992825827022718  | 0.04450644347017404 | 0.03321376378371197  | 0.028563836853992292 | 0.02125680882157566  | 0.017935432443204464 | 0.016606881891855985 | 0.06842035339444666  | 0.011956954962136309 | 0.0026571011026969575 | 0.0006642752756742394 | 0.0033213763783711972 | 0.0006642752756742394 |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       | 9.783446260130198 | 4.27926132589345  | 1.7995217218015145 | 2.309020858243656  | 1.9576192374119834 | 2.4451972897568752 | 2.000132855055135 | 1.858642221336522 | 1.9104556928391125 | 1.1804171648731234 | 1.0229839245383288 | 0.5639697090474293 | 0.6337186129932244 | 0.9685133519330411 | 0.2916168460209911  | 0.21190381294008237 | 0.35671582303706656 | 0.06310615118905274 | 0.39922944068021793 | 0.0066427527567423945 | 0.02258535937292414  | 0.053142022053939156 | 0.03188521323236349  | 0.004649926929719676 | 0.0006642752756742394 | 0.007307028032416634 | 0.0013285505513484788 | 0.01129267968646207   | 0.0039856516540454365 | 0.0006642752756742394 | 0.011956954962136309 | 0.0006642752756742394 | 0.016606881891855985  | 0.0013285505513484788 |                       |                       |                       |                      |                       |                       |                       | 0.005978477481068154 | 0.0006642752756742394 |
|   1391 | 26.594003957196556 |                    |                    |                   |                   |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                    |                    |                     |                   |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       | 13.507869891759036 | 9.712932090947056 | 2.668026810348959  | 4.363870384697014  | 2.9035416224505863 | 1.8505713288101708 | 1.9327276586130642 | 1.4931912941675851 | 2.275045699458453  | 2.509191239396699  | 2.600247838261572 | 2.3688408426500893 | 2.366102298323326  | 1.6944743021846738 | 2.1052559511991404 | 3.851762595592313  | 2.0552775172357136 | 3.046630563523959  | 1.797854350519981  | 1.2857465614152797 | 0.885234453626175  | 0.6675201796485077 | 0.6435579167893306 | 0.870172459828978  | 0.5032075200427213  | 0.9756064164093575  | 0.09927223184516269  | 0.23688408426500895 | 0.17047438434100354 | 0.1335040359297016  | 0.4032506521158678  | 0.3519029459890595  | 0.1862210142198914   | 0.32314823055804687 | 0.039708892738065084 | 0.05340161437188063 | 0.0814716937212025   | 0.0451859813915913   | 0.0075309968985985505 | 0.024646898940867985 | 0.03765498449299275  | 0.0034231804084538867 | 0.006161724735216996 | 0.020539082450723316 | 0.03423180408453887  | 0.026700807185940315 | 0.006846360816907773 | 0.008900269061980104  | 0.07188678857753161 | 0.010954177307052436 |                     | 0.017115902042269433 | 0.0034231804084538867 | 0.0006846360816907773 | 0.030123987594394202 | 0.0006846360816907773 | 0.018485174205650986 | 0.002738544326763109 | 0.0034231804084538867 | 0.002053908245072332  | 0.0013692721633815545 | 0.0013692721633815545 | 0.0006846360816907773 |                       |                       | 0.002053908245072332  |                       |                       | 0.0013692721633815545 |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       | 0.0013692721633815545 | 0.0006846360816907773 |                      |                       |
|   1392 | 26.8739446704522   | 12.85133122920511  | 10.076304333886677 | 7.960301797533467 | 4.215618521078093 | 3.6883990339059127 | 2.8213367151376114 | 2.7907009881803093 | 2.522104033229077 | 2.4921807650382233 | 2.344701800383303  | 2.278443135103556  | 2.231420856517929  | 1.9991592986555902 | 1.8987026125862967 | 1.789696421319616 | 1.4947384920097748 | 1.3415598572232632 | 1.2688890630454763 | 1.1413589438511247 | 1.0957615827983955 | 0.7480817047713364 | 0.7031968024850562 | 0.6853853333238339 | 0.4915965488497353  | 0.4260503423364373 | 0.2978077643756368  | 0.2864084241124545 | 0.2664595786518855 | 0.2322615578623387  | 0.138217000691085 | 0.13536716562528944 | 0.06554620651329804 | 0.05414686625011577 | 0.049159654884973536 | 0.03847277338824015  | 0.03277310325664902 | 0.02849835065795567  | 0.02849835065795567  | 0.02778589189150678  | 0.01994884546056897  | 0.019236386694120075 | 0.019236386694120075 | 0.01211179902963116  | 0.009974422730284486  | 0.0021373762993466753 | 0.0021373762993466753 | 0.0014249175328977836 | 0.0014249175328977836 |                    |                   |                   |                   |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                     |                    |                     |                     |                     |                     |                      |                     |                     |                     |                     |                     |                      |                      |                      |                      |                     |                     |                      |                     |                      |                      |                      |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                    |                    |                    |                    |                    |                    |                    |                    |                     |                    |                    |                    |                    |                     |                    |                    |                       |                     |                       |                     |                     |                     |                      |                      |                      |                      |                     |                      |                       |                      |                      |                       |                      |                       |                      |                       |                      |                       |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                    |                     |                     |                     |                    |                     |                      |                      |                       |                       |                       |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                   |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                    |                     |                     |                      |                     |                     |                     |                     |                     |                      |                     |                      |                     |                      |                      |                       |                      |                      |                       |                      |                      |                      |                      |                      |                       |                     |                      |                     |                      |                       |                       |                      |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                   |                   |                    |                    |                    |                    |                   |                   |                    |                    |                    |                    |                    |                    |                     |                     |                     |                     |                     |                       |                      |                      |                      |                      |                       |                      |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                      |                       |


**category data**

|   Year | Primar   |   nan |   Secondary |   Pre_University |   Bachelors |   Tertiary |   College |   Masters |   Unofficial |   PhD | Primary   |
|-------:|:---------|------:|------------:|-----------------:|------------:|-----------:|----------:|----------:|-------------:|------:|:----------|
|   1393 |          | 26.4  |       14.09 |            12.78 |        7.07 |       5.18 |      2.74 |      1.05 |         2.83 |  0.07 | 27.78     |
|   1394 |          | 25.97 |       14.48 |            13.21 |        7.09 |       4.58 |      2.72 |      1.15 |         2.73 |  0.08 | 27.97     |
|   1395 |          | 25.86 |       14.55 |            13.44 |        7.02 |       4.41 |      2.69 |      1.34 |         2.93 |  0.09 | 27.66     |
|   1396 |          | 25.45 |       14.64 |            13.76 |        7.09 |       4.2  |      2.67 |      1.4  |         2.91 |  0.1  | 27.78     |
|   1397 | 28.72    | 24.99 |       15.38 |            14.36 |        7.41 |       3.93 |      2.84 |      1.59 |         0.71 |  0.07 |           |
|   1398 | 29.24    | 24.49 |       15.35 |            14.46 |        7.39 |       4.14 |      2.72 |      1.56 |         0.55 |  0.1  |           |
|   1399 | 29.46    | 23.04 |       15.79 |            14.67 |        7.74 |       4.4  |      2.7  |      1.59 |         0.49 |  0.1  |           |
|   1400 | 29.87    | 21.74 |       16.03 |            15.04 |        8.12 |       4.42 |      2.61 |      1.62 |         0.44 |  0.11 |           |
|   1401 | 30.06    | 21.07 |       16.18 |            15.36 |        8.02 |       4.67 |      2.57 |      1.66 |         0.29 |  0.11 |           |


#### Categories

|    | 1363-1392   | 1393-1396      | 1397-1401      |
|---:|:------------|:---------------|:---------------|
|  1 |             |                | Primar         |
|  2 |             |                | Secondary      |
|  3 |             |                | Tertiary       |
|  4 |             |                | Pre_University |
|  5 |             |                | College        |
|  6 |             |                | Bachelors      |
|  7 |             |                | Masters        |
|  8 |             |                | PhD            |
|  9 |             |                | Unofficial     |
| 11 |             | Primary        |                |
| 21 |             | Secondary      |                |
| 31 |             | Tertiary       |                |
| 41 |             | Pre_University |                |
| 51 |             | College        |                |
| 52 |             | Bachelors      |                |
| 53 |             | Masters        |                |
| 61 |             | PhD            |                |
| 71 |             | Unofficial     |                |


#### Replacements

|   Year |   Value |   Replace_Value |   Frequency |
|-------:|--------:|----------------:|------------:|
|   1394 |       1 |             nan |           1 |


### Activity_State

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
    
    ```
#### Column Codes

| Years     | Activity_State                                          |
|:----------|:--------------------------------------------------------|
| 1363-1365 | [COL11](/HBSIR/tables/raw/members_properties#col11)     |
| 1366-1383 | [COL09](/HBSIR/tables/raw/members_properties#col09)     |
| 1384-1401 | [DYCOL09](/HBSIR/tables/raw/members_properties#dycol09) |


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


#### Categories

|    | 1363-1401           |
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


### Marrital_State

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
    
    ```
#### Column Codes

| Years     | Marrital_State                                          |
|:----------|:--------------------------------------------------------|
| 1363      | [COL07](/HBSIR/tables/raw/members_properties#col07)     |
| 1364-1365 | [COL06](/HBSIR/tables/raw/members_properties#col06)     |
| 1366-1368 |                                                         |
| 1369-1383 | [COL10](/HBSIR/tables/raw/members_properties#col10)     |
| 1384-1401 | [DYCOL10](/HBSIR/tables/raw/members_properties#dycol10) |


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


#### Categories

|    | 1363-1401   |
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
| 1369-1401 |                                                     |


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
| 1366-1401 |                                                     |


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
| 1369-1401 |                                                     |


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


### Job_Code

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

| Years     | Job_Code                                            |
|:----------|:----------------------------------------------------|
| 1363-1365 | [COL12](/HBSIR/tables/raw/members_properties#col12) |
| 1366-1368 | [COL10](/HBSIR/tables/raw/members_properties#col10) |
| 1369-1401 |                                                     |


#### Summary Statistics

**string data**

|   Year |    <NA> |     612 |     614 |        753 |         956 |     410 |     985 |      622 |      613 |      133 |      452 |      624 |      X03 |      552 |      843 |       310 |       893 |      951 |      791 |      132 |      776 |      589 |      451 |      623 |       754 |      971 |       110 |      872 |       627 | 571                 | 530                 |       839 |       811 |       849 |       831 |       582 |       072 |        832 |       139 |       801 | X04                 |       391 | 875                 |       359 | 443                   | 845                  |       510 |       871 |       959 |       851 |       873 |       931 |       955 |       751 |        778 |       300 |       855 |       626 |       551 |       321 |       331 | 700                  |       441 |       974 | 858                  | 932                  |       752 |       943 |       149 |       771 |       952 |       857 |       034 | 572                 | 420                  |       629 |       141 |       953 | 962                  |       395 |       211 |       755 |        625 |       560 |       820 |       795 |       724 |       370 |       380 |       711 |       854 |        163 |        490 |       957 |       219 |       641 |        779 |        880 |       399 |       981 | 958                  | 161                   |        961 |        921 | 983                   |       973 |       339 |       892 |        803 |        394 | 963                  |        053 |        901 |       134 | 731                   | 453                  |        033 |       061 |        774 |        842 |        796 |        032 |       999 |        799 |        X01 |        819 | 078                 |       581 |        131 | 949                  |       212 |        079 |        772 |       022 |        619 |       939 |        773 |        615 |        969 |       035 |        745 |        600 |        195 |        031 |       942 |        054 | 084                   | 813                  |        599 |        841 |        193 | 351                   |        400 |        722 | 191                  |        856 | 213                   |        202 | 123                   | 055                  |        929 |        090 | 122                   | 902                   | 746                  | 076                   | 074                   | 876                   |        712 |        742 |        728 |        180 |        775 | 173                   | 083                   | 593                  | 649                   |        013 | 713                  | 201                   | 067                   | 068                   |        071 | 052                   |        926 | 744                  | 064                   | 041                   | 063                   | 729                   | 733                   |        986 |        062 |        756 | 340                   | 069                   | 760                   |        759 | 630                   | 874                   | 152                  | 910                  |        749 |        023 | 066                   | 075                   | 727                   | 616                   |        891 | 021                   |        024 | 142                   | 793                   | 038                   | 199                   | 037                   | 179                   |        129 | 121                   | 135                   | 859                   | 322                   |        979 | 042                   |         029 |        077 | 194                   | 726                   |        721 | 192                   | 862                   | 844                   | 941                   | 954                 | 393                 | 570                 | 360                 | 531                 | 442                 | 834                 | 532                 | 540                  | 392                  | 621                 | 611                  | 732                  | 853                  | 802                  | 761                   | 422                  | 632                   | 432                  | 162                  | 922                   | 421                  | 895                   | 899                   | 812                  | 073                   | 984                   | 500                  | 794                  | 789                   | 065                   | 734                   | 039                   | 781                   | 925                   | 159                   | 352                   | 723                   | 835                   | 025                   | 741                   | 591                   | 592                   | 852                   | 777                   | X02                   | 927                   | 171                   | 342                   | 783                   | 036                   | 081                   | 792                   | 014                   | 982                   | 431                   | 174                   | 027                   | 151                   | 782                   | 725                   | 631                  | 028                   | 520                   | 082                   | 026                   | 972                   | 043                   | 833                   | 861                  | 924                  | 175                  | 780                   | 877                  |
|-------:|--------:|--------:|--------:|-----------:|------------:|--------:|--------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|----------:|----------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|----------:|---------:|----------:|---------:|----------:|:--------------------|:--------------------|----------:|----------:|----------:|----------:|----------:|----------:|-----------:|----------:|----------:|:--------------------|----------:|:--------------------|----------:|:----------------------|:---------------------|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|-----------:|----------:|----------:|----------:|----------:|----------:|----------:|:---------------------|----------:|----------:|:---------------------|:---------------------|----------:|----------:|----------:|----------:|----------:|----------:|----------:|:--------------------|:---------------------|----------:|----------:|----------:|:---------------------|----------:|----------:|----------:|-----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|-----------:|-----------:|----------:|----------:|----------:|-----------:|-----------:|----------:|----------:|:---------------------|:----------------------|-----------:|-----------:|:----------------------|----------:|----------:|----------:|-----------:|-----------:|:---------------------|-----------:|-----------:|----------:|:----------------------|:---------------------|-----------:|----------:|-----------:|-----------:|-----------:|-----------:|----------:|-----------:|-----------:|-----------:|:--------------------|----------:|-----------:|:---------------------|----------:|-----------:|-----------:|----------:|-----------:|----------:|-----------:|-----------:|-----------:|----------:|-----------:|-----------:|-----------:|-----------:|----------:|-----------:|:----------------------|:---------------------|-----------:|-----------:|-----------:|:----------------------|-----------:|-----------:|:---------------------|-----------:|:----------------------|-----------:|:----------------------|:---------------------|-----------:|-----------:|:----------------------|:----------------------|:---------------------|:----------------------|:----------------------|:----------------------|-----------:|-----------:|-----------:|-----------:|-----------:|:----------------------|:----------------------|:---------------------|:----------------------|-----------:|:---------------------|:----------------------|:----------------------|:----------------------|-----------:|:----------------------|-----------:|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|-----------:|-----------:|-----------:|:----------------------|:----------------------|:----------------------|-----------:|:----------------------|:----------------------|:---------------------|:---------------------|-----------:|-----------:|:----------------------|:----------------------|:----------------------|:----------------------|-----------:|:----------------------|-----------:|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|-----------:|:----------------------|:----------------------|:----------------------|:----------------------|-----------:|:----------------------|------------:|-----------:|:----------------------|:----------------------|-----------:|:----------------------|:----------------------|:----------------------|:----------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------------------|:--------------------|:---------------------|:---------------------|:--------------------|:---------------------|:---------------------|:---------------------|:---------------------|:----------------------|:---------------------|:----------------------|:---------------------|:---------------------|:----------------------|:---------------------|:----------------------|:----------------------|:---------------------|:----------------------|:----------------------|:---------------------|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:---------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:----------------------|:---------------------|:---------------------|:---------------------|:----------------------|:---------------------|
|   1363 | 70.7621 | 6.78176 | 2.35036 | 0.00277656 | 0.0034707   | 1.71245 | 1.23071 | 0.498393 | 0.678176 | 0.848934 | 0.378307 | 0.245032 | 0.575443 | 0.224207 | 0.358871 | 0.102039  | 0.0687199 | 0.331105 | 0.308893 | 0.144381 | 0.272103 | 0.251279 | 0.261691 | 0.106898 | 2.58845   | 0.159652 | 0.0749672 | 0.191583 | 0.102039  |                     |                     | 0.0360953 | 0.0360953 | 0.0978738 | 0.179782  | 0.135357  | 0.123557  | 0.00902383 | 0.114533  | 0.102733  |                     | 0.103427  |                     | 0.014577  | 0.0006941407578628794 |                      | 0.0992621 | 0.0853793 | 0.0465074 | 0.0451191 | 0.22629   | 0.10898   | 0.039566  | 0.0131887 | 0.00555313 | 0.083991  | 0.13744   | 0.0645551 | 0.0680258 | 0.0728848 | 0.170759  |                      | 0.0242949 | 0.0610844 |                      |                      | 0.125639  | 0.0451191 | 0.0180477 | 0.0222125 | 0.044425  | 0.0277656 | 0.034707  |                     |                      | 0.0666375 | 0.0687199 | 0.0242949 |                      | 0.059002  | 0.0388719 | 0.054143  | 0.0159652  | 0.0430367 | 0.0256832 | 0.0236008 | 0.0152711 | 0.0506723 | 0.054143  | 0.0458133 | 0.0305422 | 0.0180477  | 0.00138828 | 0.0312363 | 0.0354012 | 0.0569195 | 0.0131887  | 0.0305422  | 0.079132  | 0.0596961 |                      | 0.004858985305040156  | 0.00763555 | 0.00277656 | 0.0020824222735886383 | 0.0194359 | 0.0923207 | 0.079132  | 0.0118004  | 0.00832969 |                      | 0.00902383 | 0.0187418  | 0.0215184 | 0.0027765630314515177 |                      | 0.0499781  | 0.0291539 | 0.00485899 | 0.0333188  | 0.0416484  | 0.00902383 | 1.97622   | 0.00971797 | 0.0652492  | 0.0159652  |                     | 0.0104121 | 0.00971797 | 0.013188674399394711 | 0.0242949 | 0.0291539  | 0.0118004  | 0.0124945 | 0.0124945  | 0.0569195 | 0.0277656  | 0.0319305  | 0.054143   | 0.0222125 | 0.00971797 | 0.00555313 | 0.00555313 | 0.0152711  | 0.044425  | 0.014577   | 0.006941407578628794  |                      | 0.0846852  | 0.0124945  | 0.0104121  | 0.0006941407578628794 | 0.00902383 | 0.00138828 | 0.009023829852217433 | 0.0104121  |                       | 0.0229066  |                       |                      | 0.00971797 | 0.00138828 | 0.0006941407578628794 | 0.020130081978023504  |                      | 0.0020824222735886383 | 0.004164844547177277  |                       | 0.00694141 | 0.0138828  | 0.00763555 | 0.0124945  | 0.0104121  | 0.0006941407578628794 | 0.0006941407578628794 |                      | 0.0013882815157257589 | 0.00138828 | 0.013188674399394711 | 0.0020824222735886383 | 0.0027765630314515177 | 0.020130081978023504  | 0.0131887  | 0.007635548336491674  | 0.00555313 | 0.004164844547177277 | 0.0027765630314515177 | 0.003470703789314397  | 0.0020824222735886383 | 0.0027765630314515177 |                       | 0.0367895  | 0.0277656  | 0.0242949  |                       | 0.0020824222735886383 |                       | 0.014577   |                       | 0.0013882815157257589 |                      | 0.009717970610080312 | 0.00971797 | 0.00624727 | 0.0055531260629030355 | 0.0013882815157257589 | 0.0020824222735886383 | 0.0006941407578628794 | 0.0034707  | 0.003470703789314397  | 0.00208242 |                       | 0.0013882815157257589 | 0.0013882815157257589 | 0.0027765630314515177 | 0.0006941407578628794 | 0.0027765630314515177 | 0.0131887  |                       |                       | 0.009717970610080312  |                       | 0.00832969 | 0.008329689094354553  | 0.00138828  | 0.00763555 |                       | 0.0013882815157257589 | 0.00138828 | 0.004164844547177277  | 0.0020824222735886383 | 0.004164844547177277  |                       | 0.16451135961350244 | 0.14576955915120468 | 0.14507541839334182 | 0.13605158854112437 | 0.11245080277378647 | 0.08537931321713417 | 0.08399103170140841 | 0.0708023573020137  | 0.054142979113304596 | 0.04581329001895004  | 0.03609531940886973 | 0.02290664500947502  | 0.019435941220160624 | 0.018741800462297745 | 0.016659378188709106 | 0.015271096672983347  | 0.013188674399394711 | 0.01249453364153183   | 0.010412111367943191 | 0.008329689094354553 | 0.007635548336491674  | 0.007635548336491674 | 0.006941407578628794  | 0.006941407578628794  | 0.006941407578628794 | 0.0055531260629030355 | 0.0055531260629030355 | 0.004858985305040156 | 0.004858985305040156 | 0.004164844547177277  | 0.003470703789314397  | 0.003470703789314397  | 0.0027765630314515177 | 0.0027765630314515177 | 0.0027765630314515177 | 0.0027765630314515177 | 0.0020824222735886383 | 0.0020824222735886383 | 0.0020824222735886383 | 0.0020824222735886383 | 0.0020824222735886383 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0013882815157257589 | 0.0006941407578628794 | 0.0006941407578628794 | 0.0006941407578628794 | 0.0006941407578628794 | 0.0006941407578628794 | 0.0006941407578628794 | 0.0006941407578628794 | 0.0006941407578628794 | 0.0006941407578628794 | 0.0006941407578628794 |                      |                       |                       |                       |                       |                       |                       |                       |                      |                      |                      |                       |                      |
|   1364 | 71.6579 | 7.01751 | 2.26061 | 0.00549692 | 0.000687115 | 1.41958 | 1.1626  | 0.581299 | 0.655508 | 0.765446 | 0.35249  | 0.303018 | 0.422576 | 0.232245 | 0.300269 | 0.0755827 | 0.0728342 | 0.364858 | 0.292711 | 0.171092 | 0.263852 | 0.250797 | 0.224687 | 0.119558 | 2.33276   | 0.154601 | 0.0728342 | 0.213006 | 0.105816  |                     |                     | 0.0494723 | 0.0288588 | 0.0906992 | 0.169717  | 0.14773   | 0.109251  | 0.00961961 | 0.105816  | 0.0783311 |                     | 0.0913863 |                     | 0.0164908 | 0.0006871152154793316 |                      | 0.0913863 | 0.0831409 | 0.0515336 | 0.0529079 | 0.171092  | 0.0906992 | 0.0529079 | 0.0089325 | 0.00961961 | 0.0783311 | 0.110626  | 0.0797054 | 0.0783311 | 0.0680244 | 0.151165  |                      | 0.0192392 | 0.0728342 |                      |                      | 0.118184  | 0.0666502 | 0.0192392 | 0.017865  | 0.0460367 | 0.029546  | 0.0398527 |                     |                      | 0.0467238 | 0.0570306 | 0.029546  |                      | 0.0501594 | 0.0343558 | 0.0288588 | 0.0233619  | 0.0261104 | 0.03573   | 0.0213006 | 0.0144294 | 0.0460367 | 0.0460367 | 0.041914  | 0.0267975 | 0.0288588  | 0.00137423 | 0.0288588 | 0.0398527 | 0.077644  | 0.00755827 | 0.017865   | 0.0700858 | 0.0474109 |                      | 0.004809806508355321  | 0.0199263  | 0.00343558 | 0.003435576077396658  | 0.0164908 | 0.103754  | 0.0790182 | 0.00687115 | 0.0158036  |                      | 0.0103067  | 0.017865   | 0.0213006 |                       |                      | 0.0391656  | 0.0164908 | 0.00961961 | 0.0226748  | 0.0398527  | 0.0144294  | 2.22144   | 0.0151165  | 0.00137423 | 0.00755827 |                     | 0.0144294 | 0.0144294  | 0.01236807387862797  | 0.0192392 | 0.0309202  | 0.00961961 | 0.0109938 | 0.0164908  | 0.053595  | 0.03573    | 0.0185521  | 0.0632146  | 0.0247361 | 0.0103067  | 0.00687115 | 0.00137423 | 0.0151165  | 0.0343558 | 0.017865   | 0.006871152154793316  |                      | 0.0769569  | 0.0192392  | 0.0089325  | 0.0013742304309586632 | 0.0089325  | 0.00137423 | 0.003435576077396658 | 0.0164908  |                       | 0.024049   |                       |                      | 0.00755827 | 0.00137423 | 0.0013742304309586632 | 0.0261103781882146    |                      | 0.0013742304309586632 | 0.0041226912928759895 |                       | 0.0103067  | 0.00687115 | 0.00480981 | 0.00961961 | 0.0103067  |                       | 0.0013742304309586632 |                      | 0.0006871152154793316 | 0.00137423 | 0.008245382585751979 |                       | 0.003435576077396658  | 0.0130551890941073    | 0.0089325  | 0.0041226912928759895 | 0.00274846 | 0.006184036939313985 | 0.0020613456464379947 | 0.0027484608619173265 | 0.0027484608619173265 | 0.0041226912928759895 | 0.0006871152154793316 | 0.0185521  | 0.0398527  | 0.011681   |                       | 0.0013742304309586632 |                       | 0.0206135  |                       |                       |                      | 0.004809806508355321 | 0.00687115 | 0.00824538 | 0.007558267370272647  | 0.0027484608619173265 | 0.0027484608619173265 |                       | 0.00412269 | 0.0020613456464379947 | 0.00343558 |                       | 0.0006871152154793316 | 0.0027484608619173265 | 0.003435576077396658  | 0.0013742304309586632 | 0.0013742304309586632 | 0.00755827 | 0.004809806508355321  | 0.0020613456464379947 | 0.014429419525065964  | 0.0013742304309586632 | 0.0123681  | 0.003435576077396658  | 0.000687115 | 0.00206135 | 0.0013742304309586632 | 0.0013742304309586632 | 0.00480981 | 0.0006871152154793316 | 0.0013742304309586632 | 0.005496921723834653  |                       | 0.1415457343887423  | 0.10856420404573439 | 0.132613236587511   | 0.09963170624450307 | 0.10100593667546173 | 0.0611532541776605  | 0.07764401934916447 | 0.05703056288478452 | 0.03985268249780123  | 0.028858839050131927 | 0.10031882145998242 | 0.01717788038698329  | 0.01236807387862797  | 0.0130551890941073   | 0.014429419525065964 | 0.0041226912928759895 | 0.020613456464379946 | 0.0027484608619173265 | 0.005496921723834653 | 0.01786499560246262  | 0.0041226912928759895 | 0.009619613016710642 | 0.0041226912928759895 | 0.0020613456464379947 | 0.008245382585751979 | 0.0027484608619173265 | 0.005496921723834653  | 0.004809806508355321 | 0.003435576077396658 | 0.0006871152154793316 | 0.0027484608619173265 | 0.0006871152154793316 | 0.005496921723834653  | 0.0013742304309586632 | 0.0006871152154793316 | 0.0020613456464379947 | 0.0020613456464379947 | 0.005496921723834653  | 0.0041226912928759895 | 0.0027484608619173265 | 0.0006871152154793316 | 0.0013742304309586632 | 0.0013742304309586632 |                       | 0.0020613456464379947 | 0.0006871152154793316 | 0.0027484608619173265 | 0.0006871152154793316 | 0.0013742304309586632 |                       | 0.006871152154793316  | 0.0006871152154793316 | 0.0020613456464379947 | 0.0013742304309586632 |                       | 0.0020613456464379947 | 0.0013742304309586632 | 0.0013742304309586632 |                       |                       | 0.0013742304309586632 | 0.006184036939313985 | 0.0013742304309586632 | 0.0013742304309586632 | 0.0013742304309586632 | 0.0013742304309586632 | 0.0006871152154793316 | 0.0006871152154793316 | 0.0006871152154793316 |                      |                      |                      |                       |                      |
|   1365 | 70.808  | 8.28586 | 2.30799 | 0.013095   | 0.00327375  | 1.33242 | 1.23748 | 0.615465 | 0.720225 | 0.667845 | 0.255353 | 0.294638 | 0.47142  | 0.193151 | 0.206246 | 0.0851175 | 0.02619   | 0.320828 | 0.274995 | 0.144045 | 0.307733 | 0.265174 | 0.271721 | 0.114581 | 2.59281   | 0.150593 | 0.0949388 | 0.232436 | 0.0883913 |                     |                     | 0.039285  | 0.02619   | 0.137498  | 0.147319  | 0.0851175 | 0.117855  | 0.0163688  | 0.108034  | 0.091665  |                     | 0.0687488 |                     | 0.0163688 |                       |                      | 0.091665  | 0.091665  | 0.0622013 | 0.0294638 | 0.176783  | 0.0851175 | 0.0425588 | 0.013095  | 0.00982125 | 0.07857   | 0.124403  | 0.0458325 | 0.0622013 | 0.091665  | 0.114581  |                      | 0.0294638 | 0.0556538 |                      |                      | 0.101486  | 0.0458325 | 0.013095  | 0.0163688 | 0.039285  | 0.0229163 | 0.0425588 |                     |                      | 0.0622013 | 0.0491063 | 0.0294638 |                      | 0.0556538 | 0.0229163 | 0.0458325 | 0.0065475  | 0.0196425 | 0.0294638 | 0.0229163 | 0.0229163 | 0.0556538 | 0.0360113 | 0.0360113 | 0.039285  | 0.00327375 | 0.00327375 | 0.02619   | 0.0556538 | 0.065475  | 0.013095   | 0.00327375 | 0.111308  | 0.02619   |                      |                       | 0.00982125 | 0.0065475  |                       | 0.0163688 | 0.140771  | 0.0491063 | 0.0229163  | 0.00982125 |                      | 0.013095   | 0.0491063  | 0.0163688 |                       |                      | 0.0327375  | 0.0196425 | 0.00327375 | 0.02619    | 0.0327375  | 0.00327375 | 1.72199   | 0.0229163  | 0.0065475  | 0.0327375  |                     | 0.013095  | 0.00982125 | 0.006547502127938192 | 0.0196425 | 0.0229163  | 0.00327375 | 0.0196425 | 0.0163688  | 0.039285  | 0.0163688  | 0.013095   | 0.0425588  | 0.0229163 | 0.00327375 | 0.0196425  | 0.0065475  | 0.0065475  | 0.0458325 | 0.0196425  |                       |                      | 0.10476    | 0.00982125 | 0.00982125 |                       | 0.0065475  | 0.00327375 |                      | 0.00982125 |                       | 0.0196425  |                       |                      | 0.00327375 | 0.00982125 |                       | 0.04255876383159824   |                      |                       |                       |                       | 0.00982125 | 0.0065475  | 0.0163688  | 0.0163688  | 0.013095   |                       |                       |                      |                       | 0.00327375 | 0.01636875531984548  |                       |                       | 0.02619000851175277   | 0.0065475  | 0.003273751063969096  | 0.013095   | 0.003273751063969096 |                       |                       |                       | 0.003273751063969096  |                       | 0.02619    | 0.0360113  | 0.0163688  |                       | 0.003273751063969096  |                       | 0.0065475  |                       |                       |                      | 0.003273751063969096 | 0.0065475  | 0.00327375 | 0.009821253191907287  |                       |                       | 0.009821253191907287  | 0.00327375 |                       | 0.00982125 |                       |                       |                       | 0.003273751063969096  | 0.003273751063969096  |                       | 0.0163688  | 0.006547502127938192  | 0.003273751063969096  | 0.006547502127938192  |                       | 0.013095   | 0.003273751063969096  | 0.00982125  | 0.0065475  |                       |                       | 0.00327375 |                       | 0.003273751063969096  | 0.003273751063969096  |                       | 0.17023505532639296 | 0.07529627447128921 | 0.14077129575067113 | 0.12112878936685655 | 0.07529627447128921 | 0.0720225234073201  | 0.08511752766319648 | 0.05892751915144372 | 0.05892751915144372  | 0.01636875531984548  | 0.11785503830288745 | 0.006547502127938192 | 0.02291625744778367  | 0.02619000851175277  | 0.05565376808747463  | 0.003273751063969096  | 0.01636875531984548  | 0.003273751063969096  | 0.003273751063969096 | 0.01636875531984548  | 0.009821253191907287  | 0.02619000851175277  | 0.009821253191907287  |                       | 0.003273751063969096 | 0.006547502127938192  | 0.006547502127938192  | 0.003273751063969096 | 0.003273751063969096 |                       |                       |                       | 0.003273751063969096  | 0.006547502127938192  |                       |                       |                       | 0.003273751063969096  |                       | 0.006547502127938192  |                       | 0.003273751063969096  |                       |                       | 0.003273751063969096  |                       | 0.003273751063969096  |                       |                       |                       | 0.006547502127938192  |                       | 0.003273751063969096  | 0.003273751063969096  |                       |                       |                       | 0.003273751063969096  |                       |                       |                       | 0.003273751063969096 | 0.003273751063969096  |                       |                       |                       |                       |                       | 0.003273751063969096  | 0.003273751063969096 | 0.003273751063969096 | 0.003273751063969096 |                       |                      |
|   1366 | 72.5607 | 7.68568 | 2.13207 | 1.86397    | 1.61182     | 1.42032 | 1.26392 | 0.625579 | 0.555361 | 0.529827 | 0.27768  | 0.398966 | 0.418116 | 0.465992 | 0.18512  | 0.37024   | 0.16597   | 0.300022 | 0.27768  | 0.232996 | 0.204271 | 0.23938  | 0.312789 | 0.143628 | 0.0159586 | 0.197887 | 0.153203  | 0.197887 | 0.0893684 | 0.13405253582713605 | 0.10213526539210366 | 0.130861  | 0.105327  | 0.137244  | 0.140436  | 0.0829849 | 0.0957518 | 0.0574511  | 0.0893684 | 0.134053  | 0.07340972200057451 | 0.0797932 | 0.06064281382656155 | 0.0797932 | 0.05425935973955508   | 0.04149245156554211  | 0.0829849 | 0.0925601 | 0.0446842 | 0.0414925 | 0.0542594 | 0.0542594 | 0.0446842 | 0.130861  | 0.0606428  | 0.0542594 | 0.0574511 | 0.0861766 | 0.0478759 | 0.0383007 | 0.035109  | 0.028725543391529156 | 0.0446842 | 0.0734097 | 0.03510899747853563  | 0.028725543391529156 | 0.0829849 | 0.0478759 | 0.0797932 | 0.0287255 | 0.0606428 | 0.035109  | 0.0223421 | 0.07660144904407774 | 0.025533816348025914 | 0.0734097 | 0.0127669 | 0.0127669 | 0.022342089304522677 | 0.0223421 | 0.0287255 | 0.0383007 | 0.0446842  | 0.0223421 | 0.0542594 | 0.0319173 | 0.0223421 | 0.0446842 | 0.0574511 | 0.0319173 | 0.0319173 | 0.0223421  | 0.00638345 | 0.0191504 | 0.0287255 | 0.0414925 | 0.0191504  | 0.00638345 | 0.0223421 | 0.0414925 | 0.012766908174012957 | 0.0031917270435032393 | 0.0191504  | 0.00638345 | 0.019150362261019436  | 0.0159586 | 0.0159586 | 0.0159586 | 0.00957518 | 0.00638345 | 0.0319172704350324   | 0.00319173 | 0.00638345 | 0.0159586 | 0.025533816348025914  | 0.009575181130509718 | 0.00638345 | 0.0223421 | 0.0191504  | 0.00957518 | 0.00957518 | 0.00319173 | 0.0127669 | 0.0319173  | 0.00638345 | 0.0255338  | 0.0159586352175162  | 0.0191504 | 0.00957518 | 0.009575181130509718 | 0.0255338 | 0.00319173 | 0.0191504  | 0.0191504 | 0.0255338  | 0.0223421 | 0.00638345 | 0.00319173 | 0.0127669  | 0.0191504 | 0.00638345 | 0.00957518 | 0.00319173 | 0.0287255  | 0.0542594 | 0.00957518 | 0.0031917270435032393 |                      | 0.00319173 | 0.00638345 | 0.0127669  | 0.006383454087006479  | 0.00319173 | 0.0223421  | 0.006383454087006479 | 0.00638345 | 0.0031917270435032393 | 0.0127669  | 0.0031917270435032393 | 0.006383454087006479 | 0.00319173 | 0.00957518 | 0.006383454087006479  |                       |                      |                       |                       | 0.0031917270435032393 | 0.00319173 | 0.00638345 | 0.00319173 | 0.0159586  | 0.00319173 |                       | 0.009575181130509718  | 0.006383454087006479 |                       | 0.00638345 | 0.019150362261019436 |                       | 0.0031917270435032393 | 0.0031917270435032393 | 0.0127669  |                       | 0.00319173 |                      |                       | 0.0031917270435032393 | 0.0159586352175162    |                       |                       | 0.00319173 | 0.00319173 | 0.0191504  | 0.0031917270435032393 |                       | 0.0031917270435032393 | 0.0159586  | 0.0031917270435032393 | 0.006383454087006479  | 0.006383454087006479 |                      | 0.0127669  | 0.00957518 | 0.006383454087006479  | 0.0031917270435032393 | 0.006383454087006479  | 0.009575181130509718  | 0.00957518 |                       | 0.00638345 |                       |                       |                       |                       |                       | 0.006383454087006479  | 0.00638345 |                       |                       |                       | 0.0031917270435032393 | 0.00638345 |                       | 0.00319173  | 0.00957518 | 0.009575181130509718  |                       | 0.00957518 | 0.0031917270435032393 |                       | 0.012766908174012957  |                       |                     |                     |                     |                     |                     |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                       |                      |                       |                      |                      |                       |                      |                       |                       |                      | 0.0031917270435032393 |                       |                      |                      |                       | 0.0031917270435032393 |                       |                       |                       |                       |                       |                       |                       |                       | 0.0031917270435032393 |                       |                       |                       |                       | 0.0031917270435032393 | 0.006383454087006479  |                       |                       |                       |                       | 0.006383454087006479  |                       |                       |                       |                       |                       |                       |                       | 0.0031917270435032393 |                       |                       |                      |                       |                       |                       |                       |                       |                       |                       |                      |                      |                      | 0.0031917270435032393 |                      |
|   1367 | 73.1412 | 7.06351 | 2.54111 | 1.81071    | 1.53079     | 1.41707 | 1.14153 | 0.660427 | 0.507348 | 0.53359  | 0.323653 | 0.347708 | 0.358642 | 0.422061 | 0.2493   | 0.338961  | 0.142145  | 0.303971 | 0.218684 | 0.301784 | 0.212124 | 0.231805 | 0.205563 | 0.126837 | 0.0218684 | 0.170574 | 0.183695  | 0.146519 | 0.0962211 | 0.09840797760671799 | 0.08966060181945416 | 0.139958  | 0.131211  | 0.135584  | 0.107155  | 0.113716  | 0.100595  | 0.0852869  | 0.120276  | 0.137771  | 0.06123163051084675 | 0.100595  | 0.08966060181945416 | 0.0962211 | 0.059044786564030796  | 0.059044786564030796 | 0.0940343 | 0.0590448 | 0.0437369 | 0.0787264 | 0.0721659 | 0.0502974 | 0.0481106 | 0.0896606 | 0.0328027  | 0.0502974 | 0.0371763 | 0.0831001 | 0.0634185 | 0.0524843 | 0.0371763 | 0.03717634709587124  | 0.0502974 | 0.0393632 | 0.041550034989503146 | 0.03717634709587124  | 0.069979  | 0.0349895 | 0.0568579 | 0.0153079 | 0.069979  | 0.0459237 | 0.0196816 | 0.03936319104268719 | 0.030615815255423375 | 0.069979  | 0.0306158 | 0.0196816 | 0.019681595521343596 | 0.0328027 | 0.028429  | 0.028429  | 0.00656053 | 0.0153079 | 0.0174948 | 0.0240553 | 0.0262421 | 0.0306158 | 0.0568579 | 0.0328027 | 0.028429  | 0.0262421  | 0.0153079  | 0.0481106 | 0.0174948 | 0.098408  | 0.0240553  | 0.0196816  | 0.0328027 | 0.0590448 | 0.03280265920223933  | 0.0065605318404478655 | 0.0218684  | 0.00874738 | 0.010934219734079776  | 0.0131211 | 0.0262421 | 0.0131211 | 0.0174948  | 0.0153079  | 0.030615815255423375 | 0.00437369 | 0.0218684  | 0.0174948 | 0.00874737578726382   | 0.01749475157452764  | 0.00656053 | 0.0196816 | 0.00656053 | 0.0109342  | 0.0174948  | 0.0153079  | 0.0721659 | 0.0196816  | 0.0109342  | 0.0262421  | 0.00874737578726382 | 0.0153079 | 0.0218684  |                      | 0.028429  | 0.00874738 | 0.0109342  | 0.0153079 | 0.00437369 | 0.0218684 | 0.00437369 | 0.00874738 | 0.00437369 | 0.0218684 | 0.00656053 | 0.00218684 | 0.00656053 | 0.00874738 | 0.0481106 | 0.0153079  | 0.002186843946815955  | 0.002186843946815955 | 0.0153079  | 0.00656053 | 0.0109342  | 0.00437368789363191   | 0.0109342  | 0.00218684 | 0.00437368789363191  | 0.0153079  | 0.00874737578726382   | 0.00656053 |                       | 0.00437368789363191  | 0.00874738 | 0.00874738 | 0.00874737578726382   | 0.0065605318404478655 | 0.010934219734079776 | 0.00874737578726382   | 0.00437368789363191   | 0.0065605318404478655 | 0.00437369 | 0.00656053 | 0.0109342  | 0.0131211  | 0.00874738 | 0.00437368789363191   | 0.00874737578726382   | 0.002186843946815955 | 0.0065605318404478655 | 0.00218684 |                      |                       | 0.002186843946815955  |                       | 0.0174948  | 0.002186843946815955  | 0.00437369 | 0.00437368789363191  | 0.002186843946815955  | 0.00437368789363191   | 0.00437368789363191   | 0.002186843946815955  |                       | 0.0131211  | 0.0218684  | 0.0109342  |                       |                       | 0.00437368789363191   | 0.0109342  | 0.00874737578726382   | 0.002186843946815955  | 0.002186843946815955 | 0.00874737578726382  | 0.00437369 | 0.00874738 |                       |                       | 0.00437368789363191   | 0.002186843946815955  | 0.00874738 | 0.002186843946815955  | 0.00437369 |                       |                       |                       |                       |                       |                       | 0.00218684 | 0.00874737578726382   |                       | 0.013121063680895731  | 0.00437368789363191   | 0.00218684 | 0.002186843946815955  | 0.00218684  | 0.00656053 | 0.0065605318404478655 |                       | 0.0131211  |                       |                       |                       |                       |                     |                     |                     |                     |                     |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                       |                      |                       |                      |                      |                       |                      |                       |                       |                      | 0.0065605318404478655 |                       |                      |                      |                       | 0.002186843946815955  |                       | 0.002186843946815955  |                       |                       |                       |                       |                       |                       | 0.002186843946815955  |                       |                       | 0.00437368789363191   | 0.0065605318404478655 | 0.00437368789363191   |                       |                       | 0.002186843946815955  |                       |                       | 0.00437368789363191   | 0.002186843946815955  |                       | 0.002186843946815955  |                       |                       |                       | 0.002186843946815955  | 0.002186843946815955  |                       |                       |                      |                       |                       |                       | 0.002186843946815955  |                       |                       |                       |                      |                      |                      | 0.00437368789363191   | 0.002186843946815955 |
|   1368 | 71.7589 | 7.65094 | 3.35042 | 2.16045    | 1.57252     | 1.46904 | 1.07709 | 0.661618 | 0.544032 | 0.525218 | 0.421742 | 0.406064 | 0.387251 | 0.360598 | 0.304156 | 0.297885  | 0.266529  | 0.266529 | 0.264961 | 0.260257 | 0.210087 | 0.20852  | 0.20068  | 0.177163 | 0.166188  | 0.155214 | 0.147375  | 0.12229  | 0.114451  | 0.09877240016932412 | 0.09877240016932412 | 0.0956368 | 0.0925011 | 0.0877977 | 0.0862299 | 0.0846621 | 0.0846621 | 0.0846621  | 0.0783908 | 0.076823  | 0.0736873461580672  | 0.0736873 | 0.07211953028236363 | 0.0689839 | 0.06741608265525297   | 0.06428045090384585  | 0.0642805 | 0.0627126 | 0.0627126 | 0.0580092 | 0.0580092 | 0.0564414 | 0.0564414 | 0.0564414 | 0.0548736  | 0.0533057 | 0.0517379 | 0.0517379 | 0.0517379 | 0.0501701 | 0.0486023 | 0.04703447627110672  | 0.0470345 | 0.0470345 | 0.0438988445196996   | 0.0438988445196996   | 0.0438988 | 0.042331  | 0.042331  | 0.0407632 | 0.0391954 | 0.0391954 | 0.0376276 | 0.03762758101688538 | 0.03762758101688538  | 0.0360598 | 0.0329241 | 0.0329241 | 0.03135631751407115  | 0.0313563 | 0.0313563 | 0.0297885 | 0.0297885  | 0.0297885 | 0.0282207 | 0.0266529 | 0.0250851 | 0.0250851 | 0.0250851 | 0.0250851 | 0.0250851 | 0.0235172  | 0.0235172  | 0.0235172 | 0.0235172 | 0.0219494 | 0.0219494  | 0.0219494  | 0.0219494 | 0.0203816 | 0.020381606384146246 | 0.020381606384146246  | 0.0188138  | 0.0188138  | 0.01881379050844269   | 0.0188138 | 0.017246  | 0.017246  | 0.017246   | 0.017246   | 0.017245974632739133 | 0.0156782  | 0.0156782  | 0.0156782 | 0.015678158757035574  | 0.015678158757035574 | 0.0156782  | 0.0141103 | 0.0141103  | 0.0141103  | 0.0141103  | 0.0141103  | 0.0141103 | 0.0141103  | 0.0125425  | 0.0125425  | 0.01254252700562846 | 0.0125425 | 0.0125425  | 0.01254252700562846  | 0.0109747 | 0.0109747  | 0.0109747  | 0.0109747 | 0.0109747  | 0.0109747 | 0.0109747  | 0.0109747  | 0.0094069  | 0.0094069 | 0.0094069  | 0.0094069  | 0.0094069  | 0.0094069  | 0.0094069 | 0.0094069  | 0.009406895254221346  | 0.009406895254221346 | 0.0094069  | 0.0094069  | 0.0094069  | 0.007839079378517787  | 0.00783908 | 0.00783908 | 0.007839079378517787 | 0.00783908 | 0.007839079378517787  | 0.00783908 | 0.007839079378517787  | 0.007839079378517787 | 0.00627126 | 0.00627126 | 0.00627126350281423   | 0.00627126350281423   | 0.00627126350281423  | 0.00627126350281423   | 0.00627126350281423   | 0.00627126350281423   | 0.00627126 | 0.00627126 | 0.00627126 | 0.00627126 | 0.00627126 | 0.004703447627110673  | 0.004703447627110673  | 0.004703447627110673 | 0.004703447627110673  | 0.00470345 | 0.004703447627110673 | 0.004703447627110673  | 0.004703447627110673  | 0.004703447627110673  | 0.00470345 | 0.004703447627110673  | 0.00470345 | 0.004703447627110673 | 0.004703447627110673  | 0.004703447627110673  | 0.004703447627110673  | 0.003135631751407115  | 0.003135631751407115  | 0.00313563 | 0.00313563 | 0.00313563 | 0.003135631751407115  | 0.003135631751407115  | 0.003135631751407115  | 0.00313563 | 0.003135631751407115  | 0.003135631751407115  | 0.003135631751407115 | 0.003135631751407115 | 0.00313563 | 0.00313563 | 0.003135631751407115  | 0.003135631751407115  | 0.003135631751407115  | 0.003135631751407115  | 0.00313563 | 0.0015678158757035576 | 0.00156782 | 0.0015678158757035576 | 0.0015678158757035576 | 0.0015678158757035576 | 0.0015678158757035576 | 0.0015678158757035576 | 0.0015678158757035576 | 0.00156782 | 0.0015678158757035576 | 0.0015678158757035576 | 0.0015678158757035576 | 0.0015678158757035576 | 0.00156782 | 0.0015678158757035576 | 0.00156782  | 0.00156782 | 0.0015678158757035576 | 0.0015678158757035576 | 0.00156782 | 0.0015678158757035576 | 0.0015678158757035576 | 0.0015678158757035576 | 0.0015678158757035576 |                     |                     |                     |                     |                     |                     |                     |                     |                      |                      |                     |                      |                      |                      |                      |                       |                      |                       |                      |                      |                       |                      |                       |                       |                      |                       |                       |                      |                      |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                      |                       |                       |                       |                       |                       |                       |                       |                      |                      |                      |                       |                      |


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
| 1369-1401 |                                                     |


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
| 1369-1401 |                                                     |


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
| 1369-1401 |                                                     |


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


