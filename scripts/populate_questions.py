from mycq import user_store
import json

questions = json.load(open("questions.json", "r"))

for q in questions:
    user_store.hmset("question:" + str(q['id']), q)
