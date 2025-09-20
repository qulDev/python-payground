# Demonstrasi berbagai jenis loop di Python

# For Loop dengan range
print("=== For Loop dengan range ===")
for i in range(5):
    print(f"Iterasi ke-{i}")

# For Loop dengan list
print("\n=== For Loop dengan list ===")
fruits = ["apel", "jeruk", "mangga", "pisang"]
for fruit in fruits:
    print(f"Buah: {fruit}")

# For Loop dengan enumerate
print("\n=== For Loop dengan enumerate ===")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# While Loop
print("\n=== While Loop ===")
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# Break dan Continue
print("\n=== Break dan Continue ===")
for i in range(10):
    if i == 3:
        continue  # Skip iterasi ini
    if i == 7:
        break    # Keluar dari loop
    print(f"Nilai i: {i}")

# Nested Loop
print("\n=== Nested Loop ===")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Loop dengan else
print("\n=== Loop dengan else ===")
for i in range(3):
    print(f"Iterasi {i}")
else:
    print("Loop selesai tanpa break")
