import json
from flask import Flask, request, Response
from question import Question
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
qu = Question()


@app.route('/hello')
def hello():
    return 'hello Alex Maths World!'


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


if __name__ == '__main__':
    app.run(debug=True)
