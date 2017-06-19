from conn import *
from scripts import *

"""Returns a list with author, time and amount."""
def countAuthorMostPopular():
    try:
        db, cursor = connect()
        cursor.execute(COUNT_PERCENTAGE_ERROR)
        authors = cursor.fetchall()
        closeConnCur(db, cursor)
        return authors
    except psycopg2.Error as e:
        print e.pgerror

print countAuthorMostPopular()