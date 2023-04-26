import streamlit as st
import functions


def add_todo():
    functions.add_todo(st.session_state["new_todo"])


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is yet another todo app")
st.write("Because there currently aren't enough")

# todo_key = 0

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="Enter a new Todo:", placeholder="new todo goes here...",
              on_change=add_todo, key='new_todo')

# st.session_state
