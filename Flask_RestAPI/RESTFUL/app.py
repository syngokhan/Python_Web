from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "gokhan"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

### jwt_required --> /auth --> header -> Authorization - application/json -- > Body -> json {"username" : "gokhan", "password" :"asd"}
### Then if we selected one condition for request , We must do it--> header Authorization - token values

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def get(self,name):
        # """For the status of the list, we save the list with next, it takes the first value"""
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self,name):

        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": "An item with name '{}' already exists.".format(name)}, 400

        # Headers Content-Type - application/json -- > body --> raw  -- > { "price" : 15.99 }
        #### data = request.get_json()

        data = Item.parser.parse_args()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x : x["name"] != name, items))
        return {"message" : "Item deleted"}

    def put(self,name):

        #data = request.get_json()
        data = Item.parser.parse_args()
        print(data)
        item = next(filter(lambda x : x["name"] == name,items),None)
        if item is None:
            item = {"name" : name,"price" : data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):

    def get(self):
        return {"items": items}

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

if __name__ == "__main__":
    app.run(debug=True)
