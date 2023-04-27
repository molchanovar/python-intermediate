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
my_string = "Hello World"
print(my_string.upper()) # show - 'HELLO WORLD'
print(my_string.lower()) # show - 'hello world'
print(my_string.startswith('Hello')) # show - True (start with 'Hello')
print(my_string.startswith('World')) # False
print(my_string.endswith('World')) # True (end with 'World')
print(my_string.find('o')) # Show index of symbol
