# mini-web-app

### DB Schema
##### Employee Table
| name         | Data Type | Length | Not Null? | Primary Key? |
| ------------ | ----------| ------ | --------- | ------------ |
| id           | integer   |        | Yes       | Yes          |
| first_name   | varchar   | 50     | Yes       | No           |
| last_name    | varchar   | 50     | Yes       | No           |
| email        | varchar   | 255    | Yes       | No           |
| position     | varchar   | 50     | Yes       | No           |
| phone_number | bigint    |        | Yes       | No           |
| salary       | integer   |        | Yes       | No           |
| date_hired   | date      |        | Yes       | No           |
