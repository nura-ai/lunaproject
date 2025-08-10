from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    user_text = data.get("text", "")
    
    # Здесь можно добавить обработку текста, например:
    if "привет" in user_text.lower():
        response_text = "Привет! Я Луна 🌙"
    else:
        response_text = f"Ты сказала: {user_text}"

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
