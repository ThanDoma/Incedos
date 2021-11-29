
from collections import OrderedDict

def meminfo():
    meminfo=OrderedDict()
 
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo
 
meminfo = meminfo()
Total = int(meminfo['MemTotal'][:-3])
Free = int(meminfo['MemFree'][:-3])
Total = Total/1024/1024
Free = Free/1024/1024
vm = int((Total-Free)/Total*100)
memo = 100-vm
print(f'Свободное количество оперативной памяти: {100-vm}%')