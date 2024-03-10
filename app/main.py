from flask import Flask, json, jsonify, Response
import requests

app = Flask(__name__)


@app.route("/<options>")
def getdata(options):
    urls = {
        "codes":  "https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json",
        "states": "https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_titlecase.json"
    }

    url = urls[options]

    if options not in urls:
        return Response("Error: Invalid option", status=400)

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text

        if options == "states":
            state_data = {}
            for record in json.loads(data):
                state_data[record['name'].lower()] = record['abbreviation']

            return jsonify(state_data), 200

        elif options == "codes":
            return data, 200

    except requests.exceptions.RequestException as e:
        return f"Error: {e}", 500

    except Exception as e:
        return f"Error: {e}", 500

    return "Error: Unknown error", 500


@app.route("/")
def welcome():
    return Response("Welcome to dataservice", status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
