# my_file = open('files/greeting.txt', 'r')
# print(my_file.read())

# my_file1 = open('files/movies.txt', 'r')
# print(my_file1.read(10))

# print(my_file1.readline())
# print(my_file1.readline()) 
# print(my_file1.readline()) 


my_file = open("files/greeting.txt", 'r')

line_by_line = my_file.readlines()

my_file.seek(0)    # Move back to the beginning

line_by_line1 = my_file.read().splitlines()

print("readlines:", line_by_line)
print("splitlines:", line_by_line1)

my_file.close()



# context manager no use to close file
with open('files/friends.csv', 'r') as f:
    data = f.read()

print(data)

friends = data.splitlines()
print(friends)

for friend in friends:
    friend = friend.split(',')
    name = friend[0]
    year = int(friend[1].strip())
    print(f'In 2030 {name} will be {2030 -year} years old')


with open('files/movies.txt', 'r') as f:
    for line in f:
        print(line)
        print(line.strip())