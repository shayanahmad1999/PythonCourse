print('Count vowels in a string')

def count_vowels(text):
    vowels = 'aeiou'
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1
    return count

text = input("Enter a word or sentence: ")
result = count_vowels(text)

print(f"Number of vowels: {result}")
