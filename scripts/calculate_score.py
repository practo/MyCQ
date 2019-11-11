from mycq import user_store
import csv
import sys


def calculate_result(user_id):
    score = 0
    questions_answered_correctly = 0
    questions_answered_incorrectly = 0
    answers = user_store.hgetall('user_answers:' + user_id)
    for qid in answers.keys():
        correct_answer = user_store.hget('question:' + str(qid), 'correct_answer')
        if answers[qid] == correct_answer:
            score += 10
            questions_answered_correctly += 1
        else:
            score -= 5
            questions_answered_incorrectly += 1
    return {
            'score': score,
            'q_correct': questions_answered_correctly,
            'q_incorrect': questions_answered_incorrectly
            }


user_keys = user_store.keys('user:*')
user_scores = []
for user_key in user_keys:
    user = user_store.hgetall(user_key)
    result = calculate_result(user['id'])
    user_score = result['score']
    user_scores.append((user['id'], user['name'], user['email'], user['cgpa'], user['branch'], user_score,
                        result['q_correct'], result['q_incorrect']))
    user_store.hset(user_key, 'score', user_score)

top_users = sorted(user_scores, key=lambda x: x[5], reverse=True)
cw = csv.writer(sys.stdout)
cw.writerow(('id', 'name', 'email', 'cgpa', 'branch', 'score', 'no_of_q_correct', 'no_of_q_incorrect'))
for user in top_users:
    cw.writerow(user)
