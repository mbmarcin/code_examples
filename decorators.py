# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
# #say_whee = my_decorator(say_whee)
#
# say_whee()


# -------------------------------------------------------------------------------------


# from datetime import datetime
#
#
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 21:
#             func()
#         else:
#             print('psst!')  # Hush, the neighbors are asleep
#
#     return wrapper
#
#
# @not_during_the_night
# def say_whee():
#     print("Whee!")
#
# say_whee()

# -----------------------------------------------------------------------------------

# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
#
#     return wrapper_do_twice
#
# @do_twice
# def say_whee():
#     print("Whee!")
#
# say_whee()

# Decorating Functions With Arguments----------------------------------------------------

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper_do_twice


# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
# @do_twice
# def say_whee():
#     print("Whee!")
#
# say_whee()
# greet('mm')


# Returning Values From Decorated Functions

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#
#     return wrapper_do_twice
#
#
# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"
#
#
# print(return_greeting('adam'))

#example--------------------------------------------
# import functools
#
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(100)











