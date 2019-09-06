"""
write a function that can sum all the numbers in a multi-dimensional list of numbers
"""

def multi_dim_sum_list(lst):
    sum = 0

    # iterate through the list
    for item in lst:

        # test the item to see if it is an array
        if type(item) == type([]):
            
            # call the multi_dim_sum_list function again recursively
            sum += multi_dim_sum_list(item)

        else:

            # if the item is an int, add it to the sum
            sum += item
    
    # return the sum
    return sum
