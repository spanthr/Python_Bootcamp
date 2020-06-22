from Question import Question

question_prompts = [
    "What are the apples \n (a)Red/Green \n(b)Purple \n(c) Orange \n\n",
    "What are the strwaberries \n (a)Red \n(b)Purple \n(c) Orange \n\n",
    "What are the bananas \n (a)Red/Green \n(b)Purple \n(c) Yellow \n\n"

]

question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " / " + str(len(questions))+ " correct")
run_test(question)