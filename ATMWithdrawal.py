print("Welcome To ATM")
balance=10000;
while(True):
    print("1.Check Balance")
    print("2.Withdraw")
    print("3.Remaining Amount")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        print("Your Current Balance is:",balance)
    elif ch==2:
        withdraw=int(input("Enter withdraw Amount:"))
        balance=balance-withdraw
        print("Withdraw Succesfully")
    elif ch==3:
        print("Remaining Amount:",balance)
    else:
        print("Invalid Choice")
        print("Thank You")
        break;