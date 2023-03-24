from flask import Flask

from app.routers.books import book_router

app = Flask(__name__)
app.register_blueprint(book_router)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
