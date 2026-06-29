# 🚖 RideFlow

RideFlow is a backend system for a ride-sharing platform built with FastAPI. It supports secure authentication, driver profile management, driver location updates, and nearest-driver ride matching.

---
Demo: 
https://drive.google.com/file/d/1ow7ZVO_4F5XR17VRFa2h7mRusZsFK6x-/view?usp=sharing

## Features

- JWT Authentication
- Passenger & Driver Roles
- Driver Profile Management
- Driver Location Updates
- Nearest Driver Matching
- Ride Request API
- PostgreSQL Database
- Dockerized Development Environment

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- JWT Authentication
- Pydantic

---

## Project Structure

```
app/
    api/
    core/
    db/
    dependencies/
    models/
    schemas/
    services/
```

---

## Installation

Clone the repository

```bash
git clone <repo-url>
cd rideflow
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Docker

Start services

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

Adminer

```
http://localhost:8080
```

---

## Future Improvements

- QuadTree Spatial Index
- Redis Caching
- WebSocket Ride Updates
- Real-time Driver Tracking
- ETA Calculation
- Google Maps Integration

---

## Author

Nehal Abbott
