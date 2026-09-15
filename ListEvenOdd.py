list1=[]
even=[]
odd=[]
for num in range(10):
    num=int(input("Enter 10 Numbers:"))
    list1.append(num)
print("List : ",list1)
if num % 2==0:
    even.append(num)
else:
    odd.append(num)
print("Evenv : ",even)
print("Odd : ",odd) 