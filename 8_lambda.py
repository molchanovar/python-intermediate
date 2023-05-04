# lambda arguments: expression 

## Create a function with one argument, it adds 10, argument return the result
# add10 = lambda x: x + 10
# print(add10(5)) # 15

# def add10_func(x):
#     return x + 10

# # !!! The same, but lambda is much shorter and only in one line !!!

# mult = lambda x,y: x*y
# print(mult(2,7)) # 14


# Sorting: 
# points2D = [(1, 2), (15, 1), (5, -1), (10, 4)] # list has tuples with two elements 

# points2D_sorted = sorted(points2D) # By default sorted on x arg
# points2D_sorted_y = sorted(points2D, key=lambda x: x[1]) # - sorted according to the Y index 

# ## Return the same result with lambda
# # def sort_by_y(x):
# #     return x[1]
# # points2D_sorted_y = sorted(points2D, key=sort_by_y) 

# print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]
# print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]
# print(points2D_sorted_y) # [(5, -1), (15, 1), (1, 2), (10, 4)]


# ==== Functions ==== 
# # map(func, seq)
# a = [1, 2, 3, 4, 5]
# b = map(lambda x: x*2, a)
# print (b) # <map object at 0x10466ed10>
# print (list(b)) # [2, 4, 6, 8, 10]

# # Prefer syntax (little bit easier)
# c = [x*2 for x in a] # [2, 4, 6, 8, 10]
# print(c)

# # filter(func, seq)
# # return True/False (return all elements for which the function evaluates to True)
# a = [1, 2, 3, 4, 5, 6]
# b = filter(lambda x: x%2==0, a)
# print(list(b)) # [2, 4, 6] (get only the even numbers)

# # the same: 
# c = [x for x in a if x%2==0]
# print(c) 


# reduce function  - repeatedly appliesm the function to the elements and returns a single value  
# reduce(func, seq)
from functools import reduce
a = [1, 2, 3, 4]

product_a = reduce(lambda x,y: x*y, a) # 1*2*3*4 = 24
print(product_a) 







