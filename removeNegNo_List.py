def remove_negative(numbers):
   return [n for n in numbers if n>=0]
numbers=[-1,4,2,-8,-10,1,7]
print(remove_negative(numbers))