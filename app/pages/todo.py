import streamlit as st
import pandas as pd

# Title
st.title("EASY To-Do List")

# Input for new to-do item
new_task = st.text_input("Add a new task")

# Initial list of tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Add new task to the list
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "completed": False})
        new_task = ""

# Display tasks
st.subheader("Your Tasks")
for p, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([0.05, 0.8, 0.15])
    completed = col1.checkbox("", value=task["completed"], key=p)
    if completed:
        st.session_state.tasks[p]["completed"] = completed
    task_text = task["task"]
    if task["completed"]:
        task_text = f"~~{task_text}~~"
    col2.write(task_text)
    if col3.button("Remove", key=f"remove_{p}"):
        st.session_state.tasks.pop(p)
        st.experimental_rerun()

# Clear completed tasks
if st.button("Clear Completed Tasks"):
    st.session_state.tasks = [task for task in st.session_state.tasks if not task["completed"]]
    st.experimental_rerun()


