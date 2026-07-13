msg = "! You are invited to the party on Saturday"
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names.extend(names1)
# OR
# names += names1
# OR
# names = names + names1

for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    print(name.title() + msg)