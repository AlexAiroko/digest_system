from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.favorite_digest import FavoriteDigest


class FavoriteDigestDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, FavoriteDigest)
