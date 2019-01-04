from flask import Flask, render_template, redirect, url_for, request
from crypto import Caesar

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    return render_template("caesar.html")

@app.route("/result", methods=["POST"])
def result():
    string = request.form['string']
    rotation = request.form['rotation']
    mode = request.form['mode']
    if mode == 'decode':
        newString = Caesar.decode(string, rotation)
    elif mode == 'encode':
        newString = Caesar.encode(string, rotation)
    else:
        newString = "ERROR: INVALID MODE."
    print(newString)
    return render_template('result.html', text=newString)


@app.route("/atbash")
def atbash():
    return render_template("atbash.html")

@app.route("/enigma")
def enigma():
    return render_template("enigma.html")

app.run('0.0.0.0', '80', debug=True)