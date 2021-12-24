movies = [
    {"name": "The Matrix", "Director": "Tab"},
    {"name": "Spider", "Director": "Ham" },
    {"name": "Spider", "Director": "Ham" },
    {"name": "Spider", "Director": "Ham" }

]

def find_movie(expected, finder):
     for movie in movies:
         if finder(movie) == expected:
             return movie


find_by = input("what are you looking for?  ")
looking = input("what are you looking?   ")
movie = find_movie(looking, lambda movie: movie[find_by])
print(movie)