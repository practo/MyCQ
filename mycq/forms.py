from flask.ext.wtf import Form, TextField, RadioField, Required, validators, FloatField
from flask.ext.wtf.html5 import EmailField, IntegerField
from mycq import user_store

class SignupForm(Form):
    name = TextField("Name", validators=[Required()])
    cgpa = FloatField("CGPA", validators=[Required()])
    branch = TextField("Branch", validators=[Required()])
    email = EmailField("Email", validators=[Required(), validators.Email()])
    token = TextField("Registration Token",
                      validators=[Required(),
                                  validators.regexp(r'^[0-9]{6}$',
                                                    message='Invalid registration token')])

    def validate_token(form, field):
        if len(field.errors) > 0:
            return
        if not user_store.sismember('signup_tokens', field.data):
            field.errors.append('Incorrect registration token')


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
