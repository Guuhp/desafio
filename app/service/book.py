import random
import string

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.schema.book import Base, Book

engine = create_engine("postgresql://postgres:password@db:5432/mydatabase",echo=True)
session = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(bind=engine)

class BookService:

    @staticmethod
    def find_all() -> list:
        return session.query(Book).all()

    @staticmethod
    def create(magic_code:str,form: dict, files: dict) -> None:
        form_data = {}
        form_data.update({"magic_code":magic_code})
        form_data.update(form)
        form_data.update(files)
        book = Book(book_form=form_data)
        session.add(book)

        session.commit()

    @staticmethod
    def generated_magic_code() -> str:
        while True:
            magic_code = ''.join(
                random.choice(string.ascii_uppercase) for i in range(6))
            book = session.query(Book).filter_by(magic_code=magic_code).first()
            if book is None:
                return magic_code

    @staticmethod
    def find_by_magic_code(magic_code: str) -> str:
        global db
        return session.query(Book).filter_by(magic_code=magic_code).first()
