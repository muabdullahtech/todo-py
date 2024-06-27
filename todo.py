# Import necessary libraries
import os
import sqlite3

# Connect to the todo.db database
conn = sqlite3.connect("todo.db")
cur = conn.cursor()


# Function to add a new task
def add_task():
    # Clear the screen
    os.system("clear")

    print("<=========================TO-DO_LIST_APP=========================>")
    print()

    # Prompt user for task
    task = input("Enter new task to be added:\n")

    # Insert task into database
    cur.execute("INSERT INTO tasks (name) VALUES (?)", (task,))
    conn.commit()

    # Print confirmation message
    print("Task Added")
    print("")


# Function to view all tasks
def view_task():
    # Clear the screen
    os.system("clear")

    print("<=========================TO-DO_LIST_APP=========================>")
    print()

    # Fetch all tasks from database
    cur.execute("SELECT * FROM tasks")

    # Print header
    print("List of Tasks: \n")

    # Loop through each task and print details
    for task in cur:
        print(task)

    # Print empty lines for spacing
    print()
    print()


# Function to delete a task
def del_task():
    print("<=========================TO-DO_LIST_APP=========================>")
    print()
    # Clear the screen
    os.system("clear")

    # Call view_task to display tasks before deletion
    view_task()

    # Prompt user for task number to delete
    choice = int(input("Enter the task number to be deleted: "))

    # Delete task from database using ID
    cur.execute("DELETE FROM tasks WHERE id = ?", (choice,))
    conn.commit()

    # Print confirmation message
    print("Task Deleted!")
    print()
    print()


# Main program loop
def main():
     # Display menu options
    print("<=========================TO-DO_LIST_APP=========================>")
    print()
    while True:
        print("1.) ADD TASK")
        print("2.) VIEW TASK")
        print("3.) DELETE TASK")
        print("4.) EXIT")

        # Get user choice
        op = int(input())

        # Call corresponding function based on choice
        if op == 1:
            add_task()
        elif op == 2:
            view_task()
        elif op == 3:
            del_task()
        elif op == 4:
            print("EXITING!!!")
            cur.close()
            conn.close()
            break

        # Exit the loop on option 4


# Call the main function to start the program
main()
