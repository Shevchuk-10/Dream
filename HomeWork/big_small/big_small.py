import logging

def big_small(text):
    # Створюємо логер
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Перевірка на порожній текст
    if not text.strip():
        logger.info('Текст пустой')
        return

    # Разбивка текста на слова.
    words = text.split()

    long_word = words[0]
    small_word = words[0]

    for word in words:
        if len(word) > len(long_word):
            long_word = word

        if len(word) < len(small_word):
            small_word = word

    logger.info('Самое длинное слово: ' + long_word)
    logger.info('Самое короткое слово: ' + small_word)
