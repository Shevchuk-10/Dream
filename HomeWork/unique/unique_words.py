import re


def unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    un_words = set(words)
    return len(un_words)

text = 'My mom is a by Iphone and i a by MacBook'
print('Кол-во уникальных слов: ', unique_words(text))









