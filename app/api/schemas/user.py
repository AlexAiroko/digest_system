from pydantic import BaseModel
from uuid import UUID


class SUserProfile(BaseModel):
    id: UUID
    telegram_id: int
    username: str | None
    first_name: str | None
    token_balance: int

    class Config:
        from_attributes = True
