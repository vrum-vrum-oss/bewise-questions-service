from . import api
from flask import jsonify, request
from .. import db
from ..models import Question
import requests


QUESTIONS_PUBLIC_API_URL = 'https://jservice.io/api/random'


def get_questions_from_public_api(URL: str, count: int):
    r = requests.get(URL, params={'count': count})
    return r.json()
    

@api.route('/questions', methods=['POST'])
def request_questions():
    questions_num = int(request.json.get('questions_num'))
    r = get_questions_from_public_api(URL=QUESTIONS_PUBLIC_API_URL, count=questions_num)
    
    if questions_num == 0:
        return r, 200
    if questions_num < 0:
        return r, 500
    
    for r_question in r:
        question = Question.from_json(r_question)
        # make additional requests to public api until a unique question is returned 
        while Question.query.get(question.id) is not None:
            r_question = get_questions_from_public_api(URL=QUESTIONS_PUBLIC_API_URL, count=1)
            question = Question.from_json(r_question)
            
        db.session.add(question)
        db.session.commit()
    
    # respond with last saved question
    return jsonify(question.to_json()), 201