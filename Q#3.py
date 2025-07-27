p = int(input("Enter marks for Physics: "))
c = int(input("Enter marks for Chemistry: "))
b = int(input("Enter marks for Biology: "))
m = int(input("Enter marks for Mathematics: "))
comp = int(input("Enter marks for Computer: "))

perc = (p + c + b + m + comp) /( 500) * 100

print(f"Total Marks: {p + c + b + m + comp} out of 500\n")
print(f"Percentage: {perc}%")

if perc >= 90:
    g = "A"
elif perc >= 80:
    g = "B"
elif perc >= 70:
    g = "C"
elif perc >= 60:
    g = "D"
elif perc >= 40:
    g = "E"
else:
    g = "F"

print(f"Grade: {g}")
