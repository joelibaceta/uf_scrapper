# class UFScrapper:

import requests
import re
from uf_scrapper.lib.uf_scrapper import UFScrapper

from flask import Flask
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/uf", methods=["GET"])
def get_uf_value():
    print(request.args)
    year = int(request.args.get("year"))
    month = int(request.args.get("month"))
    day = int(request.args.get("day"))

    uf_scrapper = UFScrapper()

    try:
        value = uf_scrapper.get_uf_value(year, month, day)

        return jsonify({"status": "success", "data": {"uf_value": value}})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
