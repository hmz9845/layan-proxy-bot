
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/update", methods=["GET"])
def update_number():
    number = request.args.get("number")
    if not number:
        return jsonify({"success": False, "error": "Missing number"}), 400

    try:
        url = f"https://rn.layan-t.net/?number={number}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        return jsonify({
            "success": True,
            "forwarded_to": url,
            "response_code": response.status_code
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run()
