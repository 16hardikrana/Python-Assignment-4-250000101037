def largest_element(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

values = [18, 45, 9, 72, 31]
print("Largest:", largest_element(values))
