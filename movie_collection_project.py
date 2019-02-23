movies = []
matches = []
movies.append({'Name': 'sherlock', 'Year': '2009', 'Genre': 'thriller'})
movies.append({'Name': 'titanic', 'Year' : '2009', 'Genre': 'drama'})
movies.append({'Name': 'Andhadhun', 'Year' : '2018', 'Genre': 'crime'})

def find_movie():
    choice = input("Please type 'name' to find by name/ 'year' to find by year/ 'genre' to find by genre\nHow do you want to find your movie:")
        cs = input("\nWhat are you looking for?  ")
        m = list(filter(lambda movie: movie[choice] == cs, movies))
        for mo in m:
            print(f"\nMovie Name : {mo['name']}", f"  Movie Year : {mo['year']}", f"  Movie Genre : {mo['genre']}")

def add_movie():
    movies.append({'Name': input("Please input name:"), 'Year': input("Please input year:"), 'Genre': input("Please input genre:")})
    print("\nThe movie you said is been added to your collection: \n", movies)
    return movies

def view_movie():
    for movie in movies:
        print(f"Movie Name : {movie['Name']}", f"  Movie Year : {movie['Year']}", f"  Movie Genre : {movie['Genre']}")
    return movie


running = True
while running:
    inp = input(
        "Please type 'find' to find any movie/ 'add' to add new movie/ 'view' to view your collection/ 'end' to end program\nWhat would you like to do: ")
    if inp == "find":
        find_movie()
    elif inp == "add":
        add_movie()
    elif inp == "view":
        view_movie()
    elif inp == "end":
        print("\nThank you!")
        running = False
    else:
        print("\nThank you!")
        running = False

