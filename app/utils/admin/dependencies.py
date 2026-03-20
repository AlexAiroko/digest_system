from fastapi import Depends

from app.database.models.user import User, UserRole
from app.exceptions import NotAdminException
from app.utils.auth.dependencies import get_current_user


def get_admin(user: User = Depends(get_current_user)) -> User:
    if user.role != UserRole.ADMIN:
        raise NotAdminException
    return user
