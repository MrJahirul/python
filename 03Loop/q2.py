#Problem: Calculate the sum of even numbers up to a given number n.

number=int(input("Enter your Range:"))
count=0
for i in range(number+1):
    if i%2==0:
        count+=i
print(count)
    
