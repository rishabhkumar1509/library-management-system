from sqlalchemy.orm import Session
import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.bookid == inventory.bookid).first()
    if db_inventory:
        db_inventory.quantity = inventory.quantity
    else:
        db_inventory = models.Inventory(bookid=inventory.bookid, quantity=inventory.quantity)
        db.add(db_inventory)
    db.commit()
    return db_inventory

def issue_book(db: Session, book_issue: schemas.BookIssueCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_issue.bookid).first()
    db_inventory = db.query(models.Inventory).filter(models.Inventory.bookid == book_issue.bookid).first()
    db_student = db.query(models.Student).filter(models.Student.id == book_issue.studentid).first()
    student_issues = db.query(models.BookIssue).filter(models.BookIssue.studentid == book_issue.studentid).count()

    if not db_book or not db_inventory or db_inventory.quantity <= 0 or not db_student or student_issues >= 3:
        raise ValueError("Book cannot be issued")

    db_inventory.quantity -= 1
    db_book_issue = models.BookIssue(bookid=book_issue.bookid, studentid=book_issue.studentid, issue_date=book_issue.issue_date)
    db.add(db_book_issue)
    db.commit()
    db.refresh(db_book_issue)
    return db_book_issue

def return_book(db: Session, issueid: int):
    db_issue = db.query(models.BookIssue).filter(models.BookIssue.issueid == issueid).first()
    if not db_issue:
        raise ValueError("Invalid issue ID")

    db_inventory = db.query(models.Inventory).filter(models.Inventory.bookid == db_issue.bookid).first()
    if db_inventory:
        db_inventory.quantity += 1

    db.delete(db_issue)
    db.commit()
    return db_issue
