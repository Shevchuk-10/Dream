import re


def sort_words(text):
    words = re.findall(r'\b\w+\b', text)
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

text = 'Again some text for example. Hi , my name is Lux'
sort_text = sort_words(text)
print('Отсортированый текст: ', sort_text)

# И тут я еще больше начал понимать :)