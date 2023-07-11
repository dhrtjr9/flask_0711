import os

# db를 저장할 폴더/파일 이름 설정
BASE_DIR = os.path.dirname(__file__) #file 경로를 사용할 것이다.

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'test.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False


#flask db init
#flask db migrate
