a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

print("Addition:")
for i in range(2):
    for j in range(2):
        print(a[i][j] + b[i][j], end=" ")
    print()

print("Subtraction:")
for i in range(2):
    for j in range(2):
        print(a[i][j] - b[i][j], end=" ")
    print()

print("Multiplication:")
for i in range(2):
    for j in range(2):
        s = 0
        for k in range(2):
            s += a[i][k] * b[k][j]
        print(s, end=" ")
    print()

print("Transpose:")
for i in range(2):
    for j in range(2):
        print(a[j][i], end=" ")
    print()