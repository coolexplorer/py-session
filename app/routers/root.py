import logging

from fastapi import APIRouter, Depends
from fastapi_versioning import version

from dependencies.token import validate_token
import schemas.base_response as base_response_schema


logger = logging.getLogger(__name__)
router = APIRouter(tags=['root'])


@router.get('/ping')
@version(1)
async def pong():
    return base_response_schema.BaseResponse(result=True)