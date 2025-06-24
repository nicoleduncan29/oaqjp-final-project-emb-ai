from flask import Flask
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector?textToAnalyze=<statement>")
def emotion_dector_app(statement: str) -> str:
    analysis = emotion_detector(statement)
    response = f"<p>For the given statement, the system response is 'anger': {analysis['anger']}, 'disgust': {analysis['disgust']}, 'fear': {analysis['fear']}, 'joy': {analysis['joy']}, 'sadness': {analysis['sadness']}. The dominant emotion is <strong>{analysis['dominant_emotion']}</strong.</p>"

    return response