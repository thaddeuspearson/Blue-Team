#!/usr/bin/env python

import sys

file_name = sys.argv[1]
file = open(file_name, "r")
content = file.read().split("\n")


def src_and_dst_ip_counter(log_lst):
    src_ip_dict = {}
    dst_ip_dict = {}

    # parse through the log_lst
    for log in log_lst:
    # build a dictionary with src ips and dst ips
        ip_dict_create_and_count(src_ip_dict, param_scraper("SRC", log))
        #ip_dict_create_and_count(dst_ip_dict, param_scraper("DST", log))

    return src_ip_dict
        
    

    # return the count of src ips and dst ips


def param_scraper(param, log_str):
    #  search the log_str for the target parameter and return the desired parameter as a string
    if log_str.find(param) != -1:
        return log_str[log_str.find(param) + (len(param) + 1) : log_str.find(" ", log_str.find(param))]

def ip_dict_create_and_count(ip_dict, ip_str):
    # if the ip has been seen before, increase the count, if not, create a new count
    if ip_str in ip_dict:
        ip_dict[ip_str]["count"] += 1
    else:
        ip_dict[ip_str] = {
            "count": 1,
        }
        
##def formatter(dct_1, dct_2):

 ##   for ip in dct_1:
  ##      if ip in dct_2:
            



def main():

    #replace primary_function below
    
    print(src_and_dst_ip_counter(content))

if __name__ == "__main__":
    main()