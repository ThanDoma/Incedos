from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
#import re

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://devroot:devroot@localhost:27018/mydb?authSource=admin')
#выбираем базу
mydb = client["mydb"]
#выбираем коллекцию
mycol = mydb["to"]

# Функция выводящая hostname
# x = subprocess.run("hostname", stdout=subprocess.PIPE)
# output = x.stdout.read()
# print(output)

# subprocess.Popen("echo $HOSTNAME")
# x = "echo $HOSTNAME"
# def sh():
#     global x
#     y = os.system("bash -c '%s'" % x)
#     return y
# z = sh()
# print(z)

# Поиск всех записей в коллекции
# myquery = {  }

#mydoc = mycol.find(myquery)

#for x in mydoc:
#  print(x) 

# Добавить записи
# myquery = {"name": "John", "address": "Highway 37"}

# mydoc = mycol.insert_one(myquery)


with open('/var/log/auth.log') as f:
    contents = f.readlines()
    x=[]
    for i in iter(contents):
        if 'root' in i:
            x.append(i)
    # print(x) 
for i in range(len(x)):
# ищем все строки время которых больше последнего документа в db
    x = contents[i].split()
    myquery = {"datatime": x[0:3], "time_service": x[2], "user": x[3], "host": 'host', "level deng": "2", "event": ' '.join(x[4:]), "object":"OC"}
    mydoc = mycol.insert_one(myquery)

# remove dockument db
#mycol.remove({})
