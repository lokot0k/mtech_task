import sqlalchemy as sa

from internal.entity.base import Base
from internal.entity.mixin import TimestampMixin


class Log(TimestampMixin, Base):
    ip = sa.Column(sa.Text(), nullable=False)
    method = sa.Column(sa.Text(), nullable=False)
    uri = sa.Column(sa.Text(), nullable=False)
    status_code = sa.Column(sa.Integer(), nullable=False)
