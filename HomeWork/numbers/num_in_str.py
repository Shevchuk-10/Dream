import re


def numbers_in_string(input_text):
    numbers = re.findall(r'\d+', input_text)
    total_sum = sum(int(num) for num in numbers)

    return total_sum


text = "У меня есть 2 MBW и 16 Мотоцыклов"
result = numbers_in_string(text)
