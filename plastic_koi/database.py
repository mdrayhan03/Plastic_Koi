from pymongo import MongoClient
from pymongo.errors import *

class Database:
    def __init__(self):
        client = MongoClient("mongodb+srv://mdrayhan03:mongodbrayhan03@practice.j8okl.mongodb.net/?retryWrites=true&w=majority&appName=Practice")  # Replace with your MongoDB URI if needed
        db = client["Testing_DB"]  # Database name
        self.collection = db["Testing_Col"]

    def insert_new_post(self, name, description, location, image_url) :
        data = {
            "name" : name,
            "description" : description,
            "location" : location,
            "image_url" : image_url,
            "status" : "pending"
        }
        try:
            # Insert the data into the collection
            response = self.collection.insert_one(data)

            # Check if the insertion was successful by looking at the inserted_id
            if response.inserted_id:
                print(f"Document inserted successfully with ID: {response.inserted_id}")
            else:
                print("Insertion failed: No inserted ID returned.")

        except PyMongoError as e:
            print(f"An error occurred: {e}")
    
    def find_all_post(self) :
        data = self.collection.find()
        return data