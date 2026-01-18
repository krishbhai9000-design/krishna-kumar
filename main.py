from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "API running", 200

@app.route("/get_proxy", methods=["GET", "POST"])
def get_proxy():
    proxy = "127.0.0.1:8080"
    return Response(proxy, mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
