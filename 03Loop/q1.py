# Problem: Given a list of numbers, count how many are positive numbers.
# numbers=[1,-2,3,-4,5,6-7,-8,9,10]

numbers=[1,-2,3,-4,5,6-7,-8,9,10]
# myArr=[]
# for i in numbers:
#     if i>=0:
#        myArr.append(i)   
# print("Total posative number is :",len(myArr))  

posative=0
for num in numbers:
    if num>0:
        posative+=1
print("Total posative number is :",posative)
        
        



        
  


