from unittest import result
from urllib import request
from flask import jsonify
import flask 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id':0,
     'title': 'Il nome della rosa',
     'author' : 'Umberto Eco',
     'year_published' : '1980'},
     {'id':1,
     'title': 'Il problema dei tre corpi',
     'author' : 'Liu Cixian',
     'year_published' : '2008'},
     {'id':2,
     'title': 'Fondazione',
     'author' : 'Isaac Asimov',
     'year_published' : '1951'},
]

@app.route('/', methods=["GET"])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di web API.</p>"

@app.route('/api/v1/resources/books/all', methods = ['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods = ['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Erorre: nessun file trovato"

    result = []

    for book in books:
        if book['id'] == id:
            result.append(book)

    return jsonify(result)

app.run()