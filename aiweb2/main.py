from flask import Flask, render_template, request
from classification import get_class
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/expl")
def expl():
    return render_template("expl.html")


@app.route('/upload', methods =  ["GET", "POST"])

def upload():
    file = request.files['file']
    file.save('static/img/' + file.filename)
    imgclass, score = get_class("keras_model.h5", "labels.txt", 'static/img/' + file.filename)
    print(imgclass)
    return render_template('index.html', imgclass = imgclass.strip())

app.run(debug=True)