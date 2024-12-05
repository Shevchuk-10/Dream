def big_small(text):

    # Разбивка текста на слова.
    words = text.split()


    if not words:
        print('Текст пустой')
        return

    long_word = words[0]
    small_word = words[0]

    for word in words:
        if len(word) > len(long_word):
            long_word = word

        if len(word) < len(small_word):
            small_word = word

    print('Самое длинное слово: ', long_word)
    print('Самек короткое слово: ', small_word)

text = 'Какой-то пример  текста: '
big_small(text)

# И в етом моменте я начал что-то понимать "Каеф"