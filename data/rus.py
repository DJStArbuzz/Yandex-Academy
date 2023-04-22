import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class Rus(SqlAlchemyBase):
    __tablename__ = 'russian'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    data = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    people1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    people2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    people3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)