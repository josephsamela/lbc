import datetime

from peewee import *

db = SqliteDatabase('db.sqlite')
db.connect()

class Base(Model):
    class Meta:
        database = db

class ItemModel(Base):
    class Meta:
        db_table = 'items'
    name = CharField(unique=True)
    category = CharField()

class PlayerModel(Base):
    class Meta:
        db_table = 'players'
    username = CharField(unique=True)
    password = CharField()
    balance = IntegerField(default=0, constraints=[Check('balance >= 0')])
    admin = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now())
    session_token = CharField(unique=True)
    session_expiration = DateTimeField()

class ExperienceModel(Base):
    class Meta:
        db_table = 'experience'
    player = ForeignKeyField(PlayerModel)
    skill = CharField()
    quantity = IntegerField(default=1, constraints=[Check('quantity >= 0')])

class InventoryModel(Base):
    class Meta:
        db_table = 'inventory'
    player = ForeignKeyField(PlayerModel)
    item = ForeignKeyField(ItemModel)
    quantity = IntegerField(default=0, constraints=[Check('quantity >= 0')])
