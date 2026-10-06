"""
Servidor Flask para la aplicación de detección de emociones con Watson NLP.
"""

from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
  """
  Analiza el texto enviado en la solicitud HTTP GET y devuelve las puntuaciones de las
  emociones junto con la emoción dominante.
  """
  text_to_analyze = request.args.get("textToAnalyze")

  response = emotion_detector(text_to_analyze)

  if response["dominant_emotion"] is None:
    return "Invalid text! Please try again!"

  return (
      f"For the given statement, the system response is 'anger': {response['anger']}, "
      f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
      f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
  )


@app.route("/")
def render_index_page():
  """
  Renderiza la interfaz de usuario principal de la aplicación web.
  """
  return render_template("index.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)