from flask import Flask, render_template, jsonify
# from pymongo import MongoClient
from sshcon import *
import numpy as np

app = Flask(__name__)
menu = [{"name": "Servers", "url": "serverList"},
        {"name": "Users", "url": "userList"}]

# print(results)
# print(job)
print(job())

@app.route('/')
def main():
    return render_template('main.html', menu=menu, results=job())


@app.route('/updateContent', methods=["POST"])
def updateContent():
        return jsonify('', render_template('updateContent.html', results=job()))


if __name__ == '__main__':
    app.run(debug=True)



