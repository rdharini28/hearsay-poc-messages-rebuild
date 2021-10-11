import inspect
from typing import Callable
from messages.adapters import orm
from messages.service_layer import handlers, unit_of_work, messagebus

def bootstrap(
    start_orm: bool = True,
    uow: unit_of_work.AbstractUnitOfWork = unit_of_work.SqlAlchemyUnitOfWork()):

    if start_orm:
        orm.start_mappers()

    dependencies = {"uow": uow }
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies)
            for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }

    # Need to add event, event handlers, message bus etc.

    return messagebus.MessageBus(
        uow=uow,
    )

def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **deps)