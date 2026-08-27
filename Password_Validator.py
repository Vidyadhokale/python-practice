password=input("Enter Your Password:")
has_upper = False
has_lower = False
has_digit = False
has_special_Char=False
for ch in password:
    if ch.isupper():
        has_upper=True
    elif ch.islower():
        has_lower=True
    elif ch.isdigit():
        has_digit=True  
    elif not ch.isalnum():
        has_special_Char=True
if has_upper and has_lower and has_digit and has_special_Char and len(password) >=8 :
    print("Valid Password")
else:
    print("Invalid Password")    