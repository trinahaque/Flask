from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', hello='It is me')

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', hello='It is me')

@app.route('/dojos/new')
def dojos_new():
    return render_template('dojos_new.html')


app.run(debug=True)
