# import random 

# a = random.random() # random float (from 0 to 1)
# a = random.uniform(1, 10) # float in a specific range
# a = random.randint(1, 10) # int values, include 10
# a = random.randrange(1, 10) # 1 and 10 is not included 

# a = random.normalvariate(0, 1) # normal distribution (mu = 0, sigma = 1)
# print(a)


# === Lists ====
# mylist = list("ABCDEFGH")
# a = random.choice(mylist) # will choice random letter
# a = random.sample(mylist, 3) # ['E', 'B', 'H']
# a = random.choices(mylist, k=3) # can pick elements multiple times 
# random.shuffle(mylist) # ['D', 'C', 'E', 'A', 'G', 'B', 'H', 'F']
# print(mylist)


# Example where result will be the same: 
# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))
# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))
# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))

## Not recommended to use for security purposes


# ==== Security ====
# import secrets # used for passwords, security tokens, acc auth but it takes more time 

# mylist = list("ABCDEFGH")
# a = secrets.randbelow(10) # random integer from 0 to 10 (10 is not included)
# a = secrets.randbits(4) # random binary values (1011)
# a = secrets.choice(mylist)
# print(a)


# ==== Arrays ==== 
# Use numpy module 
import numpy as np

# a = np.random.rand(3) # [0.03578045 0.93965438 0.4239442 ] - three random floats 
# a = np.random.rand(3,3)
# [[0.48714944 0.58417098 0.05882026]
#  [0.02629274 0.95020943 0.3040333 ]
#  [0.67195349 0.4898173  0.41771081]]

# a = np.random.randint(0,10,3) # [1 6 4]
# a = np.random.randint(0,10,(3, 4))
# [[6 5 6 1]
#  [6 8 9 3]
#  [6 8 8 0]]

# arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(arr)
# np.random.shuffle(arr)
# print(arr)

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# [[7 8 9] # shuffle only the elements along the first axis 
#  [1 2 3]
#  [4 5 6]]

# !!! NumPy random generator uses a different number generator than the one from Python library

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))
