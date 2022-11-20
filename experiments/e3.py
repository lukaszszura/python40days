todos = []
while True:
    user_action = input("Type add, show , delete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add' :
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' :
            for index, item in enumerate(todos):
                output = f"{index + 1}.{item}"
                print(output)
        case 'edit' :
            number = int(input("Number of to do to edit: "))
            number = number -1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'delete' :
            number = int(input("Number of to do to delete: "))
            todos.pop(number - 1)

        case 'exit' :
            break
        case _:
            print("You have enter wrong command")
print("See you next time")

