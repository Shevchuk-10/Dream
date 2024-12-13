def count_vowels(text):
    vowels = 'aeiouAEIOU'  # голосні букви (великі та малі)
    counter = 0

    # Перебираємо кожен символ в тексті
    for char in text:
        if char in vowels:  # Перевірка чи символ є голосною
            counter += 1

    return counter
