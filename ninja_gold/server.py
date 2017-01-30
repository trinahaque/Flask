from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = "ThisIsNinjaGold"

def page_load():
    if "key" in session:
        pass
    else:
        session['key']=0

    if 'history' not in session:
        session['history']=[]

@app.route('/')
def index():
    page_load()
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def farm():

    if request.form['building']=='farm':
        session['gold'] = random.randrange(10,21)
        session['key']=session['key']+session['gold']
        session['time']=datetime.datetime.utcnow()
        session['history'].append("Earned"+ " " + str(session['gold'])+ " "+ "from the farm"+ str(session['time']))

    elif request.form['building']=='cave':
        session['gold'] = random.randrange(5,10)
        session['key']=session['key']+session['gold']
        session['time']=datetime.datetime.utcnow()
        session['history'].append("Earned"+ " " + str(session['gold'])+ " "+ "from the cave"+ str(session['time']))

    elif request.form['building']=='house':
        session['gold'] = random.randrange(2,5)
        session['key']=session['key']+session['gold']
        session['time']=datetime.datetime.utcnow()
        session['history'].append("Earned"+ " " + str(session['gold'])+ " "+ "from the house"+ str(session['time']))

    else:
        session['gold'] = random.randrange(-50,51)
        session['key']=session['key']+session['gold']
        session['time']=datetime.datetime.utcnow()
        session['history'].append("Earned"+ " " + str(session['gold'])+ " "+ "from the casino"+ str(session['time']))

    return redirect('/')
#name is the key, value in the value in input

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('key')
    #session['key']=0
    session['history']=[]
    return redirect('/')

app.run(debug=True)
