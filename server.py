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

@app.route("/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit.html", user=User.read_one(data))

@app.route("/show/<int:id>")
def show(id):
    data = {
        "id":id
    }
    return render_template("read_one.html", user=User.read_one(data))

@app.route("/update",methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        'id':id
    }
    User.destroy(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)