# RideFlow API Documentation

## Authentication

### Register

POST

```
/auth/register
```

### Login

POST

```
/auth/login
```

Returns JWT Access Token.

---

## User

### Current User

GET

```
/users/me
```

Requires Authorization.

---

## Driver

### Create Driver Profile

POST

```
/drivers/profile
```

### Update Driver Location

POST

```
/matching/driver-location
```

---

## Ride

### Request Ride

POST

```
/rides/request
```

Returns nearest driver.

---

## Matching

### Find Nearest Driver

POST

```
/matching/find-driver
```

Returns nearest driver using Euclidean distance.
