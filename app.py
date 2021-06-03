from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


data = [[1, 2, 3], [4, 5, 6]]


@app.route('/table')
def make_table():
    return render_template("table.html", result_list=data)


if __name__ == "__main__":
    app.run(debug=True)
