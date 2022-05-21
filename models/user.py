import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod # to avoid hardcoding and using current class instead of self
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db') # develp a connection to a database file names data.db
        # cursor = connection.cursor()    # req to run the commands

        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,)) # parameters always a single value tuple
        # row = result.fetchone()
        # if row: # is not none
        #     #user = cls(row[0], row[1], row[2])
        #     user = cls(*row)    # using positional args instead of index positions as above
        # else:
        #     user = None

        # connection.close()
        # return user
        return cls.query.filter_by(username = username).first() #first usernameis the tablename second is the argument being passed. first() returns the first row in the table

    @classmethod # to avoid hardcoding and using current class instead of self
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db') # develp a connection to a database file names data.db
        # cursor = connection.cursor()    # req to run the commands

        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,)) # parameters always a single value tuple
        # row = result.fetchone()
        # if row: # is not none
        #     #user = cls(row[0], row[1], row[2])
        #     user = cls(*row)    # using positional args instead of index positions as above
        # else:
        #     user = None

        # connection.close()
        # return user
        return cls.query.filter_by(id = _id).first()