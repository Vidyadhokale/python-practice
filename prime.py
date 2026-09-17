n=int(input("Enter Number:"))
is_prime=False
for i in range(2,n):
    if n % i==0:
        is_prime=False
        break
    else:
        is_prime=True
    if is_prime:
        print("prime :",n)
    else:
        print("Not Prime :",n)
