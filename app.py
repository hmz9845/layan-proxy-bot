
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
            "authority": "rn.layan-t.net",
            "method": "GET",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "ar,he;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "referer": "https://chatgpt.com/",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "cross-site",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
        }

        response = requests.get(url, headers=headers, timeout=15)

        return jsonify({
            "success": True,
            "forwarded_to": url,
            "response_code": response.status_code,
            "text_snippet": response.text[:250]
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run()
