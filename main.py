from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Crypto Whale AI Bot is running!"

@app.route("/signal", methods=["POST"])
def signal():
    data = request.json
    return jsonify({"status": "received", "data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
from flask import Flask, jsonify
from bot_functions import whale_tracker, pump_dump_detector, smart_money_flow, entry_exit_zones

app = Flask(__name__)

@app.route("/")
def home():
    return "روبوت Crypto Whale AI PRO يعمل!"

@app.route("/whales")
def whales():
    data = whale_tracker()
    return jsonify(data)

@app.route("/pump_dump")
def pump_dump():
    data = pump_dump_detector()
    return jsonify(data)

@app.route("/smart_money")
def smart_money():
    data = smart_money_flow()
    return jsonify(data)

@app.route("/signals")
def signals():
    data = entry_exit_zones()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
