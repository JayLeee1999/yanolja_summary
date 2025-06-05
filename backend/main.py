""" 
simple todo
fastAPI를 활용한 DB CRUD
명령 실행 : 
  - uvicorn main:app --reload
  또는
  - python app_start.py
"""
# main.py

from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from database import engine, sessionlocal
from sqlalchemy.orm import Session
import models

# models에 정의한 모든 클래스, 연결한 DB엔진에 테이블로 생성
models.Base.metadata.create_all(bind=engine)

# FastAPI() 객체 생성
app = FastAPI()

# html 템플릿 폴더를 지정하여 jinja템플릿 객체 생성
templates = Jinja2Templates(directory="templates")

# static 폴더(정적파일 폴더)를 app에 연결
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = sessionlocal()
    try:
        # yield 키워드는 FastAPI가 함수의 실행을 일시 중지하고 데이터베이스 세션을 호출자에게 반환하도록 지시
        yield db
    finally:
        # 마지막에 무조건 닫음
        db.close()

@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    # todos = db.query(models.Todo).order_by(models.Todo.id.desc())
    # print(todos.count())
    # if todos.count() == 0:
    #     todos = 0

    return 0
    