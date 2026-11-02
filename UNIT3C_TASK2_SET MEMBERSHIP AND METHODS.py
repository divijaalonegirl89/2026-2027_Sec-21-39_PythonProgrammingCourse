s = {10, 20, 30, 40}

print("Original set:", s)

# Membership testing
print("20 in set:", 20 in s)
print("50 in set:", 50 in s)

# Add element
s.add(50)
print("After add:", s)

# Remove element
s.remove(20)
print("After remove:", s)

# Discard element
s.discard(30)
print("After discard:", s)