import random


class Question:
    def __init__(self):
        self.questions = []
        self.answers = []

    def generate_questions(self):
        self.questions = []
        self.answers = []
        for i in range(5):
            a = random.randint(1, 12)
            b = random.randint(1, 12)
            c = random.randint(1, 12)
            d = random.randint(1, 12)
            op = '+' if random.choice([True, False]) else '-'
            question_str = f'{a} x {b} {op} {c} x {d}'
            answer = eval(question_str.replace('x', '*'))
            self.questions.append(question_str)
            self.answers.append(answer)
        return self.questions

    def check_answers(self, submitted_answers):
        result = []
        for answer, submit_answer, question in zip(self.answers, submitted_answers, self.questions):
            try:
                submit_answer = int(submit_answer)
                correctness = answer == submit_answer
            except ValueError:
                correctness = False
            result.append([question, submit_answer, correctness])
        return result
