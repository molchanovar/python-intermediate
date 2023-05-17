## it allows you to add new functionality to an existing function 
## function in python are first class objects 
## Like any other object, they can be defined inside another function passed as an argument to another function 

# @mydecorator  
# def dosomething():
#     pass


# =======Closer look========
# def start_end_decorator(func):
    
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper


# # def print_name():
# #     print('Alex')
# @start_end_decorator
# def add5(x):
#     return x + 5

# add5(10) # TypeError: start_end_decorator.<locals>.wrapper() takes 0 positional arguments but 1 was given
# To fix it - use args / kwargs 
# Will show - Start/End

# result = add5(10)
# print(result) # Start/End/15

#print_name = start_end_decorator(print_name)
#print_name()


# === Function identity ===
# import functools
 
# # def start_end_decorator(func):

# def my_decorator(func):   

# # This is a template for a decorator that can be use for all func decorators 
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do ...
#         result = func(*args, **kwargs)
#         # Do ...
#         return result
#     return wrapper

# @start_end_decorator 
# def add5(x):
#     return x + 5

# # print(help(add5))
# # print(add5.__name__) # pyhton got confused  about the identity of this function 
# # Help on function wrapper in module __main__:
# # wrapper(*args, **kwargs)

# print(add5.__name__) # Help on function add5 in module __main__: add5(x)



# ==== More examples ====
### 1. 
# import functools

# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=4)
# def greet(name):
#     print(f'Hello {name}')

# greet('Alex') # Hello Alex - 4 times 


# ### 2. 
# import functools
# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper

# # This debug decorator extracts the name and the argument
# # and the keyword arguments and then prints information of func
# # it executes the func and give info about the return value 
# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper

# @debug
# @start_end_decorator
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting

# say_hello('Alex') # see below the steps of execution: 
# # 1. execute the debug function 
# # 2. then inside the debug function, will exec the start and decorator function 
# # 3. inside this func - exec say_hello func

# == Show output of exec ==
# Calling say_hello('Alex')
# Start
# Hello Alex
# End
# 'say_hello' returned 'Hello Alex'



# ===== Class decorators ====== 
## keep track of how many times I have exec this func (self.num_calls)

## Inner functions, also known as nested functions, are functions that you define inside other functions

class CountCalls:

    def __init__(self, func):
        self.func = func 
        self.num_calls = 0 

    # implement the call method: 
    def __call__(self, *args, **kwargs):
        # print('Hi there')
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

# cc = CountCalls(None)
# cc()

@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()
say_hello() # This is executed 3 times / Hello



# === Typical use cases of decorators ===
# 1. Timer decorator (exec time of a func)
# 2. Debug decorator (print more information about called function and its args)
# 3. Check decorator (check if the args fullfill some reqs and the depth behavior accordingly)
# 4. Cache the return values 
# 5. Add information or update the state


