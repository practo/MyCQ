from flask.ext.wtf import Form, TextField, RadioField, Required, validators
from flask.ext.wtf.html5 import EmailField, IntegerField
from mycq import user_store

class SignupForm(Form):
    name = TextField("Name", validators=[Required()])
    roll_no = TextField("Roll No", validators=[Required()])
    branch = TextField("Branch", validators=[Required()])
    email = EmailField("Email", validators=[Required(), validators.Email()])


class QuestionFormMixin():
    question = IntegerField("Question Id", validators=[Required()])

    def validate_question(form, field):
        qid = int(field.data)
        question = user_store.hgetall('question:' + str(qid))
        if not question:
            field.errors.append('Question %d does not exist' % qid)


class QuestionForm(Form, QuestionFormMixin):
    answer = RadioField("Choices", choices=[], validators=[Required()])


class SkipQuestionForm(Form, QuestionFormMixin):
    pass


class CompleteTestForm(Form):
    pass
