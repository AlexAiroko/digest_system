from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class SFavoriteDigest(BaseModel):
    id: UUID
    user_id: UUID
    digest_id: UUID
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
