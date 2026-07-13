movie = {
    'title' : 'Life of Brain',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

print(movie)

print(movie['title'])

print(movie.get('year'))

print(movie.get('budget'))

print(movie.get('budget', 'not found'))

movie['title'] = 'Lord of the Ring'

print(movie.get('title'))

print(movie)

movie.update({
    'title' : 'Bazigar',
    'year' : 1973,
    'cast' : ['Kajol','Eric','SRK','George','Johnny Leaver']
})

movie['budget'] = 50000000

print(movie)

print(movie.get('budget', 'not found'))

year = movie.pop('year')

print(movie)
print(year)

print(len(movie))
print(movie.keys())
print(movie.values())
print(movie.items())

for key, value in movie.items():
    print(key, value)
