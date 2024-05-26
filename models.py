from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__= 'students'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    studentname = Column(String(50))

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bookname = Column(String(50), unique=True)
    author = Column(String(50))
    inventory = relationship('Inventory', back_populates='book')

class Inventory(Base):
    __tablename__ = 'inventory'

    bookid = Column(Integer, ForeignKey('books.id'), primary_key=True, index=True)
    count = Column(Integer)
    book = relationship('Book', back_populates='inventory')

class BookIssue(Base):
    __tablename__ = 'bookissues'

    issueid = Column(Integer, primary_key=True, index=True, autoincrement=True)
    studentid = Column(Integer, ForeignKey('students.id'))
    bookid = Column(Integer, ForeignKey('books.id'))

