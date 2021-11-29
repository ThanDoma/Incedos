import platform
# from __future__ import print_function
from collections import OrderedDict

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()
 
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo
 
if __name__=='__main__':
    #print(meminfo())
    
    meminfo = meminfo()
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))
    Total = int(meminfo['MemTotal'][:-3])
    Free = int(meminfo['MemFree'][:-3])
    Total = Total/1024/1024
    Free = Free/1024/1024
    vm = int((Total-Free)/Total*100)
    print(f'Свободное количество оперативной памяти: {100-vm}%')