from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome, My name is Ram Kumar, This is Udacity final project Green Deployment"

app.run(host="0.0.0.0", port=8080, debug=True)
