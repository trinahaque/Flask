from flask import Flask, render_template, redirect, request, session, flash
import re
Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

# @app.route('/')
#get puts value in url
@app.route('/')
#/ can not be method post
def index():

    return render_template("index.html")


@app.route('/validation', methods=['POST'])
def submit():
    # print request.form['password']
    # session['first_name']=request.form['first_name']

    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password'])< 1:
        flash(u"A field can not be empty", 'error')
        # print "Field can not be empty"

    elif not Email_Regex.match(request.form['email']):
        flash(u"Invalid Email Address. Please enter a valid email.", 'email_error')
        # print "email error"

    elif request.form['first_name'].isalpha() == False or request.form['last_name'].isalpha() == False:
        flash(u"Name can not have numbers", 'name_error')
        # print 'name_error'

    elif len(request.form['password']) < 3:
        flash(u"Password needs to be more than 8 characters", 'pw_length')
        # print "password needs to be 9 character long"

    elif request.form['password'] != request.form['confirm_password']:
        flash(u"Passwords need to match", 'pw_error')
        # print 'password'

    else:
        flash("Success")
        # print "success"
        session['first_name']=request.form['first_name']
        # return render_template("result.html", a=request.form['first_name'])
        return redirect('/')
        # , session['first_name']

    return redirect("/")

    # elif (not any(letter.isupper() for letter in request.form['password']) or not any(letter.islower() for letter in request.form['password']) or not any(letter.isdigit() for letter in request.form['password'] or len(request.form['password'] < 9):
    #     flash(u"Password needs one upper, one lower, one number, and more than 8 characters", 'pw_length')

app.run(debug=True)
