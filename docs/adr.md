# Architecture Decisions (ADR)

This document records the major architectural decisions made during the development of RideFlow and the reasoning behind them.

---

# ADR-001: FastAPI as the Backend Framework

* Excellent performance through ASGI.
* Native support for asynchronous programming.
* Automatic OpenAPI (Swagger) documentation.
* Strong type safety with Pydantic.
* Built-in dependency injection.
* Well suited for REST APIs and WebSockets.

## Alternatives Considered

* Django REST Framework
* Flask

## Why Not Them?

Django provides many features that are unnecessary for this project, while Flask would require significantly more setup for validation, documentation, and dependency management.

---

# ADR-002: PostgreSQL Instead of MongoDB

## Decision

Use PostgreSQL as the primary database.

## Reason

RideFlow contains highly relational data.

Examples:

* Users → Drivers
* Drivers → Vehicles
* Passengers → Rides
* Rides → Payments
* Rides → Ratings

Maintaining these relationships is much simpler using a relational database.

## Additional Benefits

* Strong foreign key support
* Excellent indexing
* Reliable for production systems

---

# ADR-003: Docker Compose for Development

## Reason

Every developer gets an identical development environment.

A single command starts the complete backend:

```bash
docker compose up -d
```

---

# ADR-004: Separate Driver Location Table

Driver coordinates change frequently, while profile information rarely changes.

Separating them:

* reduces unnecessary row updates
* improves scalability
* enables optimized indexing for location queries

---

# ADR-005: UUID Primary Keys

## Decision

Use UUIDs instead of auto-incrementing integers.

## Reason

Benefits include:

* Harder to guess resource identifiers
* Better suited for distributed systems
* Easier future microservice integration
* Simpler data merging across environments

## Why JWT?

Stateless authentication.

Easy to scale.

---
