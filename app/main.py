from fastapi import FastAPI
from infastructure.database import engine, Base
from routers import auth

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome!!"}

app.include_router(auth.router)