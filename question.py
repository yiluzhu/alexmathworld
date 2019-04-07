import random


class Question:
    def __init__(self):
        self.difficulty_dict = {
            'easy': (1, 9),
            'medium': (3, 12),
            'hard': (5, 20),
            'nightmare': (11, 40),
        }
        self.questions = []
        self.answers = []

    def generate_questions(self, difficulty, number):
        self.questions = []
        self.answers = []
        start, end = self.difficulty_dict[difficulty]
        for i in range(int(number)):
            a = random.randint(start, end)
            b = random.randint(start, end)
            c = random.randint(start, end)
            d = random.randint(start, end)
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
