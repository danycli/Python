print("Enter your password :")
while 1:
    orig = 12345
    pas = int(input())
    if(pas == orig):
        print("Access Granted!")
        break
    else:
        print("Access denied\nTry Again :")