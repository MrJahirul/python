# Age Group Categorization
# Classify a person's age group: Child (<13)
# Teenager (13—19), Adult (20—59), Senior (60+) 

userAge=int(input("Enter Your Age: "))
if(userAge>=0 and userAge<13):
    print("Child")
elif(userAge>=13 and userAge<=19):
    print("Teenager")
elif(userAge>=20 and userAge<=59):
    print("Adult")
elif(userAge>=60):
    print("Senior")
else:
    print("Enter Valid Age")
