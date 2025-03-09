from flask import Flask
# creating an object of Flask
app = Flask(__name__)
# create a Route
@app.route("/")
def hello_world():
    return "Hello Khushi!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
