from mycq import user_store
from uuid import uuid4
import random

class User():
    def __init__(self, form):
        self.id = None
        self.score = 0
        self.name = form.name.data
        self.email = form.email.data
        self.branch = form.branch.data
        self.roll_no = form.roll_no.data

    def get_id(self):
        return self.id

    def save(self):
        if self.id is None:
            DESIRED_QUESTIONS = 3
            self.id = str(uuid4())
            all_questions = user_store.keys('question:*')
            all_questions = [int(x[9:]) for x in all_questions]
            if len(all_questions) < DESIRED_QUESTIONS:
                raise Exception("Not enough questions")
            random_questions = random.sample(all_questions, DESIRED_QUESTIONS)
            for q in random_questions:
                user_store.sadd('user_questions:' + self.id, q)
        user_store.hmset('user:' + self.id, {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'branch': self.branch,
            'roll_no': self.roll_no,
            'score': self.score
        })

    def can_answer_question(self, qid):
        if not user_store.sismember('user_questions:' + self.id, qid):
            return False
        # Presently users are not allowed to answer the question twice
        if user_store.sismember('user_answered_questions:' + self.id, qid):
            return False
        return True

    def can_skip_question(self, qid):
        if not user_store.sismember('user_questions:' + self.id, qid):
            return False
        # Presently users are not allowed to skip the question twice
        if user_store.sismember('user_skipped_questions:' + self.id, qid):
            return False
        return True

    def answer_question(self, form):
        qid = int(form.question.data)
        user_store.sadd('user_answered_questions:' + self.id, qid)
        user_store.hset('user_answers:' + self.id, qid, form.answer.data)

    def skip_question(self, form):
        qid = int(form.question.data)
        user_store.sadd('user_skipped_questions:' + self.id, qid)

    def get_next_unanswered(self):
        unanswered = user_store.sdiff('user_questions:' + self.id,
                                      'user_answered_questions:' + self.id)
        skipped = user_store.smembers('user_skipped_questions:' + self.id)
        new = unanswered - skipped
        if len(new) > 0:
            return sorted(list(new))[0]
        return None

    def get_overview(self):
        qids = user_store.smembers('user_questions:' + self.id)
        questions = []
        for qid in sorted(list(qids)):
            question = {'id': qid}
            if user_store.sismember('user_answered_questions:' + self.id, qid):
                question['status'] = 'answered'
            elif user_store.sismember('user_skipped_questions:' + self.id, qid):
                question['status'] = 'skipped'
            else:
                question['status'] = 'new'
            questions.append(question)
        return questions

    def has_completed_test(self):
        return user_store.sismember('test_completed_users', self.id)

    def complete_test(self):
        return user_store.sadd('test_completed_users', self.id)
