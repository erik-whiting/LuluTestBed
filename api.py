import flask
from flask import request, jsonify
from resources.resources import Resources


app = flask.Flask(__name__)
app.config['DEBUG'] = True

r = Resources()


@app.route('/', methods=['GET'])
def home():
    return '<h1>Prototype is working</h1>'


@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Cannot find that resource</h1>', 404


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


app.run()
