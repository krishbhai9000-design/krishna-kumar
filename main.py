from flask import Flask, Response
import os

app = Flask(__name__)

# =====================
# ROOT CHECK
# =====================
@app.route("/", strict_slashes=False)
def home():
    return "API running", 200


# =====================
# GET PROXY API
# =====================
@app.route("/get_proxy", methods=["GET", "POST"], strict_slashes=False)
def get_proxy():
    # yaha tum apna real proxy daal sakte ho
    proxy = "127.0.0.1:8080"
    return Response(proxy, mimetype="text/plain", status=200)


# =====================
# CERTIFICATE API
# =====================
@app.route("/configvalue", methods=["GET", "POST"], strict_slashes=False)
def configvalue():
    cert = """-----BEGIN CERTIFICATE-----
TEST_CERTIFICATE_DATA
-----END CERTIFICATE-----"""
    return Response(cert, mimetype="text/plain", status=200)


# =====================
# RENDER PORT BINDING
# =====================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
