FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of todo items
    :param filepath: local filename with path
    :return: list object read from file
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todo_local, filepath=FILEPATH):
    """
    Writes a list to a local file
    :param todo_local: list object containing items to be written
    :param filepath: local filepath
    :return: n/a
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_local)


def add_todo(todo_local):
    """
    opens the todo list, adds an entry on the end, then closes it
    :param todo_local: string to add as a todo
    :return: n/a
    """
    todos = get_todos()
    todos.append(todo_local + '\n')
    write_todos(todos)


def edit_todo(old_todo, new_todo):
    """
    Opens the todo list, finds the index for the existing todo, changes it to the new value,
    then write the file
    :param old_todo: Todo to be edited
    :param new_todo: new version of the todo
    :return: n/a
    """
    todos = get_todos()
    index_no = todos.index(old_todo)
    todos[index_no] = new_todo + '\n'
    write_todos(todos)


def complete_todo(todo_local):
    """
    opens the todo list, deletes the todo from the list, writes the list
    :param todo_local: todo to be completed
    :return:
    """
    todos = get_todos()
    todos.pop(todos.index(todo_local))
    write_todos(todos)


def process_action(action_tuple):
    user_action = "this should not do anything"

    if action_tuple[0] == 'Add':
        todos = get_todos()
        todos.append(action_tuple[1]['todo'] + '\n')
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your commend is not valid. Please enter edit followed by a number.")
        except IndexError:
            print("Please enter a valid number")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            completed = todos.pop(number - 1).strip('\n')

            write_todos(todos)

            print(f"{completed} was removed from the list")
        except IndexError:
            print("Please enter a valid number")

    elif user_action.startswith('exit'):
        print("exit")

    else:
        print("Command not valid.")
