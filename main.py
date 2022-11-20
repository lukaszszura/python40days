from typing import List

while True:
    user_action = input("Type add, show , delete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            output = f"{index + 1}.{item}"
            print(output)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)

        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'delete' in user_action:
        number = int(user_action[7:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        to_do_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {to_do_remove} was removed from the Todo list."
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("You have enter wrong command")

print("See you next time")
