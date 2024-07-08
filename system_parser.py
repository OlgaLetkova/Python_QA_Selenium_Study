from subprocess import (
    run
)
import datetime


def capture_out():
    result = run("ps aux", capture_output=True, shell=True, text=True)
    return result.stdout


def get_users_list():
    output = capture_out().splitlines()
    user_list = []
    for i in range(len(output)):
        user_list.append(output[i].split(" ")[0])
    return set(user_list)


def get_proc_quantity():
    output = capture_out().splitlines()
    return len(output)


def get_user_proc(user_name):
    output = capture_out().splitlines()
    user_list = []
    for i in range(len(output)):
        if output[i].split(" ")[0] == user_name:
            user_list.append(output[i].split(" ")[0])
    return len(user_list)


def get_all_memory():
    output = capture_out().splitlines()
    memory_list = []
    for i in range(len(output)):
        row = output[i].split()
        if row[3] != '%MEM':
            memory_list.append(row[3])
    float_lst = [float(x) for x in memory_list]
    all_mem = round(sum(float_lst), 1)
    return all_mem


def get_all_cpu():
    output = capture_out().splitlines()
    cpu_list = []
    for i in range(len(output)):
        row = output[i].split()
        if row[2] != '%CPU':
            cpu_list.append(row[2])
    float_lst = [float(x) for x in cpu_list]
    all_cpu = round(sum(float_lst), 1)
    return all_cpu


def max_memory_using():
    output = capture_out().splitlines()
    mem_list = []
    for i in range(len(output)):
        row = output[i].split()
        mem_list.append(row)
    max_number = float(mem_list[1][3])
    list_with_max_memory = []
    for i in range(1, len(mem_list)):
        if float(mem_list[i][3]) > max_number:
            max_number = float(mem_list[i][3])
            list_with_max_memory = mem_list[i]
    name = list_with_max_memory[10]
    return name[0:20]


def max_cpu_using():
    output = capture_out().splitlines()
    cpu_list = []
    for i in range(len(output)):
        row = output[i].split()
        cpu_list.append(row)
    max_number = float(cpu_list[1][2])
    list_with_max_cpu = []
    for i in range(1, len(cpu_list)):
        if float(cpu_list[i][2]) > max_number:
            max_number = float(cpu_list[i][2])
            list_with_max_cpu = cpu_list[i]
    name = list_with_max_cpu[10]
    return name[0:20]


def out_to_file():
    with open(f'{datetime.datetime.now().strftime("%d-%m-%Y-%H:%M")}-scan.txt', 'w+') as file:
        file.write("Отчёт о состоянии системы:\n"
                   f"Пользователи системы: {get_users_list()}\n"
                   f"Процессов запущено: {get_proc_quantity()}\n\n"
                   "Пользовательских процессов:\n"
                   f"olelet: {get_user_proc('olelet')}\n"
                   f"kernoops: {get_user_proc('kernoops')}\n"
                   f"colord: {get_user_proc('colord')}\n"
                   f"rtkit: {get_user_proc('rtkit')}\n"
                   f"root: {get_user_proc('root')}\n"
                   f"systemd+: {get_user_proc('systemd+')}\n"
                   f"avahi: {get_user_proc('avahi')}\n"
                   f"message+: {get_user_proc('message+')}\n"
                   f"syslog: {get_user_proc('syslog')}\n"
                   f"USER: {get_user_proc('USER')}\n\n"
                   f"Всего памяти используется: {get_all_memory()}\n"
                   f"Всего CPU используется: {get_all_cpu()}\n"
                   f"Больше всего памяти использует: {max_memory_using()}\n"
                   f"Больше всего CPU использует: {max_cpu_using()}")


if __name__ == '__main__':
    out_to_file()
