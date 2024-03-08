# import time

# def fast(func):
#     cache_value={}
#     def wrapper(*args,**kwargs):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args,**kwargs)
#         cache_value[args]=result
#         return result

#     return wrapper

# @fast
# def time_fun(a,b):
#     time.sleep(5)
#     return a+b


# print(time_fun(2,3))
# print(time_fun(2,3))


import time

def tool(fun):
    cache_value={}
    def wrapper(*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        result=fun(*args,**kwargs)
        cache_value[args]=result
        return result
    return wrapper

@tool
def printGreet(name):
    time.sleep(5)
    print(f"Hello Mr {name}")


printGreet("Panda")