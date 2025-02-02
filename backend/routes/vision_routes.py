from flask import Blueprint, request, jsonify
import os
from config import Config
from services.frame_extraction import extract_frames
from services.image_recognition import analyze_images

vision_bp = Blueprint("vision", __name__)

@vision_bp.route("/extract-frames", methods=["POST"])
def extract_and_analyze():
    data = request.json
    filename = data.get("filename")

    if not filename:
        return jsonify({"error": "Filename is required"}), 400

    video_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    if not os.path.exists(video_path):
        return jsonify({"error": "File not found"}), 404

    # Extract frames
    frames = extract_frames(video_path, interval=5)

    # Analyze extracted frames
    results = analyze_images(frames)

    return jsonify({"message": "Image analysis complete", "frames": frames, "results": results}), 200
