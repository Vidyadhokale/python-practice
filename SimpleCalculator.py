No1=int(input("Enter First Number:"))
No2=int(input("Enter Second Number:"))
while(True):
    print("***__Simple Calculator__***")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        print("Addition:",No1+No2)
    elif ch==2:
        print("Subtraction:",No1-No2)
    elif ch==3:
        print("Multipliction:",No1*No2)
    elif ch==4:
        print("Division:",No1/No2)
    else:
        print("Invalid Choice")
        break