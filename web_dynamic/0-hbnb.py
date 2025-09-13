from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_0():
    return "Hello flask"

@app.route("/hbnb")
def hello_1():
    return "Hello flask"

@app.route("/c/<text>")
def hello_2():
    return "Hello flask"

@app.route("/python/<text>")
def hello_3():
    return "Hello Python"

@app.route("/number/<n>")
def hello_4():
    n = 3
    if (type(n) == int):
        return f"<h1>{n}</h1>"

@app.route("/number_template/n")
def hello_5():
    n = 3
    if (type(n) == int):
        return f"<h1>{n}</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, strict_slashes=False);
