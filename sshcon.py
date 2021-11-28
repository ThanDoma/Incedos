import paramiko
from pymongo import MongoClient, results
# import subprocess
# import schedule, time
import datetime as dt
# Данные о хосте адрес, имя, пароль, порт
global host, user, secret, port
host = '192.168.1.74'
user = 'haze'
secret = '1'
port = 22
def job():
    # collection_object.remove({})
    try:
        # Подключение к mongo. Проверьте на корректность адрес хоста в "Networks->incendos_mongo_1"
        mongo_client = MongoClient('mongodb://devroot:devroot@172.18.0.3:27017/myDB?authSource=admin')
        db = mongo_client.myDB #Название БД
        collection_object = db.lowLevel #Наименование коллекции
        # Подключение к ВМ по ssh
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=secret, port=port)
        # Словарь для замены месяца на его цифру(для удобства сравнивания дат)
        mounth = {
            "Jan" : 1,
            "Feb" : 2,
            "Mar" : 3,
            "Apr" : 4,
            "May" : 5,
            "Jun" : 6,
            "Jul" : 7,
            "Aug" : 8,
            "Sep" : 9,
            "Oct" : 10,
            "Nov" : 11,
            "Dec" : 12
        }
        # строка с командой для вывода содержимого из файла auth.log с определённым условием
        cmd = "cd /var/log &&  cat auth.log |\
                egrep -a -e root | egrep -v closed | egrep -v opened"
        # выполнение команды выше на ВМ и записывание вывода команды в потоки
        # stdout - поток вывода данных; stderr - поток вывода ошибок
        stdin, stdout, stderr = client.exec_command(cmd)
        str = stdout.read().decode() + stderr.read().decode() # декодировка потоков
        new_str = str.split("\n")
        count_items = collection_object.count_documents({}) # кол-во элементов в коллекции
        if count_items != 0: # нахождение последнего элемента в кол-ции, если кол-ция не пуста
            lastWrite = collection_object.find({}).sort('_id', -1).limit(1)
            print(collection_object.count())
            for x in lastWrite:
                lastWriteDate = x["date"]
            t2 = lastWriteDate[2].split(":")
            # print(t2)
        for i in range(len(new_str)-1):# запись данных в БД
            s = new_str[i].split()
            myquery = {
                "date": s[0:3],
                "time": s[2],
                "hostname": s[3], 
                "username": "\n",
                "event": ''.join(s[5:]), 
                "obj": "OS",
                "danger": "Unknown"
                }
            # collection_object.insert_one(myquery)
            timeNew = myquery["date"][2].split(":")
            # print(dt.datetime(2021, int(mounth[myquery["date"][0]]), int(myquery["date"][1]),\
            #     int(timeNew[0]), int(timeNew[1]), int(timeNew[2]))\
            #     > dt.datetime(2021, int(mounth[lastWriteDate[0]]),\
            #     int(lastWriteDate[1]), int(t2[0]), int(t2[1]), int(t2[2])))
            # print(dt.datetime(2021, int(mounth[myquery["date"][0]]), int(myquery["date"][1]),\
            #     int(timeNew[0]), int(timeNew[1]), int(timeNew[2])))
            # print(dt.datetime(2021, int(mounth[lastWriteDate[0]]),\
            #     int(lastWriteDate[1]), int(t2[0]), int(t2[1]), int(t2[2])))
            # print(lastWriteDate)
            if count_items == 0: # если кол-ция пуста, то записываем в неё все логи
                collection_object.insert_one(myquery)
                print("DATA WAS ADDED SUCCEESSFULLY!")
            # иначе сравниваем дату последнего элемента кол-ции с датой логов
            elif dt.datetime(2021, int(mounth[myquery["date"][0]]), int(myquery["date"][1]),\
                int(timeNew[0]), int(timeNew[1]), int(timeNew[2]))\
                > dt.datetime(2021, int(mounth[lastWriteDate[0]]),\
                int(lastWriteDate[1]), int(t2[0]), int(t2[1]), int(t2[2])):   
                        collection_object.insert_one(myquery)
                        print("DATA WAS UPDATED SUCCEESSFULLY!")
        # запрос на вывод всех элементов из кол-ции
        find_result =  collection_object.find({})
        results = (list(find_result))
        return results
    except Exception as err:
        print(f"ERROR ->{err}")
job()

