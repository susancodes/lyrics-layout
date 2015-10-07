from flask_sqlalchemy import SQLAlchemy
import psycopg2

import os

db = SQLAlchemy()

# this is for top words database
class TopWord(db.Model):
	"""database for top 5,000 words to index them."""

	__tablename__ = "topwords"

	id = db.Column(db.Integer, primary_key=True)
	word = db.Column(db.String(100), nullable=False, unique=True)

	def __repr__(self):
		"""Statement when object is printed."""

		return "<Word index=%s word=%s>" % (self.id, self.word)



class Song(db.Model):
	"""database for songs with lyrics word count."""

	__tablename__ = "songs"

	id = db.Column(db.Integer, primary_key=True)
	msd_track_id = db.Column(db.String(50), nullable=False)
	mxm_track_id = db.Column(db.Integer, nullable=False)
	word_id = db.Column(db.Integer, db.ForeignKey("topwords.id"), nullable=False)
	word = db.Column(db.String(100), nullable=False)
	word_count = db.Column(db.Integer, nullable=False)

	# will add these as we look up this information
	# this requires making API calls and there's a limit so we can't do it all at once
	track_name = db.Column(db.String(500))
	artist_name = db.Column(db.String(500))
	primary_genre = db.Column(db.String(500))
	secondary_genre = db.Column(db.String(500))
	tertiary_genre = db.Column(db.String(500))
	spotify_id = db.Column(db.String(500))


	def __repr__(self):
		"""Statement when object is printed."""

		return "<Song MSD_track_id:%s word_id:%s" % (self.msd_track_id, self.word_id)



def connect_to_db(app):
    """Connect the database to our Flask app."""


    DATABASE_URL = os.environ.get("DATABASE_URL",
                              "postgresql://localhost/lyricsdb")
   
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.app = app
    db.init_app(app)



if __name__ == "__main__":
# allows working with the database directly

    from server import app
    connect_to_db(app)
    print "Connected to DB."


