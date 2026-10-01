# Assignment 4
# Updates Toy Story year to 1995
# Deletes Lawrence of Arabia
# Looks up and prints which movies were made in the year the user inputs
#
# by Peter Kindrachuk


import sqlite3
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='assignment4.log',
    filemode='w'
)


def update_year(con, title, year):
    """Change the year of a movie on the Movie table using a placeholder."""
    cur = con.cursor()
    query = '''UPDATE Movie SET year = ? WHERE name = ?'''
    cur.execute(query, (year, title))
    con.commit()
    logging.debug(f'Updated the year of {title} to {year}')


def delete_movie(con, title):
    """Delete a movie from the Movie table using a placeholder."""
    cur = con.cursor()
    query = '''DELETE FROM Movie WHERE name = ?'''
    cur.execute(query, (title,))
    con.commit()
    logging.debug(f'Deleted {title}')


def get_year():
    """Ask the user for a year until they enter a whole number."""
    while True:
        try:
            year = int(input('Please enter the year to lookup:  '))
            logging.debug(f'User entered the year {year}')
            return year
        except ValueError:
            logging.warning('User entered something that is not a year')
            print('Please enter a valid year using numbers only, like 1995.')


def lookup_year(con):
    """Ask user for year and print all movies in that year."""
    cur = con.cursor()
    year = get_year()

    # query to select movies from year specified by user (avoiding SQL injections by using placeholder)
    query = '''SELECT Movie.name, Movie.year, Movie.minutes, Category.name FROM Movie
               INNER JOIN Category ON Movie.categoryID = Category.categoryID
               WHERE Movie.year = ?'''

    # run the query
    cur.execute(query, (year,))

    # save the results in movies and log how many were found
    movies = cur.fetchall()
    logging.debug(f'Found {len(movies)} movie(s) for {year}')

    if movies:
        print('Title   Year   Length   Genre')
        # loop through and print all the movies
        for movie in movies:
            print(movie[0], '  ', movie[1], '  ', movie[2], '  ', movie[3])
    else:
        print(f'Sorry, no movie in our database for {year}.')


def main():
    con = sqlite3.connect('dbmovies.sqlite')
    logging.debug('Connected to dbmovies.sqlite')
    update_year(con, 'Toy Story', 1995)
    delete_movie(con, 'Lawrence of Arabia')
    print('Welcome to the MovieDB!')
    again = 'y'
    while again == 'y':
        lookup_year(con)
        again = input('Look up another year (y/n)? ').lower()
    print('Take care and make sure to watch more movies!')

    # Closing the DB
    if con:
        con.close()
        logging.debug('Connection closed')


if __name__ == '__main__':
    main()