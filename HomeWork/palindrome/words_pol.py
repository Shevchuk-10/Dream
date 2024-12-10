import re


def palindromes(text):
    words = re.findall(r'\b\w+\b' , text.lower()) #  Поиск всех слов без разлельных знаков

    pal = [word for word in words if word == word[:: -1]] # Проверка какие слова палиндромы

    return pal

text = 'My level is a radar and some text'
pal = palindromes(text)
print('Слова Палиндромы: ', pal)

















