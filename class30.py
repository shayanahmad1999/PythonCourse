strings = "Pakistan is the best country"
for string in strings:
    print(string)

for i in range(8):
    print(i)


for i in range(2,8):
    print(i)


for i in range(1,15,3):
    print(i)

friends = ['John','Terry','Eric','Michael','George']

# friends
# ┌─────────┐
# │ John    │ ← friend
# │ Terry   │ ← friend
# │ Eric    │ ← friend
# │ Michael │ ← friend
# │ George  │ ← friend
# └─────────┘
for friend in friends:
    print(friend)


# friends
# Index    Value
# 0   ---> John
# 1   ---> Terry
# 2   ---> Eric
# 3   ---> Michael
# 4   ---> George
for index in range(len(friends)):
    print(friends[index])

# Even Better: Use enumerate()
# Instead of range(len(...)), Python provides a cleaner way:
for index, friend in enumerate(friends):
    print(index, friend)


# 0: John
# 1: Terry
# 2: Eric
# 3: Michael
# 4: George
for index in range(len(friends)):
    print(f"{index}: {friends[index]}")


friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)