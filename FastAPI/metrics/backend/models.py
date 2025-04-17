# models.py
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# === Roles & Users ===

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    users = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")
    current_product_works = relationship(
        "CurrentProductWork", back_populates="user")
    current_tech_works = relationship("CurrentTechWork", back_populates="user")


# === Product Categories & Products ===

class ProductCategory(Base):
    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    products = relationship("Product", back_populates="category")
    current_product_works = relationship(
        "CurrentProductWork", back_populates="product_category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    product_category_id = Column(Integer, ForeignKey("product_categories.id"))
    is_active = Column(Boolean, default=True)

    category = relationship("ProductCategory", back_populates="products")
    current_product_works = relationship(
        "CurrentProductWork", back_populates="product")


# === Functions & Activities ===

class Function(Base):
    __tablename__ = "functions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    activities = relationship("FunctionActivity", back_populates="function")
    current_product_works = relationship(
        "CurrentProductWork", back_populates="function")


class FunctionActivity(Base):
    __tablename__ = "function_activities"

    id = Column(Integer, primary_key=True, index=True)
    function_id = Column(Integer, ForeignKey("functions.id"))
    name = Column(String, nullable=False)
    index = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    function = relationship("Function", back_populates="activities")
    current_product_works = relationship(
        "CurrentProductWork", back_populates="function_activity")


# === Current Product Work & Worktimes ===

class CurrentProductWork(Base):
    __tablename__ = "current_product_works"

    id = Column(Integer, primary_key=True, index=True)
    week = Column(Date, nullable=False)
    product_category_id = Column(Integer, ForeignKey(
        "product_categories.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    function_id = Column(Integer, ForeignKey("functions.id"), nullable=False)
    function_activity_id = Column(Integer, ForeignKey(
        "function_activities.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.uid"), nullable=False)
    index = Column(Integer, nullable=False)

    product_category = relationship(
        "ProductCategory", back_populates="current_product_works")
    product = relationship("Product", back_populates="current_product_works")
    function = relationship("Function", back_populates="current_product_works")
    function_activity = relationship(
        "FunctionActivity", back_populates="current_product_works")
    user = relationship("User", back_populates="current_product_works")
    worktimes = relationship(
        "ProductWorktime", back_populates="current_product_work")


class ProductWorktime(Base):
    __tablename__ = "product_worktimes"

    id = Column(Integer, primary_key=True, index=True)
    current_product_work_id = Column(Integer, ForeignKey(
        "current_product_works.id"), nullable=False)
    datetime = Column(DateTime, nullable=False)
    worktime = Column(Float, nullable=False)

    current_product_work = relationship(
        "CurrentProductWork", back_populates="worktimes")


# === Technology Categories, Activities, Technologies ===

class TechnologyCategory(Base):
    __tablename__ = "technology_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    activities = relationship("TechnologyActivity", back_populates="category")
    technologies = relationship("Technology", back_populates="category")
    current_tech_works = relationship(
        "CurrentTechWork", back_populates="technology_category")


class TechnologyActivity(Base):
    __tablename__ = "technology_activities"

    id = Column(Integer, primary_key=True, index=True)
    technology_category_id = Column(Integer, ForeignKey(
        "technology_categories.id"), nullable=False)
    name = Column(String, nullable=False)
    index = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    category = relationship("TechnologyCategory", back_populates="activities")
    current_tech_works = relationship(
        "CurrentTechWork", back_populates="technology_activity")


class Technology(Base):
    __tablename__ = "technologies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    technology_category_id = Column(Integer, ForeignKey(
        "technology_categories.id"), nullable=False)
    is_active = Column(Boolean, default=True)

    category = relationship("TechnologyCategory",
                            back_populates="technologies")
    current_tech_works = relationship(
        "CurrentTechWork", back_populates="technology")


# === Current Tech Work & Worktimes ===

class CurrentTechWork(Base):
    __tablename__ = "current_tech_works"

    id = Column(Integer, primary_key=True, index=True)
    week = Column(Date, nullable=False)
    technology_category_id = Column(Integer, ForeignKey(
        "technology_categories.id"), nullable=False)
    technology_id = Column(Integer, ForeignKey(
        "technologies.id"), nullable=False)
    technology_activity_id = Column(Integer, ForeignKey(
        "technology_activities.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.uid"), nullable=False)
    work_ratio = Column(Integer, nullable=False)
    index = Column(Integer, nullable=False)

    technology_category = relationship(
        "TechnologyCategory", back_populates="current_tech_works")
    technology = relationship(
        "Technology", back_populates="current_tech_works")
    technology_activity = relationship(
        "TechnologyActivity", back_populates="current_tech_works")
    user = relationship("User", back_populates="current_tech_works")
    worktimes = relationship("TechnologyWorktime",
                             back_populates="current_tech_work")


class TechnologyWorktime(Base):
    __tablename__ = "technology_worktimes"

    id = Column(Integer, primary_key=True, index=True)
    current_tech_work_id = Column(Integer, ForeignKey(
        "current_tech_works.id"), nullable=False)
    datetime = Column(DateTime, nullable=False)
    worktime = Column(Float, nullable=False)

    current_tech_work = relationship(
        "CurrentTechWork", back_populates="worktimes")
