import whisper
from database.db import get_db_connection

def transcribe_video(video_path):
    """Transcribes video using Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    return result["text"]

def save_transcript(filename, transcript):
    """Saves the transcript to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transcripts (filename, text) VALUES (?, ?)", (filename, transcript))
    conn.commit()
    conn.close()
