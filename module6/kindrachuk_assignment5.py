# Assignment 5
# Connects to the degrees2.db and graphs the percentage of bachelor's degrees given to women in four majors
# (Computer Science, Psychology, English, and Education) from 1980 through 2011 as a line graph using matplotlib.
# It marks the year Computer Science reached its highest percentage.
#
# by Peter Kindrachuk


import logging
import sqlite3
import matplotlib.pyplot as plt

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='kindrachuk_assignment5.log',
    filemode='w'
)

# Setting the matplotlib logging to a higher level to lower the number of notifications.
logging.getLogger("matplotlib").setLevel(logging.WARNING)


def get_majors(con):
    """Get the year and four majors from 1980 to 2011 using placeholders."""
    cur = con.cursor()

    # query to select the four majors using placeholders
    query = '''SELECT Year, ComputerScience, Psychology, English, Education
               FROM degrees
               WHERE Year BETWEEN ? AND ?
               ORDER BY Year'''

    # run the query to use the data between 1980 and 2011
    cur.execute(query, (1980, 2011))

    # save results in rows and log how many were found
    rows = cur.fetchall()
    logging.debug(f'Found {len(rows)} years of data')
    return rows


def get_cs_peak(con):
    """Find the year Computer Science peaked from 1980 to 2011."""
    cur = con.cursor()

    # query to sort CS from highest to lowest and keep only the top row to get the year with placeholders
    query = '''SELECT Year, ComputerScience
               FROM degrees
               WHERE Year BETWEEN ? AND ?
               ORDER BY ComputerScience DESC
               LIMIT 1'''

    # run the query with years
    cur.execute(query, (1980, 2011))

    # save the result in peak
    peak = cur.fetchall()
    logging.debug(f'Computer Science peaked in {peak[0][0]} at {peak[0][1]}%')
    return peak[0]


def plot_majors(rows, peak):
    """Plot the four majors as a line graph and mark the peak for CS."""
    years = []
    computer_science = []
    psychology = []
    english = []
    education = []

    # loop the rows and put each column in its own list
    for row in rows:
        years.append(row[0])
        computer_science.append(row[1])
        psychology.append(row[2])
        english.append(row[3])
        education.append(row[4])

    # drawing lines for each major
    plt.plot(years, computer_science, label='Computer Science')
    plt.plot(years, psychology, label='Psychology')
    plt.plot(years, english, label='English')
    plt.plot(years, education, label='Education')

    # mark the CS peak year with f-string with an arrow and a label above peak
    plt.annotate(f'CS peak: {peak[0]} ({peak[1]}%)',
                 xy=(peak[0], peak[1]),
                 xytext=(peak[0] + 4, peak[1] + 12),
                 arrowprops=dict(arrowstyle='->'))

    # Naming the labels, title and legend
    plt.xlabel('Year')
    plt.ylabel('Percent of Degrees Earned by Women')
    plt.title("Bachelor's Degrees Earned by Women in the USA (1980-2011)")
    plt.legend(loc='center right')
    plt.show()


def main():
    con = sqlite3.connect('degrees2.db')
    logging.debug('Connected to degrees2.db')
    rows = get_majors(con)
    peak = get_cs_peak(con)
    print(f'Computer Science reached its highest percentage in {peak[0]} at {peak[1]}%.')
    plot_majors(rows, peak)

    # closing the db
    if con:
        con.close()
        logging.debug('Connection closed')


if __name__ == '__main__':
    main()


# Summary of trends: Computer Science is the only one of these four majors where the share
# of degrees earned by women went down. It peaked at 37.1% in 1983 and dropped
# to about 18% in 2011. Over the same years, Psychology climbed from about 65%
# to 77%, while Education and English stayed high and fairly steady.