# Demonstrasi Class dan Object-Oriented Programming di Python

# Class dasar
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self, increment):
        self.speed += increment
        print(f"Kecepatan sekarang: {self.speed} km/h")
    
    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)
        print(f"Kecepatan sekarang: {self.speed} km/h")
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Inheritance (Pewarisan)
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 100
    
    def charge(self):
        self.battery_level = 100
        print("Baterai telah terisi penuh!")
    
    def get_battery_info(self):
        return f"Level baterai: {self.battery_level}%"

# Class dengan property
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self._owner = owner
        self._balance = initial_balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Saldo tidak boleh negatif!")
        self._balance = value
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Jumlah deposit harus positif!")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Jumlah penarikan harus positif!")
        if amount > self.balance:
            raise ValueError("Saldo tidak mencukupi!")
        self.balance -= amount

# Demonstrasi penggunaan class
print("=== Demonstrasi Class dan OOP ===")

# Membuat dan menggunakan objek Car
my_car = Car("Toyota", "Camry", 2023)
print(f"Info mobil: {my_car.get_info()}")
my_car.accelerate(30)
my_car.brake(10)

print("\n=== Demonstrasi Inheritance ===")
# Membuat dan menggunakan objek ElectricCar
tesla = ElectricCar("Tesla", "Model 3", 2023, "75 kWh")
print(f"Info mobil listrik: {tesla.get_info()}")
print(tesla.get_battery_info())
tesla.accelerate(50)
tesla.charge()

print("\n=== Demonstrasi Property ===")
# Membuat dan menggunakan objek BankAccount
account = BankAccount("John Doe", 1000)
print(f"Saldo awal: {account.balance}")
account.deposit(500)
print(f"Saldo setelah deposit: {account.balance}")
account.withdraw(200)
print(f"Saldo setelah penarikan: {account.balance}")

# Demonstrasi error handling
try:
    account.withdraw(2000)  # Mencoba menarik lebih dari saldo
except ValueError as e:
    print(f"Error: {e}")

try:
    account.balance = -100  # Mencoba set saldo negatif
except ValueError as e:
    print(f"Error: {e}")
