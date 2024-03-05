# yeld

# def fun_generator():
#     yield "Hello world!!"
#     yield "Geeksforgeeks"

# obj = fun_generator()
# print(type(obj))  # Output: <class 'generator'>
# print(next(obj))  # Output: Hello world!!
# print(next(obj))  # Output: Geeksforgeeks


def even_generator(limit):
    for i in range(2,limit,2):
        yield i
for num in even_generator(10):
    print(num)


