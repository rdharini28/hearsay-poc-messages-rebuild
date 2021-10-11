from messages.service_layer import unit_of_work

def get_message(message_id: int, uow: unit_of_work.SqlAlchemyUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM messages WHERE id = :message_id
            """,
            dict(message_id=message_id),
        )
    return [dict(r) for r in results]