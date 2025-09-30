import datetime

from db import *

class PlayerModel(Base):
    class Meta:
        db_table = 'players'
    username = CharField(unique=True)
    password = CharField()
    balance = IntegerField(default=0, constraints=[Check('balance >= 0')])
    admin = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now())

class Player(Record):
    _model = PlayerModel

    @property
    def inventory(self):
        return Inventory(self)

from .inventory import Inventory
