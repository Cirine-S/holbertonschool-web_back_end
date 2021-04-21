#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self):
        """ creates engine """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ saves a new user to the database """
        user = User()
        user.email = email
        user.hashed_password = hashed_password
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Description: Find a user by keyword argument
        Args:
            keyword argument([dict]): [user Input]
        Return:
            user instance if user exist or raise an Error
        """

        try:
            searched_user = self.__session.query(
                User).filter_by(**kwargs).first()
        except InvalidRequestError:
            raise InvalidRequestError
        except AttributeError:
            raise NoResultFound
        return searched_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user

        Args:
            user_id (int): [the id of the user to update]

        Raises:
            ValueError: [if a passed argument doesn't correspond to user attrs]
        """
        try:
            self._session.query(User).filter(
                User.id == user_id).update(kwargs)
        except ValueError:
            raise ValueError
