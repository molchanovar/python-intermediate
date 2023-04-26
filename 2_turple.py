# myTuple = ("Max", 28, "Boston") - The same without brackets
# myTuple = "Max", 28, "Boston"

# myTuple = ("Max") # is string type
# myTuple = ("Max", ) # is turple type 
# print(type(myTuple))

# myTuple = tuple(["Max", 28, "Boston"])
# print(myTuple)

# item = myTuple[0] # 1st element
# item = myTuple[1] # 2nd element 
# item = myTuple[-1] # the last element
# print(item)

# myTuple[0] = "Tim" # not possible to change exist tuple (TypeError: 'tuple' object does not support item assignment)

# Check object in Tuple: 
# if "Tim" in myTuple:
#     print('yes')
# else:
#     print('no')

# ========= Operations ========
# my_tuple = ('a', 'p', 'p', 'l', 'e')
# print(len(my_tuple)) # - print length of tuple 
# print(my_tuple.count('p')) # - count of 'p' meet times = 2
# print(my_tuple.index('p')) # - get index number = 1 (if no sting in tuple = tuple.index(x): x not in tuple)

# my_list = list(my_tuple) # - create list from tuple
# print(my_list)

# my_tuple2 = tuple(my_list) # - create tuple back from list
# print(my_tuple2)

# ======= Slices =======
# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# b = a[2:5] # - get slice tuple (3, 4, 5)
# b = a[2:] # - (3, 4, 5, 6, 7, 8, 9, 10)
# b = a[::2] # - step by 2 - (1, 3, 5, 7, 9) 
# b = a[::-1] # - reverse tuple - (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
# print(b)

# ======= Unpacking =====
# my_tuple = "Max", 28, "Boston"

# name, age, city = my_tuple
# print(name) # - Max 
# print(age) # 28
# print(city) # Boston

# my_tuple = (0, 1, 2, 3, 4)

# i1, *i2, i3 = my_tuple
# print(i1) # - 0
# print(i3) # - 4 
# print(i2) # - converted to the list - [1, 2, 3]

# Why use tuple instead List - 1. protected from changes; 2. Smaller size

# ====== Size of tuple compared with list ======
# import sys 
# my_list = [0, 1, 2, "hello", True]
# my_tuple = (0, 1, 2, "hello", True)
# print(sys.getsizeof(my_list), "bytes") # - 104 bytes
# print(sys.getsizeof(my_tuple), "bytes") # - 80 bytes

# ======== timeit - repeat N times =======
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) # 0.034887124988017604
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) # 0.004775583001901396