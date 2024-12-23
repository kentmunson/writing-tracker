"""
Offers Google Doc Analysis
"""
import os
import yaml

from flask import Flask, render_template

from src.docs import get_word_counts

# pylint: disable=C0103
app = Flask(__name__)

with open("config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's running!"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)


@app.route("/counts")
def word_counts():
    return get_word_counts(config=CONFIG)


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
