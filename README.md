*Note: this repository is still a work in progress*

# Store Tweets

This repo contains a collection of information, code snippets and learnings around storing Tweet data. 

## Getting Started

### Authentication

Use `sample/credentials_example.yml` to create a new file where you can store your credentials: 
* Rename the file `credentials.yml` 
* Save it alongside `run.py` (one level above the `sample` directory)
* Replace `INSERT-HERE` with your API and database credentials

You're now ready to run the application

### Run This Application

In your command line, run `python run.py`. The first time you run this application, it will generate a database and tables for you. After that, it will simply update those tables.

If you want to run analysis on the Tweets stored in your database, run `python run_analysis.py`. For now, you still need to replace the Tweet ID with a Tweet ID that is stored in your database. I will develop this further.

## Some Learnings

### Relational VS Non-relational Databases

**Relational databases** store data in such a way that it can be accessed in relation to another piece of data in the database. Relational databases (like MySQL, PostgreSQL and SQLite3) typically store data in tables and rows, which is helpful when it comes to accessing and manipulating the data. 

**Non-relational databases** (like MongoDB) are databases that do not follow the relational model described above and store data in collections of JSON documents. This is helpful for us, because the Twitter API returns data JSON objects.

#### Reading sources

* What is a Relational Database Management System? https://www.codecademy.com/articles/what-is-rdbms-sql

* What is the difference between a relational and non-relational database? https://www.quora.com/What-is-the-difference-between-a-relational-and-non-relational-database

* Why use non-relational databases instead of relational databases? https://www.quora.com/Why-use-Non-Relational-Database-instead-of-Relational-Database

### Creating Schemas

Some good information on Database Schemas related to Tweets can be found here: https://github.com/jimmoffitt/data-stores/blob/master/schemas/schemas.md 

## Before You Get Started: 

### A few things to establish

* Technologies to use, libraries, frameworks
* Directory structures, file name schemes
* Architectural patterns
* Build / Configuration / Test approaches

### Some docs & resources

* SQLAlchemy ORM Tutorial for Python Developers https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
* SQL Expression Language Tutorial https://docs.sqlalchemy.org/en/latest/core/tutorial.html
