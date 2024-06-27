# To-Do List Application

## Description
This is a simple command-line To-Do List application written in Python. It allows users to add, view, and delete tasks using an SQLite database for storage. The application provides an easy way to manage tasks directly from the terminal.

## Features
- **Add Task:** Add a new task to the to-do list.
- **View Tasks:** View all the tasks in the to-do list.
- **Delete Task:** Delete a task from the to-do list by specifying its ID.
- **Exit:** Exit the application.

## Prerequisites
- Python 3.x
- SQLite3

## Setup
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
## Usage
1. **Run the application:**
   ```bash
   python todo.py
   ```

2. **Follow the on-screen prompts to add, view, or delete tasks:**

   - To **add a task**, select option 1 and enter the task description.
   - To **view tasks**, select option 2 to see a list of all tasks.
   - To **delete a task**, select option 3, then enter the task number you wish to delete.
   - To **exit the application**, select option 4.

## Code Explanation
The main components of the application are:

1. **Database Connection:**
   ```python
   conn = sqlite3.connect("todo.db")
   cur = conn.cursor()
   ```

2. **Adding a Task:**
   ```python
   def add_task():
       task = input("Enter new task to be added:\n")
       cur.execute("INSERT INTO tasks (name) VALUES (?)", (task,))
       conn.commit()
   ```

3. **Viewing Tasks:**
   ```python
   def view_task():
       cur.execute("SELECT * FROM tasks")
       for task in cur:
           print(task)
   ```

4. **Deleting a Task:**
   ```python
   def del_task():
       choice = int(input("Enter the task number to be deleted: "))
       cur.execute("DELETE FROM tasks WHERE id = ?", (choice,))
       conn.commit()
   ```

5. **Main Menu:**
   ```python
   def main():
       while True:
           print("1.) ADD TASK")
           print("2.) VIEW TASK")
           print("3.) DELETE TASK")
           print("4.) EXIT")
           op = int(input())
           if op == 1:
               add_task()
           elif op == 2:
               view_task()
           elif op == 3:
               del_task()
           elif op == 4:
               cur.close()
               conn.close()
               break
   main()
   ```

## Acknowledgements
This application was developed as a final project for CS50x from Harvard.

Feel free to customize and expand this application as needed. Contributions are welcome!
