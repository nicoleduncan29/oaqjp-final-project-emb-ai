from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_dector_app() -> str:
    statement = request.args.get("textToAnalyze")
    analysis = emotion_detector(statement)
    
    if analysis['dominant_emotion'] is None:
        response = "<p><strong>Invalid text! Please try again!</strong></p>"
    else:
        response = f"<p>For the given statement, the system response is 'anger': {analysis['anger']}, 'disgust': {analysis['disgust']}, 'fear': {analysis['fear']}, 'joy': {analysis['joy']}, 'sadness': {analysis['sadness']}. The dominant emotion is <strong>{analysis['dominant_emotion']}</strong.</p>"

    return response