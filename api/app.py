# class UFScrapper:

import requests
import re
from .lib.uf_scrapper import UFScrapper

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Everything is working"


@app.route("/health")
def health():
    return "OK"


@app.route("/uf", methods=["GET"])
def get_uf_value():
    year = int(request.args.get("year"))
    month = int(request.args.get("month"))
    day = int(request.args.get("day"))

    uf_scrapper = UFScrapper()

    try:
        value = uf_scrapper.get_uf_value(year, month, day)

        return jsonify({"status": "success", "data": {"uf_value": value}})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
