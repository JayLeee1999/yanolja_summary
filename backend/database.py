# database.py
"""
pip install sqlalchemy
DB 연결과 관련된 정보 설정
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from db_env import user, password, host, db_name
from dotenv import load_dotenv
import os


# 환경변수 로딩
load_dotenv('../.env', override=True)    
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
DB_NAME = os.environ.get('DB_NAME')  

# sqlite 연결 시
# DB_URL = 'sqlite:///todo.sqlite3'
# DB_URL = 'sqlite:///todos_db.sqlite3'
# 데이터베이스에 연결하는 엔진을 생성하는 함수
# engine = create_engine(DB_URL, connect_args={'check_same_thread': False})

# mysql 연결 시
# "mysql+pymysql://user_ID:password@host_IP:3306/DB_name"
db_url = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:3306/{DB_NAME}"
engine = create_engine(db_url)



# 데이터베이스와 상호 작용하는 세션을 생성하는 클래스
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy의 선언적 모델링을 위한 기본 클래스
Base = declarative_base()

"""
declarative_base 클래스는 다음과 같은 기능을 제공함
- 데이터베이스 모델 클래스를 정의하는 기능
- 데이터베이스 모델 클래스와 데이터베이스 테이블을 연결하는 기능
- 데이터베이스 모델 클래스를 사용하여 데이터베이스와 상호 작용하는 기능
"""