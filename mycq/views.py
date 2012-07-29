from flask import render_template, request, redirect, url_for, session, abort
from mycq import app, user_store
from mycq.forms import SignupForm, QuestionForm, SkipQuestionForm, CompleteTestForm
from mycq.models import User
from functools import wraps

def signup_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('signup'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET'])
@signup_required
def index():
    user = session.get('user')
    if user.has_completed_test():
        return redirect(url_for('thankyou'))
    else:
        return redirect(url_for('overview'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        user_store.srem('signup_tokens', form.token.data)
        user = User(form)
        user.save()
        session['user'] = user
        return redirect(url_for('rules'))
    return render_template('signup.html', form=form)


@app.route('/rules', methods=['GET'])
@signup_required
def rules():
    user = session.get('user')
    if user.has_completed_test():
        return redirect(url_for('thankyou'))
    return render_template('rules.html')


@app.route('/question/', defaults={'qid': None}, methods=['GET'])
@app.route('/question/<int:qid>', methods=['GET', 'POST'])
@signup_required
def question(qid):
    user = session.get('user')
    form = QuestionForm(request.form)
    if qid is None:
        qid = user.get_next_unanswered()
        if qid is None:
            return redirect(url_for('overview'))
        return redirect(url_for('question', qid=qid))
    form.question.data = qid
    if not user.can_answer_question(form.question.data):
        abort(400, "You are not allowed to answer this question")
    data = user_store.hgetall('question:' + str(qid))
    form.question.label = data['question']
    form.answer.choices = list()
    form.answer.choices.append(('1', data['option1']))
    form.answer.choices.append(('2', data['option2']))
    form.answer.choices.append(('3', data['option3']))
    form.answer.choices.append(('4', data['option4']))
    if form.validate_on_submit():
        user.answer_question(form)
        next_qid = user.get_next_unanswered()
        if next_qid:
            return redirect(url_for('question', qid=next_qid))
        else:
            return redirect(url_for('overview'))
    skip_form = SkipQuestionForm()
    return render_template('question.html', form=form, skip_form=skip_form)


@app.route('/overview', methods=['GET'])
@signup_required
def overview():
    user = session.get('user')
    if user.has_completed_test():
        return redirect(url_for('thankyou'))
    questions = user.get_overview()
    complete_form = CompleteTestForm()
    return render_template('overview.html', questions=questions, complete_form=complete_form)


@app.route('/skip-question/<int:qid>', methods=['POST'])
@signup_required
def skip_question(qid):
    user = session.get('user')
    form = SkipQuestionForm(request.form)
    form.question.data = qid
    if not user.can_skip_question(form.question.data):
        abort(400, "You are not allowed to skip this question")
    if form.validate_on_submit():
        user.skip_question(form)
        next_qid = user.get_next_unanswered()
        if next_qid:
            return redirect(url_for('question', qid=next_qid))
        else:
            return redirect(url_for('overview'))
    abort(400, form.errors)


@app.route('/finish', methods=['POST'])
@signup_required
def finish():
    complete_form = CompleteTestForm()
    user = session.get('user')
    if complete_form.validate_on_submit():
        user.complete_test()
        return redirect(url_for('thankyou'))
    abort(400, complete_form.errors)


@app.route('/thankyou')
@signup_required
def thankyou():
    return render_template('/thankyou.html')
