from mycq import user_store
import csv
import sys

def calculate_score(user_id):
    score = 0
    answers = user_store.hgetall('user_answers:' + user_id)
    for qid in answers.keys():
        correct_answer = user_store.hget('question:' + str(qid), 'correct_answer')
        if answers[qid] == correct_answer:
            score += 10
        else:
            score -= 5
    return score

user_keys = user_store.keys('user:*')
user_scores = []
for user_key in user_keys:
    user = user_store.hgetall(user_key)
    user_score = calculate_score(user['id'])
    user_scores.append((user['id'], user['name'], user['email'], user['roll_no'], user['branch'], user_score))
    user_store.hset(user_key, 'score', user_score)

top_users = sorted(user_scores, key=lambda x:x[-1], reverse=True)
cw = csv.writer(sys.stdout)
cw.writerow(('id', 'name', 'email', 'roll_no', 'branch', 'score'))
for user in top_users:
    cw.writerow(user)
