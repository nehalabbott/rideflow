# Architecture Decision Records (ADR)

This document records the key architectural decisions made during the development of RideFlow.

---

# ADR-001: FastAPI

## Decision

Use **FastAPI** as the backend framework.

## Why?

- High performance
- Automatic Swagger documentation
- Built-in request validation with Pydantic
- Simple dependency injection
- Clean and easy-to-maintain code

**Alternatives:** Flask, Django REST Framework

---

# ADR-002: PostgreSQL

## Decision

Use **PostgreSQL** as the database.

## Why?

- Stores related data efficiently
- Works well with SQLAlchemy
- Supports foreign keys and indexing
- Reliable for backend applications

**Alternative:** MongoDB

---

# ADR-003: Docker

## Decision

Use **Docker Compose** for local development.

## Why?

- Same development environment on every machine
- Easy setup with a single command

```bash
docker compose up -d
```

---

# ADR-004: JWT Authentication

## Decision

Use **JWT** for user authentication.

## Why?

- Stateless authentication
- Secure API access
- Easy to use with protected routes

---

# ADR-005: UUID Primary Keys

## Decision

Use **UUIDs** as primary keys.

## Why?

- Harder to guess than sequential IDs
- Uniquely identifies records
- Commonly used in modern backend systems

---

# ADR-006: QuadTree for Driver Matching

## Decision

Use a **QuadTree** to organize driver locations.

## Why?

- Reduces the number of drivers checked during matching
- Improves nearest-driver search compared to checking every driver
- Falls back to a global search if no nearby drivers are found