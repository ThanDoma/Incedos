import os
import sys
import socket
import subprocess
import time


import paramiko


host = '192.168.43.24'
user = 'haze'
secret = '1'
port = 22
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # while (True):
    #     try:
    #         client.connect(hostname=host, username=user, password=secret, port=port)
    #         cmd = input("$> ")
    #         if cmd == "exit": break
    #         stdin, stdout, stderr = client.exec_command(cmd)
    #         str = stdout.read().decode() + stderr.read().decode()
    #         time.sleep(0.5)
    #         print(f"{str}")
    #         client.close()
    #     except KeyboardInterrupt:
    #         break
    client.connect(hostname=host, username=user, password=secret, port=port)
    cmd = "cd /var/log && cat auth.log | grep -a root"
    cmd1 = "cd /var/log && cat auth.log"
    stdin, stdout, stderr = client.exec_command(cmd)
    str = stdout.read().decode() + stderr.read().decode()
    time.sleep(0.5)
    print(f"{str}")
    client.close()    
except Exception as err:
    print(f"ERROR ->{err}")

