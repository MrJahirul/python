# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items=["apple","banana" ,"apple","orange" , "mango"]

items = ["apple","banana","apple","orange","mango"]

for fruite in items:
    if items.count(fruite)>=2:
        print(fruite)
        break
    
    








