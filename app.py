from flask import Flask, render_template, jsonify
# from pymongo import MongoClient
from sshcon import *

app = Flask(__name__)
menu = [{"name": "Servers", "url": "serverList"},
        {"name": "Users", "url": "userList"}]

# print(job())
results = job()


# @app.route('/updateContent', methods=["POST"])
# def updateContent():
#     return jsonify('', render_template('updateContent.html', results=results))



@app.route('/')
def main():
    return render_template('main.html', menu=menu, results=results)


if __name__ == '__main__':
    app.run(debug=True)



