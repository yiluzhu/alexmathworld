from flask import Flask
from maths import Question


app = Flask(__name__)
qu = Question()
blank_line_html = '<br>' * 20


@app.route('/<question_id>')
def get_a_question(question_id):
    question_str = qu.generate_a_question(question_id)
    return blank_line_html + f'<h1><center>{question_str}<h1>'


@app.route('/<question_id>/a')
def get_an_answer(question_id):
    answer = qu.get_an_answer(question_id)
    return blank_line_html + f'<h1><center>{answer}<h1>'


app.run()
