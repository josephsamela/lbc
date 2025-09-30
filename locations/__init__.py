from db import *

class LocationModel(Base):
    class Meta:
        db_table = 'locations'
    name = CharField(unique=True)

class Location(Record):
    _model = LocationModel
