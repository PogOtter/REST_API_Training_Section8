from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity as identity_function
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from datetime import timedelta

app = Flask(__name__)
# this key would need to be long, random, and not exposed to users
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'otter'
api = Api(app)


# customize JWT auth response, include user_id in response body
jwt = JWT(app, authenticate, identity_function) #/auth

# no longer have to do the decorator to tag the path in this context, also dont have to jsonify returns!
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Otter
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# prevent auto-execution of app upon import
if __name__ == '__main__':
    app.run(port=5000, debug=True)
