class movies:
    
    def __init__(self):
        self.movies = [{'name': 'sherlock', 'year': '2009', 'genre': 'thriller'},
                       {'name': 'titanic', 'year': '1997', 'genre': 'drama'},
                       {'name': 'andhadhun', 'year': '2018', 'genre': 'crime'}]
    
    def find_movie(self):
        try:
            choice = input("Please type 'name' to find by name/ 'year' to find by year/ 'genre' to find by genre\nHow do you want to find your movie:")
#             Here if choice is not equal to name/year/genre then it will not move further.
            if choice=='name' or choice =='year' or choice=='genre':
                cs = input("\nWhat are you looking for?  ")
            m = list(filter(lambda movie: movie[choice] == cs, self.movies))
        except:
            print("Invalid option, Please try again with valid input.")
            choice = input("Please type 'name' to find by name/ 'year' to find by year/ 'genre' to find by genre\nHow do you want to find your movie:")
            cs = input("\nWhat are you looking for?  ")
            m = list(filter(lambda movie: movie[choice] == cs, self.movies))
        for mo in m:
            print(f"\nMovie Name : {mo['name']}", f"  Movie Year : {mo['year']}", f"  Movie Genre : {mo['genre']}")

    def add_movie(self):
        self.movies.append({'name': input("Please input name:"), 'year': input("Please input year:"), 'genre': input("Please input genre:")})
        print(f"\nThe movie you said is been added to your collection: \n", self.movies)

    def view_movie(self):
        for movie in self.movies:
            print(f"Movie Name : {movie['name']}", f"  Movie Year : {movie['year']}", f"  Movie Genre : {movie['genre']}")


new_movie = movies()
running  = True
while running:
    inp = input("Please type 'find' to find any movie/ 'add' to add new movie/ 'view' to view your collection/ 'end' to end program\nWhat would you like to do: ")
    if inp == "find":
        new_movie.find_movie()
    elif inp == "add":
        new_movie.add_movie()
    elif inp == "view":
        new_movie.view_movie()
    elif inp == "end":
        print("\nThank you!")
        running = False
    else:
        print("\nPlease try again\nThank you!")
        running  = False

