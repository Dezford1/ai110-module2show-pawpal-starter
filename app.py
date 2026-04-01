import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

# ------------------------
# Persistent Owner in session_state
# ------------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Dezmond", "dezmond@example.com")

# ------------------------
# Persistent Scheduler in session_state
# ------------------------
if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

# For convenience, assign local variables
owner = st.session_state.owner
scheduler = st.session_state.scheduler 

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

# ------------------------
# Quick Demo Inputs (UI only)
# ------------------------
st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# ------------------------
# Add Pet Section (wired to backend)
# ------------------------
st.subheader("Add a Pet")

with st.form("add_pet_form"):
    pet_name_input = st.text_input("Pet Name")
    species_input = st.selectbox("Species", ["dog", "cat", "other"])
    age_input = st.number_input("Age", min_value=0, max_value=30, value=1)
    submitted_pet = st.form_submit_button("Add Pet")
    
    if submitted_pet and pet_name_input:
        new_pet = Pet(pet_name_input, species_input, age_input)
        owner.add_pet(new_pet)
        st.success(f"Added pet '{pet_name_input}'!")

# Display current pets from backend
if owner.pets:
    st.subheader("Current Pets:")
    for pet in owner.pets:
        st.write(f"- {pet.name} ({pet.species}, {pet.age} yrs)")

st.divider()

# ------------------------
# Add Task Section (wired to backend)
# ------------------------
if owner.pets:
    st.subheader("Add a Task")
    pet_options = [pet.name for pet in owner.pets]
    selected_pet_name = st.selectbox("Select Pet", pet_options)
    selected_pet = next(p for p in owner.pets if p.name == selected_pet_name)

    with st.form("add_task_form"):
        task_name_input = st.text_input("Task Name")
        task_type_input = st.selectbox("Type", ["feeding", "walk", "medication", "grooming", "enrichment"])
        duration_input = st.number_input("Duration (minutes)", min_value=1, value=10)
        priority_input = st.number_input("Priority (1=high)", min_value=1, max_value=5, value=1)
        submitted_task = st.form_submit_button("Add Task")

        if submitted_task and task_name_input:
            new_task = Task(task_name_input, task_type_input, duration_input, priority_input)
            selected_pet.add_task(new_task)
            st.success(f"Added task '{task_name_input}' to {selected_pet.name}")

# ------------------------
# Display Current Tasks by Pet
# ------------------------
st.subheader("Current Tasks by Pet")
for pet in owner.pets:
    if pet.tasks:
        st.write(f"**{pet.name}'s Tasks:**")
        for task in pet.tasks:
            status = "✅" if task.completed else "❌"
            st.write(f"{status} {task.name} ({task.task_type}, {task.duration} min, priority {task.priority})")
    else:
        st.write(f"{pet.name} has no tasks yet.")

st.divider()

# ------------------------
# Generate Daily Schedule
# ------------------------
st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    plan = scheduler.generate_daily_plan(owner)
    if plan:
        st.write("### Scheduled Tasks:")
        for pet, task in plan:
            status = "✅" if task.completed else "❌"
            st.write(f"{status} {pet.name}: {task.name} ({task.task_type}, {task.duration} min, priority {task.priority})")
    else:
        st.info("No tasks scheduled for today.")
