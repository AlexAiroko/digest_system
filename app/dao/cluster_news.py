from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.cluster_news import ClusterNews


class ClusterNewsDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ClusterNews)
