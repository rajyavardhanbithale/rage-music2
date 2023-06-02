#If5gaaR2EgFgYGrn  rage-admin
from pymongo.mongo_client import MongoClient
import gzip
uri = "mongodb+srv://rage-admin:If5gaaR2EgFgYGrn@rage-music.k8cl2q0.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(uri)





db = client['accounts']


collection = db['account']


def addData(data):

    result = collection.insert_one(data)


    print('Inserted document ID:', result.inserted_id)