from pydantic import BaseModel

class SessionBase(BaseModel):
    data: dict

class SessionIn(SessionBase):
    expired_time: str
    expired_time_unit: str
    pass

class SessionOut(SessionBase):
    pass