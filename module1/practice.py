### Assignment 1
### Author: Peter Kindrachuk
import sqlite3
con = sqlite3.connect('movies.sqlite')
cur = con.cursor()

#query to select all the elements from the movie table
query = '''SELECT * FROM Movie'''

#run the query
cur.execute(query)

#save the results in movies
movies = cur.fetchall()

#loop through and print all the movies
for movie in movies:
    print(movie[2] , " " ,movie[3] , " " ,  movie[4])

if con:
    con.close()
