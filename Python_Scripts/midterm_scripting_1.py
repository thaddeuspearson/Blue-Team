#!/usr/bin/env python

import sys

file_name = sys.argv[1]
file = open(file_name, "r")
content = file.read().splitlines()


def scripting_1(log_file):
    ip_dct = {}
    ip_count = []
    for log in log_file:
        src_ip = log.split(";")[2]

        if src_ip in ip_dct:
            ip_dct[src_ip]["count"] += 1
        else:
            ip_dct[src_ip] = {
                "count" : 1
            } 
    
    for ip_and_count in ip_dct:
        # print ip_dct[ip_and_count]["count"]
        ip_count.append([ip_dct[ip_and_count]["count"], ip_and_count])

    return sorted(ip_count, key=lambda x: x[0])

    





def main():

    #replace primary_function below
    
    print(scripting_1(content))

if __name__ == "__main__":
    main()