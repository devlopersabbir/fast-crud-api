from sqlalchemy import Integer, Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from configs.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name: Column(String, nullable=True)
    username: Column(String, nullable=False, unique=True, index=True)
    password: Column(String)
    is_active = Column(Boolean, default=True)
