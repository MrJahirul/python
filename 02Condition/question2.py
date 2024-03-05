# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone
# gets a $2 discount on Wednesday.

userAge=int(input("Enter Your Age: "))
day=input("Enter Your Booking Date: ")
day.lower()

if(userAge>=18):
    if(day=="wednesday"):
        print("Orginal Prize $12 \n Discount $2 \n Payable Money $10")
    else:
        print("Your Ticket Prize $12")
elif(userAge>=0 and userAge<18):
    if(day=="wednesday"):
        print("Orginal Prize $8 \n Discount $2 \n Payable Money $6")
    else:
        print("Your Ticket Prize $8")
else:
    print("Enter Valid Date")
