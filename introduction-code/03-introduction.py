# my github delted this when I did 12 and 15 so I made a tldr
x: str = "Hello World"
print(x + x)
print(x + "I am so sad")
print(x.upper())

# Print formating: dont use .format use f stirng

print(f"YO! {x}")  # tbh this is all you need. Use AI for any other formating

# lists are muttable and ordered also allow dublicaitons. Lists are sick

my_list: list = ["string", 100, 2.3]
print(len(my_list))
print(my_list[0])
print(my_list[0:])
another_list = [1, 2, "2"]
print(my_list + another_list)
# You can use .append just look this up there are like 100 different list functions you can use

# pop is acutually cool because it is o(1) and can do stuff with stacks can use indexing
print(my_list.pop())

# numbers. int, float, double.

x: int = 1
y: float = 1.0
z: float = 1.0  # float but more decimals

# This entire video is just teaching basic math and its good we are engineeirngs

xy: float = x * y
xsquare: int = x**x
# you can also do this which they didnt teach but is very important
x = +1

# Dictonaries. mutable unordered, no duplicates for keys. These rock for json like functions
# and for database stuff. They are also 0(1) lookup which is nice

my_dict: dict = {"key1": "value1", "key2": "value2"}
print(my_dict["key1"])

# you can also nest with list other dictionaries and sets and stuff.
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# tuples are sick. They are immutable and great for functions and OOP

t: tuple = ("one", 2, 3.5)
print(t.count(2))
print(t.index("one"))
# This is video did not cover the most important part of tuples but I am sure it will be there at some point'
# tuples are great for functions    

# sets are unordred and unique, they are usefull but def my least used type

myset: set = set()
myset.add(1)

print(myset)

myset.add(2)

#Cannot add dup values nice to get only unique values. they are prop nice for something idk

#Booleans are like as simple as possble. taht is just true or false :


