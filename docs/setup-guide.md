
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


Swagger

localhost:8000/docs

pgAdmin

localhost:5050
