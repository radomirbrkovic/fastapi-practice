from fastapi import FastAPI
from infastructure.database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome!!"}
