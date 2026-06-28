from fastapi import FastAPI
from sqlalchemy import text

from app.db.engine import engine

app = FastAPI()

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