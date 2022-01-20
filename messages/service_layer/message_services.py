import datetime
import logging

from messages.service_layer import unit_of_work
from messages.domain import model


def send_message(
    id: int, name: str, status: str, time: datetime, text: str,
    uow: unit_of_work.AbstractUnitOfWork
):
    logging.info("About to save message")
    # for now, just save the message. 
    with uow:
        uow.messages.add(model.Message(id, name, status, time, text))
        uow.commit()
