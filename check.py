
from data.db_session import SqlAlchemyBase
from data.users import User
from data.pupels_group_rus import Rus
from data.pupel_example import Pupel
from flask import Flask, render_template, request
from data.users import User
from data.db_session import create_session


db_sess = create_session()
user = db_sess.query(User).all()
for i in user:
    print(i)
