from app.db.base import Base
from app.models.mixins import UUIDMixin, TimestampMixin


class BaseModel(UUIDMixin, TimestampMixin, Base):
    __abstract__ = True