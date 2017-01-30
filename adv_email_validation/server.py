from flask import Flask, render_template, redirect, request, session, flash
import re
Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email can not be blank")
        # return redirect('/')
    elif not Email_Regex.match(request.form['email']):
        flash("Invalid Email Address. Please enter a valid email.")
    else:
        flash("Success")
        # return redirect("/")
    return redirect("/")
app.run(debug=True)
