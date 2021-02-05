# tasks = []
#
# choice = (input(' press 1 to add task\n press 2 to delete task\n press 3 to view all tasks\n press q to quit: '))
# while True:
#     if choice == '1':
#         name = input('What chore would you like to do?: ')
#         priority = input('low, medium or high priority?: ')
#         task = {'name': name, 'priority': priority}
#         tasks.append(task)
#     elif choice == '2':
#         for key, value in task.items():
#             print(key, value)
#     elif choice == '3':
#         for key, value in task.items():
#             print(key, "-", value)
#     quit = input('enter q to quit or press any key to continue: ')
#     if choice == 'q':
#         break


# CREATE TASK
tasks = []
def add():
    while True:
        title = input('\nenter the title of your task: ')
        priority = input('\nenter the priority (low, medium, high): ')
        task = {'title': title, 'priority': priority}

        tasks.append(task)

        quit = input('\nenter q to quit or press any key to continue: ')
        if quit == 'q':
            break

# VIEW TASK
def view():
    for index in range(0, len(tasks)):
        task = tasks[index]
        print(f"\n{index + 1} - {task['title']} : {task['priority']} priority")

# DELETE TASK
def delete():
    while True:
        delete_task = input('\nwhich task would you like to delete?: ')
        if delete_task == 'q':
            break
        else:
            del tasks[(int(delete_task)) - 1]
            break

#MENU
while True:
    menu = (input('\npress 1 to add task\n'
                   'press 2 to delete task\n'
                    'press 3 to view all tasks\n'
                    'press q to quit: '))
    if menu == '1':
        add()
    elif menu == '2':
        view()
        delete()
    elif menu == '3':
        view()
    elif menu == 'q':
        break
    else:
        print('\nyou have entered an invalid option. Please try again')

    # VIEW ALL TASKS
# for key, value in task.items():
#     order = 0
#     order += 1
#     print(order, key, value)
