number = int(input("Введите десятичное число: "))

binary_number = bin(number)[2:] 
octal_number = oct(number)[2:]

print(f"Двоичное представление введенного числа: {binary_number}")
print(f"Восьмеричное представление введенного числа: {octal_number}")
