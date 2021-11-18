from pymongo import MongoClient, collection


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
mongo_client = MongoClient('mongodb://devroot:devroot@172.18.0.3:27017/myDB?authSource=admin')


db = mongo_client.myDB
collection_object = db.lowLevel



#mydb = client["myDB"]
#lowLevel = mydb["lowLevel"]
# mediumLevel = mydb["mediumLevel"]
# highLevel = mydb["highLevel"]

# Поиск всех записей в коллекции
myquery = {  }


find_result = collection_object.find(myquery)

insert_query = {
'date': "01.01.2001", 
'username': "test", 
'danger': "Низкий", 
'event': "none", 
'object': "none"
}

# result_object = collection_object.insert_one(insert_query)