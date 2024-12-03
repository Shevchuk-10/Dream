def numbers_in_string(input_text):
    words = input_text.split()  # Разбивка текста на части по пробелам

    total_sum = 0

    for word in words:
        if word.isdigit():  # Проверка, является ли слово числом
            total_sum += int(word)  # Прибавление числа к общей сумме

    return total_sum


text = "Есть например 56 Айфона и 6 симок."
result = numbers_in_string(text)  # Вычисление суммы чисел
print(result)




