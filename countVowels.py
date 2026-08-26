text="I Love Programming".lower()
count=0
vowels=""
for ch in text:
    if ch in 'aeiou':
        count=count+1
        vowels=vowels+ch
print("Vowels:",vowels)
print("vowels Count:",count)