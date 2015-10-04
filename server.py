from model import TopWord, Song, connect_to_db, db
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension


import os

echonest_key = os.environ["ECHONEST_KEY"]
echonest_secret = os.environ["ECHONEST_SECRET"]

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")

@app.route("/")
def homepage():
	"""Display webapp."""

	return render_template("index.html")


@app.route("/songsearch")
def song_search():
	"""display graph of word composition in lyrics."""

	test_song_id = "TRZZZZD128F4236844"

	song_lyrics_object = Song.query.filter(Song.msd_track_id == test_song_id).all()

	words_list = []
	for item in song_lyrics_object:

		word = item.word
		count = item.word_count

		word_dictionary = {"word": word, "count": count}
		print word_dictionary
		
		words_list.append(word_dictionary)

	return jsonify(data=words_list[:10])







if __name__ == "__main__":

	connect_to_db(app)
	PORT = int(os.environ.get("PORT", 5000))
	DebugToolbarExtension(app)

	DEBUG = "NO_DEBUG" not in os.environ

	app.run(debug=DEBUG, host="0.0.0.0", port=PORT)