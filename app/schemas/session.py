from pydantic import BaseModel

class SessionBase(BaseModel):
    email: str
    data: dict

class SessionIn(SessionBase):
    expired_time: str
    expired_time_unit: str
    pass

class SessionOut(SessionBase):
    pass