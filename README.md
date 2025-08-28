# TaskFlow – Flask-Based Task Manager

**TaskFlow** is a **modern web-based task management application** built with **Flask** and **Jinja2 templates**.  
It allows users to **add, edit, delete, and track tasks** efficiently through a clean, responsive, and user-friendly interface.

---

## **Project Overview**

TaskFlow provides a simple yet functional way to organize daily or ongoing tasks.  
The project demonstrates:

- Flask backend routing and logic
- Dynamic HTML rendering with Jinja2 templates
- Form handling for adding and updating tasks
- Responsive and modern frontend design using HTML/CSS

Users can manage their tasks easily while learning how a Python web application works end-to-end.

---

## **Purpose**

The main goals of TaskFlow are:

- To help users **organize and manage tasks** efficiently
- To **learn and demonstrate Flask development** with template rendering
- To showcase **modern, responsive UI design** using HTML and CSS

---

## **Core Features**

1. **Add Tasks**  
   Users can type a task name and click "Add" to include it in the task list.

2. **Edit Tasks**  
   Each task has an **Edit** button. Clicking it opens a form pre-filled with the current task name for easy updates.

3. **Delete Tasks**  
   Remove tasks individually with the **Delete** button.

4. **Mark Done/Pending**  
   Toggle tasks between done and pending status. Completed tasks are visually marked with strikethrough and a different color.

5. **Modern Responsive UI**  
   - Clean card-style layout with shadows and rounded edges  
   - Hover effects on buttons and tasks  
   - Uses **Google Fonts (Inter)** for a contemporary look  
   - Fully responsive on desktop and mobile screens

---

## **How It Works**

- **Backend (Flask)**: Handles all routes for adding, editing, deleting, and toggling tasks. Uses an **in-memory Python list** as temporary storage.  
- **Frontend (Jinja2 + HTML/CSS)**: Dynamically displays tasks and forms. Uses loops and conditionals to render task data.  
- **Form Handling**: Uses `request.form.get()` to capture user input for adding or editing tasks.  
- **Task Status**: Each task stores a `done` boolean to track completion, used for styling in the frontend.

---

## **Installation**

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/taskflow.git
cd taskflow
