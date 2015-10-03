from model import TopWord, Song, connect_to_db, db
from server import app


def load_topwords():
	"""Loads top 5,000 words into database."""

	the_file = open("./seed_data/topwords.csv")

	split_words = the_file.read().split(",")

	for word in split_words:

		word = word

		new_word = TopWord(word=word)
		print new_word

		db.session.add(new_word)
		db.session.commit()


def load_songs():
	"""Loads songs with word count."""

	# this is the test file
	the_file = open("./seed_data/mxm_dataset_test.txt")

	for line in the_file:

		line = line.decode(encoding="UTF-8")

		split_words = line.rstrip().split(",")
		msd_track_id = split_words[0]
		mxm_track_id = split_words[1]

		# each song will have different compositions of top words 
		# using range will account for this
		for i in range (2, len(split_words)):

			# each word and count is separated by : so need to split them
			word_and_count = split_words[i].split(":")
			word_id = word_and_count[0]

			word_query = TopWord.query.get(word_id)
			word = word_query.word
			print word 

			word_count = word_and_count[1]

			new_song = Song(msd_track_id=msd_track_id, mxm_track_id=mxm_track_id, word_id=word_id, word=word, word_count=word_count)
			print new_song

			db.session.add(new_song)

		# don't want to commit so often because it slows down
		# this commits once for each song
		db.session.commit()




if __name__ == "__main__":
    connect_to_db(app)

    load_topwords()
    load_songs()

