#!/usr/bin/env python

'''
{This will parse a log file, count, validate, and sort ip4 addresses}
'''

import sys
import re

file_name = sys.argv[1]
file = open(file_name, "r")
content = file.read()



def ip_finder_and_validator(lst):
    ip_dict = {}
    sorted_ips = []
    return_str = ""


    # Helper Functions

    def is_it_valid(str):
        numbers = str.split(".")
        return_bool = True

        for num in numbers:
            if int(num) > 255 or len(num) >1 and num[0] =="0":
                return_bool = False

        return return_bool


    def ip_as_tuple(s):
        lst = s.split(".")
        
        return ( int(lst[0]), int(lst[1]), int(lst[2]), int(lst[3]) )


    def three_digits(str):
        return_str = ""

        if len(str) == 1:
            return_str += "(" + "00" + str + ")"
       
        if len(str) == 2:
            return_str += "(" + "0" + str + ")"
       
        if len(str) == 3:
            return_str +="(" + str + ")"
        
        return return_str


    def spacer(elem):
        return_str = ""
        num_of_spaces = 16 - len(elem)
        
        for space in range(0, num_of_spaces):
            return_str += " "
        
        return return_str

    
    # Main Code Body


    ips_found = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", lst)

    for ip4 in ips_found:
        
        if ip4 in ip_dict:
           ip_dict[ip4]["count"] += 1

        else:
           ip_dict[ip4] = {
                   "count": 1,
                   "valid": is_it_valid(ip4),
                   "num_ip": ip_as_tuple(ip4)
                   }


    # Create An Ordered List With Required Information


    for address in ip_dict:
        sorted_ips.append([ip_dict[address]["count"], ip_dict[address]["num_ip"], address, ip_dict[address]["valid"]])

    final_sorted = sorted(sorted_ips)


    # Concatenate The Return String And Return It


    for final in final_sorted:
        return_str += three_digits(str(final[0]))
        
        if final[3] == False:
            return_str += " "

        elif final[3] == True:
            return_str += "  "

        return_str += str(final[3]) + ": " + spacer(final[2]) + final[2] + " *"

        if final == final_sorted[-1]:
            return_str += "*"
            return return_str

        else:
            return_str += "\n"


def main():

    print(ip_finder_and_validator(content))

main()