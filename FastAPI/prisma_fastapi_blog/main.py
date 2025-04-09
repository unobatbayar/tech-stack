from fastapi import FastAPI
from prisma import Prisma

app = FastAPI()
prisma = Prisma()

@app.on_event("startup")
async def on_startup():
    await prisma.connect()

@app.on_event("shutdown")
async def on_shutdown():
    await prisma.disconnect()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI + Prisma microservice!"}
