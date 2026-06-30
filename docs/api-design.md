# API Design

This document provides an overview of the available REST API endpoints in RideFlow.

---

# Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate a user and return a JWT access token |

---

# Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users/me` | Retrieve details of the authenticated user |

> **Authorization Required:** Bearer Token

---

# Driver

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/drivers/profile` | Create a driver profile |
| POST | `/matching/driver-location` | Update the driver's current location |

> **Authorization Required:** Driver

---

# Ride

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/rides/request` | Request a ride and assign the nearest available driver |

> **Authorization Required:** Passenger

---

# Matching

RideFlow uses a **QuadTree** to efficiently retrieve nearby drivers before selecting the closest one using Euclidean distance.

---

# Response Format

All endpoints return JSON responses.

### Success

```json
{
    "message": "Success"
}
```

### Error

```json
{
    "detail": "Error message"
}
```