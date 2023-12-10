from typing import Sequence

from fastapi import Depends
from pytorm.repository import InjectRepository
from sqlalchemy.ext.asyncio import AsyncSession

from internal.dto.log import BaseLog, LogFilter, LogRead
from internal.entity.log import Log
from internal.usecase.utils import get_session


class LogService(object):

    def __init__(
        self, session: AsyncSession = Depends(get_session),
    ) -> None:
        self.repository = InjectRepository(Log, session)

    async def create(self, dto: BaseLog) -> Log:
        dto.ip = str(dto.ip)
        log = self.repository.create(**dto.dict())
        return await self.repository.save(log)

    async def find(self, dto: LogFilter) -> Sequence[Log]:
        return await self.repository.find(
            Log.created.between(dto.date_from, dto.date_to),
        )

    # flake8: noqa
    async def get_log_read(self, dto: LogFilter) -> list[LogRead]:
        logs = await self.find(dto)
        base_logs = [BaseLog.from_orm(log) for log in logs]
        read_logs = [LogRead(log=base_log, **log.__dict__) for base_log, log in
                     zip(base_logs, logs)]
        return read_logs
