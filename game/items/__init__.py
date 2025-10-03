import re

from db import Record, ItemModel

class Item(Record):
    _model = ItemModel

    state = None
    cookable = False

    @property
    def name(self):
        '''
        Return name of object class.

        Add space " " between words. "PinkSalmon" -> "Pink Salmon".
        '''
        pattern=r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))'
        replace=r'\1 '
        name=self.__class__.__name__
        return re.sub(pattern, replace, name)
