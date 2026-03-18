from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.token_transaction import TokenTransaction


class TokenTransactionDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, TokenTransaction)
