#A function can be stored in a variable.
def say_hello():
    print("Hello!")
greet=say_hello
greet()
#A function can be passed into another function
def run_twice(func):
    func()
    func()

run_twice(say_hello)

#A function can return another function

def make_greeter():
    def greeter():
        print("Hello from inside!")
    return greeter

my_func = make_greeter()
my_func()

#All above together

def add_lines(func):    #decorator
    def wrapper():      #wrapper
        print("--- start ---")
        func()          #original
        print("--- end ---")
    return wrapper

say_hello = add_lines(say_hello)  #decorator[@add_lines    def say_hello(say_hello)]
say_hello()

#@ shortcut & with input
def add_lines1(function):
    def wrapper1(name):
        print("--- start ---")
        function(name)
        print("--- end ---")
    return wrapper1

@add_lines1             #decorator[gteet()=add_lines1(greet)    greet(name)]
def greet(name):
    print("Hello!", name)

greet("Ali")

# Step 8: wrapper that accepts any number of inputs
def add_lines2(function):
    def wrapper2(*args):
        print("--- start ---")
        function(*args)
        print("--- end ---")
    return wrapper2

@add_lines2
def add_numbers(a, b):
    print("Sum is", a + b)

add_numbers(3, 4)

# Step 9: the wrapper must return the result
def add_lines3(function):
    def wrapper3(*args,**kwargs):     #**kwargs for step 10 error correction
        print("--- start ---")
        answer=function(*args,**kwargs) 
        print("--- end ---")
        return answer
    return wrapper3

@add_lines3
def square(n):
    return n * n

result = square(5)
print("Result is", result)

# Step 10: experiment - calling with keyword arguments
@add_lines3
def full_name(first, last):
    return first + " " + last

print(full_name(first="Ali", last="Khan"))
print(full_name.__name__)   #.__name__ reads the name tag of whatever function the name currently points to.

import time
from functools import wraps

def timer(function):
    @wraps(function)
    def timer_wrapper(*args, **kwargs):
        start = time.time()
        answer = function(*args, **kwargs)
        end = time.time()
        print("Took", round(end - start, 2), "seconds")
        return answer
    return timer_wrapper

@timer
def slow_task(seconds):
    time.sleep(seconds)
    return "Done"

print(slow_task(2))

# Step 12: what is the name of a decorated function?
print(slow_task.__name__)