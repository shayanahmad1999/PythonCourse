print('Reverse the order of words')

sentence = input("Enter a sentence: ")

words = sentence.split()
words.reverse()

reversed_sentence = " ".join(words)

print("Reversed sentence:", reversed_sentence)