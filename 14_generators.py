# Generators - function that return an object that can be iterated over 
# Much more memory efficient than other sequence objects (with large data sets)


# # ==== Simple example ==== 
# # yield = return (return generator)

# def mygenerator():
#     yield 1
#     yield 2
#     yield 3 

# g = mygenerator()
# # print(g) # <generator object mygenerator at 0x102aeb4c0>

# # for i in g:
# #     print(i) # 1 2 3

# value = next(g)
# print(value) # 1

# value = next(g)
# print(value) # 2

# value = next(g)
# print(value) # 3

# value = next(g)
# print(value) # StopIteration (because a generator object will always raise a stop iteration)


# === Inputs to other func that take iterables === 
# def mygenerator():
#     yield 3
#     yield 2
#     yield 1 

# g = mygenerator()
# print(sorted(g)) # [1, 2, 3]



# === Closer look on Generator ===
# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num 
#         num -= 1

# cd = countdown(4)
# value = next(cd) # Starting
# print(value)  # 4 

# print(next(cd)) # 3
# print(next(cd)) # 2
# print(next(cd)) # 1


# # === Example with mem efficent ===
# import sys
# def firstn(n):
#     nums = [] # all numbers stores in this list (takes a lot of memory)
#     num = 0 
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1

# # print(fistn(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(sum(firstn(10))) # 45
# # print(sum(firstn_generator(10))) # 45
# print(sys.getsizeof(firstn(100000))) # 800984
# print(sys.getsizeof(firstn_generator(100000))) # 104


# # === Fibonacci example ===
# def fibonacci(limit):
#     # 0 1 1 2 3 5 8 13 ... 
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b

# fib = fibonacci(30)
# for i in fib:
#     print(i) # ... 13 21 



# == Generator expression ==
import sys
mygenerator = (i for i in range(10000) if i % 2 == 0)
# print(list(mygenerator)) # [0, 2, 4, 6, 8]
print(sys.getsizeof(mygenerator)) # 104
# for i in mygenerator:
#     print(i) # 0 2 4 6 8

mylist = [i for i in range(10000) if i % 2 == 0]
# print(mylist) # [0, 2, 4, 6, 8]
print(sys.getsizeof(mylist)) # 41880
