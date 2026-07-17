import random, string

print('<==========Simple==========>')
print(random.random())

print('<==========Simple in loop==========>')
for i in range(5):
    print(random.random())

print('<==========upto value in loop==========>')
for i in range(5):
    print(random.random()*6)

print('<==========uniform in loop==========>')
for i in range(5):
    print(random.uniform(1,6))

print('<==========randint in loop==========>')
for i in range(5):
    print(random.randint(1,6))

print('<==========randrange (select odd number) in loop==========>')
for i in range(5):
    print(random.randrange(1, 100, 2))

print('<==========randrange (select even number) in loop==========>')
for i in range(5):
    print(random.randrange(2, 100, 2))


print('<==========worked with list==========>')
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))

print('<==========sample mean how many we want==========>')
print(random.sample(friends_list, 3))

print('<==========shuffle==========>')
random.shuffle(friends_list)
print(friends_list)

print('<====================>')

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

letters_numbers = string.ascii_letters + string.digits
# print(letters_numbers)
word = ''
for i in range(8):
    word += random.choice(letters_numbers)
print(word)

print('<==========also generate but not duplicate==========>')
word1 = ''.join(random.sample(letters_numbers,8))
print(word1)

print('<====================>')
word3 = random.choices(letters_numbers, k=6) 
print(word3)
