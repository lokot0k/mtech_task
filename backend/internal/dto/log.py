import uuid
from dataclasses import dataclass
from datetime import datetime

from fastapi import Query
from pydantic import AnyHttpUrl, BaseModel, IPvAnyAddress


class BaseLog(BaseModel):
    ip: IPvAnyAddress
    method: str
    uri: AnyHttpUrl
    status_code: int

    class Config(object):
        orm_mode = True


class LogRead(BaseModel):
    id: uuid.UUID
    created: datetime
    log: BaseLog

    class Config(object):
        orm_mode = True


class LogInput(BaseModel):
    log_str: str


@dataclass
class LogFilter(object):
    date_from: datetime = Query(datetime.fromtimestamp(0))
    date_to: datetime | None = Query(None)
