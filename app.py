from flask import Flask, render_template, request, jsonify
from luna import Luna

app = Flask(__name__)
luna = Luna()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    user_text = data.get("text", "")
    emotion = luna.detect_emotion(user_text)
    # Здесь логика ответа
    response_text = f"Ты сказала: {user_text}"
    return jsonify({"response": response_text})
    
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
