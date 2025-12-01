import os
import tkinter as tk
from tkinter import messagebox, simpledialog

TASKS_FILE = "tasks.txt"
def load_tasks():
    tasks = []
    if not os.path.exists(TASKS_FILE):
        return tasks
    try:
        with open(TASKS_FILE, "r") as f:
            for line in f:
                line = line.rstrip("\n\r")
                if not line:
                    continue
                parts = line.split("|", 1)  # only split on first |
                if len(parts) == 2:
                    desc = parts[0]
                    completed = parts[1].strip().lower() == "true"
                    tasks.append({"description": desc, "completed": completed})
    except Exception as e:
        print("Failed to read tasks:", e)
    return tasks


def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as f:
            for t in tasks:
                desc = t["description"].replace("\n", " ")
                f.write(f"{desc}|{t['completed']}\n")
    except Exception as e:
        messagebox.showerror("Save error", f"Could not save tasks: {e}")

# ------------------ GUI ------------------

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("560x420")
        self.resizable(False, False)

        self.tasks = []

        self._build_widgets()
        self.load_and_refresh()

    def _build_widgets(self):
        top_frame = tk.Frame(self, pady=8, padx=8)
        top_frame.pack(fill="x")

        self.entry = tk.Entry(top_frame)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self.entry.bind("<Return>", lambda e: self.on_add())

        add_btn = tk.Button(top_frame, text="Add Task", command=self.on_add)
        add_btn.pack(side="left")

        list_frame = tk.Frame(self, padx=8)
        list_frame.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(list_frame, height=16, activestyle="none", font=("Segoe UI", 10))
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind('<Double-Button-1>', self.on_toggle_complete)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="left", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        btn_frame = tk.Frame(self, pady=6, padx=8)
        btn_frame.pack(fill="x")

        tk.Button(btn_frame, text="Mark Complete", command=self.on_mark_complete).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Mark Incomplete", command=self.on_mark_incomplete).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Edit", command=self.on_edit_task).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Delete", command=self.on_delete).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Refresh", command=self.load_and_refresh).pack(side="left", padx=4)

        self.status_var = tk.StringVar()
        status = tk.Label(self, textvariable=self.status_var, anchor="w", relief="sunken")
        status.pack(side="bottom", fill="x")

    # ------------------ Data / Display helpers ------------------
    def load_and_refresh(self):
        """Load tasks from disk and update the listbox."""
        self.tasks = load_tasks()
        self.refresh_display()
        self.status_var.set(f"{len(self.tasks)} tasks loaded from {TASKS_FILE}.")

    def refresh_display(self):
        """Redraw the listbox to reflect self.tasks."""
        self.listbox.delete(0, tk.END)
        for i, t in enumerate(self.tasks, start=1):
            mark = "✓" if t["completed"] else " "
            self.listbox.insert(tk.END, f"{i:>3}. [{mark}] {t['description']}")

    def get_selected_index(self):
        sel = self.listbox.curselection()
        return sel[0] if sel else None

    # ------------------ Actions ------------------
    def on_add(self):
        desc = self.entry.get().strip()
        if not desc:
            messagebox.showwarning("Empty", "Please type a task before adding.")
            return
        self.tasks.append({"description": desc, "completed": False})
        save_tasks(self.tasks)
        self.entry.delete(0, tk.END)
        self.refresh_display()
        self.status_var.set(f"Added: {desc}")

    def on_mark_complete(self):
        idx = self.get_selected_index()
        if idx is None:
            messagebox.showinfo("Select", "Select a task first.")
            return
        self.tasks[idx]["completed"] = True
        save_tasks(self.tasks)
        self.refresh_display()
        self.status_var.set(f"Task {idx+1} marked complete.")

    def on_mark_incomplete(self):
        idx = self.get_selected_index()
        if idx is None:
            messagebox.showinfo("Select", "Select a task first.")
            return
        self.tasks[idx]["completed"] = False
        save_tasks(self.tasks)
        self.refresh_display()
        self.status_var.set(f"Task {idx+1} marked incomplete.")

    def on_delete(self):
        idx = self.get_selected_index()
        if idx is None:
            messagebox.showinfo("Select", "Select a task to delete.")
            return
        desc = self.tasks[idx]["description"]
        if not messagebox.askyesno("Confirm", f"Delete: {desc} ?"):
            return
        self.tasks.pop(idx)
        save_tasks(self.tasks)
        self.refresh_display()
        self.status_var.set(f"Deleted: {desc}")

    def on_edit_task(self):
        idx = self.get_selected_index()
        if idx is None:
            messagebox.showinfo("Select", "Select a task to edit.")
            return
        old = self.tasks[idx]["description"]
        new = simpledialog.askstring("Edit", "Edit description:", initialvalue=old)
        if new is None:
            return
        new = new.strip()
        if not new:
            messagebox.showwarning("Empty", "Description cannot be empty.")
            return
        self.tasks[idx]["description"] = new
        save_tasks(self.tasks)
        self.refresh_display()
        self.status_var.set(f"Edited task {idx+1}.")

    def on_toggle_complete(self, event=None):
        idx = self.get_selected_index()
        if idx is None:
            return
        self.tasks[idx]["completed"] = not self.tasks[idx]["completed"]
        save_tasks(self.tasks)
        self.refresh_display()
        self.status_var.set(f"Toggled task {idx+1}.")

# ------------------ Run ------------------

def main():
    if not os.path.exists(TASKS_FILE):
        open(TASKS_FILE, "a").close()

    app = TodoApp()
    app.mainloop()


if __name__ == "__main__":
    main()