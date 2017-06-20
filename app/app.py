from sqlalchemy.orm.exc import NoResultFound\
    , MultipleResultsFound
from flask import Flask, render_template, jsonify
from reports import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/report/error')
def percentage_error():
    """
    Methodo retorn a list with all erros by time
    :return json list of erros: 
    """
    try:
        Erros= percentage_error_and_time()
        return render_template('error.html', erros=Erros)

    except (NoResultFound,MultipleResultsFound):
        return jsonify(error='No result Found!', code=404)

@app.route('/report/articles')
def articles():
    """
    Methodo retorn a list with three must popular article, show title and amount
    :return json list three must popular article, show title and amount: 
    """
    try:
        Articles= articles_list()
        return render_template('articles.html', articles=Articles)

    except (NoResultFound,MultipleResultsFound):
        return jsonify(error='No result Found!', code=404)

@app.route('/report/most_popular')
def most_popular():
    """
    Methodo retorn a list with three must populars authors, show author name and amount
    :return json list of three must populars authors, show author name and amount: 
    """
    try:
        Authors= most_popular_author()
        return render_template('authors.html', authors=Authors)

    except (NoResultFound,MultipleResultsFound):
        return jsonify(error='No result Found!', code=404)

@app.route('/report/article_by_author/<string:name>',methods=['GET'])
def article_by_author(name):
    """
    Methodo retorn a list with all amount article by author, show the title, time and amount
    :return json list of amount article by author, show the title, time and amount: 
    """
    try:
        print name
        Articles= amount_article_by_author(name)
        return render_template('article_by_author.html', articles=Articles, author=name)

    except (NoResultFound,MultipleResultsFound):
        return jsonify(error='No result Found!', code=404)

if __name__ == '__main__':
    app.run(debug=True)