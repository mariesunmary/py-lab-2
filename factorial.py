def calculate_factorial(n):
    try:
        result = 1
        for i in range(2, 2*n + 1, 2):
            result *= i
        return result
    except TypeError:
        print("Помилка: введіть натуральне число для n.")
        return None
