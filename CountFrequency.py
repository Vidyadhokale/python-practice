numbers=[2,3,2,5,3,2,7,5]
frequency={}
for n in numbers:
    if n in frequency:
        frequency[n]= frequency[n] +1
    else:
        frequency[n]=1
print(frequency)