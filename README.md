# kata
Lab on Flask

* [Setup the project in dev mode](docs/setup_dev_env.md)

## Context
"Properties Portfolio" is a web application developed by a real estate company that specializes
in property management. The application offers insights to around 1,000 investors on the
properties managed by the company's property managers. The application's frontend is built
using a SPA in Angular, while the backend is developed using Flask with Gunicorn and Python
3.9. The backend runs as a Docker image within a service in ECS (Fargate) behind an application
load balancer that is served by AWS API Gateway. The backend uses SQLAlchemy as an ORM
for CRUD operations and Pandas as an ETL (mainly to feed the database daily with properties
data). The database is deployed on a PostgreSQL 14 engine on AWS RDS.

## Use Case
The real estate company wants to improve the user experience of their web application by
adding new features which would impact existing API, models, database etc...

## Answers of Questions

* [Question 1](docs/question_one.md)

* [Question 2](docs/question_two.md)

* *Question 3*
We prevent SQL injection attacks by serialize user input data and by validate each field of
our new serialize object.
I would use a schema validation with Marshmallow library.
```py

```

* *Question 4*
For authentication, an SSO service can managed it. And for authorization on our web application, we can use the framework OAuth2 with the SSO service.

* *Question 5*
We can define rate limiting for API endpoints at the web server configuration file. It's a good pratice, because if not defined, our web server would shut down. It's Denied Of Service if the web server get more connections than he can managed.

* [Question 7](docs/question_seven.md)

