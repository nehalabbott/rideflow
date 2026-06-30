# Development Log

## Sprint 1 – Project Setup

### Completed
- Set up FastAPI project structure
- Configured Docker Compose, PostgreSQL, and Adminer
- Integrated SQLAlchemy ORM
- Added environment-based configuration
- Established database connection and session management

###  Learned
- Docker networking and containers
- SQLAlchemy sessions and models
- Environment variable management

---

## Sprint 2 – Authentication

### Completed
- User registration and login
- Secure password hashing with bcrypt
- JWT authentication
- Protected routes with Bearer tokens
- `/users/me` endpoint
- Request/response validation using Pydantic
- Role-based users (Passenger, Driver, Admin)

### 📌 Endpoints
- `POST /auth/register`
- `POST /auth/login`
- `GET /users/me`

###  Learned
- JWT Authentication
- Password Hashing
- Dependency Injection
- Protected APIs

---

## Sprint 3 – Driver & Ride Matching

### Completed
- Driver profile creation
- Driver location updates
- Ride request endpoint
- Nearest-driver matching using Euclidean distance
- Service-layer architecture for business logic

### 📌 Endpoints
- `POST /drivers/profile`
- `POST /matching/driver-location`
- `POST /rides/request`

### Learned
- Service layer architecture
- Spatial distance calculation
- Backend request flow

---

## Sprint 4- Ride related

- ✅ Authentication
- ✅ PostgreSQL Integration
- ✅ Driver Profiles
- ✅ Driver Location Updates
- ✅ Ride Request Flow
- ✅ Nearest Driver Matching

---

## 🔜 Next Sprint

- QuadTree-based driver search
