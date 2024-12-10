def count_vowels(text):
    vowels = 'aeiouAEIOU'
    counter = 0

    for index in text:
        if index in vowels:
            counter += 1

    return counter

user_input = input("Enter some: ")
print("Кол-во гласных букв:", count_vowels(user_input))







