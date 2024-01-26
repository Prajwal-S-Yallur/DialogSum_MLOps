from flask import Flask, request
from transformers import pipeline

distilled_student_sentiment_classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
    return_all_scores=True
)

# distilled_student_sentiment_classifier ("I love this movie and i would watch it again and again!")

# Initialize Flask
app = Flask(__name__)

@app.route("/get_sentiment", methods = ["POST", "GET"])
def get_sentiment():

  if request.method == "POST":
    # Get the data from the form and placed into a variable.
    input_data = request.form

  input_sentence = input_data["input_sentence"],
  predicted_sentiments = distilled_student_sentiment_classifier (input_sentence)
  return predicted_sentiments


if __name__ == "__main__":
    app.run(debug=True, port=5000)