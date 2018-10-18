#!/usr/bin/env python3

import sys
import flask
import json
import psycopg2

app = flask.Flask(__name__)

try:
    connection = psycopg2.connect(database=perlman@mathcs.carleton.edu, user=user, password=password)
except Exception as e:
    print(e)
    exit()

# Query the database, leaving you with a "cursor"--an object you can
# use to iterate over the rows generated by your query.
try:
    cursor = connection.cursor()
    query = 'SELECT first_name, last_name FROM authors ORDER BY last_name'
    cursor.execute(query)
except Exception as e:
    print(e)
    exit()