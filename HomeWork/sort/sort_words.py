import re


def sort_words(text):
    # Видалити всі непотрібні символи (числа, знаки пунктуації)
    words = re.findall(r'[a-zA-Z]+', text.lower())  # Це збере лише літери
    # Сортуємо слова в алфавітному порядку
    sorted_words = sorted(words)
    # Повертаємо відсортовані слова як один рядок
    return ' '.join(sorted_words)



