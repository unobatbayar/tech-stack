from fastapi import FastAPI, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models

# Create the database tables (you can remove this once you're using Alembic migrations)
# Base.metadata.create_all(bind=engine)

app = FastAPI()

# CREATE
@app.post("/items/")
def create_item(
    name: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    db_item = models.Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# READ
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# READ ALL
@app.get("/items/")
def get_all_items(db: Session = Depends(get_db)):
    # Query all items from the database
    items = db.query(models.Item).all()
    return items

# UPDATE
@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    name: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        db_item.name = name
        db_item.description = description
        db.commit()
        db.refresh(db_item)
        return db_item

# DELETE
@app.delete("/items/{item_id}")
def delete_item(
    item_id: int, 
    db:Session = Depends(get_db)):
    # Deleting a user
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        db.delete(db_item)
        db.commit()
        return {"detail": "Item deleted successfully"}





