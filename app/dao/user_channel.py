from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.database.models.channel import TelegramChannel
from app.database.models.user_channel import UserTelegramChannel


class UserTelegramChannelDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, UserTelegramChannel)
    
    async def get_user_channels(self, user_id: UUID | str):
        stmt = (
            select(TelegramChannel)
            .join(UserTelegramChannel, UserTelegramChannel.channel_id == TelegramChannel.id)
            .where(UserTelegramChannel.user_id == user_id)
        )
        
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def delete(self, **filter_by):
    # фильтры должны включать и user_id, и channel_id
        return await super().delete(**filter_by)