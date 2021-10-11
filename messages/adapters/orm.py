
import logging
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    event,
)
from sqlalchemy.orm import mapper, relationship

logger = logging.getLogger(__name__)

metadata = MetaData()

messages = Table(
    "messages",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("status", String(255), nullable=False),
    Column("time", Date, nullable=False),
    Column("text", String(255), nullable=True)
)

def start_mappers():
    #TODO: Add mappers for objects in domaint that need them
    pass
