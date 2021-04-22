#!/usr/bin/env python3
"""Flask App"""
from flask import Flask, jsonify, request, make_response, abort, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    """returns home page result"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
