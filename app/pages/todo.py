import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json

# Title
st.title("Easy To-Do List")

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Sidebar for adding new tasks
with st.sidebar:
    st.header("Add New Task")
    new_task = st.text_input("Task Description")
    category = st.selectbox("Category", ["Work", "Personal", "Shopping", "Other"])
    due_date = st.date_input("Due Date", min_value=datetime.today())
    priority = st.select_slider("Priority", options=["Low", "Medium", "High"])
    
    if st.button("Add Task"):
        if new_task:
            st.session_state.tasks.append({
                "task": new_task,
                "category": category,
                "due_date": due_date.strftime("%Y-%m-%d"),
                "priority": priority,
                "completed": False
            })
            st.success("Task added successfully!")

# Main area for displaying tasks
st.header("Your Tasks")

# Filter and sort options
col1, col2, col3 = st.columns(3)
with col1:
    filter_category = st.multiselect("Filter by Category", ["All"] + list(set([task["category"] for task in st.session_state.tasks])), default="All")
with col2:
    sort_by = st.selectbox("Sort by", ["Due Date", "Priority", "Category"])
with col3:
    show_completed = st.checkbox("Show Completed Tasks", value=True)

# Apply filters and sorting
filtered_tasks = st.session_state.tasks
if "All" not in filter_category:
    filtered_tasks = [task for task in filtered_tasks if task["category"] in filter_category]
if not show_completed:
    filtered_tasks = [task for task in filtered_tasks if not task["completed"]]

# Sort tasks
if sort_by == "Due Date":
    filtered_tasks.sort(key=lambda x: x["due_date"])
elif sort_by == "Priority":
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    filtered_tasks.sort(key=lambda x: priority_order[x["priority"]])
elif sort_by == "Category":
    filtered_tasks.sort(key=lambda x: x["category"])

# Display tasks
for idx, task in enumerate(filtered_tasks):
    col1, col2, col3, col4, col5 = st.columns([0.05, 0.4, 0.2, 0.2, 0.15])
    completed = col1.checkbox("", value=task["completed"], key=f"check_{idx}")
    task_text = task["task"]
    if completed:
        task_text = f"~~{task_text}~~"
    col2.write(task_text)
    col3.write(f"Due: {task['due_date']}")
    col4.write(f"{task['category']} - {task['priority']}")
    if col5.button("Remove", key=f"remove_{idx}"):
        st.session_state.tasks.remove(task)
        st.experimental_rerun()
    
    # Update task status
    for t in st.session_state.tasks:
        if t == task:
            t["completed"] = completed

# Task statistics
st.header("Task Statistics")
total_tasks = len(st.session_state.tasks)
completed_tasks = len([task for task in st.session_state.tasks if task["completed"]])
st.write(f"Total Tasks: {total_tasks}")
st.write(f"Completed Tasks: {completed_tasks}")
st.write(f"Completion Rate: {completed_tasks/total_tasks*100:.2f}%" if total_tasks > 0 else "No tasks yet")

# Save and load functionality
st.header("Save/Load Tasks")
col1, col2 = st.columns(2)
with col1:
    if st.button("Save Tasks"):
        with open("tasks.json", "w") as f:
            json.dump(st.session_state.tasks, f)
        st.success("Tasks saved successfully!")
with col2:
    if st.button("Load Tasks"):
        try:
            with open("tasks.json", "r") as f:
                st.session_state.tasks = json.load(f)
            st.success("Tasks loaded successfully!")
        except FileNotFoundError:
            st.error("No saved tasks found.")

# Clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.experimental_rerun()