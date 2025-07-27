orig = 223344
print("Enter your password :")
for i in range(3):
    pas = int(input())
    if(pas == orig):
        print("Access Granted")
        break
    else:
        print("Access Denied\nTry again :")
else:
    print("Account blocked due to many wrong attempts")