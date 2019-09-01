#!/usr/bin/env python

import sys

file_name = sys.argv[1]
file = open(file_name, "r")
content = file.read().splitlines()


def scripting_1(log_file):
    ip_dct = {}
    ip_count = []

    # read each log in the log_file

    for log in log_file:

        # strip the source ip address

        src_ip = log.split(";")[4]

        # count the number of instances a source ip exists in the log_file
        
        if src_ip in ip_dct:
            ip_dct[src_ip]["count"] += 1
        else:
            ip_dct[src_ip] = {
                "count" : 1
            } 
    
    # create a list for sorting the source ips by count

    for ip_and_count in ip_dct:
        ip_count.append([ip_dct[ip_and_count]["count"], ip_and_count])

    # sort the ips from least to greatest

    return sorted(ip_count, key=lambda x: x[0])

    
    


def main():
    
    print(scripting_1(content))

if __name__ == "__main__":
    main()