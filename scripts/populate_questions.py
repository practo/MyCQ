from mycq import user_store

questions = [
    {
        "id": 1,
        "question": "Sample question 1",
        "option1": "Sample answer 1",
        "option2": "Sample answer 2",
        "option3": "Sample answer 3",
        "option4": "Sample answer 4",
        "correct_answer": 3
    },
    {
        "id": 2,
        "question": "Sample question 2",
        "option1": "Sample answer 1",
        "option2": "Sample answer 2",
        "option3": "Sample answer 3",
        "option4": "Sample answer 4",
        "correct_answer": 3
    },
    {
        "id": 3,
        "question": "Sample question 3",
        "option1": "Sample answer 1",
        "option2": "Sample answer 2",
        "option3": "Sample answer 3",
        "option4": "Sample answer 4",
        "correct_answer": 3
    },
]

for q in questions:
    user_store.hmset("question:" + str(q['id']), q)
