from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.embedding_projection import EmbeddingProjection


class EmbeddingProjectionDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, EmbeddingProjection)
