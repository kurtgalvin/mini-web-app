# mini-web-app

Hello!
This [here](http://afternoon-dusk-09486.herokuapp.com/) is my mini-web-app project!

## DB Schema
Employee Table

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
```sql
UNIQUE(first_name, last_name)
```

## Stack
### Hosting
* Database: Amazon Relational Database Service (AWS RDS). 
* Web: Heroku.

### Backend
* Python: Flask, without SQLAlchemy.

### Frontend
* HTML5
* CSS
* Javascript
