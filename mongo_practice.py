from pymongo import MongoClient

client = MongoClient('mongodb://root:root@localhost:27017')

database = client['dev']

collection = database['mydev']


if __name__ == '__main__':
    data = collection.find({})
    print(list(data))
