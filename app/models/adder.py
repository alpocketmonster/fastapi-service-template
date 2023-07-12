from pydantic import BaseModel


class AdderRequest(BaseModel):
    x: int
    y: int


class AdderResponse(BaseModel):
    sum: int
