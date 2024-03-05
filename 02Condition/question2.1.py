userAge=int(input("Enter Your Age: "))
day=input("Enter Your Booking Date: ")

Prize=12 if userAge>=18 else 8
if day=="Wednesday":
    Prize=Prize-2;
print("Your Ticket Prize is $",Prize)