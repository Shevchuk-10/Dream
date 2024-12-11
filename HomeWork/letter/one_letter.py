def letter(text):
    words = text.split()
    result = []

    for word in words:
        if word[0].lower() == word[-1].lower():  # Порівнюємо першу і останню букву в нижньому регістрі
            result.append(word.lower())  # Додаємо слово в нижньому регістрі

    return result
