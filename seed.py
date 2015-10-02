from model import TopWord, connect_to_db, db
from server import app

def load_topwords():
	"""load top words into database."""

	the_file = open("./seed_data/topwords.csv")

	split_words = the_file.read().split(",")

	for word in split_words:

		word = word

		new_word = TopWord(word=word)
		print new_word

		db.session.add(new_word)
		db.session.commit()


def load_songs():
	"""loads songs with word count."""

	pass

if __name__ == "__main__":
    connect_to_db(app)

    load_topwords()

