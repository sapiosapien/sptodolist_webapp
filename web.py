import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state["new_todo"] + "\n"
    todos.append(local_todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("Sarah's Awesome To-Do App")
st.subheader("Welcome to Efficiency")
st.write("This app allows you to add, edit, and delete to-dos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter your todo...",
              on_change=add_todo, key="new_todo")
