from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, Time
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base() 

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class User(Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))

class ProductCategory(Base):
    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    product_category_id = Column(Integer, ForeignKey("product_categories.id"))
    is_active = Column(Boolean, default=True)

class Function(Base):
    __tablename__ = "functions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

class FunctionActivity(Base):
    __tablename__ = "function_activities"

    id = Column(Integer, primary_key=True, index=True)
    function_id = Column(Integer, ForeignKey("functions.id"))
    name = Column(String, nullable=False)
    index = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

class CurrentProductWork(Base):
    __tablename__ = "current_product_works"

    id = Column(Integer, primary_key=True, index=True)
    week = Column(Date, nullable=False)
    product_category_id = Column(Integer, ForeignKey("product_categories.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    function_id = Column(Integer, ForeignKey("functions.id"), nullable=False)
    function_activity_id = Column(Integer, ForeignKey("function_activities.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.uid"), nullable=False)
    index = Column(Integer, nullable=False)

class ProductWorktime(Base):
    __tablename__ = "product_worktimes"

    id = Column(Integer, primary_key=True, index=True)
    current_product_work_id = Column(Integer, ForeignKey("current_product_works.id"), nullable=False)
    datetime = Column(DateTime, nullable=False)
    worktime = Column(Float, nullable=False)

class TechnologyCategory(Base):
    __tablename__ = "technology_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

class TechnologyActivity(Base):
    __tablename__ = "technology_activities"

    id = Column(Integer, primary_key=True, index=True)
    technology_category_id = Column(Integer, ForeignKey("technology_categories.id"), nullable=False)
    name = Column(String, nullable=False)
    index = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

class Technology(Base):
    __tablename__ = "technologies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    technology_category_id = Column(Integer, ForeignKey("technology_categories.id"), nullable=False)
    is_active = Column(Boolean, default=True)

class CurrentTechWork(Base):
    __tablename__ = "current_tech_works"

    id = Column(Integer, primary_key=True, index=True)
    week = Column(Date, nullable=False)
    technology_category_id = Column(Integer, ForeignKey("technology_categories.id"), nullable=False)
    technology_id = Column(Integer, ForeignKey("technologies.id"), nullable=False)
    technology_activity_id = Column(Integer, ForeignKey("technology_activities.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.uid"), nullable=False)
    work_ratio = Column(Integer, nullable=False)
    index = Column(Integer, nullable=False)

class TechnologyWorktime(Base):
    __tablename__ = "technology_worktimes"

    id = Column(Integer, primary_key=True, index=True)
    current_tech_work_id = Column(Integer, ForeignKey("current_tech_works.id"), nullable=False)
    datetime = Column(DateTime, nullable=False)
    worktime = Column(Float, nullable=False)  # Worktime in hours
