# # Dictionaries = key/values pair
# mydict = {"name": "Max", "age": 28, "city": "New York"} # declare variant 1
# print(mydict) 

# mydict2 = dict(name='Mary', age=27, city="Boston") # declare variant 2
# print(mydict2)

# value = mydict["age"] # - get 28 (int)
# print(type(value))

# value = mydict["lastname"] # - get error - KeyError: 'lastname'
# print(value)


# ==== ADD ====
# mydict["email"] = "max@mail-address.com" # add new key/value at the end = {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@mail-address.com'}
# print(mydict)

# mydict["email"] = "coolmax@mail.com" # change key/value = {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'coolmax@mail.com'}
# print(mydict)


# === DEL ==== 
# del mydict["name"] # Use del (delete)
# print(mydict)

# mydict.pop("age") # OR use a pop method 
# print(mydict)

# Remove last element: 
# mydict.popitem() # {'name': 'Max', 'age': 28}
# print(mydict)


# === Check if element exist in Dictionary === 
# if "name" in mydict:
#     print(mydict["name"]) # - Max

# try:
#     print(mydict["name"]) # - show Max 
# except:
#     print("Error")


# ==== Get Key ====
# Loop for all dict key: 
# for key in mydict:
#     print(key) # - name / age/ city 

# The same result via .keys Method: 
# for key in mydict.keys():
#     print(key) # - name / age/ city 



# ==== Get Value ====
# for value in mydict.values():
#     print(value) # - Max / 28 / New York

# ==== Get Both (Key/ Value) ====
# for key, value in mydict.items():
#     print(key, value) # - name Max / age 28 / city New York



# ======== Copy dictionary =======
# Bad method: 
# mydict_cpy = mydict # the same dictionary inside the memory 
# print(mydict_cpy) # will be the same Dictionary, but changes in 1st will changes the 2nd :(

# mydict_cpy["email"] = "max@mail.com"
# print(mydict_cpy) # = {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@mail.com'}
# print(mydict) # = {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@mail.com'}


# # Better method 1: 
# mydict_cpy = mydict.copy()
# mydict_cpy["email"] = "max@mail.com"
# print(mydict_cpy) # = {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@mail.com'}
# print(mydict) # = {'name': 'Max', 'age': 28, 'city': 'New York'}

# # Better method 2: 
# mydict_cpy = dict(mydict)
# mydict_cpy["email"] = "max@mail.com"
# print(mydict_cpy) # = {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@mail.com'}
# print(mydict) # = {'name': 'Max', 'age': 28, 'city': 'New York'}


# # ====== Merge two dictionaries ======= 
# my_dict = {"name": "Max", "age": 28, "email": "max@mail.com"}
# my_dict_2 = dict(name='Mary', age=27, city="Boston")

# # City added: 
# my_dict.update(my_dict_2) # {'name': 'Mary', 'age': 27, 'email': 'max@mail.com', 'city': 'Boston'}
# print(my_dict)



# ====== Possible Key types ======= 
my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

#value = my_dict[0] # - KeyError: 0
# value = my_dict[3]
# print(value) # - 9 

# # Tuple in dictionary: 
# mytuple = (8, 7)
# my_dict = {mytuple: 15}
# print(my_dict) # {(8, 7): 15}

# List doesn't work: 
mylist = [8, 7]
my_dict = {mylist: 15} # - TypeError: unhashable type: 'list'
print(my_dict)