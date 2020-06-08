from questions import Question

question_prompt = [
    "What Color?\n(a) red/green\n(b) purple\n(c) orange\n\n",
    "What Size?\n(a) red/green\n(b) purple\n(c) orange\n\n",
    "What Weight?\n(a) red/green\n(b) purple\n(c) orange\n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b")
]


def runTest(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score +=1
    print("you got : " + str(score) + "/" + str(len(questions)) + " CORRECT")


runTest(questions)