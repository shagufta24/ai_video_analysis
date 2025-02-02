from flask import Blueprint, request, jsonify
import os
from config import Config

video_bp = Blueprint("video", __name__)

@video_bp.route("/upload", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filename = os.path.join(Config.UPLOAD_FOLDER, file.filename)
    file.save(filename)

    return jsonify({"message": "File uploaded successfully", "filename": file.filename}), 200
