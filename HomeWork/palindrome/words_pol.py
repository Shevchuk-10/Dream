import re

def palindromes(text):
    # Видаляємо всі непотрібні символи (апострофи, розділові знаки)
    words = re.findall(r'\b\w+\b', text.lower())  # Пошук усіх слів
    palindromes = [word for word in words if word == word[::-1]]  # Перевірка на паліндром
    return palindromes
