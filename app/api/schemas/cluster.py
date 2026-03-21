from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class SCluster(BaseModel):
    id: UUID
    digest_id: UUID
    title: str
    summary_text: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
