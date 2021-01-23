def decorate(func):
    def wrapper():
        print("Before Hello World")
        func()
        print("After Hello World")
    return wrapper

def validate(func):
    def wrapper():
   		print("Validating User")
   		func()
   	return wrapper

@decorate
@validate
def hello_world():
     print("Hello World")

hello_world()

#===============================================================================

def validate(func):
   def wrapper(*args):
      if args[0] < args[1]:
   	   print("Warning: a is less than b")
   	func(*args)
   return wrapper

@validate
def hello_world(int_a, int_b):
   print("Hello World")

hello_world(1, 2)


#===============================================================================

def decorate(func):
   def wrapper():
       print("Before Hello World")
       func()
       print("After Hello World")
   return wrapper

@decorate
def hello_world():
     print("Hello World")

hello_world()


#=========================================================================

def decorate(func):
    def wrapper():
         print("Before Hello World") 
         func()
         print("After Hello World")
    return wrapper

def hello_world():
    print("Hello World")

something = decorate(hello_world)


# without deco--------------------------------------------------------------------
# def add(x, y):
#     print("add is called with parameter {0},{1}".format(x, y))
#     return x + y
#
#
# def sub(x, y):
#     print("sub is called with parameter {0},{1}".format(x, y))
#     return x - y
#
#
# def mul(x, y):
#     print("mul is called with parameter {0},{1}".format(x, y))
#     return x * y
#
#
# print(add(5, 3))
# print(sub(5, 3))
# print(mul(5, 3))



# example with deco ---------------------------------------------------------------
# def my_decorator(func):
#     def wrapper_function(*args):
#         print("{0} is called with parameter {1}".format(func.__name__,args))
#         return func(*args)
#
#     return wrapper_function
#
#
# @my_decorator
# def add(x, y):
#     return x + y
#
#
# @my_decorator
# def sub(x, y):
#     return x - y
#
#
# @my_decorator
# def mul(x, y):
#     return x * y
#
# print(add(5, 3))
# print(sub(5, 3))
# print(mul(5, 3))
#--------------------------------------------------------------------------------------

# meta classs
def debug_function(func):
    def wrapper(*args, **kwargs):
        print("{0} is called with parameter {1}".format(func.__qualname__, args[1:]))
        return func(*args, **kwargs)

    return wrapper


def debug_all_methods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug_function(val))
    return cls


class MetaClassDebug(type):
    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debug_all_methods(obj)
        return obj


class Calc(metaclass=MetaClassDebug):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

calc = Calc()
print(calc.add(2, 3))
print(calc.sub(2, 3))
print(calc.mul(2, 3))







# """Examples of decorators
# See https://realpython.com/primer-on-python-decorators/
# The decorators with dependencies outside of the standard library (Flask
# and Pint) are available in separate files.
# """
#
# import functools
# import time
#
#
# PLUGINS = dict()  # Dictionary used by @register to store plugins
#
#
# def do_twice(func):
#     """Run the decorated function twice"""
#
#     @functools.wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#
#     return wrapper_do_twice
#
#
# def timer(func):
#     """Print the runtime of the decorated function"""
#
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value
#
#     return wrapper_timer
#
#
# def debug(func):
#     """Print the function signature and return value"""
#
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {value!r}")
#         return value
#
#     return wrapper_debug
#
#
# def slow_down_1sec(func):
#     """Sleep 1 second before calling the function"""
#
#     @functools.wraps(func)
#     def wrapper_slow_down(*args, **kwargs):
#         time.sleep(1)
#         return func(*args, **kwargs)
#
#     return wrapper_slow_down
#
#
# def register(func):
#     """Register a function as a plug-in"""
#     PLUGINS[func.__name__] = func
#     return func
#
#
# def repeat(_func=None, *, num_times=2):
#     """Run the decorated function the given number of times"""
#
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#
#         return wrapper_repeat
#
#     if _func is None:
#         return decorator_repeat
#     else:
#         return decorator_repeat(_func)
#
#
# def count_calls(func):
#     """Count the number of calls made to the decorated function"""
#
#     @functools.wraps(func)
#     def wrapper_count_calls(*args, **kwargs):
#         wrapper_count_calls.num_calls += 1
#         print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
#         return func(*args, **kwargs)
#
#     wrapper_count_calls.num_calls = 0
#     return wrapper_count_calls
#
#
# class CountCalls:
#     """Count the number of calls made to the decorated function"""
#
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#         self.num_calls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f"Call {self.num_calls} of {self.func.__name__!r}")
#         return self.func(*args, **kwargs)
#
#
# def slow_down(_func=None, *, rate=1):
#     """Sleep given amount of seconds before calling the function"""
#
#     def decorator_slow_down(func):
#         @functools.wraps(func)
#         def wrapper_slow_down(*args, **kwargs):
#             time.sleep(rate)
#             return func(*args, **kwargs)
#
#         return wrapper_slow_down
#
#     if _func is None:
#         return decorator_slow_down
#     else:
#         return decorator_slow_down(_func)
#
#
# def singleton(cls):
#     """Make a class a Singleton class (only one instance)"""
#
#     @functools.wraps(cls)
#     def wrapper_singleton(*args, **kwargs):
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance = cls(*args, **kwargs)
#         return wrapper_singleton.instance
#
#     wrapper_singleton.instance = None
#     return wrapper_singleton
#
#
# def cache(func):
#     """Keep a cache of previous function calls"""
#
#     @functools.wraps(func)
#     def wrapper_cache(*args, **kwargs):
#         cache_key = args + tuple(kwargs.items())
#         if cache_key not in wrapper_cache.cache:
#             wrapper_cache.cache[cache_key] = func(*args, **kwargs)
#         return wrapper_cache.cache[cache_key]
#
#     wrapper_cache.cache = dict()
#     return wrapper_cache
#
#
# def set_unit(unit):
#     """Register a unit on a function"""
#
#     def decorator_set_unit(func):
#         func.unit = unit
#         return func
#
#     return decorator_set_unit
#
# """Examples using decorators
# See https://realpython.com/primer-on-python-decorators/
# This file contains code for many of the examples in the text. You can
# find the decorators themselves in the decorators.py file.
# """
#
# from datetime import datetime
# import functools
# import math
# import random
#
# from decorators import (
#     cache,
#     count_calls,
#     debug,
#     do_twice,
#     PLUGINS,
#     register,
#     set_unit,
#     singleton,
#     slow_down,
#     timer,
# )
#
#
# # First-Class Objects
# def say_hello(name):
#     return f"Hello {name}"
#
#
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
#
#
# # Returning Functions From Functions
# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
#
# # Simple Decorators
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass  # Hush, the neighbors are asleep.
#
#     return wrapper
#
#
# # Syntactic Sugar!
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
#
# # Reusing Decorators
# @do_twice
# def say_whee_twice():
#     print("Whee!")
#
#
# # Returning Values From Decorated Functions
# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"
#
#
# # A Few Real World Examples
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before.
#         value = func(*args, **kwargs)
#         # Do something after.
#         return value
#
#     return wrapper_decorator
#
#
# # Timing Functions
# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i ** 2 for i in range(10000)])
#
#
# # Debugging Code
# @debug
# def make_greeting(name, age=None):
#     if age is None:
#         return f"Howdy {name}!"
#     else:
#         return f"Whoa {name}! {age} already, you are growing up!"
#
#
# # Apply a decorator to a standard library function
# math.factorial = debug(math.factorial)
#
#
# def approximate_e(terms=18):
#     return sum(1 / math.factorial(n) for n in range(terms))
#
#
# # Slowing Down Code (Revisited)
# @slow_down
# def countdown(from_number):
#     if from_number < 1:
#         print("Liftoff!")
#     else:
#         print(from_number)
#         countdown(from_number - 1)
#
#
# # Registering Plugins
# #
# # The names of the plugins have been changed from the text to avoid name
# # clashes with earlier examples
# @register
# def say_hi(name):
#     return f"Hi {name}"
#
#
# @register
# def be_cool(name):
#     return f"Yo {name}, together we are the coolest!"
#
#
# def randomly_greet(name):
#     greeter, greeter_func = random.choice(list(PLUGINS.items()))
#     print(f"Using {greeter!r}")
#     return greeter_func(name)
#
#
# # Example Using Built-in Class Decorators
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#
#     @property
#     def radius(self):
#         """Get value of radius"""
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         """Set radius, raise error if negative"""
#         if value >= 0:
#             self._radius = value
#         else:
#             raise ValueError("Radius must be positive")
#
#     @property
#     def area(self):
#         """Calculate area inside circle"""
#         return self.pi() * self.radius ** 2
#
#     def cylinder_volume(self, height):
#         """Calculate volume of cylinder with circle as base"""
#         return self.area * height
#
#     @classmethod
#     def unit_circle(cls):
#         """Factory method creating a circle with radius 1"""
#         return cls(1)
#
#     @staticmethod
#     def pi():
#         """Value of π, could use math.pi instead though"""
#         return 3.141_592_653_5
#
#
# # Decorating Classes
# class TimeWaster:
#     @debug
#     def __init__(self, max_num):
#         self.max_num = max_num
#
#     @timer
#     def waste_time(self, num_times):
#         for _ in range(num_times):
#             sum([i ** 2 for i in range(self.max_num)])
#
#
# # Nesting Decorators
# @do_twice
# @debug
# def greet(name):
#     print(f"Hello {name}")
#
#
# # Creating Singletons
# @singleton
# class TheOne:
#     pass
#
#
# # Caching Return Values
# @cache
# @count_calls
# def fibonacci(num):
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# @functools.lru_cache(maxsize=4)  # lru_cache is preferred to rolling your own
# def fibonacci_lru(num):
#     print(f"Calculating fibonacci({num})")
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# # Adding Information About Units
# @set_unit("cm^3")
# def volume(radius, height):
#     return math.pi * radius ** 2 * height
