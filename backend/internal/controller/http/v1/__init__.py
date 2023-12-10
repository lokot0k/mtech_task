from fastapi import APIRouter

from . import health, logs

router = APIRouter()
router.include_router(
    logs.router,
    prefix='/data',
    tags=['logs'],
)
router.include_router(
    health.router,
    prefix='/health',
    tags=['health'],
)
