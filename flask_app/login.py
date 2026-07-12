from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy user credentials
USERNAME = "admin"
PASSWORD = "12345"

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == USERNAME and password == PASSWORD:
        return render_template("success.html", username=username)
    else:
        error = "Invalid username or password"
        return render_template("login.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)