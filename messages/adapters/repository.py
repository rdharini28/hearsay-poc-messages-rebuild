
# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from messages.domain import model
from messages.service_layer import unit_of_work


from messages import config
from messages.adapters import repository

class AbstractRepository(abc.ABC):
    
    @abc.abstractmethod
    def add(self, message: model.Message):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, reference) -> model.Message:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
         self.session = session

    def add(self, message):
        self.session.add(message)

    def get(self, reference):
        return self.session.query(model.Message).filter_by(reference=reference).one()
