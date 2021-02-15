from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True, help="This field cant be blank")
    parser.add_argument("store_id", type=float, required=True, help="This field cant be blank")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):

        # check if the item already exists
        if ItemModel.find_by_name(name):
            return {'message': 'Item with name {0} already exists.'.format(name)}, 400

        # need to assume in testing the type and body is JSON
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting this item"}, 500 #Internal Server Error

        return item.json(), 201

    def delete(self, name):

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return{'message': 'Item not found'}, 400

    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        # create the item if missing, otherwise update it
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json


class ItemList(Resource):

    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
