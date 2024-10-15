from flask import Flask, jsonify
from src.routes import router  # Ensure this is a Flask blueprint

app = Flask(__name__)

# Include your router logic
app.register_blueprint(router)  # Modify this to adapt the router to Flask's blueprint system

# Root endpoint
@app.route("/", methods=["GET"])
def read_root():
    return jsonify({"message": "Welcome to the Speech Recognition API"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)