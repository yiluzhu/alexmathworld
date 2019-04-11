import random
from secrets import passcode


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
        self.difficulty = None
        self.number = None

    def generate_questions(self, difficulty=None, number=None):
        if difficulty:
            self.difficulty = difficulty
        if number:
            self.number = number

        self.questions = []
        self.answers = []
        start, end = self.difficulty_dict[self.difficulty]
        for i in range(int(self.number)):
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
        results = []
        for answer, submit_answer, question in zip(self.answers, submitted_answers, self.questions):
            if submit_answer == passcode:
                correctness = True
                submit_answer = answer
            else:
                try:
                    submit_answer = int(submit_answer)
                    correctness = answer == submit_answer
                except ValueError:
                    correctness = False
            results.append([question, submit_answer, correctness])
        return results
