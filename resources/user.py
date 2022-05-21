import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser() # parser will parse through the JSON of the request make sure usernamne and password are there
    parser.add_argument('username', type = str, required= True, help = "This field cannot be blank")
    parser.add_argument('password', type = str, required= True, help = "This field cannot be blank")

    def post(self):
        data = UserRegister.parser.parse_args() # Parse the args using the User register parser which is going to expect username and password

        if UserModel.find_by_username(data['username']): # is not none
            return {"message": "A user with that name already exists!"}, 400

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data['username'], data['password'],))

        # connection.commit()
        # connection.close()
        # user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully!"}
    

