from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Welcome to my Flask API!",
            "endpoints": ["/", "/hello", "/palindrome/<word>", "/add/<int:a>/<int:b>"],
        }
    )


@app.route("/hello")
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/palindrome/<word>")
def check_palindrome(word):
    is_pal = word.lower() == word.lower()[::-1]
    return jsonify({"word": word, "is_palindrome": is_pal, "reverse": word[::-1]})


@app.route("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    return jsonify({"operation": "addition", "a": a, "b": b, "result": a + b})


@app.route("/api/calc", methods=["POST"])
def calculator():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else None,
    }

    if operation not in operations:
        return jsonify({"error": "Invalid operation"}), 400

    try:
        result = operations[operation](a, b)
        return jsonify({"operation": operation, "a": a, "b": b, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
