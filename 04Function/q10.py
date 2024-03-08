# Problem: Create a recursive function to calculate the factorial of a number.

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

def recur_fun(n):
    if n==0:
        return 1
    else:
        return n*recur_fun(n-1)

print(recur_fun(5))