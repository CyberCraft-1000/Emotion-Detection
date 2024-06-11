from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def emotion_detector(text):
    if not text:
        return {'error': 'No text provided'}, 400
    try:
        authenticator = IAMAuthenticator('<your_api_key>')
        nlu = NaturalLanguageUnderstandingV1(
            version='2021-08-01',
            authenticator=authenticator
        )
        nlu.set_service_url('<your_service_url>')

        response = nlu.analyze(
            text=text,
            features=Features(emotion=EmotionOptions())
        ).get_result()

        emotions = response['emotion']['document']['emotion']
        formatted_output = {
            'text': text,
            'emotions': emotions
        }

        return formatted_output
    except Exception as e:
        return {'error': str(e)}, 500
