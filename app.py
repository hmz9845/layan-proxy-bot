
import asyncio
from playwright.async_api import async_playwright
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/update", methods=["GET"])
async def update_number():
    number = request.args.get("number")
    if not number:
        return jsonify({"success": False, "error": "Missing number"}), 400

    try:
        result = await perform_browser_refresh(number)
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

async def perform_browser_refresh(number):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        url = f"https://rn.layan-t.net/?number={number}"
        await page.goto(url)
        await page.wait_for_timeout(4000)  # الانتظار 4 ثواني للسماح للـ JS بالعمل
        content = await page.content()
        await browser.close()
        return {
            "success": True,
            "forwarded_to": url,
            "html_snippet": content[:250]
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
