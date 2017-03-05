import logging

from flask import Flask, render_template
from flask import request

from evaluator.main import evaluate_mixtape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST','GET'])
def evaluate():
    if request.method == 'POST':
        mixtape = request.form['mixtape']
        score = evaluate_mixtape(request.form['mixtape'])
        # score = 0
        return render_template('results.html', mixtape=mixtape, score=score)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500