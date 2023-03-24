from flask import Blueprint, redirect, render_template, request

from app.service.book import BookService

book_router = Blueprint('book_router',
                        __name__,
                        template_folder='../templates',
                        static_folder='../static',
                        url_prefix='/book_router')


@book_router.route('/', methods=['GET'])
def list_books():
    books = BookService.find_all()
    return render_template("home.html", books=books)


@book_router.route('/create', methods=["GET", 'POST'])
def create_book():
    if request.method == 'GET':
        return render_template("cad_book.html")
    if request.method == 'POST':
        magic_code = BookService.generated_magic_code()
        BookService.create(magic_code, request.form.to_dict(), request.files.to_dict())
        return redirect('/book_router/')


@book_router.route('/find/<string:magic_code>')
def find_by_magic_code(magic_code):
    book = BookService.find_by_magic_code(magic_code)
    return render_template("book.html", book=book)
