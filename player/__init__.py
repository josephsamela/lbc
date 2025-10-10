from db import PlayerModel

from .inventory import InventoryManager
from .experience import ExperienceManager
from .journal import JournalManager

class Player:
    def __init__(self, username, password=None, session_token=None, session_expiration=None):

        if self.username_exists(username):
            # Look-up player by username.
            self._record = PlayerModel.get(username=username)
        else:
            # If they don't exist, create a new player.
            self._record, created = PlayerModel.get_or_create(
                username=username,
                password=password,
                session_token=session_token,
                session_expiration=session_expiration
            )

        self.inventory = InventoryManager(self)
        self.experience = ExperienceManager(self)
        self.journal = JournalManager(self)

    @property
    def name(self):
        if hasattr(self, 'username'):
            return self.username.title()

    def username_exists(self, username):
        '''
        Check if player with this username exists.
        '''
        if PlayerModel.get_or_none(username=username):
            return True
        return False

    def session_exists(self, session_token):
        '''
        Check if player with this session_token exists.
        '''
        if PlayerModel.get_or_none(session_token=session_token):
            return True
        return False   
