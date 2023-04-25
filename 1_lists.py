#myList = ["banana", "cherry", "apple"]
#print(myList)

# Length on List: 
# print(len(myList))

# Add into List
# myList.append("lemon")
# print(myList)

# myList.insert(1, "blueberry")
# print(myList)

# Remove last element: 
# item = myList.pop()
# print(item)
# print(myList)

# Remove named element: 
# item = myList.remove("cherry")
# print(myList)

# Remove all elements in List: 
# item = myList.clear()
# print(myList)

# Sort list 
# item = myList.sort()
# print(myList)

# Create new sorted List 
# new_list = sorted(myList)
# print(myList)
# print(new_list)

# ======================= Operations with two Lists ==================
# myList = [0] * 5
# print(myList)

# myList2 = [1, 2, 3, 4, 5]

# new_list = myList + myList2
# print(new_list) # - [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]

# ======= Slices ========
#myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a = myList[1:5] # - [2, 3, 4, 5] 
# a = myList[:5] # - [1, 2, 3, 4, 5]
# a = myList[1:] # - [2, 3, 4, 5, 6, 7, 8, 9]
#a = myList[1::2] # - [2, 4, 6, 8] - add step 
#a = myList[::2] # - [1, 3, 5, 7, 9]
#a = myList[::-1] # - [9, 8, 7, 6, 5, 4, 3, 2, 1]
#print(a)

# list_org = ["banana", "cherry", "apple"]

#list_cpy = list_org # the same place in memory = ['banana', 'cherry', 'apple', 'lemon']
#list_cpy.append("lemon") # append to org list too 
 
# list_cpy = list_org.copy() # append only to list_cpy
# list_cpy.append("lemon") 

# list_cpy = list_org[:] # append only to list_cpy too 
# list_cpy.append("lemon") 

# print(list_org)
# print(list_cpy) 

# ======== Advance technique ========= 
# Expression on 1 line: 
myList = [1, 2, 3, 4, 5, 6]
b = [i*i for i in myList] 

print(myList) # - [1, 2, 3, 4, 5, 6]
print(b) # - [1, 4, 9, 16, 25, 36]