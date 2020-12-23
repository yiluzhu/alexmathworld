import json
from flask import Flask, request, Response
from flask_cors import CORS

from services.question import Question
from services.comment import Comment


app = Flask(__name__)
CORS(app)
qu = Question()
co = Comment()


@app.route('/hello')
def hello():
    return 'Hello Alex Maths World!'


@app.route('/questions', methods=['POST'])
def show_questions():
    body = json.loads(request.data)
    difficulty = body.get('difficulty')
    number = int(body.get('number'))
    question_list = qu.generate_questions(difficulty, number)
    return Response(json.dumps(question_list), 200, mimetype='application/json')


@app.route('/result', methods=['POST'])
def check_answer():
    body = json.loads(request.data)
    correct_answers, result = qu.check_answers(body.get('questions'), body.get('submittedAnswers'))
    return Response(json.dumps({'correct_answers': correct_answers, 'result': result}),
                    200, mimetype='application/json')


@app.route('/comments')
def load_comments():
    comments = co.load_all_comments()
    return Response(json.dumps({'comments': comments}),
                    200, mimetype='application/json')


@app.route('/comments', methods=['POST'])
def save_comments():
    body = json.loads(request.data)
    name = body.get('name')
    content = body.get('content')
    status_code = co.save_a_comment(name, content)
    msg = 'ok' if status_code == 200 else 'error'

    return Response(json.dumps({'msg': msg}),
                    status_code, mimetype='application/json')
