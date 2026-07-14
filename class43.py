with open('files/favorite_movies.txt', 'w') as f:
    for i in range(3):
        movie = input(f"Enter movie {i+1}: ")
        f.write(movie + "\n")
print("\nThree movies have been saved successfully!")



new_movie = input("\nEnter one more favorite movie: ")

with open('files/favorite_movies.txt', 'a') as f:
    f.write(movie + "\n")

print("New movie has been appended successfully!")


print("\nYour Favorite Movies:")
with open("files/favorite_movies.txt", "r") as f:
    for line in f:
        print(line.strip())


