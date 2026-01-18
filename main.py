from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API running"

@app.route("/configvalue", methods=["GET", "POST"])
def configvalue():
    return """-----BEGIN CERTIFICATE-----
TEST-CERTIFICATE-DATA
-----END CERTIFICATE-----"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
