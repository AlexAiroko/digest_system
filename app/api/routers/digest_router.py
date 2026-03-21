import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.cluster import SCluster
from app.api.schemas.digest import SDigest
from app.dao.cluster import ClusterDAO
from app.dao.digest import DigestDAO
from app.database.database import get_session


router = APIRouter(prefix="/digests", tags=["digests"])


@router.post("/")
async def add_digest():
    # Нужен функционал с ML для лучшего понимания, как реализовать данный эндпоинт
    pass


@router.get("/")
async def get_digest_list():
    pass


@router.get("/{digest_id}")
async def get_digest_by_id(
    digest_id: uuid.UUID | str,
    session: AsyncSession = Depends(get_session)
) -> SDigest:
    digest_dao = DigestDAO(session)
    digest = await digest_dao.get_by_id(digest_id)
    return SDigest.model_validate(digest)


@router.get("/{digest_id}/audio")
async def get_digest_audio(
    digest_id: uuid.UUID | str,
    session: AsyncSession = Depends(get_session)
):
    digest_dao = DigestDAO(session)
    digest = await digest_dao.get_by_id(digest_id)
    audio_path = digest.audio_path
    #  TODO: доделать после добавления ML сервиса


@router.get("/{digest_id}/clusters")
async def get_clusters(
    digest_id: uuid.UUID | str,
    session: AsyncSession = Depends(get_session)
) -> list[SCluster]:
    cluster_dao = ClusterDAO(session)
    clusters = await cluster_dao.get_all(digest_id=digest_id)
    return [SCluster.model_validate(cluster) for cluster in clusters]
