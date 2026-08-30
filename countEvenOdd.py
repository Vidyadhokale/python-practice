numbers=[2,3,1,4,5,6,7,8,9,10,12]
Evencount=0
OddCount=0
for n in numbers:
    if n%2==0:
        Evencount=Evencount+1
    else:
        OddCount=OddCount+1
print("Even Numbers Count:",Evencount)
print("Odd Numbers Count:",OddCount)