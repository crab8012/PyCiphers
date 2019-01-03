from flask import Flask, render_template, redirect, url_for, request
from forms import CaesarForm
from crypto import Caesar

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    form = CaesarForm()
    if form.validate_on_submit():
        print("FOMAM")
        return redirect(url_for('index'))
    return render_template("caesar.html")

@app.route("/result", methods=["POST"])
def result():
    string = request.form['string']
    rotation = request.form['rotation']
    newString = Caesar.encode(string, rotation)
    print(newString)
    return newString


@app.route("/atbash")
def atbash():
    return render_template("atbash.html")

@app.route("/enigma")
def enigma():
    return render_template("enigma.html")

app.run('0.0.0.0', '80')