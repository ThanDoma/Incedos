from flask import Flask, render_template
# from pymongo import MongoClient
# import schedule
from sshcon import *

app = Flask(__name__)
menu = [{"name": "Servers", "url": "serverList"},
        {"name": "Users", "url": "userList"}]

# print(job())

# schedule.every(3).seconds.do(job())

# while(True):
#     schedule.run_pending()
#     time.sleep(1)


@app.route('/')
def main():
    return render_template('main.html', menu=menu, results = job())


if __name__ == '__main__':
    app.run(debug=True)



