from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class SSubscription(BaseModel):
    id: UUID
    name: str
    token_limit: int
    requests_per_day: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SSubscriptionCreate(BaseModel):
    name: str
    token_limit: int
    requests_per_day: int

    model_config = ConfigDict(from_attributes=True)
