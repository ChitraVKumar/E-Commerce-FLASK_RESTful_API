from ast import parse
from email import parser
from email.parser import Parser
from typing_extensions import Required
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from collections.abc import Mapping

from security import authenticate, identity

app = Flask(__name__)   # CReated an object of the class Flask with a unique name
app.secret_key = 'jskdsjdjmxkms'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be empty!')

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name']==name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name']==name, items), None):    # filter(func, sequenec)
            return {"message": "An item with name {} already exists".format(name)}, 400
        
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}
    
    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name']==name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug= True)



# stores = [
#     {
#         'name': 'CVK Electroics', 
#         'items': [
#             {
#             'name': 'TV', 
#             'price': 155.99
#             }
#         ]
#     }
# ]


# @app.route('/')
# def home():
#     return render_template('index.html')

# # POST /store data: {name:}
# @app.route('/store', methods=['POST'])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         'name': request_data['name'],
#         'items': []
#     }
#     stores.append(new_store)
#     return jsonify(new_store)

# # GET /store/<string:name>
# @app.route('/store/<string:name>') # default method is GET for browser
# def get_store(name):
#     # Iterate over stores 
#     # IF the store name matches, return it
#     # Else if none matches, return error message
#     for store in stores:
#         if store['name'] == name:
#             return jsonify(store)
#     return jsonify({'message': 'Store not Found!'})


# # GET /store
# @app.route('/store/') # default method is GET for browser
# def get_stores():
#     return jsonify({'stores': stores})

# # POST /store/<string:name>/item {name:, price:}
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_item_in_store(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store['name'] == name:
            
#             new_item = {
#                 'name': request_data['name'],
#                 'price': request_data['price']
#             }
#             store['items'].append(new_item)
#             return jsonify(store)
#     return jsonify({'message': 'Store Not Found!'})

# # GET /store/<string:name>/item
# @app.route('/store/<string:name>/item')
# def get_items_in_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify({'items': store['items']})
#     return jsonify({'message': 'Items not Found in the store!'})


# app.run(port=5000)