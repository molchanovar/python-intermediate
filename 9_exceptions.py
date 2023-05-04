# Errors and Exceptions

## == syntax error === 
# a = 5
# print(a)) # SyntaxError: unmatched ')'


## === type error === 
# a = 5 + '10'
# print(a) # TypeError: unsupported operand type(s) for +: 'int' and 'str'


## === ModuleNotFoundError === 
# import somemodule  # ModuleNotFoundError: No module named 'somemodule'


## === NameError === 
# a = 5
# b = c # NameError: name 'c' is not defined


# === FileNotFoundError === 
# f = open('somefile.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'
 

# === list ===
# a = [1, 2, 3]
# #a.remove(4) 
# # print(a) # ValueError: list.remove(x): x not in list

# a[4]
# print(a) # IndexError: list index out of range


#  # === dict === 
# my_dict = {'name': 'Max'}
# my_dict['age'] # KeyError: 'age' (not inside in dictionary)



# === Raising an exception ===
# x = -5 
# if x < 0: 
#     raise Exception('x should be positive') # Exception: x should be positive


# === Assert statements === 
# x = -5 
# assert(x>=0), 'x is not positive' # AssertionError: x is not positive (an assertion error if assertion is True)


# # === try === 
# # Programm doesn't stop here, will continue with line ('an error happened'), may catch specify exception 
# try:
#     a = 5 / 1 # ZeroDivisionError: division by zero
#     # b = a + '10'
#     b = a + 4
# # except:
# #     print('an error happened')
# # except Exception as e:
# #     print(e) # division by zero / the same above 
# except ZeroDivisionError as e:
#     print(e) # division by zero
# except TypeError as e:
#     print(e) # unsupported operand type(s) for +: 'float' and 'str'
# else: 
#     print('everything is fine')
# finally: 
#     print('clearning up ...')




# ==== How define our own exception ====
class ValueTooHighError(Exception): 
    pass 

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5: 
        raise ValueTooSmallError('value is too small', x)

try: 
    # test_value(200) # ValueTooHighError: value is too high
    test_value(1) # ValueTooHighError: value is too high
except ValueTooHighError as e:
    print(e) # value is too high
except ValueTooSmallError as e:
    print(e.message, e.value) # value is too small 1

