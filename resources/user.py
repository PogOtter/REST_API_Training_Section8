import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    # fetch the data provided, force user to provide correct data
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="This field cant be blank")
    parser.add_argument("password", type=str, required=True, help="This field cant be blank")

    def post(self):

        data = UserRegister.parser.parse_args()
        # check if username already exists
        if UserModel.find_by_username(data['username']):
            return {'message', "The username {0} already exists!".format(data['username'])}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully"}, 201