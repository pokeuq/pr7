def decimal_to_seven(number):
    if number == 0:
        return "0"
    seven = ""
    while number > 0:
        remainder = number % 7
        seven = str(remainder) + seven
        number //= 7
    return seven

def main():
    while True:
        user_input = input("Введите положительное десятичное число (или 'exit' для выхода): ")
        if user_input.lower() == 'exit':
            print("Завершение программы.")
            break
        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: введите положительное число.")
            else:
                seven_number = decimal_to_seven(number)
                print(f"Число в семеричной системе счисления: {seven_number}")
        except ValueError:
            print("Ошибка: введите корректное целое число.")

if __name__ == "__main__":
    main()
