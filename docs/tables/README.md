# Tables

## Original Tables

### General Tables

#### Metadata

* household_information 
([raw](raw/household_information.md), 
[cleaned](cleaned/household_information.md), 
[normalized](normalized/household_information.md))
* members_properties
([raw](raw/members_properties.md),
[cleaned](cleaned/members_properties.md),
[normalized](normalized/members_properties.md))
* house_specifications
([raw](raw/house_specifications.md),
[cleaned](cleaned/house_specifications.md),
[normalized](normalized/house_specifications.md))
* house_specifications (Old, Rural)
([raw](raw/old_rural_house_specifications.md),
[cleaned](cleaned/old_rural_house_specifications.md))
* house_specifications (Old, Urban)
([raw](raw/old_urban_house_specifications.md),
[cleaned](cleaned/old_urban_house_specifications.md))
* census_month
([raw](raw/census_month.md), 
[cleaned](cleaned/census_month.md), 
[normalized](normalized/census_month.md))

#### Availability

| Table                          | 1363 - 1368 | 1369 - 1386 | 1387  - 1401 |
| ------------------------------ | ----------- | ----------- | ------------ |
| household_information          | ❌           | ❌           | ✅            |
| members_properties             | ✅           | ✅           | ✅            |
| house_specifications           | ❌           | ✅           | ✅            |
| old_rural_house_specifications | ✅           | ❌           | ❌            |
| old_urban_house_specifications | ✅           | ❌           | ❌            |

### Expenditure Tables

#### Metadata

* food
([raw](raw/food.md), 
[cleaned](cleaned/food.md), 
[normalized](normalized/food.md))
* tobacco
([raw](raw/tobacco.md), 
[cleaned](cleaned/tobacco.md), 
[normalized](normalized/tobacco.md))
* cloth
([raw](raw/cloth.md), 
[cleaned](cleaned/cloth.md), 
[normalized](normalized/cloth.md))
* home
([raw](raw/home.md), 
[cleaned](cleaned/home.md), 
[normalized](normalized/home.md))
* furniture
([raw](raw/furniture.md), 
[cleaned](cleaned/furniture.md), 
[normalized](normalized/furniture.md))
* medical
([raw](raw/medical.md), 
[cleaned](cleaned/medical.md), 
[normalized](normalized/medical.md))
* transportation
([raw](raw/transportation.md), 
[cleaned](cleaned/transportation.md), 
[normalized](normalized/transportation.md))
* communication
([raw](raw/communication.md), 
[cleaned](cleaned/communication.md), 
[normalized](normalized/communication.md))
* entertainment
([raw](raw/entertainment.md), 
[cleaned](cleaned/entertainment.md), 
[normalized](normalized/entertainment.md))
* education
([raw](raw/education.md), 
[cleaned](cleaned/education.md), 
[normalized](normalized/education.md))
* hotel
([raw](raw/hotel.md), 
[cleaned](cleaned/hotel.md), 
[normalized](normalized/hotel.md))
* miscellaneous
([raw](raw/miscellaneous.md), 
[cleaned](cleaned/miscellaneous.md), 
[normalized](normalized/miscellaneous.md))
* durable
([raw](raw/durable.md), 
[cleaned](cleaned/durable.md), 
[normalized](normalized/durable.md))
* investment
([raw](raw/investment.md), 
[cleaned](cleaned/investment.md), 
[normalized](normalized/investment.md))

#### Availability

| Table          | 1363 - 1365 | 1366 - 1376 | 1375 - 1377 | 1378 - 1382 | 1383 - 1401 |
| -------------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| food           | ✅           | ✅           | ✅           | ✅           | ✅           |
| tobacco        | ❌           | ❌           | ❌           | ❌           | ✅           |
| cloth          | ✅           | ✅           | ✅           | ✅           | ✅           |
| home           | ✅           | ✅           | ✅           | ✅           | ✅           |
| furniture      | ✅           | ✅           | ✅           | ✅           | ✅           |
| medical        | ✅           | ✅           | ✅           | ✅           | ✅           |
| transportation | ✅           | ✅           | ✅           | ✅           | ✅           |
| communication  | ❌           | ❌           | ❌           | ❌           | ✅           |
| entertainment  | ✅           | ✅           | ✅           | ✅           | ✅           |
| education      | ❌           | ❌           | ❌           | ❌           | ✅           |
| hotel          | ❌           | ❌           | ❌           | ❌           | ✅           |
| other          | ✅           | ✅           | ✅           | ✅           | ✅           |
| durable        | ✅           | ✅           | ✅           | ✅           | ✅           |
| investment     | ❌           | ✅           | ❌           | ✅           | ✅           |

### Income Tables

#### Metadata

* employment_income
([raw](raw/employment_income.md), 
[cleaned](cleaned/employment_income.md),
[normalized](normalized/employment_income.md))
* self_employed_income
([raw](raw/self_employed_income.md), 
[cleaned](cleaned/self_employed_income.md),
[normalized](normalized/self_employed_income.md))
* other_income
([raw](raw/other_income.md), 
[cleaned](cleaned/other_income.md),
[normalized](normalized/other_income.md))
* subsidy
([raw](raw/subsidy.md), 
[cleaned](cleaned/subsidy.md),
[normalized](normalized/subsidy.md))
* old_rural_public_employment_income
([raw](raw/old_rural_public_employment_income.md), 
[cleaned](cleaned/old_rural_public_employment_income.md))
* old_urban_public_employment_income
([raw](raw/old_urban_public_employment_income.md), 
[cleaned](cleaned/old_urban_public_employment_income.md))
* old_rural_private_employment_income
([raw](raw/old_rural_private_employment_income.md), 
[cleaned](cleaned/old_rural_private_employment_income.md))
* old_urban_private_employment_income
([raw](raw/old_urban_private_employment_income.md), 
[cleaned](cleaned/old_urban_private_employment_income.md))
* old_agricultural_self_employed_income
([raw](raw/old_agricultural_self_employed_income.md), 
[cleaned](cleaned/old_agricultural_self_employed_income.md))
* old_non_agricultural_self_employed_income
([raw](raw/old_non_agricultural_self_employed_income.md), 
[cleaned](cleaned/old_non_agricultural_self_employed_income.md))
* old_other_income
([raw](raw/old_other_income.md), 
[cleaned](cleaned/old_other_income.md))

#### Availability

| Table                                     | 1363 - 1368 | 1369 - 1389 | 1390 - 1401 |
| ----------------------------------------- | ----------- | ----------- | ----------- |
| employment_income                         | ❌           | ✅           | ✅           |
| self_employed_income                      | ❌           | ✅           | ✅           |
| other_income                              | ❌           | ✅           | ✅           |
| subsidy                                   | ❌           | ❌           | ✅           |
| old_rural_public_employment_income        | ✅           | ❌           | ❌           |
| old_urban_public_employment_income        | ✅           | ❌           | ❌           |
| old_rural_private_employment_income       | ✅           | ❌           | ❌           |
| old_urban_private_employment_income       | ✅           | ❌           | ❌           |
| old_agricultural_self_employed_income     | ✅           | ❌           | ❌           |
| old_non_agricultural_self_employed_income | ✅           | ❌           | ❌           |
| old_other_income                          | ✅           | ❌           | ❌           |

## Standard Tables
