from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.channel import STelegramChannel
from app.dao.channel import TelegramChannelDAO
from app.dao.user_channel import UserTelegramChannelDAO
from app.database.database import get_session
from app.database.models.user import User
from app.utils.admin.dependencies import get_admin
from app.utils.auth.dependencies import get_current_user


router = APIRouter(prefix="/channels", tags=["channels"])


@router.get("/channels")
async def get_user_channels(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
) -> list[STelegramChannel]:
    user_channel_dao = UserTelegramChannelDAO(session)
    channels = await user_channel_dao.get_user_channels(user.id)
    return [STelegramChannel.model_validate(channel) for channel in channels]


@router.post("/channels")
async def add_user_channel():
    # 1) Сделать проверку на наличие данного канала в бд
    # 2) Если нет, то достать информацию о нем и записать в бд, 
    #    а после создать запись в many-to-many таблице user_telegram_channel
    # 3) Вернуть сообщение об успехе, если такой канал существует и был добавлен
    pass


@router.delete("/channels/{channel_id}")
async def delete_user_channel(
    channel_id: UUID,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
) -> STelegramChannel:
    user_channel_dao = UserTelegramChannelDAO(session)
    deleted_channel = await user_channel_dao.delete(user_id=user.id, channel_id=channel_id)
    await session.commit()
    return STelegramChannel.model_validate(deleted_channel)


@router.get("/channels/all", dependencies=[Depends(get_admin)])
async def get_all_channels(
    session: AsyncSession = Depends(get_session)
) -> list[STelegramChannel]:
    channel_dao = TelegramChannelDAO(session)
    channels = await channel_dao.get_all()
    return [STelegramChannel.model_validate(channel) for channel in channels]
