from flask import Flask, request, jsonify
import time
import os

app = Flask(__name__)

# =========================
# 🔧 CONTROL FLAGS
# =========================
ALLOW_LOGIN = True
EXPIRE_AT = 0  # 0 = no expiry (unix timestamp)

# =========================
# 🧠 FORWARDER ENDPOINT
# =========================
@app.route("/forward", methods=["POST"])
def forward():
    data = request.get_json(silent=True) or {}

    # ---- Kill switch ----
    if not ALLOW_LOGIN:
        return jsonify({
            "status": 403,
            "headers": {},
            "bodyB64": ""
        })

    # ---- Time limit ----
    if EXPIRE_AT != 0 and time.time() > EXPIRE_AT:
        return jsonify({
            "status": 403,
            "headers": {},
            "bodyB64": ""
        })

    # ---- Allow (echo same body back) ----
    return jsonify({
        "status": 200,
        "headers": {},
        "bodyB64": data.get("bodyB64", "")
    })

# =========================
# 🔎 HEALTH CHECK
# =========================
@app.route("/", methods=["GET"])
def home():
    return "Control API running", 200

# =========================
# 🚀 RUN
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
