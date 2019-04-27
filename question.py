import random
import time
from secrets import passcode
import jinja2


class Question:
    def __init__(self):
        self.difficulty_dict = {
            'easy': (1, 9),
            'medium': (3, 12),
            'hard': (5, 20),
            'extreme': (11, 40),
        }
        self.questions = []
        self.answers = []
        self.difficulty = None
        self.number = None
        self.timer = 0

    def generate_questions(self, difficulty=None, number=None):
        if difficulty:
            self.difficulty = difficulty
        if number:
            self.number = number

        self.questions = []
        self.answers = []
        self.timer = time.time()
        start, end = self.difficulty_dict[self.difficulty]
        for i in range(int(self.number)):
            a = random.randint(start, end)
            b = random.randint(start, end)
            c = random.randint(start, end)
            d = random.randint(start, end)
            op = '+' if random.choice([True, False]) else '-'
            div_str = self.create_division(c, d)
            question_str = f'{a} x {b} {op} {div_str}'
            answer = eval(question_str.replace('x', '*').replace('&divide;', '/'))
            self.questions.append(question_str)
            self.answers.append(answer)
        return self.questions

    def create_division(self, c, d):
        mul = c * d
        return f'{mul} &divide; {c}'

    def check_answers(self, submitted_answers):
        results = []
        for answer, submit_answer, question in zip(self.answers, submitted_answers, self.questions):
            if submit_answer == passcode:
                correctness = True
                submit_answer = int(answer)
            else:
                try:
                    submit_answer = int(submit_answer)
                    correctness = answer == submit_answer
                except ValueError:
                    correctness = False
            results.append([question, submit_answer, correctness])
        time_taken = time.time() - self.timer
        return results, time_taken, self.difficulty
