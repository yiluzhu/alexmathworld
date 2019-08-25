import json
from flask import Flask, request, Response
from question import Question
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
qu = Question()


@app.route('/questions', methods=['GET', 'POST'])
def show_questions():
    if request.method == 'GET':
        question_list = qu.generate_questions()
    else:
        body = json.loads(request.data)
        difficulty = body.get('difficulty')
        number = int(body.get('number'))
        question_list = qu.generate_questions(difficulty, number)
    return Response(json.dumps(question_list), 200, mimetype='application/json')


@app.route('/result', methods=['POST'])
def check_answer():
    body = json.loads(request.data)
    print('answers are', body.get('answers'))
    result = qu.check_answers(body.get('questions'), body.get('answers'))
    return Response(json.dumps(result), 200, mimetype='application/json')


app.run()

