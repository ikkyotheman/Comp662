import sqlite3
import logging
import os

logging.basicConfig(
    filename="SQL_practice.log",
    level=logging.DEBUG,
    format="[SQL_practice]:%(asctime)s:%(levelname)s:%(message)s"
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
    cur = con.cursor( )
    cur.execute("CREATE TABLE Student (ID INT, Name VARCHAR(255), Age INT)")

def insert_students(con):
    cur = con.cursor( )

    cur.execute("INSERT INTO Student (ID, Name, Age) VALUES (1, 'Peter', 40)")
    cur.execute("INSERT INTO Student (ID, Name, Age) VALUES (2, 'Michael', 20)")


def main():
    dbfile = "students.db"
    con = db_connect(dbfile)

    create_tables(con)
    insert_students(con)
    db_checkfile(dbfile)
    cur = con.cursor()
    cur.execute("SELECT * FROM Student")

    con.close()
    logging.debug("DB Closed")
    print("Done!")
if __name__ == '__main__':
    main()