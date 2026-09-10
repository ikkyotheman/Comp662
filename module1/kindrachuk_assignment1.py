### Assignment 1
### Author: Peter Kindrachuk
### Description: Connects to chinook.db and prints the list of artists.
import sqlite3

def connect():
    con = sqlite3.connect('chinook.db')
    cur = con.cursor()
    return con, cur

def getArtists(cur):
    query = '''SELECT * FROM artists'''
    cur.execute(query)
    artists = cur.fetchall()
    return artists

def printArtists(artists):
    print('Artist List')
    for artist in artists:
        print(artist[1])

def close(con):
    if con:
        con.close()
    print()
    print('Done - See you next time!')

def main():
    con, cur = connect()
    artists = getArtists(cur)
    printArtists(artists)
    close(con)

if __name__ == '__main__':
    main()