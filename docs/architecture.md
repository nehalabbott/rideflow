
                Client

                   │

             FastAPI API

                   │

        Configuration Layer

                   │

           SQLAlchemy ORM

                   │

             PostgreSQL

                   │

        Redis (Background Tasks)

                   │

            Docker Compose

Why FastAPI?
High-performance asynchronous framework
Automatic OpenAPI documentation
Excellent dependency injection
Native async support

Why PostgreSQL?
Strong relational model
ACID compliance
Excellent indexing
Ideal for ride dispatch data

Why Redis?

Currently reserved for:

Driver location cache
Ride queue
Celery broker