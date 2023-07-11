from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy() #db는 sqlalchemy로 통제 / ORM
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config) #config.py 속성
    db.init_app(app)
    migrate.init_app(app,db)

    from .views import basic_views, okseok_views
    app.register_blueprint(basic_views.fisa)
    app.register_blueprint(okseok_views.okseok)
    print(__name__)

    @app.route('/about_me')
    def about_me():
        return f'저는 {__name__} 입니다.'

    @app.route('/hello')
    def hello():
        return f'안녕하세요'

    @app.route('/bye')
    def bye():
        return f'잘가세요'
    
    return app