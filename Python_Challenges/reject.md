# Reject

Write the function `reject` that accepts as an argument a list and function.

The `reject` function returns a list made of the elements that are the logical opposite of what the given function returns when invoked with each element.

```python
def less_than_five(num):
    return num < 5

list_of_values = reject([1, 3, 4, 5, 6, 9, 11], less_than_five)
## list_of_values = [6, 9, 11]
```

<details><summary><b>Solution</b></summary>

```python

def main():
    
    # return the opposite of a given function
    def opposite(func, param):
	    return not func(param)

    # reject function
    def reject(lst, func):
	return_lst = []

        # test each element for the opposite
	    for item in lst:
		    if opposite(func, item) == True:
		        return_lst.append(item)
    
        # return the opposite elements
	    return return_lst

if __name__ == "__main__":
    main()
```
</details>