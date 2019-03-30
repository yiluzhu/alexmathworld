import random


class Question:
    def __init__(self):
        self.question_dict = {}

    def generate_a_question(self, question_id):
        if question_id not in self.question_dict:
            a = random.randint(1, 12)
            b = random.randint(1, 12)
            c = random.randint(1, 12)
            d = random.randint(1, 12)
            op = '+' if random.choice([True, False]) else '-'
            question_str = f'{a} x {b} {op} {c} x {d}'
            answer = eval(question_str.replace('x', '*'))
            self.question_dict[question_id] = question_str, answer
        return self.question_dict[question_id][0]

    def get_an_answer(self, question_id):
        if question_id in self.question_dict:
            question_str, answer = self.question_dict.get(question_id)
            return str(answer)
        else:
            return f'No question found for question {question_id}.'
