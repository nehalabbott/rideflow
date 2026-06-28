# Architecture Decisions (ADR)

This document records the major architectural decisions made during the development of RideFlow and the reasoning behind them.

---

# ADR-001: FastAPI as the Backend Framework

## Decision

Use **FastAPI** as the primary backend framework.

## Reason

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

* ACID transactions
* Strong foreign key support
* Excellent indexing
* Mature query planner
* Reliable for production systems

---

# ADR-003: SQLAlchemy 2.0 as the ORM

## Decision

Use SQLAlchemy 2.0.

## Reason

* Modern ORM with type hints
* Flexible query building
* Database independence
* Clean model definitions
* Easy integration with Alembic

---

# ADR-004: Docker Compose for Development

## Decision

Run all services through Docker Compose.

## Services

* FastAPI
* PostgreSQL
* Redis
* pgAdmin

## Reason

Every developer gets an identical development environment.

A single command starts the complete backend:

```bash
docker compose up -d
```

---

# ADR-005: Environment Variables

## Decision

Store configuration inside `.env`.

## Reason

Sensitive information should never be committed to Git.

Examples:

* Database URL
* JWT Secret
* Redis URL
* API Keys

Configuration is loaded using `pydantic-settings`.

---

# ADR-006: Layered Project Structure

## Decision

Separate the application into multiple layers.

```text
API
↓

Services
↓

Algorithms
↓

Database
```

## Reason

Each layer has a single responsibility.

Benefits:

* Easier testing
* Better maintainability
* Cleaner codebase
* Lower coupling

---

# ADR-007: Separate Driver and User Tables

## Decision

Keep authentication data separate from driver-specific data.

```text
Users
  │
  ├── Passenger
  │
  └── Driver
```

## Reason

Authentication information is shared across all users, while drivers and passengers have different business-specific fields.

This reduces null values and follows database normalization principles.

---

# ADR-008: Separate Driver Location Table

## Decision

Store live driver locations in a dedicated table.

## Reason

Driver coordinates change frequently, while profile information rarely changes.

Separating them:

* reduces unnecessary row updates
* improves scalability
* enables optimized indexing for location queries

---

# ADR-009: UUID Primary Keys

## Decision

Use UUIDs instead of auto-incrementing integers.

## Reason

Benefits include:

* Harder to guess resource identifiers
* Better suited for distributed systems
* Easier future microservice integration
* Simpler data merging across environments

---

# ADR-010: Alembic for Database Migrations

## Decision

Manage schema evolution using Alembic.

## Reason

Benefits:

* Version-controlled schema changes
* Easy upgrades and rollbacks
* Team-friendly database development
* Production-ready migration workflow

---

# ADR-011: Redis for Temporary Data

## Decision

Use Redis for frequently changing, short-lived data.

## Planned Usage

* Driver location cache
* Active ride requests
* Background task broker
* Session storage (future)

## Reason

Redis is significantly faster than repeatedly querying PostgreSQL for highly dynamic data.

---

# ADR-012: Celery for Background Processing

## Decision

Run long-running tasks asynchronously.

## Planned Tasks

* Receipt generation
* Push notifications
* Email delivery
* Analytics
* Scheduled cleanup jobs

## Reason

These operations should not delay API responses.

---

# ADR-013: WebSockets for Live Ride Updates

## Decision

Use WebSockets instead of HTTP polling.

## Reason

Ride tracking requires continuous communication between the server and connected clients.

Benefits:

* Lower latency
* Reduced network overhead
* Real-time user experience

---

# ADR-014: Algorithm-Driven Dispatch Engine

## Decision

Implement custom algorithms instead of relying solely on database queries.

## Planned Components

* QuadTree for nearest-driver lookup
* Priority Queue for driver selection
* A* for shortest route computation

## Reason

The goal of RideFlow is to demonstrate software engineering and algorithmic problem-solving, not just CRUD operations.

---

# Future Decisions

The following architectural decisions will be documented as the project evolves:

* Authentication strategy
* Rate limiting
* Logging framework
* Testing strategy
* CI/CD pipeline
* Deployment architecture
* Caching strategy
* Scaling approach
* Monitoring and observability
