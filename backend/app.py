from flask import Flask
from flask_cors import CORS
from config import Config
from routes.video_routes import video_bp
from routes.vision_routes import vision_bp
from routes.transcript_routes import transcript_bp
from database.db import init_db


app = Flask(__name__)
CORS(app)

# Initialize DB
init_db()

# Register Blueprints (routes)
app.register_blueprint(video_bp, url_prefix="/api")
app.register_blueprint(transcript_bp, url_prefix="/api")
app.register_blueprint(vision_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
