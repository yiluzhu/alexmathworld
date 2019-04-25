from flask import Flask, render_template, request
from question import Question


app = Flask(__name__)
qu = Question()


@app.route('/')
def index():
    return render_template('main.html', range=range)


@app.route('/questions', methods=['GET', 'POST'])
def show_questions():
    if request.method == 'GET':
        question_list = qu.generate_questions()
    else:
        difficulty = request.form.get('difficulty')
        number = request.form.get('number')
        question_list = qu.generate_questions(difficulty, number)
    return render_template('question.html', question_list=question_list, enumerate=enumerate, replace=str.replace)


@app.route('/check', methods=['POST'])
def check_answer():
    submitted_answers = [request.form.get(str(i)) for i in range(10)]
    result, time_taken = qu.check_answers(submitted_answers)
    return render_template('result.html', result=result, time_taken=round(time_taken, 1))



app.run()

