import subprocess
import sys

cpu_percent = open('cpu1.txt', 'a')
cpu_percent = subprocess.run(['mpstat','1','1'], stdout=cpu_percent, stderr=cpu_percent, shell=True)

with open("cpu1.txt") as f:
    cpu_dict = {}
    for line in f:
        key, *value = line.split('   ')
        cpu_dict[key] = value
# print(cpu_dict)
sp = []
for key in cpu_dict:
    cpu_key = ' '.join(cpu_dict[key])
    cpu_load_percent = cpu_key[18:23]
    cpu_load_percent = cpu_load_percent.replace(',', '.')
    sp.append(cpu_load_percent)
for i in range(2, len(sp)):
    cpu = float(sp[i])
    print(f'Загруженность процессора: {cpu}%')