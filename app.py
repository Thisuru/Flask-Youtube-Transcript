from flask import Flask, jsonify
from youtube_transcript_api import YouTubeTranscriptApi as yta  # Assuming you have youtube_transcript_api installed
import re

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_HomePage():
    return "Hello, Thisuru"

@app.route("/transcript", methods=["GET"])  # Using a more descriptive route name
def get_transcript():
    video_id = "goXzCh_ofNs"  # Retrieving video ID from query string

    if not video_id:
        return jsonify({"error": "Missing video ID in query string"}), 400

    try:
        data = yta.get_transcript(video_id)
        transcript_text = ' '.join(item['text'] for item in data)

        with open("Transcript.txt", 'w') as file:  # Using context manager for safer file handling
            file.write(transcript_text)

        return jsonify({"transcript": transcript_text})  # Returning transcript as JSON

    except Exception as e:  # Catching general exceptions for more informative error handling
        return jsonify({"error": f"Error fetching transcript: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
