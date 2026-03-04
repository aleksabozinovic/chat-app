from datetime import datetime, timedelta
from typing import Set, List, Dict, Optional
import secrets

class Room:
    def __init__(self, room_id: str, password_hash: str, max_users: int = 2):
        self.room_id = room_id
        self.password_hash = password_hash
        self.created_at = datetime.now()
        self.last_active = datetime.now()
        self.users: Set[str] = set()
        self.max_users = max_users
        self.message_history: List[Dict] = []

class Message:
    def __init__(self, content: bytes, recipient: str, ttl_seconds: int = 300):
        self.id = secrets.token_urlsafe(8)
        self.content = content
        self.recipient = recipient
        self.expires_at = datetime.now() + timedelta(minutes=5)

        def is_expired(self) -> bool:
            """Check if message has expired"""
            return datetime.now() > self.expires_at

class UserSession:
    def __init__(self, username: str, room_id: str, websocket):
        self.username = username
        self.room_id = room_id
        self.websocket = websocket
        self.connected_at = datetime.now()
        self.last_activity = datetime.now()

        def update_activity(self):
            """Call this when user sends/receives message"""
            self.last_activity = datetime.now()

        def is_idle(self, timeout_minutes: int = 30) -> bool:
            """Check if user has been idle too long"""
            idle_time = datetime.now() - self.last_activity
            return idle_time.total_seconds() > timeout_minutes * 60