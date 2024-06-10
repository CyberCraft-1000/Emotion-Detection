import os
import unittest
from my_emotion_detector.emotion_detector import emotion_detector

# Debugging information
print("Current Working Directory:", os.getcwd())
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))

class TestEmotionDetector(unittest.TestCase):
 def test_emotion_detection(self):
 text = "text = "I am happy today!."
 result = emotion_detector(text)
 self.assertIn('emotions', result)
 self.assertIn('joy', result['emotions'])

if __name__ == '__main__':
 unittest.main()