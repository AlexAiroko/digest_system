from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.news import SNews
from app.dao.cluster_news import ClusterNewsDAO
from app.database.database import get_session


router = APIRouter(prefix="/clusters", tags=["clusters"])


@router.get("/{cluster_id}/news")
async def get_cluster_news(
    cluster_id: UUID,
    session: AsyncSession = Depends(get_session)
) -> list[SNews]:
    cluster_news_dao = ClusterNewsDAO(session)
    news = await cluster_news_dao.get_all_news_by_cluster_id(cluster_id)
    return [SNews.model_validate(n) for n in news]
