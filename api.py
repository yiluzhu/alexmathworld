from flask import Flask, render_template, request
from maths_question import Question


app = Flask(__name__)
qu = Question()
blank_line_html = '<br>' * 20



@app.route('/')
def show_questions():
    question_list = qu.generate_questions()
    return render_template('question.html', question_list=question_list, enumerate=enumerate)



@app.route('/submit', methods=['POST'])
def check_answer():
    submitted_answers = [request.form.get(str(i)) for i in range(5)]
    result = qu.check_answers(submitted_answers)
    return render_template('result.html', result=result)


app.run()

