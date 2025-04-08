# backend/routes/chat_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/chats", tags=["chats"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create chat
@router.post("/", response_model=schemas.Chat)
def create_chat(chat: schemas.ChatCreate, db: Session = Depends(get_db)):
    new_chat = models.Chat(title=chat.title, user_id=1)  # TODO: replace 1 with actual user from token
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat

# Get all chats
@router.get("/", response_model=List[schemas.Chat])
def get_chats(db: Session = Depends(get_db)):
    return db.query(models.Chat).filter(models.Chat.user_id == 1).all()

# Add message
@router.post("/message", response_model=schemas.Message)
def add_message(msg: schemas.MessageCreate, db: Session = Depends(get_db)):
    message = models.Message(**msg.dict())
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

# Get messages by chat
@router.get("/{chat_id}/messages", response_model=List[schemas.Message])
def get_messages(chat_id: int, db: Session = Depends(get_db)):
    return db.query(models.Message).filter(models.Message.chat_id == chat_id).all()

#bvdfs