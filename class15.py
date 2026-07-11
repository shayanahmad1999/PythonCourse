text = "Python is   fun"
print(text.split())

csv_data = "apple,banana,cherry"
print(csv_data.split(','))

text = "one-two-three-four"
print(text.split("-", 2))  

words = ['Python', 'is', 'fun']
print(" ".join(words))  

print("-".join(words))  

print("".join(words))  

sentence = "this is a comma separated sentence"
result = "-".join(sentence.split())
print(result) 