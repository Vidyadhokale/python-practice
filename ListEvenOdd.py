list1=[]
even=[]
odd=[]
for num in range(10):
    num=int(input("Enter 10 Numbers:"))
    list1.append(num)
    if num % 2==0:
        even.append(num)
    else:
        odd.append(num)
print("List : ",list1)
print("Even : ",even)
print("Odd : ",odd) 
