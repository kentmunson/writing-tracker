"""
Offers Google Doc Analysis
"""
import os

import yaml
from flask import Flask

from src.docs import get_word_counts

# pylint: disable=C0103
app = Flask(__name__)

with open("config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    return {"status": "ok"}


@app.route("/counts")
def word_counts():
    """Get word counts for all documents in the app's config."""
    word_counts = get_word_counts(config=CONFIG)
    total = sum(list(word_counts.values()))
    return {
        "word_counts": word_counts,
        "total": total,
    }


if __name__ == "__main__":
    server_port = os.environ.get("PORT", "8080")
    app.run(debug=False, port=server_port, host="0.0.0.0")
