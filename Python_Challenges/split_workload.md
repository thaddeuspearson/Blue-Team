# split_workload 

Write a function called `split_workload` which takes in a list of tasks and a list of people. 

Given this list of tasks, return a dictionary of the tasks assigned to each individual in order in the list of people. The tasks should be split equally amongst them.

```python
chore_list = split_workload(['wash dishes', 'do stuff', 'call mom', 'go to NY'], ['joe', 'lily'])

# chorelist = {'joe': ['wash dishes', 'call mom'],'lily': ['do stuff', 'go to NY']}
```

<details><summary><b>Solution</b></summary>

```python

def main():
    
    def split_workload(task_list, people_list):
        return_dict = {}

        # build the return dictionary keys
        for person in people_list:
            return_dict[person] = []
        
        # counter to cycle through the people_list
        current_person_index = 0

        # iterate through tasks, and assign them to people in order
        for task in task_list:
            
            # cycle through the person list
            current_person = current_person_index % len(people_list)

            # assign task to proper person
            return_dict[people_list[current_person]].append(task)
            
            # move to the next person in the people list
            current_person_index += 1

        return return_dict

if __name__ == "__main__":
    main()
```
</details>