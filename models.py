from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    author = Column(String(50), index=True)
    numofissues = Column(Integer, default=0, nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    bookid = Column(Integer, ForeignKey('books.id'), primary_key=True)
    quantity = Column(Integer)
    book = relationship("Book")

class BookIssue(Base):
    __tablename__ = 'bookissue'
    issueid = Column(Integer, primary_key=True, index=True)
    bookid = Column(Integer, ForeignKey('books.id'))
    studentid = Column(Integer, ForeignKey('students.id'))
    issue_date = Column(DateTime, default=datetime.datetime.utcnow)

    book = relationship("Book")
    student = relationship("Student")
