# Store Tweets

This repo contains a collection of information, code snippets and learnings around storing Tweet data. 

## Initial Learnings

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
