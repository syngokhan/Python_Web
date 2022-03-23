from flask import Flask,jsonify,request,render_template

app = Flask(__name__)
stores = [
    {
        "name" : "My Wonderful Store",
        "items" : [
            {
                "name" : "My Item",
                "price" : 15.99
            }
        ]
    }
]

#always uses "" -- > json

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/store",methods = ["POST"])
def create_store():

    request_data = request.get_json()
    print("Create Store :", request_data)
    # Bunu kendimiz yazıyoruz !!
    # Headers Content-type -- application/json --> Then Body Raw
    #Create Store : {'name': 'Another Store'}
    new_store = {
        "name" : request_data["name"],
        "items" : []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message" : "store not found"})

@app.route("/store")
def get_stores():

    #print(type({"stores" : stores}))     #< class 'dict'>
    #print(type(jsonify({"stores" : stores})))     #<class 'flask.wrappers.Response'>
    return jsonify({"stores" : stores})

@app.route("/store/<string:name>/item",methods = ["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    print("Create Item In Store :", request_data)
    # Bunu kendimiz yapıyoruz !!!
    # Headers Content-type -- application/json --> Then Body Raw
    # " Create Item In Store: {'name': 'Another item', 'price': 10.99} "

    for store in stores:
        if store["name"] == name:
            new_item = {
                "name" : request_data["name"],
                "price" : request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message" : "store not found"})

@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    # Store name göre item çek !!
    for store in stores:
        if store["name"] == name:
            return jsonify({"items" : store["items"]})

    return jsonify({"message" :"store not found"})

if __name__ == "__main__":
    app.run(debug=True)