import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item,ItemList
from resources.user import UserRegister,User
from resources.store import Store,StoreList
from security import authenticate, identity

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "gokhan"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

api.add_resource(UserRegister,"/register")
api.add_resource(User,"/user/<int:user_id>")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
