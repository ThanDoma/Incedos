import paramiko
from pymongo import MongoClient
# import subprocess
# import schedule, time
import datetime as dt

def job():
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    mongo_client = MongoClient('mongodb://devroot:devroot@172.18.0.4:27017/myDB?authSource=admin')
    db = mongo_client.myDB
    collection_object = db.lowLevel
    # collection_object.remove({})
    host = '192.168.43.24'
    user = 'haze'
    secret = '1'
    port = 22
    # Ввод команды cmd в терминал ВМ
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=secret, port=port)

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
        cmd = "cd /var/log &&  cat auth.log |\
                egrep -a -e root | egrep -v closed | egrep -v opened"
        stdin, stdout, stderr = client.exec_command(cmd)
        str = stdout.read().decode() + stderr.read().decode()
        cmd1 = "whoami"
        stdin, stdout, stderr = client.exec_command(cmd1)
        user = stdout.read().decode() + stderr.read().decode()
        #print(str)
        new_str = str.split("\n")

        lastWrite = collection_object.find({}).sort('_id', -1).limit(1)
        for x in lastWrite:
            lastWriteDate = x["date"]
        t2 = lastWriteDate[2].split(":")
        # print(t2)
        for i in range(len(new_str)-1):
            s = new_str[i].split()
            myquery = {
                "date": s[0:3],
                "time": s[2],
                "hostname": s[3], 
                "event": ''.join(s[5:]), 
                "obj": "OS",
                "danger": "Unknown", 
                "username": user}
            print(new_str[2])
            # print(new_str)
            
            timeNew = myquery["date"][2].split(":")
            print(dt.datetime(2021, int(mounth[myquery["date"][0]]), int(myquery["date"][1]),\
                int(timeNew[0]), int(timeNew[1]), int(timeNew[2]))\
                > dt.datetime(2021, int(mounth[lastWriteDate[0]]),\
                int(lastWriteDate[1]), int(t2[0]), int(t2[1]), int(t2[2])))
            print(dt.datetime(2021, int(mounth[myquery["date"][0]]), int(myquery["date"][1]),\
                int(timeNew[0]), int(timeNew[1]), int(timeNew[2])))
            #print(dt.datetime(2021, int(mounth[lastWriteDate[0]]),\
            #     int(lastWriteDate[1]), int(t2[0]), int(t2[1]), int(t2[2])))
            print(lastWriteDate)
            if dt.datetime(2021, int(mounth[myquery["date"][0]]), int(myquery["date"][1]),\
                int(timeNew[0]), int(timeNew[1]), int(timeNew[2]))\
                > dt.datetime(2021, int(mounth[lastWriteDate[0]]),\
                int(lastWriteDate[1]), int(t2[0]), int(t2[1]), int(t2[2])):
                    collection_object.insert_one(myquery)
                    print("DATA WAS ADDED SUCCEESSFULLY!")
            #print(date1[1])
            find_result =  collection_object.find({})
            results = list(find_result)
            return results
    except Exception as err:
        print(f"ERROR ->{err}")
job()
# print(job())
# schedule.every(3).seconds.do(job)

# while(True):
#     schedule.run_pending()
#     time.sleep(1)

