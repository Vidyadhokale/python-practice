def remove_duplicates(numbers):
    unique = []
    for n in numbers:
        if n not in unique:
            unique.append(n)
    return unique
numbers = [12, 34, 5, 7, 2, 12, 2, 7]
result = remove_duplicates(numbers)
print("Original list:", numbers)
print("List after removing duplicates:", result)