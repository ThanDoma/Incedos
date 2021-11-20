from flask import Flask, render_template
from sshcon import results


app = Flask(__name__)
menu = [{"name": "Servers", "url": "serverList"},
        {"name": "Users", "url": "userList"}]


print(results)


@app.route('/')
def index():
    return render_template('index.html', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)



