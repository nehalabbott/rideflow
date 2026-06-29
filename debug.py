from app.models import *
from app.db.base import Base

print(Base.metadata.tables.keys())