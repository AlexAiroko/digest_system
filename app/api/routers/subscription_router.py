from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.subscription import SSubscription, SSubscriptionCreate
from app.dao.subscription import SubscriptionDAO
from app.database.database import get_session
from app.utils.admin.dependencies import get_admin


router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])


@router.get("/", dependencies=[Depends(get_admin)])
async def get_all_subscriptions(
    session: AsyncSession = Depends(get_session)
) -> list[SSubscription]:
    subscription_dao = SubscriptionDAO(session)
    subscriptions = await subscription_dao.get_all()
    return [SSubscription.model_validate(sub) for sub in subscriptions]


@router.post("/")
async def add_subscription(
    data: SSubscriptionCreate,
    session: AsyncSession = Depends(get_session)
):
    dao = SubscriptionDAO(session)
    
    subscription = await dao.create(**data.model_dump())
    
    await session.commit()
    await session.refresh(subscription)
    
    return SSubscription.model_validate(subscription)
