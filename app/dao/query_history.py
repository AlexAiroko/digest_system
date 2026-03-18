from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.query_history import QueryHistory


class QueryHistoryDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, QueryHistory)
