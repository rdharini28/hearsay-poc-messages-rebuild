
from datetime import datetime
from flask import Flask

class Message:
    def __init__(self, id:int, name: str, status: str, time: datetime, text: str):
        self.id = id
        self.name = name
        self.status = status
        self.time = time
        self.text = text

    def __repr__(self):
        return f"<Message {self.id}>"

    def __eq__(self, other):
        if not isinstance(other, Message):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)

    def __gt__(self, other):
        if self.time is None:
            return False
        if other.time is None:
            return True
        return self.time > other.time
