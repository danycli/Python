def pascal_triangle(n):
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
        
        spaces = " " * (n - i - 1)
        print(spaces + " ".join(str(num) for num in row))

triangle = []
n = int(input("Enter number of rows: "))
pascal_triangle(n)