import logging

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello(name="John Jingleheimer Smith"):
    return render_template('index.html', name=name)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500