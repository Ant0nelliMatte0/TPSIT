from crypt import methods
from wsgiref import validate
from flask import Flask, render_template, request, redirect, url_for, make_response
from pathlib import Path
import sqlite3
import random
import uuid

# LOGIN #
user = str(uuid.uuid1())
print(uuid)

path = str(Path(__file__).parent.resolve())
print(path)
app = Flask(__name__)


def verifica(username, password):
    completato = False
    coll = sqlite3.connect(f'{path}/social.db')
    cursore = coll.cursor
    cursore.execute("SELECT FROM USERS")
    rows = cursore.fetchall()
    coll.close()
    for row in rows:
        db_user = row[1]
        db_password = row[2]
        if db_user == username:
            completato = check_password(db_password, password)
    return completato

def check_password(password, user_pass):
    return password == user_pass

@app.route('/', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completato = validate(username, password)
        if completato == False:
            error = "errore, perfavore riprovare"
        else:
            #login approvato
            coll = sqlite3.connect(f'{path}/social.db')
            cursore = coll.cursor()
            cursore.execute(f"SELECT ID FROM USERS WHERE USERNAME = '{username}'")
            id_user = cursore.fetchall()

            coll.commit()
            coll.close()
