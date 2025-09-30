from db import *
import items

class MerchantModel(Base):
    class Meta:
        db_table = 'merchants'
    name = CharField(unique=True)

class Merchant(Record):
    _model = MerchantModel

class Listing:
    def __init__(self, item, price):
        self.item = item
        self.price = price
