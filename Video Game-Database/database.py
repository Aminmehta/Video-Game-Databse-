import sqlite3

CREATE_GAME_TABLE = "CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating INTEGER );"

INSERT_GAME = "INSERT INTO games (name, genre, rating) VALUES (?, ?, ?);"

GET_ALL_GAMES = "SELECT * FROM games;"
GET_GAMES_BY_NAME = "SELECT * FROM games WHERE name = ?;"
SORT_GAMES = "SELECT * FROM games ORDER BY rating DESC"
FIND_GENRE = "SELECT * FROM games WHERE genre = ?"
DELETE_GAME = "DELETE FROM games WHERE name = ?"

def connect():
    return sqlite3.connect("data.db")

def create_table(connection): # creates table defined
    with connection:
        connection.execute(CREATE_GAME_TABLE)

def add_game(connection, name, genre, rating):
    with connection:
        connection.execute(INSERT_GAME, (name, genre, rating))

def get_all_games(connection):
    with connection:
        return connection.execute(GET_ALL_GAMES).fetchall()  # returns list of rows that were returned by database

def get_games_by_name(connection, name):
    with connection:
        return connection.execute(GET_GAMES_BY_NAME, (name,)).fetchall()

def get_sorted_games(connection):
    with connection:
        return connection.execute(SORT_GAMES).fetchall()

def get_games_by_genre(connection, genre):
    with connection:
        return connection.execute(FIND_GENRE, (genre,)).fetchall()

def delete_game_by_name(connection, name):
    with connection:
        return connection.execute(DELETE_GAME, (name,)).fetchall()
