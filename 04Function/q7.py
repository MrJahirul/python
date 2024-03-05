# Problem: Write a function that takes variable number of arguments and returns their sum.

def sums(*args):
    return sum(args)

print(sums(1,2,3,4))
print(sums(5,6))