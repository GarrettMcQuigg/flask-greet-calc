from flask import Flask, request
from operations import add, sub, mult, div

@app.route('/add')
def addition():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return result

@app.route('/sub')
def subtract():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return result

@app.route('/mult')
def multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return result

@app.route('/div')
def divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return result
