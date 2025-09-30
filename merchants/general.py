from . import *

class General(Merchant):
    name = "General Store"
    open = True
    listings = [
        Listing(
            item=items.lures.Crankbait,
            price=3
        )
    ]
