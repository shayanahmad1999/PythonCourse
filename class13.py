friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']

print(friends)
print(friends[0])
print(friends[2], friends[4])
print(friends[2:4])
print(friends[:3])
print(friends[:])
print(friends[1:4])
print(len(friends))
print(friends.index('Terry'))
print(friends.count('Eric'))

friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)

friends.append('TerryG')
print(friends)

friends.insert(1, 'MichaelG')
print(friends)

# its important to note that the index starts at 0, so friends[3] is the fourth element in the list.
# Which is 'Eric' in this case. So we are replacing 'Eric' with 'JohnG'
friends[0] = 'JohnG'
print(friends)

friends.remove('Terry')
print(friends)

print("<==========Copying List==========>")
new_friends = friends.copy()
print(new_friends)

new_friends = friends[:]
print(new_friends)

new_friends = list(friends)
print(new_friends)
print("<==========Copying List==========>")

# The pop() method removes the last element from the list.
friends.pop()
print(friends)
# The pop(0) method removes the first element from the list.
friends.pop(0)
print(friends)

del friends[3]
print(friends)

friends.clear()
print(friends)


print("<==========Cars List==========>")
cars = [911, 130, 328, 535, 740, 308]
print(cars)
print(min(cars))
print(max(cars))
print(sum(cars))

friends.extend(cars)
print(friends)