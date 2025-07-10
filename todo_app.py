import os

# Define the file where tasks will be saved
# Tasks are stored one per line: "description|completed_status" (e.g., "Buy groceries|False")
TASKS_FILE = "tasks.txt"

def load_tasks():
    """
    Loads tasks from the TXT file. Each line is parsed into a dictionary.
    Handles file not found or malformed lines gracefully.
    """
    tasks = []
    if not os.path.exists(TASKS_FILE):
        return tasks # Return empty list if file doesn't exist yet

    try:
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                line = line.strip() # Remove newline characters and whitespace
                if not line: # Skip empty lines
                    continue

                parts = line.split('|', 1) # Split only on the first '|' to allow '|' in description
                if len(parts) == 2:
                    description = parts[0]
                    # Convert the string "True" or "False" to a boolean value
                    completed = parts[1].lower() == 'true'
                    tasks.append({"description": description, "completed": completed})
                else:
                    # Inform about malformed lines but continue loading valid ones
                    print(f"Warning: Skipping malformed task line: '{line}'")
    except Exception as e:
        # Catch any other file reading errors
        print(f"Error loading tasks from {TASKS_FILE}: {e}. Starting with an empty task list.")
        return [] # Return empty list on error to prevent application crash
    return tasks

def save_tasks(tasks):
    """
    Saves the current list of tasks to the TXT file.
    Each task is written on a new line in the "description|completed_status" format.
    """
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            # Format each task as a string and write to file with a newline
            file.write(f"{task['description']}|{task['completed']}\n")

def display_tasks(tasks):
    """
    Displays all tasks in a formatted list.
    Shows a checkmark for completed tasks.
    """
    if not tasks:
        print("\nNo tasks in your list yet!")
        return

    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks):
        # Determine status symbol: '✓' for complete, ' ' for incomplete
        status = "✓" if task["completed"] else " "
        print(f"{i + 1}. [{status}] {task['description']}")
    print("-----------------------\n")

def add_task(tasks):
    """
    Prompts the user for a new task description and adds it to the list.
    New tasks are always added as incomplete.
    """
    description = input("Enter the task description: ").strip()
    if description:
        tasks.append({"description": description, "completed": False})
        save_tasks(tasks) # Save immediately after adding
        print(f"Task '{description}' added.")
    else:
        print("Task description cannot be empty.")

def mark_task_complete(tasks):
    """
    Allows the user to mark an existing task as complete by its number.
    """
    display_tasks(tasks) # Show tasks so user can pick
    if not tasks: # No tasks to mark
        return

    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        # Adjust for 0-based indexing
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks) # Save immediately after updating
            print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """
    Allows the user to delete an existing task by its number.
    """
    display_tasks(tasks) # Show tasks so user can pick
    if not tasks: # No tasks to delete
        return

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        # Adjust for 0-based indexing
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1) # Remove the task
            save_tasks(tasks) # Save immediately after deleting
            print(f"Task '{deleted_task['description']}' deleted.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """
    The main function that runs the To-Do List application loop.
    It loads tasks, presents a menu, and calls appropriate functions based on user choice.
    """
    tasks = load_tasks() # Load tasks when the application starts

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice: ").strip() # Get user input and remove whitespace

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main() # Run the main application function when the script is executed