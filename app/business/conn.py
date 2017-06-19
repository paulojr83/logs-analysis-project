import psycopg2


_HOST = "54.205.145.192"
_DATA_BASE = "news"
_USER = "postgres"
_PASSWORD = "12qw"
_DATA_BASE_NAME = "news"
def connect(database_name=_DATA_BASE_NAME):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect(host=_HOST
                              , database=database_name
                              , user=_USER
                              , password=_PASSWORD)
        cursor = db.cursor()
        return db, cursor
    except:
        print "I am unable to connect to the database"

def closeConnCur(conn, cur):
    if conn:
        conn.close()
    if cur:
        cur.close()