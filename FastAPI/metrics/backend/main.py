# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Role  # Import your models
from database import get_db

app = FastAPI()

@app.get("/roles/")
def read_users(db: Session = Depends(get_db)):
    return db.query(Role).all()

@app.post("/roles/")
def create_role(name: str, db: Session = Depends(get_db)):
    role = Role(name=name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role
