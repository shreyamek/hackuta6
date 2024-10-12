from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

uri = "mongodb+srv://fudgemonkey1219:W6vHjV4w5SyJgwiD@cluster0.ipon1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['your_database_name']  # Replace with your database name
collection = db['your_collection_name']  # Replace with your collection name

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find())
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.json
    collection.insert_one(new_data)
    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(debug=True)
