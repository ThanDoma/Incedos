from pymongo import MongoClient
# pprint library is used to make the output look more pretty
import schedule, time

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://devroot:devroot@localhost:27018/mydb?authSource=admin')
#выбираем базу
mydb = client["mydb"]
#выбираем коллекцию
mycol = mydb["to"]


# def job():
#     with open('/var/log/auth.log') as f:
#         contents = f.readlines()
#         new_contents_list=[]
#         for i in iter(contents):
#         # disconect,clesed
#             if 'root' in i:
#                 new_contents_list.append(i)
#     # print(x) 
#     for i in range(len(new_contents_list)):
# # ищем все строки время которых больше последнего документа в db
#         new_contents_list = contents[i].split()
#         myquery = {"datatime": new_contents_list[0:3], "time_service": new_contents_list[2], "user": new_contents_list[3], "host": 'host', "level deng": "2", "event": ' '.join(new_contents_list[4:]), "object":"OC"}
#         mydoc = mycol.insert_one(myquery)

# schedule.every(5).to(10).seconds.do(job)
# # бесконечный цикл, проверяющий каждую секунду, не пора ли запустить задание 
# while 1:
#     schedule.run_pending()
#     time.sleep(1) 
# #remove dockument db
# mycol.remove({})



#mycol.remove({})

with open('/var/log/auth.log') as f:
    contents = f.readlines()
    new_contents_list=[]
if mycol.count() == 0:
    # print(x) 
        for i in range(len(contents)):
# ищем все строки время которых больше последнего документа в db
            new_contents_list = contents[i].split()
            myquery = {"datatime": new_contents_list[0:3], "time_service": new_contents_list[2], "user": new_contents_list[3], "host": 'host', "level deng": "2", "event": ' '.join(new_contents_list[4:]), "object":"OC"}
            mydoc = mycol.insert_one(myquery)
else:
    # находим последюю запись в db
    x = mycol.find().sort('_id',1)
    print(x)
    k, s=[],[]
    for i in x:
        k = i.values()
        s = list(k)
        c = s[1]
    # print(c)
    search_last_db = 0
    new_contents_list4=[]
    for i in range(len(contents)):
    # ищем все строки время которых больше последнего документа в db
        new_contents_list = contents[i].split()
        if c == new_contents_list[0:3]:
             search_last_db = i + 1
    print(search_last_db)
    print(len(contents))
    # print(contents[search_last_db:])

    for i in range(len(contents[search_last_db:])):
        new_contents_list4 = contents[search_last_db:]
        new_contents_list4 = new_contents_list4[i].split()
        # print(new_contents_list4)
        myquery = {"datatime": new_contents_list4[0:3], "time_service": new_contents_list4[2], "user": new_contents_list4[3], "host": 'host', "level deng": "2", "event": ' '.join(new_contents_list4[4:]), "object":"OC"}
        mydoc = mycol.insert_one(myquery)
    