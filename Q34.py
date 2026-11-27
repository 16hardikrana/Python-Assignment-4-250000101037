def count_case(text):
    upper = 0
    lower = 0
    for character in text:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
    return upper, lower

upper_count, lower_count = count_case("Hello Python 2026")
print("Uppercase:", upper_count)
print("Lowercase:", lower_count)
