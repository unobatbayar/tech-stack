# main.py
# FastAPI app
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Role, User, FunctionActivity, TechnologyActivity
from schemas import (
    RoleCreate, UserCreate, UserOut, RoleOut,
    FunctionActivityCreate, FunctionActivityOut,
    TechnologyActivityCreate, TechnologyActivityOut
)
from typing import List


app = FastAPI()

# === Roles ===


@app.get("/roles/", response_model=List[RoleOut])
def read_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()


@app.post("/roles/", response_model=RoleOut)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


@app.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    db.delete(role)
    db.commit()
    return {"ok": True}

# === Users ===


@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.uid == user.uid).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="User with this UID already exists")

    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.get("/users/{user_uid}", response_model=UserOut)
def get_user(user_uid: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.uid == user_uid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_uid}")
def delete_user(user_uid: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.uid == user_uid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"ok": True, "message": f"User {user_uid} deleted"}

# === Function Activity Routes ===


@app.get("/function-activities/", response_model=List[FunctionActivityOut])
def get_function_activities(db: Session = Depends(get_db)):
    return db.query(FunctionActivity).all()


@app.post("/function-activities/", response_model=FunctionActivityOut)
def create_function_activity(activity: FunctionActivityCreate, db: Session = Depends(get_db)):
    db_activity = FunctionActivity(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


# === Technology Activity Routes ===

@app.get("/technology-activities/", response_model=List[TechnologyActivityOut])
def get_tech_activities(db: Session = Depends(get_db)):
    return db.query(TechnologyActivity).all()


@app.post("/technology-activities/", response_model=TechnologyActivityOut)
def create_tech_activity(activity: TechnologyActivityCreate, db: Session = Depends(get_db)):
    db_activity = TechnologyActivity(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity
