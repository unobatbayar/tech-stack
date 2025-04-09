from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from prisma import Prisma
from pydantic import BaseModel
from typing import List

app = FastAPI()
prisma = Prisma()

# Pydantic models for request validation
class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str

# Create the lifespan context manager for Prisma client
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to Prisma during startup
    await prisma.connect()
    print("Prisma connected.")
    yield
    # Disconnect Prisma during shutdown
    await prisma.disconnect()
    print("Prisma disconnected.")

app = FastAPI(lifespan=lifespan)

# Create a new user
@app.post("/users/", response_model=UserOut)
async def create_user(user: UserCreate):
    created_user = await prisma.user.create(
        data={
            "name": user.name,
            "email": user.email
        }
    )
    print("user created")
    return created_user

# Get all users
@app.get("/users/", response_model=List[UserOut])
async def get_users():
    users = await prisma.user.find_many()
    return users

# Get a user by ID
@app.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    user = await prisma.user.find_unique(where={"id": user_id})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update a user by ID
@app.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserCreate):
    updated_user = await prisma.user.update(
        where={"id": user_id},
        data={
            "name": user.name,
            "email": user.email
        }
    )
    return updated_user

# Delete a user by ID
@app.delete("/users/{user_id}", response_model=UserOut)
async def delete_user(user_id: int):
    deleted_user = await prisma.user.delete(where={"id": user_id})
    return deleted_user
