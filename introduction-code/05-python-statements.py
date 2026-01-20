# if elif, and else. He also talked about python architeture. pretty much it uses indentation and : to control the flow which was pretty uniqure when it came out 

#if some_condition: 
#   execute some some code 
#else:
# do something else 
# You can also have an elif statement. if statements are nice but easy to overuse and write bad code 

hungry: bool = True

if hungry:
    print("Feed me")
else:
    print("Please dont give me any more")

#he did more examples but I am not typing all dat 

#for loops are sick. Nice to iterate a block of code for each object 
# iterate means perform an action over an entire object ie every character in a string or every item in a list
# my_iterable = [1, 2, 3]
# for item_name in my_iterable:
#   print(item_name) 
#   prints 1 2 3


my_list: list = [1, 2, 3, 4, 5, 6]

for num in my_list:
    print(num)
    if num % 2 == 0:
        print(f"{num} is even")

list_sum: int = 0

for num in my_list:
    list_sum += num

d: dict[str, int] = {'k1': 1, 'k2':2, 'k3': 3}

for key, value in d.items():
    print(f"{value} value")
    print(key)
