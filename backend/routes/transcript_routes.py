from flask import Blueprint, request, jsonify
import os
from config import Config
from services.transcription import transcribe_video, save_transcript
from services.summarization import summarize_text
from services.keywords import extract_key_phrases
from services.frame_extraction import extract_frames
from services.image_recognition import analyze_images

transcript_bp = Blueprint("transcript", __name__)

@transcript_bp.route("/transcribe", methods=["POST"])
def transcribe():
    data = request.json
    filename = data.get("filename")

    if not filename:
        return jsonify({"error": "Filename is required"}), 400

    video_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    if not os.path.exists(video_path):
        return jsonify({"error": "File not found"}), 404

    transcript = transcribe_video(video_path)
    save_transcript(filename, transcript)
    return jsonify({"message": "Transcription complete", "transcript": transcript}), 200

@transcript_bp.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    transcript = data.get("transcript", "")

    if not transcript:
        return jsonify({"error": "Transcript is required"}), 400

    summary = summarize_text(transcript)
    return jsonify({"summary": summary}), 200

@transcript_bp.route("/keywords", methods=["POST"])
def get_keywords():
    data = request.json
    transcript = data.get("transcript", "")

    if not transcript:
        return jsonify({"error": "Transcript is required"}), 400

    keywords = extract_key_phrases(transcript)
    return jsonify({"keywords": keywords}), 200

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

    return jsonify({"message": "Image analysis complete", "results": results}), 200

