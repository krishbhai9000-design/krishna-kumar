from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API running"

@app.route("/configvalue", methods=["GET", "POST"])
def configvalue():
    return (
        "-----BEGIN CERTIFICATE-----\n"
        "TEST_CERTIFICATE_DATA\n"
        "-----END CERTIFICATE-----"
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
