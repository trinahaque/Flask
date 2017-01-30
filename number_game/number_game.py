from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsGreatGame"

def check_session():
    if "key" in session:
        pass
    else:
        session["key"] = random.randrange(0,101)



@app.route('/')
def great_game():
    check_session()
    return render_template("number_game.html")


# @app.route("/check/<guess>")
# if i don't use form, use the route above. get method. not recommended
@app.route("/check", methods=['POST'])
def submit():
    testData = request.form['guess']
    number = int(testData)


    if number == session["key"]:

        session['result'] ='equal' + " " + str(session["key"])

    elif number < session["key"]:

        session['result'] ='low'+ " " + str(session["key"])
    else:

        session['result'] = 'high'+ " " + str(session["key"])

    return redirect("/")

@app.route('/reset')
def reset():
    session.pop('key')
    #session["key"]= random.randrange(0,100)
    return redirect("/")

app.run(debug=True)
