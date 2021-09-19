"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from sqlalchemy.orm import relationship

import os

from sqlalchemy.ext.asyncio import create_async_engine

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI")
# or "postgresql+asyncpg://postgres:password@localhost/postgres"
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    Text,
    DateTime,
    func,
)
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///asyncdb.sqlite")

Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)



class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    name = Column(Boolean, nullable=False, default=False)
    email  = Column(Boolean, nullable=False, default=False)
    posts=relationship("Post", back_populates="post")


class Post(Base):
    __tablename__ = "Post"
    postid=Column(Integer, primary_key=True)
    user = relationship("User", back_populates="user")
    title = Column(String(120), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")


if __name__ == "__main__":
    Base.metadata.create_all()
