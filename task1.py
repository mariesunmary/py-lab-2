import math

# Функція для обчислення z=(sqrt)(m+3/m-3)
def calculate_z(m):
    try:
        result = math.sqrt((m + 3) / (m - 3))
        return result
    except ValueError:
        print("Помилка: ви ввели неправильне значення для m.")
        return None
    except ZeroDivisionError:
        print("Помилка: ділення на нуль. Введіть інше значення для m.")
        return None

# Функція для обчислення y = 2*4*6*...*2*n
def calculate_y(n):
    try:
        result = 1
        for i in range(2, 2*n + 1, 2):
            result *= i
        return result
    except TypeError:
        print("Помилка: введіть натуральне число для n.")
        return None

# Введення числа m користувачем
m = float(input("Введіть число m: "))

# Виклик функції для обчислення z та виведення результату
z = calculate_z(m)
if z is not None:
    print("Результат обчислення z:", z)

# Введення натурального числа n користувачем
n = int(input("Введіть натуральне число n: "))

# Виклик функції для обчислення y та виведення результату
y = calculate_y(n)
if y is not None:
    print("Результат обчислення y:", y)
