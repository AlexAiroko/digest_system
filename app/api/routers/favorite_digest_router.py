from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.digest import SDigest
from app.dao.favorite_digest import FavoriteDigestDAO
from app.database.database import get_session
from app.database.models.user import User
from app.utils.auth.dependencies import get_current_user


router = APIRouter(prefix="/digests/favorites", tags=["favorites"])


@router.get("/")
async def get_user_favorites(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
) -> list[SDigest]:
    favorite_dao = FavoriteDigestDAO(session)
    digests = await favorite_dao.get_user_favorite_digests(user.id)
    return [SDigest.model_validate(digest) for digest in digests]


@router.delete("/{favorite_id}")
async def delete_user_favorite_digest(
    favorite_id: UUID,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    favorite_dao = FavoriteDigestDAO(session)
    deleted_favorite = await favorite_dao.delete(user_id=user.id, id=favorite_id)
    await session.commit()
    return deleted_favorite
