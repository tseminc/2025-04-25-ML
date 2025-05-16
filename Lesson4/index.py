from flask import Flask

# To execute this service, use :  flask --app index run
#To use debug mode, use :  flask --app index run --debug
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html.jinja2")

@app.route("/user")
def Hello():
    return "<H1>Hello, World!</H1><br><H2>This is my second page</H2>"

@app.route("/product")
def hello3():
    return "<H1>Hello, World!</H1><br><H2>This is my third page</H2>"

