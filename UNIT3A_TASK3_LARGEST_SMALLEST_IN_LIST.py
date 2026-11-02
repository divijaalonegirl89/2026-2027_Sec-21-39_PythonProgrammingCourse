a = list(map(int, input("Enter list elements: ").split()))

largest = smallest = a[0]

for i in a:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest element =", largest)
print("Smallest element =", smallest)