from crud.session import SessionCrud

class RedisAccount():
    def __init__(self, session_crud: SessionCrud = None) -> None:
        self.session_crud = session_crud
    
    def set_redis(self, session_crud: SessionCrud) -> None:
        self.session_crud = session_crud

redis_account = RedisAccount()
