#Tuples - faster Lists you can't change
friends_tuple = ('John','Michael','Terry','Eric','Graham')

print(friends_tuple)
print(friends_tuple[2:4])

y = list(friends_tuple)
y[1] = "kiwi"
friends_tuple = tuple(y)

print(friends_tuple)
