from flask import render_template, request, redirect, url_for
from mycq import app
from mycq.forms import SignupForm

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('take_test'))
    return render_template('signup.html', form=form)


@app.route('/take-test', methods=['GET', 'POST'])
def take_test():
    return "Under construction"
