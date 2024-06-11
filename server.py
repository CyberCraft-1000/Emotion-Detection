from flask import Flask, request, jsonify
from my_emotion_detector.emotion_detector import emotion_detector

app = Flask(__name__)

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    try:
        result = emotion_detector(text)
        if isinstance(result, tuple) and 'error' in result[0]:
            return jsonify(result[0]), result[1]  # Return status code from emotion_detector
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
