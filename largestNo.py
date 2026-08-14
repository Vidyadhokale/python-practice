n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print(f"{n1} is Largest Number")
elif n2>n1 and n2>n3:
    print(f"{n2} is Largest Number")
else:
    print(f"{n3} is Largest Number")