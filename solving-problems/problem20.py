print('Check whether a string is a palindrome')

def is_string_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    reversed_text = cleaned_text[::-1]

    return cleaned_text == reversed_text

text = input('Enter a word or sentence: ')

if is_string_palindrome(text):
    print(f"Yes the {text} is a palindrome.")
else:
    print(f"Not {text} is not a palindrome.")
