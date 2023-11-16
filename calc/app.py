from flask import Flask, request
from operations import *
# http://localhost:5000/add?a=10&b=20

app = Flask(__name__)

math_ops = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route('/math/<ops>')
def opperation(ops):
    a = int(request.args["a"])
    b = int(request.args["b"])
    action = math_ops[ops]
    return str(action(a, b))


@app.route('/add')
def add_route():
    a = request.args["a"]
    b = request.args["b"]
    print(request.args)
    return str(add(int(a), int(b)))


@app.route('/sub')
def sub_route():
    a = request.args["a"]
    b = request.args["b"]
    print(request.args)
    return str(sub(int(a), int(b)))


@app.route('/mult')
def mult_route():
    a = request.args["a"]
    b = request.args["b"]
    print(request.args)
    return str(mult(int(a), int(b)))


@app.route('/div')
def div_route():
    a = request.args["a"]
    b = request.args["b"]
    print(request.args)
    return str(div(int(a), int(b)))
