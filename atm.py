bal = 10000
pin = 1321

print("Welcome to Saad Khan ATM System\n")
print("Enter your account no :")
ab = int(input())
print("Enter your pin :")

while 1000:
        pin1 = int(input())
        if pin1 == pin :
            print("Access granted\n")
            print(f"Accont ={ab}")
            break
            

        else:
            print("Access denied\n")
            print("Invalid Pin!\nTry again :")
    
while 1000:
    print("1.Withdraw\n2.Deposit\n3.Show Balance\n0.Exit\n ")
    print("Chhose an option :")
    op = int(input())
    if op == 1:
        print("Enter the ammount you want to withdraw :")
        while 1000:
                wit = int(input())
                if wit > bal:
                    print("Insufficient balance in account!\nTry again :")
                else:
                    print(f"Withdrawn Successfully___\nCurrent balance ={bal-wit}")
                    break
        
    elif op == 2:
        print("Enter the amount to deposit :")
        dep = int(input())
        print(f"Amount deposited successfuly\nNew balance ={bal + dep}")
    
    elif op == 3:
        print(f"The amount you have in your account is {bal}")
    
    elif op == 0:
        break

    else:
        print("Invalid Option !\nTry again \n")

print("Thanks for Using our ATM System________")