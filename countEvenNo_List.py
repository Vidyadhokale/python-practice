def count_even(numbers):
    count=[n for n in numbers if n%2==0]
    return len(count)
numbers=[2,4,1,5,7,6,8,4,2]
count_even(numbers)