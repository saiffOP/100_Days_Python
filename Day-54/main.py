from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "hello world"


@app.route('/bye')
def say_bye():
    return "bye"


if __name__ == "__main__":
    app.run(debug=True)
