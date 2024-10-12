from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Replace 'localhost' and '27017' with your MongoDB server details if needed
client = MongoClient('localhost', 27017)
db = client['your_database_name']  # Replace with your database name
collection = db['your_collection_name']  # Replace with your collection name

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
