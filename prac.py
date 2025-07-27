# print("Hi how are you.")

# a = 10
# b = 19.5
# c = "Dany"
# print((c),"has",(a)+(b),"coins")

# '''Hi how are you'''
# """Hi how are you""" Multiple line string representation


#Basic Calculator...
# op = int(input("Enter the operation you want to perform\n1.+\n2.-\n3./\n4.*\nChoose :"))

# while op>4 or op <1:
#     op = int (input ("Invalid Operation!\nTry Again\nChoose (1-4):"))

# num1 = int (input("Enter first number :"))
# num2 = int (input("Enter second number :"))

# if op == 1:
#     print("The sum of",(num1),"&",(num2),"is",(num1+num2))
# if op == 2:
#     print("The Subtraction of",(num1),"&",(num2),"is",(num1-num2))
# if op == 3:
#     print("The Division of",(num1),"&",(num2),"is",(num1/num2))
# if op == 4:
#     print("The Multiplication of",(num1),"&",(num2),"is",(num1*num2))

# pas = input("Enter password :")
# p = "1234"

# while pas!=p:
#     pas = input("Incorect password.\nAccess Denied...\nTry again!\n....")

# print("Access Granted.....")

# n = int(input("Enter a number :"))
# if n%2==0:
#     print("Even")
# else :
#     print("Odd")

# n = int(input("Enter a number :"))
# for i in range(n):
#     if i%2 == 0:
#         print(i)
#     i = i - 1

# year = int(input("Enter year :"))
# if year%4==0:
#     if year%100!=0 or year%400==0:
#         print("Year is leap")
#     else:
#         print("Year is not leap")
# else:
#     print("Year is not leap")

# x = "Weak ass bitch"
# print(len(x))

# a = "DANY"
# b = a[::-1]
# print(b)

# a = "dany"
# b = 'z' + a[1:]
# print(b)

# i = "danial ahmed"
# print(i[::2])

# st = input("Enter first string :")
# st2 = input("Enter second string :")
# st3 = st[:2] + st2[2:]
# st4 = st2[:2] + st[2:]
# print(st3," ",st4)

# a = int(input("Enter a number :"))
 
# for i in range(2,a):
#     if a%1 == 0:
#         print("Not a Prime number")
#     else:
#         print("A prime number")

# for i in range(1,9):
#     print() 
#     print()
#     for j in range(1,11):
#         print(f"{i}x{j}={i*j}")
# print()    

# max = 0
# for i in range(0,4):
#     a = int(input(f"Enter {i} number"))
#     if a > max:
#         max = a
    
# print(max)

# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             print("Not Prime")
#         else:
#             print("Prime")

# i = int(input("Enter anumber :"))
# prime(i)

# def fib(a):
#     if a<=1:
#         return a
#     return fib(a-1) + fib(a-2)


# n = int(input("Enter a number :"))
# for i in range(0,n):
#     print(fib(i))

# def fac(n):
#     if n == 0:
#         return 1
#     return n*(fac (n-1))

# n = int(input("Enter a number :"))
# print(fac(n))

# for i in range(0,5):
#     for j in range(0,i):
#         print("*",end="")
#     print()    

# for i in range(0,6):
#     for j in range(0,6-i):
#         print(" ",end="")
#     for x in range(0,i):
#         print("* ",end="")
#     print()
