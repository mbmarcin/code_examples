1. Unpacking Array Items

first_name, last_name = ['Farhad', 'Malik']
print(first_name) #It will print Farhad
print(last_name) #It will print Malik

2. Swapping Variables

first_name, last_name = ['Farhad', 'Malik']
last_name, first_name = first_name, last_name
print(first_name) #It will print Malik
print(last_name) #It will print Farhad

3. Using Global Variable

my_global_variable = True
def some_function():
  global my_global_variable
  my_global_variable= False
some_function()
print(my_global_variable) <--Returns False

4. Repeat String
'A'*3 will repeat A three times:  AAA

5. Slicing
y = 'Abc'
y[:2] = ab
y[1:] = bc
y[:-2] = a
y[-2:] = bc

6. Reversing
x = 'abc'
x = x[::-1]

7. Negative Index
y = 'abc'
print(y[-1]) # will return c

8. Intersect Sets
a = {1,2,3}
b = {3,4,5}
c = a.intersection(b)

9. Difference In Sets
a = {1,2,3}
b = {3,4,5}
c = a.difference(b)


10. Union Of Collections
a = {1,2,3}
b = {3,4,5}
c = a.union(b)

11. Optional Arguments

def my_new_function(my_value='hello'):
  print(my_value)

#Calling
my_new_function() => prints hello
my_new_function('test') => prints test

12. Unknown Arguments Using *arguments
def myfunc(*arguments):
  return a
myfunc(a)
myfunc(a,b)
myfunc(a,b,c)

13. Dictionary As Arguments Using **arguments
def myfunc(**arguments):
  return arguments['key']

14. Function With Multiple Outputs
resultA, resultB = get_result()
get_result() can return ('a', 1) which is a tuple

15. One Liner For Loops
[Variable] AggregateFunction([Value] for [item] in [collection])

16. Combining Lists Using Zip
name = 'farhad'
suffix = [1,2,3,4,5,6]
zip(name, suffix)
--> returns (f,1),(a,2),(r,3),(h,4),(a,5),(d,6)

17. Free up Memory
import gc
collected_objects = gc.collect()


18. Add Logging To Functions Using Decorators
def my_logger(function):
   
    @functools.wraps(function)
    def logger(*args, **kwargs):
        print(function.__name__)
        return function(*args, **kwargs)
    return logger

#Now use it in your functions:

@my_logger
def hi():
  print 'hi'
@my_logger
def bye(a):
  print 'bye' + a

19. Unzipping
name = 'farhad'
suffix = [1,2,3,4,5,6]
result = zip(name, suffix)
--> returns (f,1),(a,2),(r,3),(h,4),(a,5),(d,6)
unzipped = zip(*result)

21. Memory Footprint Of An Object
import sys 
x = 'farhadmalik'
print(sys.getsizeof(x))

22. Print Current Directory
import os
print(os.getcwd())

