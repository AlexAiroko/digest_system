from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.digest import Digest
from app.database.models.favorite_digest import FavoriteDigest


class FavoriteDigestDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, FavoriteDigest)

    async def get_user_favorite_digests(self, user_id: UUID | str):
        stmt = (
            select(Digest)
            .join(FavoriteDigest, FavoriteDigest.digest_id == Digest.id)
            .where(FavoriteDigest.user_id == user_id)
        )
        
        result = await self.session.execute(stmt)
        return result.scalars().all()
