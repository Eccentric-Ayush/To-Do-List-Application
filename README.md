# **To-Do List Application (GUI Version)**

A simple and user-friendly **Graphical To-Do List Application** built using **Python (Tkinter)**.
This app allows you to add, edit, mark complete/incomplete, delete, and refresh tasks.
All tasks are saved automatically to a `tasks.txt` file, making them persist across sessions.

---

## **Features**

### ✔ Add Tasks

Enter a task in the input box and click **Add Task** or press **Enter**.

### ✔ View Tasks

Tasks appear in a scrollable list with a checkmark (✓) for completed tasks.

### ✔ Mark as Complete / Incomplete

Select a task and click:

* **Mark Complete**
* **Mark Incomplete**

You can also **double-click a task** to toggle completion.

### ✔ Edit Task

Select a task → click **Edit** → update the text.

### ✔ Delete Task

Select a task → click **Delete**
A confirmation message appears before removing the task.

### ✔ Refresh Tasks

Loads tasks again from `tasks.txt` and refreshes the list.

### ✔ Persistent Storage

Tasks are saved in `tasks.txt` using the format:

```
description|True/False
```

---

## 📂 **File Structure**

```
project_folder/
│── todo_app.py          # Main application file
│── tasks.txt            # Automatically created storage file
```

* The file `tasks.txt` is created automatically if it does not already exist.
* Each line contains one task with its completion state.

---

## ▶️ **How to Run the Application**

### **1. Save the code**

Save the script as:

```
todo_app.py
```

### **2. Install Python (if not installed)**

Python 3.x is required.

### **3. Run the Application**

Open terminal / CMD inside the folder and run:

```
python todo_app.py
```

The graphical To-Do List window will appear.

---

## 🖥️ **How to Use the Application**

### **1. Add a Task**

* Type a task in the entry box.
* Press **Enter** or click **Add Task**.

### **2. Select a Task**

Click once on a task from the list.

### **3. Mark Complete / Incomplete**

Click:

* **Mark Complete**
* **Mark Incomplete**

Or double-click the task to toggle.

### **4. Edit a Task**

* Select a task
* Click **Edit**
* Modify the description

### **5. Delete a Task**

* Select a task
* Click **Delete**
* Confirm deletion

### **6. Refresh**

Reload tasks from the file using **Refresh**.

---

## 🛠️ **Behind the Scenes — How it Works**

### **Loading Tasks**

The function `load_tasks()` reads tasks from `tasks.txt` and populates them into a list of dictionaries like:

```python
{"description": "Buy milk", "completed": False}
```

### **Saving Tasks**

Every time you:

* Add
* Edit
* Mark complete/incomplete
* Delete

…the file is updated with the new state via `save_tasks()`.

### **GUI**

Built using **Tkinter** widgets:

* `Entry` for input
* `Listbox` for tasks
* Buttons for actions
* Scrollbar
* Status bar showing messages like *"Added: Task"*

---

## 📌 Example of How Tasks Appear in the App

```
  1. [✓] Buy groceries
  2. [ ] Finish project report
  3. [ ] Pay electricity bill
```

---

## ✔ Requirements

* Python 3.x
* Tkinter (comes pre-installed with Python on Windows/macOS/Linux)

---

## Screenshots

