import flask
from flask import request, jsonify, abort
from flask import make_response
from resources.resources import Resources
from resources.sale import Sale

app = flask.Flask(__name__)
app.config['DEBUG'] = True

r = Resources()


@app.route('/', methods=['GET'])
def home():
    return '<h1>Prototype is working</h1>'


@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'error': 'not Found'}), 404)


@app.route('/api/v1/resources/bands', methods=['GET'])
def api_bands():
    band_id = request.args.get('id')
    return jsonify(r.bands(band_id))


@app.route('/api/v1/resources/songs', methods=['GET'])
def api_songs():
    song_id = request.args.get('id')
    return jsonify(r.songs(song_id))


@app.route('/api/v1/resources/albums', methods=['GET'])
def api_albums():
    album_id = request.args.get('id')
    return jsonify(r.albums(album_id))


@app.route('/api/v1/resources/track_list', methods=['GET'])
def api_track_list():
    album_id = request.args.get('album_id')
    band_id = request.args.get('band_id')
    return jsonify(r.track_list(album_id=album_id, band_id=band_id))


@app.route('/api/v1/resources/make_sale', methods=['POST'])
def api_make_sale():
    if not request.json or 'line_items' not in request.json:
        abort(400)
    line_items = request.json['line_items']
    sale = Sale(line_items)
    return jsonify(sale.commit())


app.run()
