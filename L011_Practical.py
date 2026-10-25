from functools import wraps
def announce(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
       print("Calling",function.__name__)
       answer=function(*args,**kwargs)
       print("Finished")
       return answer
    return wrapper

@announce
def triple(n):
    return n*3
print(triple(5))
print(triple(n=2))