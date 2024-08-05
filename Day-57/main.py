from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', num=random.randint(1, 100), year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)
