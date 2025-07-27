mar = int(input("Enter your marks :"))

while mar <0 or mar >100:
    print("Invalid marks!\nTry again :")
    mar = int(input())

if mar<=100 and mar>=90:
    print("Grade A")
elif mar <90 and mar >= 80:
    print("Grade B")
elif mar <80 and mar >= 70:
    print("Grade C")
elif mar <70 and mar >=60:
    print("Grade D")
elif mar <60 and mar >=50:
    print("Grade E")
else:
    print("Grade F")