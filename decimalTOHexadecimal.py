decimal = int(input("Enter a number :"))
f = 1
z = 1
h = 0
while decimal > 0:
    z = int(decimal / 16)
    f = int(z*16)
    h = decimal-f
    decimal = z
    strh = str(h)
    if h == 10:
        h = 'A'
    elif h == 11:
        h = 'B'
    elif h == 12:
        h = 'C'
    elif h == 13:
        h = 'D'
    elif h == 14:
        h = 'E'
    elif h == 15:
        h = 'F'
    reverse = str(h)[::-1]
    print(reverse,end="")  