from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.cluster_news import ClusterNews
from app.database.models.news import News


class ClusterNewsDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ClusterNews)
    
    async def get_all_news_by_cluster_id(self, cluster_id: UUID | str):
        stmt = (
            select(News)
            .join(ClusterNews, ClusterNews.news_id == News.id)
            .where(ClusterNews.cluster_id == cluster_id)
            .order_by(News.published_at.desc())
        )
        
        result = await self.session.execute(stmt)
        return result.scalars().all()
