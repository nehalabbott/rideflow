
# 🚖 RideFlow

RideFlow is a backend system for a ride-sharing application built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. The project focuses on secure authentication, driver management, and efficient ride matching using a **QuadTree-based spatial index**.

---
Demo: 
https://drive.google.com/file/d/1ow7ZVO_4F5XR17VRFa2h7mRusZsFK6x-/view?usp=sharing

## ✨ Features

- 🔐 JWT Authentication
- 👥 Role-based Users (Passenger, Driver, Admin)
- 🚗 Driver Profile Management
- 📍 Driver Location Updates
- 🚕 Ride Request API
- 🌳 QuadTree-based Driver Matching
- 🐳 Dockerized Development Environment
- 🗄️ PostgreSQL Database
- 📖 Interactive Swagger Documentation

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT + bcrypt |
| Validation | Pydantic |
| Containerization | Docker |
| Database UI | Adminer |
| Spatial Search | QuadTree |

---

## 📂 Project Structure

```text
rideflow/
│
├── app/
│   ├── algorithms/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── dependencies/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── docs/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---


## 🔄 Application Flow

```text
Register User
      │
      ▼
Login
      │
      ▼
Receive JWT Token
      │
      ▼
Authorize Requests
      │
      ▼
Driver Updates Location
      │
      ▼
Passenger Requests Ride
      │
      ▼
QuadTree Finds Nearby Drivers
      │
      ▼
Nearest Driver Assigned
```

---

## 🌳 QuadTree-Based Matching

RideFlow uses a **QuadTree** to organize driver locations spatially and reduce the search space when matching drivers with passengers.

### Matching Process
1. Store driver locations in a QuadTree.
2. Query nearby drivers around the pickup location.
3. Select the closest driver using Euclidean distance.
4. Fall back to a global search if no nearby drivers are found.

---

## 📌 API Endpoints

| Module | Endpoints |
|---------|-----------|
| Authentication | `/auth/register`, `/auth/login` |
| Users | `/users/me` |
| Driver | `/drivers/profile`, `/matching/driver-location` |
| Ride | `/rides/request` |

Interactive API documentation is available through **Swagger UI**.

---

## 🚀 Future Improvements

- Ride status lifecycle
- Unit tests
- Deployment (Render + Neon)
- Driver availability management

---

## 👨‍💻 Author

**Nehal Abbott**
