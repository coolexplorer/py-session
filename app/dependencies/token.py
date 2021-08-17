import requests
from fastapi import APIRouter, Header, Depends, status, HTTPException

from config import config
from const.url import *
from utils.url import *

import utils.jwt as jwt_util


async def validate_token(authorization: str = Header(...), settings: config.Settings = Depends(config.get_settings)):
    headers_dict = { "Accept-Encoding": "application/json" }
    
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


async def get_token(authorization: str = Header(...)) -> str:
    tokens = authorization.split(' ')
    return tokens[1]


async def get_session_id(token: str = Depends(get_token)) -> str:
    payload = jwt_util.decode(token)
    return payload['session_id']