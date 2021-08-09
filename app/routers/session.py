import logging
from os import stat

from fastapi import APIRouter, Header, Depends, status, HTTPException
from fastapi_versioning import version
import requests

from config import config
from const.url import *
from utils.url import *


logger = logging.getLogger(__name__)
router = APIRouter(tags=['session'])


headers_dict = { "Accept-Encoding": "application/json" }
async def validate_token(authorization: str = Header(...), settings: config.Settings = Depends(config.get_setting)):
    if authorization:
        headers_dict["Authorization"] = authorization

        validate_url = create_url(HTTP_PROTOCOL, settings.auth_address, 1, TOKEN_VALIDATE_PATH)
        response = requests.get(validate_url, headers=headers_dict)
        
        if response.status_code != status.HTTP_200_OK or response.json()['result'] == False:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token is not valid'
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token is not valid'
        )


@router.post('/session')
@version(1)
async def create_session(token_valid: bool = Depends(validate_token), settings : config.Settings = Depends(config.get_setting)):    
    return 'session created'


@router.get('/session')
@version(1)
async def get_session():
    pass

@router.put('/session')
@version(1)
async def update_session():
    pass

@router.put('/session/touch')
@version(1)
async def touch_session():
    pass