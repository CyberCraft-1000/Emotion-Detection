import unittest
from my_emotion_detector.emotion_detector import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        text = "I am happy."
        result = emotion_detector(text)
        self.assertIn('emotions', result)
        self.assertIn('joy', result['emotions'])

    def test_empty_text(self):
        result, status_code = emotion_detector("")
        self.assertEqual(status_code, 400)
        self.assertIn('error', result)
        self.assertEqual(result['error'], 'No text provided')

    def test_invalid_api_key(self):
        # Temporarily use an invalid API key to test error handling
        old_api_key = '<your_api_key>'
        # Set an invalid API key here to test
        result, status_code = emotion_detector("Test text")
        self.assertEqual(status_code, 500)
        self.assertIn('error', result)
        # Restore the valid API key after the test
        # Set the correct API key back

if __name__ == '__main__':
    unittest.main()
