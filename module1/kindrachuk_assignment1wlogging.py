### Assignment 1
### Author: Peter Kindrachuk
### Description: Connects to chinook.db and prints the list of artists.
import sqlite3
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='assignment1.log',
    filemode='w'
)
logger = logging.getLogger(__name__)

def connect():
    logger.debug('Connecting to chinook.db')
    con = sqlite3.connect('chinook.db')
    cur = con.cursor()
    logger.info('Connection established')
    return con, cur

def getArtists(cur):
    query = '''SELECT * FROM artists'''
    logger.debug(f'Executing query: {query}')
    cur.execute(query)
    artists = cur.fetchall()
    logger.info(f'Retrieved {len(artists)} artists')
    return artists

def printArtists(artists):
    print('Artist List')
    for artist in artists:
        print(artist[1])

def close(con):
    if con:
        con.close()
        logger.info('Connection closed')
    print()
    print('Done - See you next time!')

def main():
    logger.info('Program started')
    con, cur = connect()
    artists = getArtists(cur)
    printArtists(artists)
    close(con)
    logger.info('Program finished')

if __name__ == '__main__':
    main()