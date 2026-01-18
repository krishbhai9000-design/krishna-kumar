from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# =========================
# 🔧 CONTROL FLAGS (YAHIN SE CONTROL)
# =========================
ALLOW_LOGIN = True        # True = allow, False = block
EXPIRE_AT = 0             # 0 = no expiry (unix timestamp use karo)

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
            "body_b64": ""
        })

    # ---- Time limit ----
    if EXPIRE_AT != 0 and time.time() > EXPIRE_AT:
        return jsonify({
            "status": 403,
            "headers": {},
            "body_b64": ""
        })

    # ---- Default: allow (echo back same body) ----
    return jsonify({
        "status": 200,
        "headers": {},                 # agar chaho to custom headers add kar sakte ho
        "body_b64": data.get("body_b64", "")
    })

# =========================
# 🔎 HEALTH CHECK
# =========================
@app.route("/", methods=["GET"])
def home():
    return "Control API running", 200


# =========================
# 🚀 RUN (Render compatible)
# =========================
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
