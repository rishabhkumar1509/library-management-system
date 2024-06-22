from pydantic import BaseModel
from datetime import datetime

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author: str  
    numofissues: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    bookid: int
    quantity: int

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    class Config:
        orm_mode = True

class BookIssueBase(BaseModel):
    bookid: int
    studentid: int
    issue_date: datetime

class BookIssueCreate(BookIssueBase):
    pass

class BookIssue(BookIssueBase):
    issueid: int

    class Config:
        orm_mode = True
