from flask import Flask, render_template


# 2. Create an app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/rawdata")
def rawdata():
    return render_template("rawdata.html")













if __name__ == "__main__":
    app.run(debug=True)