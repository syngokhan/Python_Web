import database
import datetime

menu = """\n\n\nPlease select one of the following options:
    1) Add new movie.
    2) View upcoming movies.
    3) View all movies.
    4) Watch a movie.
    5) View matched movies.
    6) Add user to the app.
    7) Search for a movie.
    8) Exit.

    Your Selection : \n\n\n"""

welcome = "Welcome to the watchlist app"

print(welcome)
database.create_tables()

def prompt_add_movie():
    title = input("Movie Title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date,"%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title,timestamp)

def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)

def prompt_search_movies():
    search_term = input("Enter the partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Movies Found", movies)
    else:
        print("Found no movies for that search term!")

def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list("Watched",movies)
    else:
        print("That user has no watched no movies yet!")

def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username,movie_id)

def print_movie_list(heading, movies):
    print(f" {heading} Movies ".center(30,"-"))
    for _id,title,release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{_id}: {title} (on {human_date})")
    print("".center(30,"-"))

while True:
    value = input(menu)

    if value == "1":
        prompt_add_movie()

    elif value == "2":
        movies = database.get_movies(upcoming=True)
        print_movie_list("Upcoming",movies)
    
    elif value == "3":
        movies = database.get_movies(upcoming=False)
        print_movie_list("All", movies)
    
    elif value == "4":
        prompt_watch_movie()
    
    elif value == "5":
        prompt_show_watched_movies()

    elif value == "6":
        prompt_add_user()

    elif value == "7":
        prompt_search_movies()

    elif value == "8":
        print("Quit")
        break

    else:
        print("Invalid input, please try again!")