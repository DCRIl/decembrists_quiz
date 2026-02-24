import sqlalchemy
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class People(SqlAlchemyBase):
    __tablename__ = 'peoples'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    portrait = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = orm.relationship("Abouts", back_populates='people')