import logging
from os import stat

from fastapi import APIRouter, Header, Depends, status, HTTPException
from fastapi_versioning import version
from requests.api import get

from config import config
from const.url import *
from dependencies.token import validate_token, get_token
import schemas.session as sessionSchema
from redis.redis_account import redis_account
from utils.url import *
import utils.jwt as jwt_util


logger = logging.getLogger(__name__)
router = APIRouter(
                tags=['session'],
                dependencies=[Depends(validate_token)]
                )


@router.post('/session')
@version(1)
async def create_session(sessionIn: sessionSchema.SessionIn, token: str = Depends(get_token)):
    payload = jwt_util.decode(token)
    session_id = payload['session_id']
    response = await redis_account.session_crud.set_dict(session_id, sessionIn.data)
    return f'session created : key - {session_id}, data - {sessionIn.data}'

@router.get('/session')
@version(1)
async def get_session(settings : config.Settings = Depends(config.get_settings)):
    pass

@router.put('/session')
@version(1)
async def update_session(settings : config.Settings = Depends(config.get_settings)):
    pass

@router.put('/session/touch')
@version(1)
async def touch_session(settings : config.Settings = Depends(config.get_settings)):
    pass