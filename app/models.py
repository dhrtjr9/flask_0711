from app import db

class Question(db.Model):#db의 모델을 상속받아 question테이블을 만듬
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    # 답변의 고유번호 - 숫자 PK다 : 다음번호 자동 생성from models import Question, Answer
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    # Foreign Key로 걸려있는 데이블에서 삭제가 발생했을 때
        # 1) Answer도 같이 지운다
        # 2) Answer는 남겨 놓는다
            # Question의 id를 남겨놓는다.
            # Question의 id를 삭제한다.
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) #ondelete 삭제 시, 어떤 상태를 유지하고 있을 것인지.
    question = db.relationship('Question', backref=db.backref('answer_set'))