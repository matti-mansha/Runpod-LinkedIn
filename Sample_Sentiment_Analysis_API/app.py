from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    text = data['text']
    result = sentiment_pipeline(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
