
 # RideFlow Architecture

```
                FastAPI

                  │

      ┌───────────┴───────────┐

      │                       │

 Authentication         Driver APIs

      │                       │

      └───────────┬───────────┘

                  │

            Matching Service

                  │

      Euclidean Distance Search

                  │

          Assigned Driver

                  │

             PostgreSQL
```

---

## Layers

API Layer

↓

Service Layer

↓

Database Layer

Models are separated from business logic.

Services contain all application logic.

Schemas validate requests and responses.

Dependencies handle authentication.


Driver location cache
Ride queue
Celery broker
