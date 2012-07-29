from mycq import user_store

questions = [
    {
        "id": 1,
        "question": "What percentage of numbers from 1 to 70 have squares that end in the digit 1?",
        "option1": "1",
        "option2": "14",
        "option3": "20",
        "option4": "21",
        "correct_answer": 3
    },
    {
        "id": 2,
        "question": "What is the command swapon used for in linux?",
        "option1": "Create a swap area in RAM",
        "option2": "Enables swapping of pages",
        "option3": "Specifies devices on which swapping should take place",
        "option4": "Creates a swap partition",
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
