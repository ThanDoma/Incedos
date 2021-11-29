import glob
import re
import os


dev_pattern = ['sd.*','mmcblk*']
 
def size(device):
    nr_sectors = open(device+'/size').read().rstrip('\n')
    sect_size = open(device+'/queue/hw_sector_size').read().rstrip('\n')
    return (float(nr_sectors)*float(sect_size))/(1024.0*1024.0*1024.0)
 
def detect_devs():
    for device in glob.glob('/sys/block/*'):
        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                # print('Device:: {0}, Size:: {1} GiB'.format(device, size(device)))
                sizes = round(size(device),2)
                print(f'Устройство: {device}, размер: {sizes} GiB')
 
if __name__=='__main__':
    detect_devs()