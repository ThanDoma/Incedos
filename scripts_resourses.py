import psutil


def load_vmemory():
    memory = psutil.virtual_memory()
    memory = round(100.0 - memory[2],2)
    return print(f'Доступно ОЗУ: {round(memory),2}%')


def disk_scan():
    disk = psutil.disk_usage('/')
    disk_space = round(100.0 - disk[3],2)
    print(f'Свободное место на диске: {disk_space}%')


def cpu_load(time_line):
    cpu_loadavg = psutil.getloadavg()
    cpu_count = psutil.cpu_count()
    cpu_percent = [x / cpu_count * 10 for x in cpu_loadavg]

    if time_line == 1:
        print(f'Процессор загружен на {cpu_percent[0]}%') #Загруженность процессора за 1 минуту
    elif time_line == 5:
        print(f'Процессор загружен на {cpu_percent[1]}%') #Загруженность процессора за 5 минут
    elif time_line == 15:
        print(f'Процессор загружен на {cpu_percent[2]}%') #Загруженность процессора за 15 минут3
    

# cpu_load(15)
# load_vmemory()
# disk_scan()
