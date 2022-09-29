from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", all_users = users)

@app.route("/new")
def new():
    return render_template("create.html")

@app.route("/create",methods=['POST'])
def create():
    User.save(request.form)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)