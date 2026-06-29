from app.models import *
from app.db.base import Base
from app.db.engine import engine

print("TABLES:", Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

from fastapi import FastAPI
from sqlalchemy import text
from app.api.auth import router as auth_router

app = FastAPI()
app.include_router(auth_router)

from app.api.users import router as users_router
app.include_router(users_router)

from app.api.driver import router as driver_router
app.include_router(driver_router)

from app.api.rides import router as ride_router
app.include_router(ride_router)

from app.api.matching import router as matching_router
app.include_router(matching_router)

@app.get("/")
def root():
    return {"message": "RideFlow API"}


@app.get("/db-check")
def db_check():

    with engine.connect() as conn:

        result = conn.execute(text("SELECT 1"))

        return {
            "database": result.scalar()
        }