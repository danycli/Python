fib = int(input("Enter a number :"))
# yes = 1

for i in range(0,fib):
    if(i <=2):
        yes = 1
    i = (fib-1) + (fib-2)
    print(i)