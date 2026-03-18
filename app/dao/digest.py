from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.digest import Digest


class DigestDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Digest)
