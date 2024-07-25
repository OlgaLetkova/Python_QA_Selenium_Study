import os
import argparse
import re
import json


def logs_location():
    parser = argparse.ArgumentParser()
    parser.add_argument('indir', type=str, help='Logs location')
    args = parser.parse_args()

    if os.path.isfile(args.indir):
        work_path = args.indir
        return work_path

    elif os.path.isdir(args.indir):
        files = os.listdir(args.indir)
        list_of_path = []
        for i in range(len(files)):
            work_path = f"{args.indir}" + '/' + f"{files[i]}"
            list_of_path.append(work_path)
        return list_of_path


def logs_reader():
    work_path = logs_location()
    if type(work_path) is str:
        with open(work_path, "r") as file:
            input_file = file.readlines()
            data = logs_parser(file_for_parsing=input_file)
            with open("result.json", "w") as f:
                s = json.dumps(data, indent=4)
                print(f"Logs parsing results for file {work_path} \n {data}")
                f.write(s)
    elif type(work_path) is list:
        for item in work_path:
            with open(item, "r") as file:
                input_file = file.readlines()
                data = logs_parser(file_for_parsing=input_file)
                with open("result.json", "w") as f:
                    s = json.dumps(data, indent=4)
                    print(f"Logs parsing results for file {item} \n {data}")
                    f.write(s)


def logs_parser(file_for_parsing):
    total_requests = len(file_for_parsing)
    total_stat = get_total_stat(file_for_parsing)
    top_ips = get_top_ips(file_for_parsing)
    top_longest = get_top_longest(file_for_parsing)

    data = {
        "top_ips": top_ips,
        "top_longest": top_longest,
        "total_stat": total_stat,
        "total_requests": total_requests
    }
    return data


def get_total_stat(file):
    dict_of_methods = {"\"GET ": 0, "\"POST ": 0, "HEAD": 0, "PUT": 0, "OPTIONS": 0, "DELETE": 0}

    for i in range(0, len(file)):
        for method in dict_of_methods.keys():
            if re.search(method, file[i]) is not None:
                value = dict_of_methods[f"{method}"] + 1
                dict_of_methods[f"{method}"] = value
                break

    dict_of_methods["GET"] = dict_of_methods["\"GET "]
    del dict_of_methods["\"GET "]
    dict_of_methods["POST"] = dict_of_methods["\"POST "]
    del dict_of_methods["\"POST "]

    sorted_dict_of_methods = dict(sorted(dict_of_methods.items(), key=lambda item: item[1], reverse=True))

    return sorted_dict_of_methods


def get_top_ips(file):
    ips_list = []
    ips_dict = {}
    for i in range(0, len(file)):
        ips_list.append(file[i].split(" ")[0])
    for i in range(0, len(ips_list)):
        if ips_list[i] not in ips_dict.keys():
            ips_dict[ips_list[i]] = 1
        else:
            ips_dict[ips_list[i]] += 1

    sorted_ips = sorted(ips_dict.items(), key=lambda item: item[1], reverse=True)
    ips = dict(sorted_ips)
    result_list = list(ips.items())[:3]
    return dict(result_list)


def get_top_longest(file):
    duration_list = []
    result = []
    item_result = {}
    for item in file:
        duration_list.append(item.split()[-1])
    int_lst = [int(x) for x in duration_list]
    sorted_list = sorted(int_lst, reverse=True)
    top_list = sorted_list[:3]
    for i in range(0, len(file)):
        if int(file[i].split()[-1]) in top_list:
            item_result["ip"] = file[i].split(" ")[0]
            item_result["date"] = file[i].split(" ")[3] + " " + file[i].split(" ")[4]
            item_result["method"] = file[i].split(" ")[5].replace("\"", "")
            item_result["url"] = file[i].split(" ")[10].replace("\"", "")
            item_result["duration"] = int(file[i].split()[-1])
            result.append(item_result)
        item_result = {}
        if len(result) == 3:
            break
    return result


if __name__ == '__main__':
    logs_reader()
