import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship
from sqlalchemy import (Integer, String, Column,
                        create_engine, ForeignKeyConstraint, UniqueConstraint)

NAME_DB = 'user_info.db'
Base = declarative_base()
abs_path_file = os.path.abspath(__file__)[:-len('models.__inti__.py')]
engine = create_engine(F'sqlite:///{NAME_DB}' + '?check_same_thread=False')
session = Session(bind=engine)


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    params = relationship('ParametrModel', back_populates='user', cascade="all, delete-orphan")


class ParametrModel(Base):
    __tablename__ = 'parametrs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    value = Column(String, nullable=False)

    user_id = Column(Integer, nullable=False)
    user = relationship('UserModel', back_populates='params')

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id']),
        UniqueConstraint('type', 'name')
    )

    def __str__(self):
        return f'name={self.name}, type={self.type}, value={self.value}'


def init_db() -> None:
    print('init data base')
    if os.path.exists(NAME_DB):
        os.remove(NAME_DB)
    Base.metadata.create_all(engine)
