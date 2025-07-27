operator = int (input("Enter your desired operation\n1.+\n2.-\n3./\n4.*\nChoose :"))


if operator >4 or operator <1:
    print("Invalid number")
    exit()

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))

if operator == 1:
    print("The sum of",first, "&",second," is",second+first)
elif operator == 2:
    print("The subtraction of ",first,"&",second,"is ",first-second)
elif operator == 3:
    print("The division of ",first,"&",second," is ",first/second)
elif operator == 4:
    print("The multiplication of",first,"&",second," is ",first*second)

