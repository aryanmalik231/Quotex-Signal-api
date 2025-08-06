from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "📡 Quotex Signal API is Live!"

@app.route("/signal")
def signal():
    return jsonify({
        "pair": "EURUSD",
        "direction": "CALL",
        "confidence": "95%",
        "expiry": "1 minute"
    })

if __name__ == "__main__":
    app.run()
