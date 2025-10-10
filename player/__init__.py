from db import PlayerModel

from .inventory import InventoryManager
from .experience import ExperienceManager
from .journal import JournalManager

class Player:
    def __init__(self, username=None, password=None, session_token=None, session_expiration=None):

        if session_token and self.session_exists(session_token):
            # Look-up player by session.
            self._record = PlayerModel.get(session_token=session_token)
        elif username and self.username_exists(username):
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
        return self._record.username.title()

    @staticmethod
    def username_exists(username):
        '''
        Check if player with this username exists.
        '''
        if PlayerModel.get_or_none(username=username):
            return True
        return False

    @staticmethod
    def session_exists(session_token):
        '''
        Check if player with this session_token exists.
        '''
        if PlayerModel.get_or_none(session_token=session_token):
            return True
        return False   
