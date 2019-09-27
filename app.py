from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'obsidian'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth
# when we call /auth we send it a username and a password
# then the JWT extension gets that username and password
# then JWT sends it to the authenticate() function we created
# the authenticate function then gives us back a JWT (JSON Web Token)
# JWT then calls the identity() function to get the correct user_id it gets the correct user
# if it does get the correct user then the user is Authenticated.


@app.route('/')
def hello_world():
    return 'Hello World!'


items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        # the get and post in the same class method must have the same methods
        # this way we can get access to the same endpoint by just changing the HTTP verb (get or post)
        item = next(filter(lambda x: x['name'] == name, items), None)
        # this uses a filter function with the params (iteration lambda, list filtering though
        # the 'next' function the filter function returns the first object with the name == 'name'
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            # if the item already exists 'is not none' this code returns the message below.
            return {'message': f'An Item with name {name} already exists'}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)  # we add the above dictionary to the list items = []
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item Deleted'}


class ItemList(Resource):
    def get(self):
        return {'Items': items}


api.add_resource(Item, '/item/<string:name>')  # /item
api.add_resource(ItemList, '/items')
if __name__ == '__main__':
    app.run(debug=True)
