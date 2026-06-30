# Setup Guide

## Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Git

---

## Installation

### Clone the repository

```bash
git clone <https://github.com/nehalabbott/rideflow.git>
cd rideflow
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Start Docker Services

```bash
docker compose up -d
```

To stop the services:

```bash
docker compose down
```

---

## Run the Backend

```bash
uvicorn app.main:app --reload
```

---

## Access the Application

| Service | URL |
|---------|-----|
| Swagger UI | http://localhost:8000/docs |
| Adminer | http://localhost:8080 |