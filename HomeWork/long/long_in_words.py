def long_words(text):
    # Разбиваю текст на слова
    words = text.split()

    # Сумма длинны всех всех слов
    total_lengh = sum(len(word) for word in words)

    # Вычисление Средний длинны слов
    num_words = len(words)

    if num_words == 0:# Проверка если текст пустой
        return 0
    else:
        avarage_lengh = total_lengh / num_words
        return avarage_lengh


text = 'Пример текста.'
print('Средняя длинна слов', long_words(text))


















