from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)   # CReated an object of the class Flask with a unique name 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jskdsjdjmxkms'
api = Api(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':  # The main helps in running the below statement only when app.py is called not when importing the app.py file
    from db import db
    db.init_app(app)
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