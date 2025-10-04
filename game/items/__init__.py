import re

from db import Record, ItemModel

class Item(Record):
    _model = ItemModel
   
    states = []
    state = None
    
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

    def __init__(self):

        # Some items have multiple "states". Basically multiple versions of the same item.
        # "Raw Salmon", "Cooked Salmon" & "Burnt Salmon" are all different states of "Salmon".
        # If an item has states but doesn't have state assigned, set state "default" first state.
        if self.states and not self.state:

            self.state = self.states[0]

            for state in self.states:

                c = self.__class__
                n = c.__name__
                state_class = type(n, (c,), {'state': state})

                setattr(self, state.lower(), state_class)

                


