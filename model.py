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
