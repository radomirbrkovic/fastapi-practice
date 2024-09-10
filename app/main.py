from fastapi import FastAPI
from infastructure.database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome!!"}

@app.get("/check-db")
async def startup_event():
    try:
        engine.connect()
        print("Database connection established successfully")
    except Exception as e:
        print(f"Database connection error: {e}")