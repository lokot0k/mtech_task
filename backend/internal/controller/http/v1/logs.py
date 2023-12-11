import datetime
from typing import Any, List

from fastapi import APIRouter, Depends, Response

from internal.dto.log import BaseLog, LogFilter, LogInput, LogRead
from internal.service.log import LogService
from internal.usecase.utils.response import (
    HTTP_201_CREATED,
    HTTP_418_SOMETHING_IS_WRONG,
)

router = APIRouter()


@router.get('', response_model=List[LogRead])
async def read_logs(
    dto: LogFilter = Depends(),
    log_service: LogService = Depends(),
) -> Any:
    # if there's no parameter, fill default value
    dto.date_to = dto.date_to or datetime.datetime.now()
    return await log_service.get_log_read(dto)


@router.post('', responses={
    201: {'description': 'Log was saved'},
    418: {'description': 'Something went wrong'},
},
)
async def create_log(
    res: Response,
    input_log_str: LogInput,
    log_service: LogService = Depends(),
) -> Any:
    res.status_code = 418
    response = HTTP_418_SOMETHING_IS_WRONG
    try:
        ip, method, uri, status_code = input_log_str.log.split()
        dto = BaseLog(ip=ip, method=method, uri=uri, status_code=status_code)
        await log_service.create(dto)
        res.status_code = 201
        response = HTTP_201_CREATED
    finally:
        return response
