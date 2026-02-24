import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Abouts(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    people_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("peoples.id"))
    people = orm.relationship('People')