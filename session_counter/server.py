from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsCountKey"

@app.route('/')
def index():
    if "counter" in session:
        pass
    else:
        session["counter"] = 1

    return render_template("index.html", counter=session['counter'])

@app.route('/normal')
def normal():
    session["counter"]= session["counter"]+1
    return redirect('/')

@app.route('/ninja')
def ninja():
    session["counter"]= session["counter"]+2
    return redirect('/')

@app.route('/hacker')
def hacker():
    session["counter"]= 0
    return redirect('/')

app.run(debug=True)
