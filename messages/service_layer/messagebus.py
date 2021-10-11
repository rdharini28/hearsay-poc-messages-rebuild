
from messages.service_layer import unit_of_work

class MessageBus:
    def __init__(
        self,
        uow: unit_of_work.AbstractUnitOfWork,
    ):
        self.uow = uow