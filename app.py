from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task storage
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_name = request.form.get("task")
        if task_name:
            tasks.append({"name": task_name, "done": False})
        return redirect(url_for("index"))
    return render_template("index.html", tasks=tasks)

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    if task_id < 0 or task_id >= len(tasks):
        return redirect(url_for("index"))
    if request.method == "POST":
        updated_task = request.form.get("task")
        if updated_task:
            tasks[task_id]["name"] = updated_task
        return redirect(url_for("index"))
    return render_template("edit.html", task=tasks[task_id], task_id=task_id)

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = not tasks[task_id]["done"]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True , port=8000)
