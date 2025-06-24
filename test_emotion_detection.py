import unittest

from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        emotion_statement_dict = {
            "joy": "I am glad this happened",
            "anger": "I am reall mad about this",
            "disgust": "I feel disgusted just hearing about this",
            "sadness": "I am so sad about this",
            "fear": "I am really afraid that this will happen"
        }
        for emotion, statement in emotion_statement_dict.items():
            self.assertEqual(emotion_detector(statement)["dominant_emotion"], emotion)

if __name__ == "__main__":
    unittest.main()