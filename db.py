import datetime
import inspect

from peewee import *

db = SqliteDatabase('db.sqlite')
db.connect()

class Base(Model):
    class Meta:
        database = db

class SkillModel(Base):
    class Meta:
        db_table = 'skills'
    name = CharField(unique=True)

class ItemModel(Base):
    class Meta:
        db_table = 'items'
    name = CharField(unique=True)

class PlayerModel(Base):
    class Meta:
        db_table = 'players'
    username = CharField(unique=True)
    password = CharField()
    balance = IntegerField(default=0, constraints=[Check('balance >= 0')])
    admin = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now())

class ExperienceModel(Base):
    class Meta:
        db_table = 'experience'
    player = ForeignKeyField(PlayerModel)
    skill = ForeignKeyField(SkillModel)
    quantity = IntegerField(default=0, constraints=[Check('quantity >= 0')])

class InventoryModel(Base):
    class Meta:
        db_table = 'inventory'
    player = ForeignKeyField(PlayerModel)
    item = ForeignKeyField(ItemModel)
    quantity = IntegerField(default=0, constraints=[Check('quantity >= 0')])

class GardenModel(Base):
    class Meta:
        db_table = 'gardens'

    name = CharField()
    player = ForeignKeyField(PlayerModel)
    seed = ForeignKeyField(ItemModel, null=True)
    planted_at = DateTimeField(null=True)

class Record:

    def __init__(self, *args, **kwargs):
        pass

    def _get_params(self, *args, **kwargs):
        # Build list of object attributes
        attrs = {}
        for a in dir(self):
            if not a.startswith('_'):
                attrs[a] = getattr(self, a)   
        attrs.update(kwargs)

        # Filter attribute to list of params
        params = {}
        for key, value in attrs.items():
            if key in self._model._meta.sorted_field_names:
                # Only pass attributes that correspond to model columns

                # Convience. If passed a class, instantiate it.
                if inspect.isclass(value):
                    value = value()

                # Convience. Replace objects with their _record handles.
                if hasattr(value, '_record'):    
                    params[key] = value._record

                else:
                    params[key] = value

        return params

    def _pre_init(self, *args, **kwargs):
        '''
        Code to run before subclass __init__
        '''
        if len(args) > 0:
            raise Exception(f'Keyword arguments required. {self.__class__.__name__} can accept kwargs: {self._model._meta.sorted_field_names}.')

        self._initializing = True

        # If table for this record model doesn't already exist, create it
        if not self._model._meta.database.table_exists(self._model._meta.table_name):
            self._model.create_table()

        params = self._get_params(*args, **kwargs)

        # try:
        #     self._record = self._model.get(**params)
        #     self.__dict__.update(self._record.__data__)
        # except Exception as e:
        #     pass


    def _post_init(self, *args, **kwargs):
        '''
        Code to run after subclass __init__
        '''
        params = self._get_params(*args, **kwargs)

        # Get or create record based on kwargs
        self._record, created = self._model.get_or_create(**params)

        # Add record fields to class as attributes
        self.__dict__.update(self._record.__data__)

        if hasattr(self, '_initializing'):
            delattr(self, '_initializing')

    def __setattr__(self, attr_name, attr_value):
        '''
        Write record attribute changes to database.
        '''
        if hasattr(attr_value, '_record'):
            attr_value = getattr(attr_value, '_record')

        self.__dict__[attr_name] = attr_value

        # Write object attr updates to db if...
        #    1. Object is initialized
        #    2. Updated attr is part of model
        if not hasattr(self, '_initializing') and attr_name in self._model._meta.sorted_field_names:
            setattr(self._record, attr_name, attr_value)
            self._record.save()

    def __init_subclass__(cls, **kwargs):
        '''
        Overwrite subclass __init__ to call methods before and after.

        _pre_init()     Runs before subclass __init__
        _post_init()    Runs after subclass __init__
        '''
        super().__init_subclass__(**kwargs)
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            self._pre_init(*args, **kwargs)
            original_init(self, *args, **kwargs)
            self._post_init(*args, **kwargs)

        cls.__init__ = new_init
