from flask import Flask, render_template
from pymongo import results
from con import find_result


app = Flask(__name__)
menu = [{"name": "Servers", "url": "serverList"},
        {"name": "Users", "url": "userList"}]

results = list(find_result)

@app.route('/')
def index():
    return render_template('index.html', menu=menu, results=results)


if __name__ == '__main__':
    app.run(debug=True)



