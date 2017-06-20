# Logs Analysis Project

### About logs analysis
#### Why this project?

In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

Report generation

Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

Database as shared resource

In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

This shows one of the valuable roles of a database server in a real-world application: it's a point where different pieces of software (a web app and a reporting tool, for instance) can share data.


So what are we reporting, anyway?

Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:
"Princess Shellfish Marries Prince Handsome" — 1201 views

"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views

"Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:
Ursula La Multa — 2304 views

Rudolf von Treppenwitz — 1985 views

Markoff Chaney — 1723 views

Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)

Example:
July 29, 2016 — 2.5% errors

## Mobile screen logs analysis Project
![alt text](https://github.com/paulojr83/logs-analysis-project/blob/master/mobile1.PNG "Welcome")
![alt text](https://github.com/paulojr83/logs-analysis-project/blob/master/mobile2.PNG "About")
![alt text](https://github.com/paulojr83/logs-analysis-project/blob/master/mobile3.PNG "Reports")
![alt text](https://github.com/paulojr83/logs-analysis-project/blob/master/mobile4.PNG "Menu")
![alt text](https://github.com/paulojr83/logs-analysis-project/blob/master/mobile5.PNG "Example report")


## logs analysis Project
 Need some additional help getting started with the logs analysis Project.
1. Set up the environment database: in conn.py YOUR_HOST, DATA_BASE, _PASSAWORD, DATA_BASE_NAME
 * For more information abou set up [Psycopg](http://initd.org/psycopg/docs/install.html)

2. Run the project: in your terminal > python app/app.py access => than [http://localhost:5000/](http://localhost:5000/)

#### The webcasts for the logs analysis include:  
  * [Flask Templates](http://flask.pocoo.org/)
  * [Make Your App a Maximum Security Prison](https://pythonhosted.org/Flask-Security/)
  * [Deploying a Flask App with Heroku](https://www.youtube.com/watch?v=pmRT8QQLIqk)
  
#### Dependency
* antiorm
* appdirs
* bcrypt
* beautifulsoup4
* bleach
* cffi
* click
* db
* Flask
* Flask-HTTPAuth
* Flask-Login
* google
* html5lib
* httplib2
* itsdangerous
* Jinja2
* MarkupSafe
* oauth2client
* packaging
* passlib
* pipdeptree
* psycopg2
* pyasn1
* pyasn1-modules
* pycparser
* pyparsing
* redis
* requests
* rsa
* six
* SQLAlchemy
* virtualenv
* webapp2
* webencodings
* Werkzeug
