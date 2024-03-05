#leap year or not

year=int(input("Enter Year what you want to check: "))

if (year%400==0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not")