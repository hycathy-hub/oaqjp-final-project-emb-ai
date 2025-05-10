"""Final project emotion detector deployed as Flask web app"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """call emotion detector method"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    # Return a formatted string
    return (f"For the given statement, the system response is "
            f"'anger': {anger_score}, "
            f"'disgust': {disgust_score}, "
            f"'fear': {fear_score}, "
            f"'joy': {joy_score}, "
            f"and 'sadness': {sadness_score}. "
            f"The dominant emotion is <b>{dominant_emotion}</b>")

@app.route("/")
def render_index_page():
    """to render index.html"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
