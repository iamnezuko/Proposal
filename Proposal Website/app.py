from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/yes")
def yes():
    with open("response.txt", "a") as f:
        f.write(f"YES at {datetime.now()}\n")
    return render_template("yes.html")

@app.route("/no")
def no():
    with open("response.txt", "a") as f:
        f.write(f"NO at {datetime.now()}\n")
    return render_template("no.html")

if __name__ == "__main__":
    app.run(debug=True)
