from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class SNews(BaseModel):
    id: UUID
    channel_id: UUID
    telegram_message_id: int
    text: str
    published_at: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
