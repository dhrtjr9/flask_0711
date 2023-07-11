from flask import Flask #플라스크 패키지에서 플라스크를 가져다 씀

# 따로 set Flask_APP= 파일명 적어주지 않으면 app.py 기본으로 발동
app = Flask(__name__) #한장짜리 플라스크 서버의 시작점

def create_app():
    app = Flask(__name__)
    print(__name__)

    @app.route('/about_me')
    def about_me():
        return f'저는 {__name__} 입니다' 

    @app.route('/hello')
    def hello():
        return f'안녕하세요' 

    @app.route('/bye')
    def bye():
        return f'안녕히가세요' 
    
    #블루프인트에 등록된 피사를 담은 객체의 함수를 실행해줘~
    from .views import basic_views
    app.register_blueprint(basic_views.fisa)
    
    return app