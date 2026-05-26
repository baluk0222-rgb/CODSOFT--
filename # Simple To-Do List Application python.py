# Simple To-Do List Application

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks in the list.")
    else:
        print("\nYour To-Do List:")
        count = 1
        for task in tasks:
            print(str(count) + ". " + task)
            count += 1

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add task
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        show_tasks()

    # Remove task
    elif choice == "3":
        show_tasks()

        if len(tasks) > 0:
            number = int(input("Enter task number to remove: "))

            if number >= 1 and number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Removed task:", removed)
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Thank you for using To-Do List App!")
        break

    # Wrong input
    else:
        print("Invalid choice. Please try again.")