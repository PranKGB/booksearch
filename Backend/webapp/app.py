from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/book_search')
def book_search():
    return 'We will help you find the book!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
