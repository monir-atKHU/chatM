# backend/models.py
from sqlalchemy import Column, Integer, String
from backend.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Chat(Base):
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))

    user = relationship("User", backref="chats")
    messages = relationship("Message", backref="chat", cascade="all, delete")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    content = Column(String)
    role = Column(String)  # 'user' or 'assistant'
    timestamp = Column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
