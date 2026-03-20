from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.query_history import SQueryHistory
from app.api.schemas.subscription import SSubscription
from app.api.schemas.user import SUserProfile
from app.dao.query_history import QueryHistoryDAO
from app.dao.subscription import SubscriptionDAO
from app.database.database import get_session
from app.database.models.user import User
from app.utils.auth.dependencies import get_current_user


router = APIRouter(prefix="/user/me", tags=["users"])


@router.get("/")
async def get_me(user: User = Depends(get_current_user)) -> SUserProfile:
    return SUserProfile.model_validate(user)


@router.get("/subscription")
async def get_user_subscription(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
) -> SSubscription:
    subscription_dao = SubscriptionDAO(session) 
    subscription = await subscription_dao.get_by_id(user.subscription_id)
    return SSubscription.model_validate(subscription)


@router.get("/history")
async def get_user_history(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
) -> list[SQueryHistory]:
    query_history_dao = QueryHistoryDAO(session)
    queries = await query_history_dao.get_all(user_id=user.id)
    return [SQueryHistory.model_validate(query) for query in queries]
