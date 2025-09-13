#!/usr/bin/python3
"""Database Storage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None
    cities = "relationship with class City\
            if State object is deleted delete linked City\
            name the reference of city to state as state"

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        # dialect+driver://username:password@host:port/database
        self.__engine = create_engine(f'mysql+mysqldb://\
                {user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        if os.getenv('HBNB_ENV'):
            print("drop tables")
            Base.metadata.drop_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        
        db_session = Session(bind=self.__engine, expire_on_commit=True)

    def all(self, cls=None):
        # query(self.__session, for cls.__class__.__name__)
        if cls is None:
            print("Query all classes")
        else:
            print("Query cls.__class__.__name__")
            return f"{cls.__class__.__name__}.{cls.id}"

    def new(self, obj):
        self.__session[obj.__class__.__name__] = obj

    def save(self, obj=None):
        """Commits changes of current db"""
        pass

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        pass

    def reload(self):
        """
        Create all tables in database"""
        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        # Base.metadata.create_all(engine)
        # create self.__session from self.__engine
        # use sessionmaker
        # expire_on_commit=False
        # scoped_session
