from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models import Message
from app.db import init_db, get_db, MessageDB


app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()


@app.post("/history/")
def post_message(msg: Message, db: Session = Depends(get_db)):
    db_msg = MessageDB(**msg.dict())
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return {"status": "saved"}


@app.get("/history/{chatroom_id}", response_model=List[Message])
def get_history(chatroom_id: str, db: Session = Depends(get_db)):
    messages = db.query(MessageDB).filter(MessageDB.chatroom_id == chatroom_id).order_by(MessageDB.timestamp.asc()).all()
    return messages
