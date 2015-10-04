from model import TopWord, Song, connect_to_db, db
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

import requests
import pprint
import os

echonest_key = os.environ["ECHONEST_KEY"]
echonest_secret = os.environ["ECHONEST_SECRET"]
musixmatch_key = os.environ["MUSIXMATCH_KEY"]

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")

@app.route("/")
def homepage():
	"""Display webapp."""

	return render_template("index.html")


@app.route("/songsearch")
def song_search():
	"""display graph of word composition in lyrics."""

	test_song_msd_id = "TRZZZZD128F4236844"
	song_lyrics_query = Song.query.filter(Song.msd_track_id == test_song_msd_id)

	test_song_mxm_id = song_lyrics_query.first().mxm_track_id

	request_url = "http://api.musixmatch.com/ws/1.1/track.get?format=json&apikey=%s&track_id=%s" % (musixmatch_key, test_song_mxm_id)
	print request_url
	response = requests.get(request_url)
	response_text = response.json()

	pprint.pprint(response_text)

	artist_name = response_text["message"]["body"]["track"]["artist_name"]
	print "ARTIST NAME: ", artist_name

	song_name = response_text["message"]["body"]["track"]["track_name"]
	print "TRACK NAME: ", song_name


	words_list = []
	for item in song_lyrics_query.all():

		word = item.word
		count = item.word_count

		word_dictionary = {"word": word, "count": count}
		print word_dictionary
		
		words_list.append(word_dictionary)

	return jsonify(artist=artist_name, song_name=song_name, lyrics=words_list[:20])







if __name__ == "__main__":

	connect_to_db(app)
	PORT = int(os.environ.get("PORT", 5000))
	DebugToolbarExtension(app)

	DEBUG = "NO_DEBUG" not in os.environ

	app.run(debug=DEBUG, host="0.0.0.0", port=PORT)