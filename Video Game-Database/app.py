
import database

MENU_STRUCT = """ 
    ----- Your Game Database App -----

Choose one of the following options:

1) add a new game
2) see all the games
3) find a game's info by name
4) see all games sorted by their rating
5) see all games from a specific genre
6) Remove a game
7) exit

Enter your choice: 
"""


def menu():
    connection = database.connect()
    database.create_table(connection)

    while (user_input := input(MENU_STRUCT)) != "7":
        if user_input == "1":
            name = input("Enter the name for the game: ")
            genre = input("Enter the genre for the game: ")
            rating = int(input("Enter the rating for the game (0-10): "))
            database.add_game(connection,name, genre, rating)
        elif user_input == "2":
            games = database.get_all_games(connection)

            for game in games:
                print(f"{game[1]} : {game[2]} : {game[3]}/10")
        elif user_input == "3":
            name = input("Enter the game you want to search up: ")
            games = database.get_games_by_name(connection, name)

            for game in games:
                print(f"{game[1]} : {game[2]} : {game[3]}/10")
        elif user_input == "4":
            games = database.get_sorted_games(connection)

            for game in games:
                print(f"{game[1]} : {game[2]} : {game[3]}/10")
        elif user_input == "5":
            genre = input("Enter the genre you want to search: ")
            games = database.get_games_by_genre(connection, genre)

            for game in games:
                print(f"{game[1]} : {game[2]} : {game[3]}/10")
        elif user_input == "6":
            name = input("Enter the name of the game you want to delete: ")
            database.delete_game_by_name(connection, name)
        else:
            print("Input was not valid, try again!")



menu()
