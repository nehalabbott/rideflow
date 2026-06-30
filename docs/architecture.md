# RideFlow Architecture

```text
                    Client
                       │
                       ▼
                   FastAPI API
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
 Authentication   Driver APIs    Ride APIs
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                 Service Layer
                       │
        ┌──────────────┼──────────────┐
        │                             │
        ▼                             ▼
 Matching Service             Authentication Service
        │
        ▼
 QuadTree + Distance Calculation
        │
        ▼
 PostgreSQL (Users & Driver Profiles)
```

---

# Architecture Layers

### API Layer

- Handles incoming HTTP requests
- Validates requests using Pydantic schemas
- Returns JSON responses

---

### Service Layer

- Contains business logic
- Handles authentication, ride requests, and driver matching
- Keeps API routes lightweight

---

### Database Layer

- Stores users and driver profiles
- Uses SQLAlchemy ORM with PostgreSQL

---

### Matching Layer

- Stores driver locations in a QuadTree
- Finds nearby drivers efficiently
- Selects the nearest driver using Euclidean distance

---

## Design Principles

- Separation of concerns
- Layered architecture
- Service-based business logic
- Schema validation with Pydantic
- Stateless JWT authentication