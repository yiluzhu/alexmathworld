"""
To run chalice locally:
    chalice local --port=5000 --no-autoreload

To deploy app to AWS Lambda:
    chalice deploy
"""

import json
from chalice import Chalice, Response

from chalicelib.services.question import Question
from chalicelib.services.comment import Comment


app = Chalice(app_name='alexworld')
app.api.cors = True

qu = Question()
co = Comment()


@app.route('/hello')
def hello():
    return 'Hello Alex Maths World!'


@app.route('/questions', methods=['POST'])
def show_questions():
    body = app.current_request.json_body
    difficulty = body.get('difficulty')
    number = int(body.get('number'))
    question_list = qu.generate_questions(difficulty, number)
    return Response(json.dumps(question_list), headers={'Content-Type': 'application/json'}, status_code=200)


@app.route('/result', methods=['POST'])
def check_answer():
    body = app.current_request.json_body
    correct_answers, result = qu.check_answers(body.get('questions'), body.get('submittedAnswers'))
    return Response(json.dumps({'correct_answers': correct_answers, 'result': result}),
                    headers={'Content-Type': 'application/json'}, status_code=200)


@app.route('/comments')
def load_comments():
    comments = co.load_all_comments()
    return Response(json.dumps({'comments': comments}),
                    headers={'Content-Type': 'application/json'}, status_code=200)


@app.route('/comments', methods=['POST'])
def save_comments():
    body = app.current_request.json_body
    name = body.get('name')
    content = body.get('content')
    status_code = co.save_a_comment(name, content)
    msg = 'ok' if status_code == 200 else 'error'

    return Response(json.dumps({'msg': msg}),
                    headers={'Content-Type': 'application/json'}, status_code=200)
