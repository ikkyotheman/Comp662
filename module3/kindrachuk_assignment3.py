import logging  # DEBUG,INFO,ERROR,WARNING,CRITICAL
import os
import sqlite3

logging.basicConfig(
    filename="assignment3.log",
    level=logging.DEBUG,
    format="[Movies]:%(asctime)s:%(levelname)s:%(message)s"
)


def db_checkfile(dbfile):
    if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
        logging.debug("{a} found and not zero size".format(a=dbfile))
    else:
        logging.error("{a} not found or zero size".format(a=dbfile))


def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB Connected".format())
    return con

def create_tables(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE movies_info_1 (show_id INT PRIMARY KEY, genre VARCHAR(255), title VARCHAR(255), director VARCHAR(255))")
    cur.execute("CREATE TABLE movies_info_2 (show_id INT, release_year INT, description VARCHAR(255), FOREIGN KEY (show_id) REFERENCES movies_info_1 (show_id))")
    con.commit()

def insert_movies(con):
    cur = con.cursor()

    # movies_info_1
    cur.execute("INSERT INTO movies_info_1 (show_id, genre, title, director) VALUES (1, 'Crime', 'The Godfather', 'Francis Ford Coppola')")
    cur.execute("INSERT INTO movies_info_1 (show_id, genre, title, director) VALUES (2, 'Crime', 'Pulp Fiction', 'Quentin Tarantino')")
    cur.execute("INSERT INTO movies_info_1 (show_id, genre, title, director) VALUES (3, 'Crime', 'Cidade de Deus', 'Kátia Lund, Fernando Meirelles')")

    # movies_info_2
    cur.execute("INSERT INTO movies_info_2 (show_id, release_year, description) VALUES (1, 1972, 'Mafia family struggles with power and loyalty.')")
    cur.execute("INSERT INTO movies_info_2 (show_id, release_year, description) VALUES (2, 1994, 'Bizarre connected criminals navigate crime, violence with dark humor.')")
    cur.execute("INSERT INTO movies_info_2 (show_id, release_year, description) VALUES (3, 2002, 'Follows the lives of kids from a Favela in Rio de Janeiro.')")
    con.commit()


def main():
    dbfile = "movies.db"

    print("My Movie Database")

    # file checking
    if os.path.exists(dbfile):
        os.remove(dbfile)

    con = db_connect(dbfile)
    create_tables(con)
    insert_movies(con)
    db_checkfile(dbfile)

    # INNER JOIN tables with show_id
    cur = con.cursor()
    cur.execute("SELECT movies_info_1.genre, movies_info_1.title, movies_info_1.director, movies_info_2.release_year, movies_info_2.description FROM movies_info_1 INNER JOIN movies_info_2 ON movies_info_1.show_id = movies_info_2.show_id")

    # Headers
    print("Genre | Title | Director | Year | Description")

    # Printing table
    rows = cur.fetchall()
    for row in rows:
        print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4])

    con.close()
    logging.debug("DB Closed")
    print("Done!")

if __name__ == "__main__":
    main()