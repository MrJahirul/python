# Problem: Assign a letter grade based on a studentis score: A (90-100), B (80-89), C (70-79), D (60-69), F
# (below 60).

grade=int(input("Enter Your Number: "))
if (grade>=90 and grade<=100):
    print("A GRADE")
elif (grade>=80 and grade<=89):
    print("B GRADE")
elif (grade>=70 and grade<=79):
    print("C GRADE")
elif (grade>=60 and grade<=69):
    print("D GRADE")
else:
    print("F GRADE")