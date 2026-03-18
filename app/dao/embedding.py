from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.embedding import Embedding


class EmbeddingDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Embedding)

    async def get_by_news_id(self, news_id: int):
        return self.get_one_or_none(news_id=news_id)
