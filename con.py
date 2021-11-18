from pymongo import MongoClient
# pprint library is used to make the output look more pretty
import schedule, time

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://devroot:devroot@localhost:27018/mydb?authSource=admin')
#выбираем базу
mydb = client["mydb"]
#выбираем коллекцию
mycol = mydb["to"]

def job():
    with open('/var/log/auth.log') as f:
        contents = f.readlines()
        new_contents_list=[]
        for i in iter(contents):
        # disconect,clesed
            if 'root' in i:
                new_contents_list.append(i)
    # print(x) 
    for i in range(len(new_contents_list)):
# ищем все строки время которых больше последнего документа в db
        new_contents_list = contents[i].split()
        myquery = {"datatime": new_contents_list[0:3], "time_service": new_contents_list[2], "user": new_contents_list[3], "host": 'host', "level deng": "2", "event": ' '.join(new_contents_list[4:]), "object":"OC"}
        mydoc = mycol.insert_one(myquery)

schedule.every(5).to(10).seconds.do(job)
# бесконечный цикл, проверяющий каждую секунду, не пора ли запустить задание 
while 1:
    schedule.run_pending()
    time.sleep(1)

# remove dockument db
mycol.remove({})





# Функция выводящая hostname
# x = subprocess.run("hostname", stdout=subprocess.PIPE)
# output = x.stdout.read()
# print(output)

# subprocess.Popen("echo $HOSTNAME")
# x = "echo $HOSTNAME"
# def sh():
#     global x
#     y = os.system("hostname")
#     return y
# z = sh()


# Поиск всех записей в коллекции
# myquery = {  }

#mydoc = mycol.find(myquery)

#for x in mydoc:
#  print(x) 

# Добавить записи
# myquery = {"name": "John", "address": "Highway 37"}

# mydoc = mycol.insert_one(myquery)
