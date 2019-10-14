from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()  # default code 200
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f'Store {name} already exists.'}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except SystemError:
            return {'message': 'An error occurred while creating the store'}, 500 #internal server error

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()


class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
