#prime Number

number=int(input("Enter a number: "))
for i in range(2,number):
    if number%i==0:
        print("Not")
        break
    else:
        print("Yes")
        break