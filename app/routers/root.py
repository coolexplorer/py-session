import logging

from fastapi import APIRouter, Depends
from fastapi_versioning import version

from dependencies.token import validate_token
import schemas.base_response as baseResponseSchema


logger = logging.getLogger(__name__)
router = APIRouter(
                tags=['root'],
                dependencies=[Depends(validate_token)]
                )


@router.get('/ping')
@version(1)
async def pong():
    return baseResponseSchema.BaseResponse(result=True)