import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form.get("title")
    todos.append({"title": todo, "done": False})
    return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))