from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
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
    __table__ = "users"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)

    role_id = Column(Integer, ForeignKey("roles.id"))

    # This connects the user to the role
    # Lets you do user.role to get the Role object for a given user.
    role = relationship("Role", back_populates="users")

#### product_categories, products

class ProductCategory(Base):
    __table__ = "product_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # Relationship with Product
    products = relationship("Product", back_populates="category")

class Product(Base):
    __table__ = "products"

    id = Column()
    name = Column(String, nullable=False)
    product_category_id = Column(Integer, ForeignKey("product_categories.id"))
    is_active = Column(Boolean, default=True)

    # Relationship to ProductCategory
    category = relationship("ProductCategory", back_populates="products")