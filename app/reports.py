from conn import *
from scripts import *

"""Returns a list with percentage of error, time."""
def percentage_error_and_time():
    """
    :rtype: lista of error
    """
    try:
        db, cursor = connect()
        cursor.execute(PERCENTAGE_ERROR)
        erros = cursor.fetchall()
        closeConnCur(db, cursor)
        return erros
    except psycopg2.Error as e:
        return e.pgerror

"""Returns a list with author."""
def articles_list():
    try:
        db, cursor = connect()
        cursor.execute(MOST_POPULAR_ARTICLE)
        authors = cursor.fetchall()
        closeConnCur(db, cursor)
        return authors
    except psycopg2.Error as e:
        return e.pgerror

"""Returns a list with author, time and amount."""
def most_popular_author():
    try:
        db, cursor = connect()
        cursor.execute(MOST_POPULAR_AUTHOR)
        most_populars = cursor.fetchall()
        closeConnCur(db, cursor)
        return most_populars
    except psycopg2.Error as e:
        return e.pgerror

"""list with all amount article by author, show the title, time and amount"""
def amount_article_by_author(name):
    try:
        db, cursor = connect()
        cursor.execute(AMOUNT_ARTICLE_BY_AUTHOR % name)
        amount_articles = cursor.fetchall()
        closeConnCur(db, cursor)
        return amount_articles
    except psycopg2.Error as e:
        return e.pgerror