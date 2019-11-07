from flask import *
from datetime import datetime
import Calculator as calculator
app = Flask(__name__)


@app.route('/')
def index():
    return "安安"



if __name__ == '__main__':
    app.run(debug=True)