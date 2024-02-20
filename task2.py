import math
import factorial

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

# Введення числа m користувачем
m = float(input("Введіть число m: "))

# Виклик функції для обчислення z та виведення результату
z = calculate_z(m)
if z is not None:
    print("Результат обчислення z:", z)

# Введення натурального числа n користувачем
n = int(input("Введіть натуральне число n: "))

# Виклик функції для обчислення факторіалу та виведення результату
y = factorial.calculate_factorial(n)
if y is not None:
    print("Результат обчислення y:", y)

