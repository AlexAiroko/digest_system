from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.cluster import Cluster


class ClusterDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Cluster)

