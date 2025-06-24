import json
import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(
    text_to_analyze: str
) -> str:
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url=URL,
        headers=HEADERS,
        json=input_json
    )

    text = json.loads(response.text)
    emotion_scores = text["emotionPredictions"][0]["emotion"]
    dominant_emotion_key = max(emotion_scores, key=lambda k: emotion_scores[k])
    return_text = {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"],
        "dominant_emotion": dominant_emotion_key
    }
    return return_text