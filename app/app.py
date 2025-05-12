from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "✅ Hello from ECS Fargate with CI/CD Pipeline!"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("🚀 Flask app is starting on 0.0.0.0:8080")
    app.run(host="0.0.0.0", port=8080)
