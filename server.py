from flask import Flask, render_template, redirect, request, flash, session, jsonify

import os

echonest_key = os.environ["ECHONEST_KEY"]
echonest_secret = os.environ["ECHONEST_SECRET"]

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")

@app.route("/")
def homepage():
	"""Display webapp."""

	pass






if __name__ == "__main__":

	connect_to_db(app)
	PORT = int(os.environ.get("PORT", 5000))
	DebugToolbarExtension(app)

	DEBUG = "NO_DEBUG" not in os.environ

	app.run(debug=DEBUG, host="0.0.0.0", port=PORT)