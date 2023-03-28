import os
import time
from datetime import datetime

from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    magic_code  = Column(String(6),primary_key=True,unique=True)
    title  = Column(String(50))
    author  = Column(String(50))
    teacher  = Column(String(50))
    paragraph1  = Column(Text())
    paragraph2  = Column(Text())
    paragraph3  = Column(Text())
    paragraph4  = Column(Text())
    paragraph5  = Column(Text())
    paragraph6  = Column(Text())
    image1 = Column(String(100))
    image2 = Column(String(100))
    image3 = Column(String(100))
    image4 = Column(String(100))
    image5 = Column(String(100))
    image6 = Column(String(100))


    def __init__(self,book_form: dict):
        self.magic_code = book_form.get("magic_code")
        self.title = book_form.get("title")
        self.author = book_form.get("author")
        self.teacher = book_form.get("teacher")
        self.paragraph1 = book_form.get("paragraph1")
        self.paragraph2 = book_form.get("paragraph2")
        self.paragraph3 = book_form.get("paragraph3")
        self.paragraph4 = book_form.get("paragraph4")
        self.paragraph5 = book_form.get("paragraph5")
        self.paragraph6 = book_form.get("paragraph6")
        self.image1 = self.get_image_filename(book_form.get("photo1"),self.magic_code,"image1")
        self.image2 = self.get_image_filename(book_form.get("photo2"),self.magic_code,"image2")
        self.image3 = self.get_image_filename(book_form.get("photo3"),self.magic_code,"image3")
        self.image4 = self.get_image_filename(book_form.get("photo4"),self.magic_code,"image4")
        self.image5 = self.get_image_filename(book_form.get("photo5"),self.magic_code,"image5")
        self.image6 = self.get_image_filename(book_form.get("photo6"),self.magic_code,"image6")


    def get_image_filename(self,photo,magic_code:str, image_position:str) -> str:
        hour = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        file = photo
        file.filename = f"{image_position}-{magic_code}-{hour}.jpg"
        file.save(os.path.join("app/static/upload", file.filename))
        return "../static/upload/" + file.filename

