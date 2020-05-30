import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

books = [
  {
    'id': 1, 'title': 'Some Book', 'author': 'Erik Whiting'
  },
  {
    'id': 2, 'title': 'Another Book', 'author': 'Lina Adwer'
  }
]

@app.route('/', methods=['GET'])
def home():
  return '<h1>Prototype is working</h1>'

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
  return jsonify(books)

app.run()