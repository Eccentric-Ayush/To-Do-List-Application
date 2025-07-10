# To-Do-List-Application

This is a basic command-line To-Do List application written in Python. It allows users to manage their daily tasks by adding, viewing, marking as complete, and deleting tasks. All tasks are saved to a plain text file (tasks.txt) for persistence across sessions.

## Features
Add Tasks: Quickly add new tasks to your list.

View Tasks: See all your tasks with their current completion status.

Mark Tasks Complete: Mark tasks as done.

Delete Tasks: Remove tasks from your list.

Persistence: Tasks are automatically saved to tasks.txt and loaded when the application starts, so you don't lose your data.

## How to Run
Save the Code:
Save the provided Python code into a file named todo_app.py (or any other .py extension).

Open a Terminal/Command Prompt:
Navigate to the directory where you saved todo_app.py using your terminal or command prompt.

Run the Application:
Execute the script using Python:

python todo_app.py

## How to Use
Once the application is running, you will see a menu with several options:

--- To-Do List Menu ---
1. View tasks
2. Add task
3. Mark task complete
4. Delete task
5. Exit
Enter your choice:

Enter the number corresponding to the action you want to perform and press Enter:

1. View tasks: Displays all tasks currently in your list, showing a ✓ next to completed tasks.

2. Add task: Prompts you to enter the description for a new task.

3. Mark task complete: Shows your current tasks and asks for the number of the task you wish to mark as complete.

4. Delete task: Shows your current tasks and asks for the number of the task you wish to delete.

5. Exit: Closes the application. Your tasks will be saved automatically.

## Example Usage:
Run the app:

python todo_app.py

Add a task:

Enter your choice: 2
Enter the task description: Buy groceries
Task 'Buy groceries' added.

Add another task:

Enter your choice: 2
Enter the task description: Finish report
Task 'Finish report' added.

View tasks:

Enter your choice: 1

--- Your To-Do List ---
1. [ ] Buy groceries
2. [ ] Finish report
-----------------------

Mark a task complete:

Enter your choice: 3

--- Your To-Do List ---
1. [ ] Buy groceries
2. [ ] Finish report
-----------------------

Enter the number of the task to mark as complete: 1
Task 1 marked as complete.

View tasks again:

Enter your choice: 1

--- Your To-Do List ---
1. [✓] Buy groceries
2. [ ] Finish report
-----------------------

Exit the application:

Enter your choice: 5
Exiting To-Do List. Goodbye!

## File Structure
The application will create a file named tasks.txt in the same directory where todo_app.py is located. This file stores your tasks, with each task on a new line in the format description|completed_status (e.g., Buy groceries|True). You generally won't need to interact with this file directly.