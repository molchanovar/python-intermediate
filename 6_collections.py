# Five different types from the collections: 
# 1. Counter; 2. namedtuple; 3. OrderedDict; 4. defaultdict; 5. deque


# ========= COUNTER ===========
# from collections import Counter
# a = 'aaaaabbbbbbccccc'
# my_counter = Counter(a) # show -> Counter({'b': 6, 'a': 5, 'c': 5})
# # print(my_counter.items()) # dict_items([('a', 5), ('b', 6), ('c', 5)])
# # print(my_counter.keys()) # dict_keys(['a', 'b', 'c'])
# # print(my_counter.values()) # dict_values([5, 6, 5])

# print(my_counter) # Counter({'b': 6, 'a': 5, 'c': 5})
# print(my_counter.most_common(1)) # [('b', 6)]
# print(my_counter.most_common(2)) # [('b', 6), ('a', 5)]

# print(my_counter.most_common(1)[0]) # ('b', 6)
# print(my_counter.most_common(1)[0][0]) # b

# # Get all different elemets as a list: 
# print(my_counter.elements()) # <itertools.chain object at 0x1030361d0>
# print(list(my_counter.elements())) # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c']



# ========= NAMEDTUPLE =======
# from collections import namedtuple
# # Create a class called point with fields X and Y 
# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)

# print(pt) # Point(x=1, y=-4) 
# print(pt.x, pt.y) # - show only elements  ( 1 -4 )



# ========== OrderedDict ========= 
# like a regular dictionary, but remember the order that the items were inserted
# from collections import OrderedDict
# ordered_dict = OrderedDict()
# # ordered_dict = {} # will be just DICT
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1
# print(ordered_dict) # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])


# ========== default dict =========
from collections import defaultdict
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['a']) # 1
# print(d['b']) # 2
# print(d['c']) # 0 - if put in a key that not exist - will return the default value of integer 

# d = defaultdict(float)
# d['a'] = 1
# d['b'] = 2
# print(d['a']) # 1
# print(d['b']) # 2
# print(d['c']) # 0.0 - if put in a key that not exist - will return the default value of integer

# d = defaultdict(list)
# d['a'] = 1
# d['b'] = 2
# print(d['a']) # 1
# print(d['b']) # 2
# print(d['c']) # [] - if put in a key that not exist - will return the default value of integer

# d = {}
# d['a'] = 1
# d['b'] = 2
# print(d['c']) # - error (KeyError: 'c')

# ========= deque ======= (Двусторонняя очередь)
# deque is a double ended queue
# used to add/remove elements from both ends 
from collections import deque
d = deque()

d.append(1)
d.append(2) # deque([1, 2])
d.appendleft(3) # deque([3, 1, 2])
print(d) 

# d.pop() # - remove the last element 
# print(d) # deque([3, 1])

# d.clear() # - remove all elements
# print(d) # deque([])

# d.extend([4,5,6]) # - deque([3, 1, 2, 4, 5, 6]) - extend deque with multiple elements at a time (add all elements at the right side)
d.extendleft([4,5,6]) # deque([6, 5, 4, 3, 1, 2])
print(d) 

# d.rotate(1) # rotate all elements one place to the right  - deque([2, 6, 5, 4, 3, 1])
# d.rotate(2) # deque([1, 2, 6, 5, 4, 3])
d.rotate(-1) # rotate to the left side (use '-')  deque([5, 4, 3, 1, 2, 6])
print(d) 




