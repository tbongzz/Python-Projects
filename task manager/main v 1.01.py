#numeric bullet point update
import tkinter as tk
from tkinter import messagebox


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        self.task_counter = 1  # Counter for bullet points

        # Create and configure the task listbox
        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.pack(pady=10)

        # Create and configure the entry widget for new tasks
        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        # Create and configure the buttons
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Load any saved tasks from a file
        self.load_tasks()

    def add_task(self):
        """
        Add a new task to the task listbox.
        """
        task = self.task_entry.get()
        if task:
            task_with_bullet = f"{self.task_counter}. {task}"
            self.tasks.append(task_with_bullet)
            self.task_listbox.insert(tk.END, task_with_bullet)
            self.task_entry.delete(0, tk.END)
            self.task_counter += 1
            self.save_tasks()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def delete_task(self):
        """
        Delete the selected task from the task listbox.
        """
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")

    def save_tasks(self):
        """
        Save the tasks to a file.
        """
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        """
        Load tasks from a file and display them in the task listbox.
        """
        try:
            with open("tasks.txt", "r") as file:
                for task in file.readlines():
                    self.tasks.append(task.strip())
                    self.task_listbox.insert(tk.END, task.strip())
                    self.task_counter += 1
        except FileNotFoundError:
            return


# Create the main window
root = tk.Tk()

# Create an instance of the TodoListApp
app = TodoListApp(root)

# Run the application
root.mainloop()
