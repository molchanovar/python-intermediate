# Sets - Not allowed duplicates elements
# unorder, mutable, no duplicates

# myset = {1, 2, 3} # - {1, 2, 3}
#myset = {1, 2, 3, 1, 3}  # {1, 2, 3} too 

# myset = set("Hello") # - {'e', 'H', 'o', 'l'}
# print(myset)

#myset = {} # - dict
# myset = set() # - set 
# print(type(myset))



# ==== Mutable =====
# myset = set() # - set 

# myset.add(1)
# myset.add(2)
# myset.add(3) # - {1, 2, 3}

#myset.remove(2) # remove exact element (key) - {1, 3}
#myset.discard(3) # - the same (remove) - {1, 2}, but if element doesn't exist - no error
#myset.clear() # remove all elements - set()
#print(myset.pop()) # show 1 -> the set will be {2, 3}

# for i in myset:
#     print(i) # - show 1 2 3 

# if 1 in myset:
#     print("yes") # - show yes

#print(myset)


# ======== Union and Intersection =========
# Union combines elements from both from two sets without duplication 
# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds.union(evens) # - {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(u)

# i = odds.intersection(evens) # no intersection - will be empty = set()
# print(i)

# i = odds.intersection(primes) # {3, 5, 7} 
# print(i)

# i = evens.intersection(primes) # {2}
# print(i)

# ========== Calculates ============
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# diff = setA.difference(setB) # - {4, 5, 6, 7, 8, 9} !!! only from 4 to 9
# print(diff)

# diff = setB.difference(setA) # - {10, 11, 12}
# print(diff)

# diff = setB.symmetric_difference(setA) # - {4, 5, 6, 7, 8, 9, 10, 11, 12} 
# print(diff)

# ===== Modified original sets ======
# setA.update(setB) # add element from anoth er set - {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# print(setA)

# setA.intersection_update(setB) # {1, 2, 3}
# print(setA)

# setA.difference_update(setB) # {4, 5, 6, 7, 8, 9} - update, by removing elements find in another set  
# print(setA)


# setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# setC = {7, 8}

# issubset means - all the elements of our  1st set are also in 2nd set. 
#setA.issubset(setB) # - False
#print(setA.issubset(setB))
 
#print(setB.issubset(setA)) # True // because all element of setB exist in 1st 

# === superset ===
#print(setB.issuperset(setA)) # False // superset returns TRUE if the 1st set contains all the number of 2nd 
# print(setA.issuperset(setB)) # True 

# print(setA.isdisjoint(setB)) # False // they have the same elements 
# print(setA.isdisjoint(setC)) # True // elements are different


# ====== Copy =======
# setA = {1, 2, 3, 4, 5, 6}

# # setB = setA # Bad - memory assing the same  
# # print(setB)

# setB = set(setA)
# print(setB) # copy with new mem assighnment 



# ====== Frozen Set =======
# inmutable variant of original Set

a = frozenset([1, 2, 3, 4])

#a.add(2) # error - 'frozenset' object has no attribute 'add'
a.remove(1) # - 'frozenset' object has no attribute 'remove'

print(a)