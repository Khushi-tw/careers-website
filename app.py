from flask import Flask,render_template
# creating an object of Flask
app = Flask(__name__)
# create a Route
@app.route("/")
def hello_world():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
