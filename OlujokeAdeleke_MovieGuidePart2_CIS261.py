import os

def create_movie_file():
    with open("movies.txt", "w") as file:
        file.write("Cat on a Hot Tin Roof\n")
        file.write("On the Waterfront\n")
        file.write("Monty Python and the Holy Grail\n")

def display_menu():
    print("\nMovie Manager")
    print("1. View movie list")
    print("2. Add a movie")
    print("3. Delete a movie")
    print("4. Exit")

def load_movies():
    if not os.path.exists("movies.txt"):
        create_movie_file()
    with open("movies.txt", "r") as file:
        return [line.strip() for line in file]

def display_movies(movies):
    print("\nMovie List:")
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie}")

def add_movie(movies):
    new_movie = input("Enter the name of the movie to add: ")
    movies.append(new_movie)
    write_movies(movies)
    print(f"'{new_movie}' has been added.")

def delete_movie(movies):
    display_movies(movies)
    try:
        index = int(input("Enter the number of the movie to delete: ")) - 1
        if 0 <= index < len(movies):
            removed_movie = movies.pop(index)
            write_movies(movies)
            print(f"'{removed_movie}' has been deleted.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def write_movies(movies):
    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def main():
    movies = load_movies()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            display_movies(movies)
        elif choice == "2":
            add_movie(movies)
            display_movies(movies)
        elif choice == "3":
            delete_movie(movies)
            display_movies(movies)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()
