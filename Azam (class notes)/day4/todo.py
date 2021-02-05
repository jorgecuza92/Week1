tasks = []

while True:
    name =input('enter name of your task: ')
    priority = input('enter priority: ')

    task = {'name': name, 'priority': priority}

    tasks.append(task)

    choice = input('enter q to quit or any key to continue: ')
    if choice == 'q':
        break

print(tasks)