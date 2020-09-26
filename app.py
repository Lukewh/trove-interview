from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/gender_analysis')
def get_gender_analysis():
    data = [
        ['Engineering', 100, 90, 110, 60, 96, 104, 120],
        ['Android', 120, 95, 130, 90, 113, 124, 140],
        ['Sales', 130, 105, 140, 100, 117, 133, 139],
        ['Accounting', 90, 85, 95, 85, 88, 92, 95],
        ['Product Marketing', 70, 74, 63, 67, 69, 70, 72],
        ['Strategy', 30, 39, 22, 21, 28, 34, 40],
        ['Finance', 80, 77, 83, 70, 77, 85, 90],
        ['Web', 100, 90, 110, 85, 95, 102, 110]
      ]

    return jsonify(data)


if __name__ == "__main__":
    app.run()

