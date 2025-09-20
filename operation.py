# Demonstrasi berbagai operasi di Python

# Operasi Aritmetika
a = 10
b = 3

print("=== Operasi Aritmetika ===")
print(f"Penjumlahan: {a} + {b} = {a + b}")
print(f"Pengurangan: {a} - {b} = {a - b}")
print(f"Perkalian: {a} × {b} = {a * b}")
print(f"Pembagian: {a} ÷ {b} = {a / b}")
print(f"Pembagian Bulat: {a} ÷ {b} = {a // b}")
print(f"Sisa Bagi: {a} % {b} = {a % b}")
print(f"Pangkat: {a} ^ {b} = {a ** b}")

# Operasi Perbandingan
print("\n=== Operasi Perbandingan ===")
print(f"{a} > {b}:", a > b)
print(f"{a} < {b}:", a < b)
print(f"{a} >= {b}:", a >= b)
print(f"{a} <= {b}:", a <= b)
print(f"{a} == {b}:", a == b)
print(f"{a} != {b}:", a != b)

# Operasi Logika
x = True
y = False

print("\n=== Operasi Logika ===")
print(f"AND: {x} and {y} =", x and y)
print(f"OR: {x} or {y} =", x or y)
print(f"NOT: not {x} =", not x)

# Operasi Assignment
number = 5
print("\n=== Operasi Assignment ===")
print(f"Nilai awal: {number}")

number += 3  # number = number + 3
print(f"Setelah += 3: {number}")

number -= 2  # number = number - 2
print(f"Setelah -= 2: {number}")

number *= 4  # number = number * 4
print(f"Setelah *= 4: {number}")

number /= 2  # number = number / 2
print(f"Setelah /= 2: {number}")
