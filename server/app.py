#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    # Print to console
    print(parameter)
    # Return plain text
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    print(f'Counting up to {parameter}')
    # Build numbers starting at 0, separated by newlines
    numbers = ''
    for i in range(parameter):
        numbers += f'{i}\n'
    return numbers

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return f'Invalid operation: {operation}'

    print(f"{num1} {operation} {num2} = {result}")
    # Return just the result as plain text
    return str(result)
