from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Data storage file
DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Initialize tasks
tasks = load_tasks()

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/dashboard")
def dashboard():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['done'])
    pending_tasks = total_tasks - completed_tasks
    
    # Get tasks by category
    tasks_by_category = {}
    for task in tasks:
        category = task.get('category', 'Uncategorized')
        if category not in tasks_by_category:
            tasks_by_category[category] = 0
        tasks_by_category[category] += 1
    
    return render_template("dashboard.html", 
                          total_tasks=total_tasks,
                          completed_tasks=completed_tasks,
                          pending_tasks=pending_tasks,
                          tasks_by_category=tasks_by_category)

@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task")
    task_category = request.form.get("category", "Uncategorized")
    task_priority = request.form.get("priority", "medium")
    
    if task_name:
        new_task = {
            "id": len(tasks) + 1,
            "name": task_name,
            "category": task_category,
            "priority": task_priority,
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        tasks.append(new_task)
        save_tasks(tasks)
    
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return redirect(url_for("index"))
    
    if request.method == "POST":
        updated_name = request.form.get("task")
        updated_category = request.form.get("category", "Uncategorized")
        updated_priority = request.form.get("priority", "medium")
        
        if updated_name:
            task['name'] = updated_name
            task['category'] = updated_category
            task['priority'] = updated_priority
            save_tasks(tasks)
        
        return redirect(url_for("index"))
    
    return render_template("edit.html", task=task)

@app.route("/delete/<int:task_id>")
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task:
        task['done'] = not task['done']
        save_tasks(tasks)
    
    return redirect(url_for("index"))

@app.route("/api/tasks")
def api_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True, port=8000)