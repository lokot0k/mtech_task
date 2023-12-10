from fastapi import APIRouter

from internal.usecase.utils import SuccessfulResponse

router = APIRouter()


# special endpoint for checking accessibility of backend
@router.get('', responses=SuccessfulResponse.schema())
async def health() -> SuccessfulResponse:
    return SuccessfulResponse()
