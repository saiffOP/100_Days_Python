from flask import Flask
import random
random_number = random.randint(0, 9)
app = Flask(__name__)


@app.route('/')
def guess_a_number():
    return "<h1><b>Guess a Number between 0 and 9<b/><h1/>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:number>')
def check_number(number):
    if number == random_number:
        return "<h1 style='color:green'><b>You found me!<b/><h1/>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif random_number < number <= 9:
        return "<h1 style='color:purple'><b>Too high, try again!<b/><h1/>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif 0 <= number < random_number:
        return "<h1 style='color:red'><b>Too low, try again!<b/><h1/>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color:red'><b>Invalid Choice!<b/><h1/>" \
               "<img src='https://media.tenor.com/QG8vtwUEbaAAAAAM/roujin-z-anime.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
