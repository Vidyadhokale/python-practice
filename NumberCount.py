list1=[]
frequency={}
count=0
for num in range(10):
    num=int(input("enter 10 numbers:"))
    list1.append(num)
print("List : ",list1)
for num in list1:
    if num in frequency:
        frequency[num]=frequency[num]+1
    else:
        frequency[num]=1
print("Frequency Count : ",frequency)