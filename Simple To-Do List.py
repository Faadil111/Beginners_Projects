#Definition of functions for iterating our list
def add_task(task_list,task_description):
    task_list.append(task_description)

def delete_task(task_list, task_index):
    try:
        del task_list[task_index]

    except IndexError:
        print("Error: Task not found")

def view_task(task_list):
    if not task_list:
        print("No tasks found")
    else:
        for i, task in enumerate(task_list, start = 1):
            print(f"{i}. {task}")

#The function that implements our To-Do List
def to_dos():
    tasks = []
    while True:
        print("\n To-Do List: ")
        view_task(tasks)
        choice = input("\nOptions: add, delete, view, quit\n  ").lower()

# The conditions that determine what happens to our list according to the options that we pick
        if choice == "add":
            task_description = input("Enter Task: ")
            add_task(tasks, task_description)

        elif choice == "delete":
            try:
                task_index_deletion = int(input("Enter Task Index To Delete: "))
                delete_task(tasks, task_index_deletion)
            except ValueError:
                print("Error: Invalid Input")

        elif choice == "view":
            view_task(tasks)

        elif choice == "quit":
            break

        else:
            print("Error: Invalid Choice")

#The Opening for our Simple To-Do List
Organisation = input("Want to open up your To-Do list? (yes/no): ").lower()
if Organisation == "yes":
    to_dos()
else:
    print("HMMMMMM :)")





