from . import db


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    created_at = db.Column(db.DateTime)


    def __repr__(self):
        return '<Question id: {}, question: {}>'.format(self.id, self.question)
    
    
    def to_json(self):
        json_question = {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'created_at': self.created_at,
        }
        return json_question
    
    
    @staticmethod
    def from_json(json_question):
        id = json_question.get('id')
        question = json_question.get('question')
        answer = json_question.get('answer')
        created_at = json_question.get('created_at')
        return Question(id=id, question=question, answer=answer, created_at=created_at)
    