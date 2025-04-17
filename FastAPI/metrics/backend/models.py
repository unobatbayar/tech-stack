from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base() 

class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.now)

######### Metrica_ER

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

