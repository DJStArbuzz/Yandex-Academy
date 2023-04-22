import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class Example(SqlAlchemyBase, UserMixin):
    __tablename__ = 'example'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    math = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    russian = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chemistry = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    pe = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    it = sqlalchemy.Column(sqlalchemy.String, nullable=True)

