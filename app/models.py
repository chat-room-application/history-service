from pydantic import BaseModel
from datetime import datetime


class Message(BaseModel):
    chatroom_id: str
    sender: str
    message: str
    timestamp: datetime
