from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name =  Column(String, nullable=False)
    birth= Column(DateTime)
    created= Column(DateTime, default=datetime.now)


user = [
    UserModel(first_name = 'Bob', last_name='Khan', birth=datetime(1980, 5,2)),
    UserModel(first_name = 'Susan', last_name='Sage', birth=datetime(1979, 6,12)),
]
