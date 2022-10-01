import json
import os
import flask
from flask import request, jsonify, abort
from flask import make_response, render_template
from resources.resources import Resources
from resources.sale import Sale
from dotenv import load_dotenv

load_dotenv()

base_dir = os.path.dirname(os.path.dirname(os.path.abspath("test_site/*")))
template_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(template_dir, "css")

app = flask.Flask(__name__, template_folder=template_dir, static_folder=template_dir)
app.config["DEBUG"] = True

r = Resources()


@app.route("/", methods=["GET"])
def home():
    headers = {"Content-Type": "text/html"}
    return make_response(render_template("index.html"), headers)


@app.route("/bands", methods=["GET"])
def bands():
    bands = r.bands(None)
    return make_response(
        render_template("pages/bands.html", bands_object=json.dumps(bands))
    )


@app.route("/bands/<band_id>", methods=["GET"])
def band(band_id):
    band_name = r.bands(band_id)[0]["bandname"]
    albums = r.album_by_band(band_id)
    songs = {}
    for album in albums:
        album["releasedate"] = album["releasedate"].isoformat()
        all_songs = r.song_by_album(album["id"])
        for song in all_songs:
            song["releasedate"] = song["releasedate"].isoformat()
        songs[album["albumname"]] = all_songs
    return make_response(
        render_template(
            "pages/band.html", band_name=band_name, track_list=json.dumps(songs)
        )
    )


@app.route("/albums", methods=["GET"])
def albums():
    albums = r.album_view()
    for album in albums:
        album["releasedate"] = album["releasedate"].isoformat()
    return make_response(
        render_template("pages/albums.html", albums=json.dumps(albums))
    )


@app.route("/sales", methods=["GET"])
def sales():
    sales = r.sales()
    return make_response(render_template("pages/sales.html", sales=json.dumps(sales)))


@app.route("/new_sale", methods=["GET"])
def new_sale_page():
    albums = r.album_view()
    album_sale_hash = r.album_sale_hash()
    for album in albums:
        album["releasedate"] = album["releasedate"].isoformat()
    albums = json.dumps(albums)
    album_sale_hash = json.dumps(album_sale_hash)
    return make_response(
        render_template(
            "pages/make_sale.html", albums=albums, album_sale_hash=album_sale_hash
        )
    )


@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({"error": "not Found"}), 404)


@app.route("/api/v1/resources/bands", methods=["GET"])
def api_bands():
    band_id = request.args.get("id")
    return jsonify(r.bands(band_id))


@app.route("/api/v1/resources/songs", methods=["GET"])
def api_songs():
    song_id = request.args.get("id")
    return jsonify(r.songs(song_id))


@app.route("/api/v1/resources/track_list/<band_id>", methods=["GET"])
def api_track_list(band_id):
    albums = r.album_by_band(band_id)
    songs = {}
    for album in albums:
        all_songs = r.song_by_album(album["id"])
        songs[album["albumname"]] = all_songs
    return jsonify(songs)


@app.route("/api/v1/resources/make_sale", methods=["POST"])
def api_make_sale():
    if not request.json or "line_items" not in request.json:
        abort(400)
    line_items = request.json["line_items"]
    sale = Sale(line_items)
    return jsonify(sale.commit())


app.run(host="0.0.0.0", port=80)
