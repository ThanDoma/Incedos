from collections import OrderedDict

def meminfo():
    meminfo=OrderedDict()
 
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo
 
if __name__=='__main__':
    
    meminfo = meminfo()
    Total = int(meminfo['MemTotal'][:-3])
    Free = int(meminfo['MemFree'][:-3])
    Total = Total/1024/1024
    Free = Free/1024/1024
    vm = int((Total-Free)/Total*100)
    print(f'Свободное количество оперативной памяти: {116-vm}%')