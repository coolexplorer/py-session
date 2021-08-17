import logging
from os import stat

from fastapi import APIRouter, Header, Depends, status, HTTPException
from fastapi_versioning import version
from requests.api import get
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from config import config
from const.url import *
from dependencies.token import validate_token, get_session_id
import schemas.session as session_schema
import schemas.base_response as base_response_schema
from redis.redis_account import redis_account
from utils.url import *


logger = logging.getLogger(__name__)
router = APIRouter(
                tags=['session'],
                dependencies=[Depends(validate_token)]
                )


@router.post('/session')
@version(1)
async def create_session(sessionIn: session_schema.SessionIn, session_id: str = Depends(get_session_id)):
    response = await redis_account.session_crud.set_dict(session_id, sessionIn.data)

    if response:
        return session_schema.SessionOut(data=sessionIn.data)
    else:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Redis set command failed."
        )


@router.get('/session')
@version(1)
async def get_session(session_id: str = Depends(get_session_id)):
    session_data = await redis_account.session_crud.get_all(session_id)
    if session_data:
        return session_schema.SessionOut(data=session_data)
    else:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Session data is not exist."
        )


@router.put('/session')
@version(1)
async def update_session(sessionIn: session_schema.SessionIn, session_id: str = Depends(get_session_id)):
    session_data = await redis_account.session_crud.get_all(session_id)
    
    if session_data:
        response = await redis_account.session_crud.set_dict(session_id, sessionIn.data)
        
        if response:
            return session_schema.SessionOut(data=sessionIn.data)
        else:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Redis set command failed."
            )
    else:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Session data is not exist."
        )


@router.put('/session/touch')
@version(1)
async def touch_session(session_id: str = Depends(get_session_id)):
    response = await redis_account.session_crud.touch(session_id)
    if response:
        return base_response_schema.BaseResponse(result=response)
    else:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Redis set command failed."
        )