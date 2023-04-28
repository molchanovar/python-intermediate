 # Ordered, immutable, text representation 

# my_string = "Hello World"
# my_string = 'I\'m a programmer' # - #Escaping

# my_string = """Hello 
# World""" # use for multiline
# my_string = """Hello \
# World""" # \ show on one line

#my_string = "Hello World"
#char = my_string[0] # - H
#char = my_string[-1] # - d (last symbol)

# 'str' object does not support item assignment
#my_string[0] = 'h' # will be error
#print(char)


# ======== Slices ========
# my_string = "Hello World"
# #substring = my_string[1:5] # - 'ello'
# substring = my_string[:] # - Hello World
# substring = my_string[::2] # step - 'HloWrd'
# substring = my_string[::-1] # step - 'dlroW olleH' - allow easy reverse string 
# print(substring)


# ======= Concatenate =======
# greeting = "Hello"
# name = "Tom"
# sentence = greeting + " " + name # = Hello Tom

# greeting = "Hello"
# for i in greeting:
#     print(i) # H e l l o (by element)
# print(sentence) 

# if 'ell' in greeting:
#     print('yes') # show 'yes'
# else:
#     print('no') 


# ===== More usefull methods ====== 
# 1. Remove whitespace - .strip
# my_string = '      Hello World     '
# my_string = my_string.strip() # whitespace is gone 

# !!!  my_string.strip() - because 'str' immutable, .strip doesn't change original string !!!
# print(my_string) 

# 2. Upper
# my_string = "Hello World"
# print(my_string.upper()) # show - 'HELLO WORLD'
# print(my_string.lower()) # show - 'hello world'
# print(my_string.startswith('Hello')) # show - True (start with 'Hello')
# print(my_string.startswith('World')) # False
# print(my_string.endswith('World')) # True (end with 'World')
# print(my_string.find('o')) # Show index of symbol - 4
# print(my_string.find('lo')) # = 3
# print(my_string.find('pp')) # = -1

# print(my_string.count('p')) # = 0
# print(my_string.replace('World', 'Universe')) # Hello Universe
# print(my_string.replace('Worrrld', 'Universe')) # Show original - Hello Universe


# 3. List and Strings: 
# my_sting = 'how are you doing'
# my_list = my_sting.split() # ['how', 'are', 'you', 'doing']

# my_sting = 'how,are,you,doing'
# my_list = my_sting.split(',') # ['how', 'are', 'you', 'doing']
# print(my_list)

# Concatinating: 
# !join elements of list into string!
# my_sting = 'how,are,you,doing'
# my_list = my_sting.split(',') # ['how', 'are', 'you', 'doing']
# new_string = ''.join(my_list) # howareyoudoing
 # new_string = ' '.join(my_list) # how are you doing
# print(new_string)

# ============ USE join ===================
# from timeit import default_timer as timer 
# #my_list = ['a'] * 6 # ['a', 'a', 'a', 'a', 'a', 'a']
# my_list = ['a'] * 1000000 # ['a', 'a', 'a', 'a', 'a', 'a']

# # === BAD === 
# # (Very expensive operation) because will create a new string here and then assign back to original string 
# start = timer()
# my_string = ''
# for i in my_list:
#     my_string += i  # aaaaaa
# stop = timer()
# print(stop-start) # 9.199474916007603

# # === GOOD === 
# # Much faster: 
# start = timer()
# my_string = ''.join(my_list) # aaaaaa
# stop = timer()
# print(stop-start) # 0.004075624994584359
# ============================================


# ===== Formating =====
# %, .format(), f-Strings 

# 1. OLD Format (%)
# var = "Tom"
# my_string = "the variable is %s" % var  # placeholder with a string here 
# print(my_string) # the variable is Tom

# var = 4
# my_string = "the variable is %d" % var  # %d for decimal values 
# print(my_string) # the variable is 4

# var = 3.12345
# my_string = "the variable is %.2f" % var  # %f for floating values  (2 digits after a point)
# print(my_string) # the variable is 3.12

# 2. New format - .format()
# var = 3.12345
# var2 = 6 
# my_string = "the variable is {}".format(var) # the variable is 3.12345
# my_string = "the variable is {:.2f}".format(var) # the variable is 3.12
# my_string = "the variable is {:.2f} and {}".format(var,var2) # the variable is 3.12 and 6
# print(my_string)

# 3. Another format - f-Strings 
# !RECOMMEND USE this format!
var = 3.12345
var2 = 6 
my_string = f"the variable is {var} and {var2}"
my_string2 = f"the variable is {var*2} and {var2}" # the variable is 6.2469 and 6
print(my_string)
print(my_string2)