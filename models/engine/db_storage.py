#!/usr/bin/python3
"""DB storage class"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.base_model import Base
from models import stringtemplates as ENV
import models

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """SQLAlchemy DB"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Class constructor"""

        user = getenv(ENV.HBNB_MYSQL_USER)
        pwd = getenv(ENV.HBNB_MYSQL_PWD)
        host = getenv(ENV.HBNB_MYSQL_HOST)
        db = getenv(ENV.HBNB_MYSQL_DB)
        env = getenv(ENV.HBNB_ENV, 'none')

        connection = f'mysql+mysqldb://{user:s}:{pwd:s}@{host:s}/{db:s}'
        self.__engine = create_engine(connection, pool_pre_ping=True)

        if env == ENV.TEST:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None) -> dict:
        """Query current DB session"""
        database = {}

        if cls != '':
            objs = self.__session.query(models.classes[cls]).all()
            for obj in objs:
                key = f'{obj.__class__.__name__}.{obj.id}'
                database[key] = obj
            return database
        else:
            for key, value in models.classes.items():
                if key != 'BaseModel':
                    objs = self.__session.query(value).all()
                    if len(objs):
                        for obj in objs:
                            k = f'{obj.__class__.__name__}.{obj.id}'
                            database[k] = obj
            return database

    def new(self, obj) -> None:
        """Add a new object to DB"""
        self.__session.add(obj)

    def save(self):
        """Commit all current DB changes"""
        self.__session.commit()

    def delete(self, obj=None) -> None:
        """Delete current DB session"""
        if obj is None:
            return
        self.__session.delete(obj)

    def reload(self) -> None:
        """Commit all current DB changes and session"""
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self) -> None:
        """"Close the working SQLAlchemy session."""
        self.__session.close()

    def get(self, cls, id):
        """Retrieves an object based on class name and id"""
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if(value.id == id):
                return value

        return None

    def count(self, cls=None):
        """Returns the count of all objects in the storage"""
        all_cls = classes.values()
        if not cls:
            count = 0
            for clas in all_cls:
                count += len(models.storage.all(clas).values())
            else:
                count = len(models.storage.all(cls).values())
            return count
