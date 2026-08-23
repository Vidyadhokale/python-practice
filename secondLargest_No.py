def secondLargest_No(numbers):
    largest = numbers[0]
    second_largest = numbers[0]
    for n in numbers:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest and n != largest:
            second_largest = n
    return second_largest
numbers = [12, 45, 7, 89, 34, 67]
result = secondLargest_No(numbers)
print("Second largest number:", result)