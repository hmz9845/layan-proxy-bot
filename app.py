
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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://google.com",
            "Connection": "keep-alive"
        }
        response = requests.get(url, headers=headers, timeout=10)
        return jsonify({
            "success": True,
            "forwarded_to": url,
            "response_code": response.status_code,
            "text_snippet": response.text[:150]
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run()
