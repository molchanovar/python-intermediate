# itertools: product, permutations, combinations, 
# accumulate, groupby, infinite iterators 

# ==== product ====
# from itertools import product
# a = [1,2]
# # b = [3,4]
# b = [3] # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)] 
# # prod = product(a,b)
# prod = product(a,b, repeat=2) # very large list - [(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4), (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4), (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)]
# print(prod) # <itertools.product object at 0x1030bc1c0>
# print(list(prod)) # show [(1, 3), (1, 4), (2, 3), (2, 4)]


# ==== permutations ====
# return all possible ordering of an input 
# from itertools import permutations
# a = [1,2,3]
# # perm = permutations(a)
# # print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# perm = permutations(a, 2) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
# print(list(perm))


# ==== combinations ====
# make all possible combinations with specified length 
# from itertools import combinations, combinations_with_replacement
# a = [1, 2, 3, 4]
# comb = combinations(a, 2) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# print(list(comb))

# comb_wr = combinations_with_replacement(a, 2) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
# print(list(comb_wr))


# ==== accumulate ====
# by default - compute the sums 
# from itertools import accumulate
# a = [1, 2, 3, 4]
# acc = accumulate(a)
# print(a) # [1, 2, 3, 4]
# print(list(acc)) # [1, 3, 6, 10]

# # Multiply the elements
# import operator
# acc_multy = accumulate(a, func=operator.mul)
# print(list(acc_multy)) # [1, 2, 6, 24]

# # MAX operator (compared with the next element in list)
# b = [1, 2, 5, 3, 4]
# acc_max = accumulate(b, func=max) # [1, 2, 5, 5, 5]
# print(list(acc_max))


# ==== groupby ==== + lambda simple example 
# from itertools import groupby

# # def smaller_than_3(x):
# #     return x < 3

# # a = [1, 2, 3, 4]
# # group_obj = groupby(a, key=smaller_than_3)
# # print(group_obj) # <itertools.groupby object at 0x103145170>

# ##### lambdas are small one line function that have input and will do some expression and return an output. Result the same expression above #####
# # a = [1, 2, 3, 4]
# # group_obj = groupby(a, key=lambda x: x<3)
# # print(group_obj)
# # for key, value in group_obj:
# #     print(key, value) # Show True/False (True <itertools._grouper object at 0x104523880>)
# #     print(key, list(value)) # True [1, 2] / False [3, 4]

# persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
#            {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

# group_obj = groupby(persons, key=lambda x: x['age'])
# for key, value in group_obj:
#     print(key, list(value)) # 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}] / 27 [{'name': 'Lisa', 'age': 27}] / 28 [{'name': 'Claire', 'age': 28}]

  
# ==== infinite iterators ==== 
from itertools import count, cycle, repeat

### count
# for i in count(10):
#     print(i) # infinte loop starts at 10 :) 
#     if i == 15: 
#         break # stop at i=15 

### cycle 
# a = [1, 2, 3]
# for i in cycle(a):
#     print(i) # infintely print 1,2,3 and again 

### repeat
# for i in repeat(1):
#     print(i) # infinite loop and will print 1
for i in repeat(1, 4):
    print(i) # repeat 4 times 