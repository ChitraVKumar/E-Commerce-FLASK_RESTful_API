# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be empty!')
    parser.add_argument('store_id', type=int, required=True, help='Every item needs a store id!')

    @jwt_required()
    def get(self, name):
        # item = next(filter(lambda x: x['name']==name, items), None)
        # return {'item': item}, 200 if item else 404
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found!'}, 404


    def post(self, name):
        # if next(filter(lambda x: x['name']==name, items), None):    # filter(func, sequenec) checks if the item already exists
        if ItemModel.find_by_name(name):
            return {"message": "An item with name {} already exists".format(name)}, 400
        
        data = Item.parser.parse_args()
        # item = ItemModel(name, data['price'], data['store_id'])
        item = ItemModel(name, **data)

        try:
            # item.insert()
            item.save_to_db()
        except:
            return {"message": "An error occured inserting the item."}, 500
        return item.json(), 201

    def delete(self, name):
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()
        
        # return {'message': 'Item deleted'}
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}
    
    def put(self, name):
        data = Item.parser.parse_args()

        # item = next(filter(lambda x: x['name']==name, items), None)
        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])

        if item is None:
            # try:
            #     updated_item.insert()
            # except:
            #     return {'message': "An error has occured while inserting an item"}, 500
            # item = ItemModel(name, data['price'], data['store_id'])
            item = ItemModel(name, **data)
            # items.append(item)
        else:
            # item.update(data)
            # try:
            #     updated_item.update()
            # except:
            #     return {'message': "An error has occured while updating an item"}, 500
            item.price = data['price']
        item.save_to_db()
        # return updated_item.json()
        return item.json()


class ItemList(Resource):
    def get(self):
        
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []

        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})

        # connection.close()
        
        # return {'items': items}
        return {'items': [item.json() for item in ItemModel.query.all()]}
