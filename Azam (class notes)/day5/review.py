# TODO LIST ASSIGNMENT
tasks = []

def menu():
    print('press 1 to add task')
    print('press 2 to delete tasks')
    print('press 3 to view tasks')
    print('press q to quit or any other key to continue')


def display_all_tasks():
    # DISPLAYS LIST OF ALL TASKS
    print('*********ALL TASKS*********')
    for index in range(0, len(tasks)):
        task = tasks[index]  # assigns dictionary to a tasks array
        print(f"{index + 1} - {task['name']} - {task['priority']} priority")

menu()
# CHOICE

while True:

    choice = input('Enter choice: ')

    if choice == '1':
        name_task = input('enter task you want to add: ')
        priority = input('enter the priority (low, med, high): ')
        task = {'name': name_task, 'priority': priority}
        tasks.append(task)

    elif choice == '2':
        # DISPLAYS LIST OF ALL TASKS
        # for index in range (0, len(tasks)):
        #     task = tasks[index]  # assigns dictionary to a tasks array
        #     print(f"{index + 1} - {task['name']} - {task['priority']} priority")
        display_all_tasks() # replaced above code with function for readability

        delete = input('enter the task number you would like to delete: ')
        # tasks.pop(delete)
        del tasks[delete - 1] # remember we moved the list up 1 for readability but to delete a task think of the index position will be -1

    elif choice == '3':
        # for index in range (0, len(tasks)):
        #     task = tasks[index]  # assigns dictionary to a tasks array
        #     print(f"{index + 1} - {task['name']} - {task['priority']} priority") # index + 1 so that you can view the tasks from starting at '1' not at index 0
        # DISPLAYS LIST OF ALL TASKS
        display_all_tasks() # replaced above code with function for readability

    elif choice == 'q':
        break

print(tasks)


