from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
target_names = joblib.load("target_names.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        message = request.form["message"]
        vec = vectorizer.transform([message])
        pred = model.predict(vec)[0]
        result = target_names[pred]
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
