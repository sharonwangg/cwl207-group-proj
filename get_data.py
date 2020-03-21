from imdb import IMDb
import csv

# create an instance of the IMDb class
ia = IMDb()

# get list of film IDs
movie = ia.get_movie('0133093')
print(movie)

print('Directors:')
for director in movie['directors']:
    print(director['name'])

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)

ids = ['0142666', '0051694', '0063668']
movies = []
for id in ids:
    movies.append(ia.get_movie(id))

with open('films.csv', 'w', newline='') as file:

    writer = csv.writer(file)
    #writer.writerow(["Title", "Release Date", "Rating", "Length", "Genre", "Director", "Studio"])
    writer.writerow(["Director", "Genre"])

    #titles = []

    #for title in movie['titles']:
    #    titles.append(title)

    for movie in movies:

        director = ""

        print(type(movie['directors']))

        for director in movie['directors']:
            director += director['name']

        genre = ""

        for genre in movie['genres']:
            genres.append(genre)

        for i in range(0, len(directors)):
            writer.writerow([titles[i], directors[i], genres[i]])


#people = ia.search_person('Mel Gibson')
#for person in people:
#    print(person.personID, person['name'])
