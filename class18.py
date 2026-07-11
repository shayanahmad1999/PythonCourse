friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends_set.remove('Michael'))
print(friends_set.discard('Graham'))

print(friends_set)

print('John' in friends_set)

print("Terry" not in friends_set)

print(friends_set.add('Reg'))

tropical = {"pineapple", "mango", "papaya"}

print(friends_set.update(tropical))

print(friends_set.pop())

my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
print(friends_set.intersection(my_friends_set))

print(friends_set.union(my_friends_set))

print(friends_set.difference(my_friends_set))

print(friends_set.clear())

del friends_set
print(friends_set) # this will throw an error because the set has been deleted

#Sets - blazingly fast unordered Lists 
#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()