# Demonstrasi berbagai jenis fungsi di Python

# Fungsi sederhana tanpa parameter
def say_hello():
    print("Halo, Selamat datang!")

# Fungsi dengan parameter
def greet(name):
    print(f"Halo, {name}!")

# Fungsi dengan parameter default
def greet_with_time(name, time="pagi"):
    print(f"Selamat {time}, {name}!")

# Fungsi dengan multiple parameter
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Fungsi dengan args (variable-length arguments)
def sum_all(*args):
    return sum(args)

# Fungsi dengan kwargs (keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Fungsi lambda (anonymous function)
square = lambda x: x**2

# Demonstrasi penggunaan fungsi
print("=== Demonstrasi Fungsi ===")

# Memanggil fungsi sederhana
say_hello()

# Memanggil fungsi dengan parameter
greet("John")

# Memanggil fungsi dengan parameter default
greet_with_time("John")
greet_with_time("Jane", "siang")

# Memanggil fungsi yang mengembalikan multiple values
area, perimeter = calculate_rectangle(5, 3)
print(f"Luas persegi panjang: {area}")
print(f"Keliling persegi panjang: {perimeter}")

# Memanggil fungsi dengan args
print(f"Jumlah: {sum_all(1, 2, 3, 4, 5)}")

# Memanggil fungsi dengan kwargs
print_info(nama="John Doe", usia=30, pekerjaan="Programmer")

# Menggunakan fungsi lambda
print(f"Kuadrat dari 5: {square(5)}")
