# census_month

## Table Code

| Years     |   File Code |
|:----------|------------:|
| 1387      |         nan |
| 1388-1389 |         nan |
| 1390      |         nan |
| 1391      |         nan |


## Columns Availability

| Years     | 0       | 1          |
|:----------|:--------|:-----------|
| 1387-1390 | address | MahMorajeh |
| 1391      | Address | MahMorajeh |


## Annual Summary Tables

### 1387

| Column     |   Missing Count |   Availability Ratio | Data Type   |   Unique Values | Frequent Values                             |
|:-----------|----------------:|---------------------:|:------------|----------------:|:--------------------------------------------|
| address    |               0 |                  100 | integer     |           39305 | 1297653005: 1; 2000194001: 1; 2000194002: 1 |
| MahMorajeh |               0 |                  100 | integer     |              12 | 7: 3,533; 3: 3,461; 4: 3,396                |


### 1388

| Column     |   Missing Count |   Availability Ratio | Data Type   |   Unique Values | Frequent Values                             |
|:-----------|----------------:|---------------------:|:------------|----------------:|:--------------------------------------------|
| address    |               0 |                  100 | integer     |           37045 | 1290112003: 1; 2000272004: 1; 2000224005: 1 |
| MahMorajeh |               0 |                  100 | integer     |              12 | 4: 3,164; 3: 3,141; 8: 3,113                |


### 1390

| Column     |   Missing Count |   Availability Ratio | Data Type   |   Unique Values | Frequent Values                             |
|:-----------|----------------:|---------------------:|:------------|----------------:|:--------------------------------------------|
| address    |               0 |                  100 | integer     |           40010 | 1300040067: 1; 2000081293: 1; 2000105234: 1 |
| MahMorajeh |               0 |                  100 | integer     |              12 | 9: 3,516; 12: 3,493; 4: 3,466               |


### 1391

| Column     |   Missing Count |   Availability Ratio | Data Type   |   Unique Values | Frequent Values                             |
|:-----------|----------------:|---------------------:|:------------|----------------:|:--------------------------------------------|
| Address    |               0 |                  100 | integer     |           40007 | 1300080121: 1; 2000157154: 1; 2000157163: 1 |
| MahMorajeh |               0 |                  100 | integer     |              12 | 3: 3,515; 5: 3,372; 8: 3,371                |


## Column Code Summary Tables

### ADDRESS

??? abstract "Column Metadata"
    ``` yaml
    1363:
      new_name: ID
      type: UInt64
    
    ```
|      |   Missing_Count |   Availability_Ratio | Data_Type   |   Unique_Values | Frequent_Values                             |
|-----:|----------------:|---------------------:|:------------|----------------:|:--------------------------------------------|
| 1387 |               0 |                  100 | integer     |           39305 | 1297653005: 1; 2000194001: 1; 2000194002: 1 |
| 1388 |               0 |                  100 | integer     |           37045 | 1290112003: 1; 2000272004: 1; 2000224005: 1 |
| 1390 |               0 |                  100 | integer     |           40010 | 1300040067: 1; 2000081293: 1; 2000105234: 1 |


### MAHMORAJEH

??? abstract "Column Metadata"
    ``` yaml
    1363:
      new_name: Month
      type: UInt8
    
    ```
|      |   Missing_Count |   Availability_Ratio | Data_Type   |   Unique_Values | Frequent_Values               |
|-----:|----------------:|---------------------:|:------------|----------------:|:------------------------------|
| 1387 |               0 |                  100 | integer     |              12 | 7: 3,533; 3: 3,461; 4: 3,396  |
| 1388 |               0 |                  100 | integer     |              12 | 4: 3,164; 3: 3,141; 8: 3,113  |
| 1390 |               0 |                  100 | integer     |              12 | 9: 3,516; 12: 3,493; 4: 3,466 |
| 1391 |               0 |                  100 | integer     |              12 | 3: 3,515; 5: 3,372; 8: 3,371  |


