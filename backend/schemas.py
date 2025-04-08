# backend/schemas.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ChatBase(BaseModel):
    title: str

class ChatCreate(ChatBase):
    pass

class Chat(ChatBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    content: str
    role: str  # "user" or "assistant"

class MessageCreate(MessageBase):
    chat_id: int

class Message(MessageBase):
    id: int
    chat_id: int
    timestamp: datetime

    class Config:
        orm_mode = True