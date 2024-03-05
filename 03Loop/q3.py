#Problem: Reverse a string using a loop.

str=input("Enter a string:")
Reverse=""

for i in str:
    Reverse=i+Reverse
print(Reverse)