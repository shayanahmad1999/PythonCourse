friends = {"John", "Michael", "Terry", "Eric", "Graham"}
#1. Check if ‘Eric’ and ‘John’ exist in friends
print('John' and 'Michael' in friends)

my_friends = {"Reg", "Loretta", "Colin", "Eric", "Graham"}
#2. combine or add the two sets 
print(friends.union(my_friends))
print(friends | my_friends)

#3. Find names that are in both sets
print(friends.intersection(my_friends))
print(friends & my_friends)

#4. find names that are only in friends
print(friends.difference(my_friends))
print(friends - my_friends)

#5. Show only the names who only appear in one of the lists
print(friends.symmetric_difference(my_friends))
print(friends ^ my_friends)

#6. Create a new cars-list without duplicates
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

cars_no_dup = set(cars)
print(cars_no_dup)
