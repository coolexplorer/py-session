import logging

from fastapi import APIRouter
from fastapi_versioning import version

import schemas.BaseResponse as baseResponseSchema


logger = logging.getLogger(__name__)
router = APIRouter(tags=['root'])


@router.get('/ping')
@version(1)
async def pong():
    return baseResponseSchema.BaseResponse(result=True)