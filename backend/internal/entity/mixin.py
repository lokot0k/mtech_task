import sqlalchemy as sa
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class TimestampMixin(object):

    created = sa.Column(
        sa.DateTime,
        default=sa.func.now(),
    )
