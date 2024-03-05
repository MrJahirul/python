#Problem: Check if a password is "Weak", "Medium" j or "Strong", Criteria: < 6 chars (Weak), 6-10 chars (Medium), chars (Såong).

password=input("Enter Your Password: ")

if len(password)<6:
    print("Weak")
elif len(password)>=6 and len(password)<=10:
    print("Medium")
else:
    print("Strong")