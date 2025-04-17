from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base() 

class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.now)

#### roles, users

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # This creates a "back-reference" so you can access Role.users
    # Lets you do role.users to get a list of all users with that role.
    users = relationship("User", back_populates="role")

class User(Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))

    # This connects the user to the role
    # Lets you do user.role to get the Role object for a given user.
    role = relationship("Role", back_populates="users")

#### product_categories, products

class ProductCategory(Base):
    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # Relationship with Product
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    product_category_id = Column(Integer, ForeignKey("product_categories.id"))
    is_active = Column(Boolean, default=True)

    # Relationship to ProductCategory
    category = relationship("ProductCategory", back_populates="products")

#### functions, function_activities

class Function(Base):
    __tablename__ = "functions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # Relationship to FunctionActivity
    activities = relationship("FunctionActivity", back_populates="function")

class FunctionActivity(Base):
    __tablename__ = "function_activities"

    id = Column(Integer, primary_key=True, index=True)
    function_id = Column(Integer, ForeignKey("functions.id"))
    name = Column(String, nullable=False)
    index = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    # Relationship to Function
    function = relationship("Function", back_populates="activities")

#### current_product_works, product_worktimes

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

    # Relationships (if needed later for queries)
    product_category = relationship("ProductCategory", back_populates="current_works")
    product = relationship("Product", back_populates="current_works")
    function = relationship("Function", back_populates="current_works")
    function_activity = relationship("FunctionActivity", back_populates="current_works")
    user = relationship("User", back_populates="current_works")

class ProductWorktime(Base):
    __tablename__ = "product_worktimes"

    id = Column(Integer, primary_key=True, index=True)
    current_product_work_id = Column(Integer, ForeignKey("current_product_works.id"), nullable=False)
    datetime = Column(DateTime, nullable=False)
    worktime = Column(Float, nullable=False)

    # Relationship (optional, for easier querying if needed)
    current_product_work = relationship("CurrentProductWork", back_populates="worktimes")