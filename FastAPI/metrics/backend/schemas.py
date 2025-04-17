# schemas.py
from pydantic import BaseModel
from typing import Optional


class RoleCreate(BaseModel):
    name: str


class RoleOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    uid: str
    name: str
    role_id: int


class UserOut(BaseModel):
    uid: str
    name: str
    role_id: int

    class Config:
        orm_mode = True


class FunctionActivityCreate(BaseModel):
    function_id: int
    name: str
    index: int
    is_active: Optional[bool] = True


class FunctionActivityOut(BaseModel):
    id: int
    function_id: int
    name: str
    index: int
    is_active: bool

    class Config:
        orm_mode = True


class TechnologyActivityCreate(BaseModel):
    technology_category_id: int
    name: str
    index: int
    is_active: Optional[bool] = True


class TechnologyActivityOut(BaseModel):
    id: int
    technology_category_id: int
    name: str
    index: int
    is_active: bool

    class Config:
        orm_mode = True
