import os
import sys
import socket
import subprocess
import time
from pymongo import MongoClient, collection

import paramiko
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
mongo_client = MongoClient('mongodb://devroot:devroot@172.18.0.4:27017/myDB?authSource=admin')


db = mongo_client.myDB
collection_object = db.lowLevel


host = '192.168.43.24'
user = 'haze'
secret = '1'
port = 22
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname=host, username=user, password=secret, port=port)
    cmd = "cd /var/log &&  cat auth.log | egrep -a -e root | egrep -v closed | egrep -v opened && whoami"
    # cmd1 = "cd /var/log && cat auth.log"
    stdin, stdout, stderr = client.exec_command(cmd)
    str = stdout.read().decode() + stderr.read().decode()
    # str1 = str[0:4]
    new_str = str.split("\n")
    for i in range(len(new_str)-2):
        s = new_str[i].split()
        myquery = {"date": s[0:3], "time": s[2], "hostname": s[3], "event": ''.join(s[5:]), "obj": "OS", "danger": "Unknown", "username": "haze"}
        result_object = collection_object.insert_many(myquery)
        print(myquery)
    client.close()
    # print(f"str->{len(str)}\n new_str->{len(new_str)}")  
except Exception as err:
    print(f"ERROR ->{err}")

