def letter(text):
    words = text.split()
    result = []

    for word in words:
        word = word.lower()
        if word[0] == word[-1]:
            result.append(word)

    return result

text = 'Level apple radar chery civic'
print(letter(text))


#Done .










