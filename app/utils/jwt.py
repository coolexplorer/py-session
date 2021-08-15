import jwt

from config import config


settings: config.Settings = config.get_settings()

def decode(token: str) -> dict:
    return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])