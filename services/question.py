import random
from services.secrets import passcode


class Question:
    def __init__(self):
        self.difficulty_dict = {
            'easy': (1, 9),
            'medium': (3, 12),
            'hard': (5, 20),
            'extreme': (11, 40),
        }

    def generate_questions(self, difficulty, number):
        questions = []
        start, end = self.difficulty_dict[difficulty]
        for i in range(number):
            a = random.randint(start, end)
            b = random.randint(start, end)
            c = random.randint(start, end)
            d = random.randint(start, end)
            op = '+' if random.choice([True, False]) else '-'
            div_str = self.create_division(c, d)
            question_str = f'{a} x {b} {op} {div_str}'
            questions.append(question_str)
        return questions

    def create_division(self, c, d):
        mul = c * d
        return f'{mul} \u00f7 {c}'

    def check_answers(self, questions, submitted_answers):
        results = []
        correct_answers = []
        for question, submit_answer in zip(questions, submitted_answers):
            correct_answer = eval(question.replace('x', '*').replace('\u00f7', '/'))
            if submit_answer == passcode:
                correctness = True
            else:
                try:
                    submit_answer = int(submit_answer)
                except ValueError:
                    correctness = False
                else:
                    correctness = correct_answer == submit_answer
            results.append(correctness)
            correct_answers.append(correct_answer)
        return correct_answers, results
