import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure your API Key
genai.configure(api_key="AIzaSyCwrgOAQv9jFD70IXAUBG5EgB0nUbFGntQ")
model = genai.GenerativeModel('gemini-2.5-flash')

# This route serves the main page
@app.route('/')
def index():
    return render_template('index.html')

# This route handles the chat logic
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate response using Gemini
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)