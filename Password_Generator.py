import random
upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters=upper_letters.lower()
digits="0123456789"
symbols="@#$*?+-%^ "

upper,lower,nums,syms=True,True,True,True
all =""
if upper:
    all+=upper_letters
if lower:
    all+=lower_letters
if nums:
    all+=digits
if syms:
    all+= symbols

length =int(input("Enter the length of the passwords:"))
amt=int(input("Number of passwords you wish to generate: "))

if(length==0 or amt==0):
    print("Enter valid length and number of passwords to be generated.")


for x in range(amt):
    password= "".join(random.sample(all,length))
    print(password)
