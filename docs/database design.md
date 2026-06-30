# Database Design

## Current Tables

| Table | Purpose |
|-------|---------|
| `users` | Stores user accounts, authentication details, and roles |
| `driver_profiles` | Stores driver-specific information |
| `rides` | Stores ride requests and ride details |

---

## Relationships

```text
Users
   │
   ├── Driver Profile (1:1)
   │
   └── Rides (1:N)
```

- One user can create multiple rides.
- A driver profile belongs to exactly one user.

---

## Planned Tables

These tables are planned for future development:

- `vehicles`
- `payments`
- `ratings`
- `notifications`
- `ride_logs`
- `receipts`
- `refresh_tokens`
- `otp_codes`
- `surge_zones`
- `admin_logs`