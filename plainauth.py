from flask import Flask
app = Flask(__name__)

@app.route('/<password>')
def index(password):
    with open("password_list.txt", "r") as fsock:
        passwords = fsock.read().splitlines()
    return str(password in passwords)

if __name__ == '__main__':
    app.debug = True
    app.run()
