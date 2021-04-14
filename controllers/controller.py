from app import app
from flask import render_template
from modules.calculator import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add/<x>/<y>')
def add_nums(x,y):
    answer = add(int(x), int(y))
    return render_template('answer.html', answer = answer)

@app.route('/sub/<x>/<y>')
def sub_nums(x,y):
    answer = sub(int(x), int(y))
    return render_template('answer.html', answer = answer)

@app.route('/divide/<x>/<y>')
def divide_nums(x,y):
    answer = divide(int(x), int(y))
    return render_template('answer.html', answer = answer)

@app.route('/multiply/<x>/<y>')
def multiply_nums(x,y):
    answer = multiply(int(x), int(y))
    return render_template('answer.html', answer = answer)