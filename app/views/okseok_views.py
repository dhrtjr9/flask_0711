from flask import Blueprint

                #우리가 부를 이름, flask 프레임궈크가 찾을 이름, 라우팅주소
okseok = Blueprint('okseok', __name__, url_prefix='/okseok')

@okseok.route('/about_me')
def about_me():
    return f'저는 {__name__} 입니다' 

@okseok.route('/hello')
def hello():
    return f'안녕하세요' 

@okseok.route('/bye')
def bye():
    return f'안녕히가세요' 
    