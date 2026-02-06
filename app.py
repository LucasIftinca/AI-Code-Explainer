import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain():
    """Handles the AI explanation request."""
    data = request.json
    code_input = data.get("code", "")

    if not code_input:
        return jsonify({"error": "No code provided"}), 400

    prompt = f"Explain this code step by step for a beginner. Use clear headings and bullet points:\n\n{code_input}"

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return jsonify({"explanation": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)