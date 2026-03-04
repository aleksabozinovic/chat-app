from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class RoomCreate(BaseModel):
    password: str

class RoomJoin(BaseModel):
    room_id: str
    password: str
    username: str

class MessageSend(BaseModel):
    receiver: str
    content: str

class MessageResponse(BaseModel):
    sender: str
    content: str
    timestamp: datetime
    message_id: Optional[str] = None