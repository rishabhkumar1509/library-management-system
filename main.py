from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import uvicorn

app = FastAPI()
models.Base.metadata.create_all(engine)


class StudentBase(BaseModel):
    id: int
    studentname: str

class BookBase(BaseModel):
    id: int
    bookname: str
    author: str

class InventoryBase(BaseModel):
    bookid: int
    count: int

class BookIssueBase(BaseModel):
    issueid: int
    studentid: int
    bookid: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@app.post('/students/', status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentBase, db: db_dependency):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()

@app.get('/students/{student_id}', status_code=status.HTTP_200_OK)
async def read_student(student_id: int, db: db_dependency):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Student not found')
    return student



#Code for debugging purposes
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)