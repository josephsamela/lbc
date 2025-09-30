from . import *

class Tackle(Merchant):
    name = "Bait & Tackle"
    open = True
    listings = [
        Listing(
            item=items.lures.Crankbait(),
            price=3
        ),
        Listing(
            item=items.lures.Popper(),
            price=3
        ),
        Listing(
            item=items.lures.Spinner(),
            price=3
        )
    ]
