from model import TopWord, Song, connect_to_db, db
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

import random
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


@app.route("/songsearch.json")
def song_search():
	"""display graph of word composition in lyrics."""

	# get random song for purpose of building up song info as we test
	random_song_id_num = random.randrange(1, 2199389)
	random_song = Song.query.get(random_song_id_num)
	random_song_msd_id = random_song.msd_track_id

	# get the random song's lyrics
	song_lyrics_query = Song.query.filter(Song.msd_track_id == random_song_msd_id)

	# check if random song's additional info is already in the database
	# if None, make an API call to get all of that
	if song_lyrics_query.first().artist_name == None:

		# get mxm id so we can use it to make an API call
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

		if response_text["message"]["body"]["track"]["primary_genres"]["music_genre_list"] != []:
			primary_genre = response_text["message"]["body"]["track"]["primary_genres"]["music_genre_list"][0]["music_genre"]["music_genre_name"]
			print "GENRE: ", primary_genre
		else:
			primary_genre = "Not Available"

		spotify_id = response_text["message"]["body"]["track"]["track_spotify_id"]

	# build the word list to send over to d3
	words_list = []
	for item in song_lyrics_query.all():

		if item.artist_name == None:

			item.artist_name = artist_name
			item.song_name = song_name
			item.primary_genre = primary_genre
			item.spotify_id = spotify_id
			db.session.commit()
			print "commited to lyricsdb"

		else:

			print "already in database"

		artist_name = item.artist_name
		song_name = item.song_name
		primary_genre = item.primary_genre
		spotify_id = item.spotify_id
		spotify_url = "https://play.spotify.com/track/%s" %spotify_id

		word = item.word
		count = item.word_count

		word_dictionary = {"word": word, "count": count}
		print word_dictionary
		
		words_list.append(word_dictionary)

	# song_dict = {"artist": artist_name,
	# 				"song_name": song_name,
	# 				"genre": primary_genre,
	# 				"spotify": spotify_url,
	# 				"lyrics": words_list}

	return jsonify(artist=artist_name, song_name=song_name, genre=primary_genre, spotify=spotify_url, lyrics=words_list)







if __name__ == "__main__":

	connect_to_db(app)
	PORT = int(os.environ.get("PORT", 5000))
	DebugToolbarExtension(app)

	DEBUG = "NO_DEBUG" not in os.environ

	app.run(debug=DEBUG, host="0.0.0.0", port=PORT)