def replace_wo(text):
    #Разделение текста на список слов
    words = text.split()

    for i in range(len(words)):
        #Проверяю являеться ли первый символ s or S.
        if words[i][0].lower() == 's':
            words[i] = 'Python'

    #Обьединение слов в строку
    result = ' '.join(words)

    return result

text = 'She sells a new snap and sneakers'
result = replace_wo(text)
print(result)


