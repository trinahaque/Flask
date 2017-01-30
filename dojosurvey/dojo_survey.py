from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "DojoSurvey"

@app.route('/')
def survey():
    return render_template('dojo_survey_index.html')


@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    email = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(name)<1 or (len(comment) < 1 or len(comment)>120):
        flash("name or comment can not be empty or comment has to be less than 120 characters")
        return redirect("/")

    else:
        flash("Your name is {}".format(name))
        return render_template('dojo_survey_result.html', a=name, b=email, c=language, d=comment)

    # return render_template('dojo_survey_result.html', a=name, b=email, c=language, d=comment)


app.run(debug=True)
