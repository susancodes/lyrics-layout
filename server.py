from flask import Flask, render_template, redirect, request, flash, session, jsonify

import os

echonest_key = os.environ["ECHONEST_KEY"]
echonest_secret = os.environ["ECHONEST_SECRET"]

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")
