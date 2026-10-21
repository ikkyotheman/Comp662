import logging
import sqlite3
import matplotlib.pyplot as plt

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='kindrachuk_assignment5.log',
    filemode='w'
)
# logging.getLogger("matplotlib").setLevel(logging.WARNING)


def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB Connected")
    return con


def db_runquery(cur, query):
    cur.execute(query)
    res = cur.fetchall()
    logging.debug("Query returned %d rows", len(res))
    return res


def print_years(res):
    plt.hist(res, bins=40)
    plt.ylabel('Number of Movies')
    plt.xlabel('Year Released')
    plt.locator_params(axis='y', integer=True)
    plt.title('COMP662 Movie Database')
    plt.show()


# Main program
con = db_connect('dbmovies.sqlite')
cur = con.cursor()

allyears = []
query = 'SELECT year from Movie'
res = db_runquery(cur, query)
for result in res:
    allyears.append(result[0])

print_years(allyears)

if con:
    con.close()