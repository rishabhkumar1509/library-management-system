from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

@app.post("/inventory/", response_model=schemas.Inventory)
def update_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.update_inventory(db=db, inventory=inventory)

@app.post("/issue/", response_model=schemas.BookIssue)
def issue_book(book_issue: schemas.BookIssueCreate, db: Session = Depends(get_db)):
    try:
        return crud.issue_book(db=db, book_issue=book_issue)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/return/{issueid}", response_model=schemas.BookIssue)
def return_book(issueid: int, db: Session = Depends(get_db)):
    try:
        return crud.return_book(db=db, issueid=issueid)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/popular-books/", response_model=list[schemas.Book])
def popular_books(db: Session = Depends(get_db)):
    return crud.max_issues(db=db)