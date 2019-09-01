#!/usr/bin/env python

import sys

file_name = sys.argv[1]
file = open(file_name, "r")
content = file.read().splitlines()


def scripting_3(log_file):
    ip_dct = {}
    ip_count = []

    # read each log in the log_file

    for log in log_file:
        src_ip = log.split(";")
        
        # parse only for FTP requests (port 21)

        if src_ip[5] == "21":

            # count the number of instances an ip exists in the log_file

            if src_ip[4] in ip_dct:
                ip_dct[src_ip[4]]["count"] += 1
            else:
                ip_dct[src_ip[4]] = {
                    "count" : 1
                } 
    # create a list for sorting the ips by count
    
    for ip_and_count in ip_dct:
        ip_count.append([ip_dct[ip_and_count]["count"], ip_and_count])

    # return the ips from least to greatest

    return sorted(ip_count, key=lambda x: x[0])



def main():
    
    print(scripting_3(content))

if __name__ == "__main__":
    main()
