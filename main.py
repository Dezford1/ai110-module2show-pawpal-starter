from pawpal_system import Owner, Pet, Task, Scheduler

# ------------------------
# Step 1: Create Owner
# ------------------------
owner = Owner("Dezmond", "dezmond@example.com")

# ------------------------
# Step 2: Create Pets
# ------------------------
dog = Pet("Buddy", "Dog", 3)
cat = Pet("Milo", "Cat", 2)

# ------------------------
# Step 3: Add Tasks
# ------------------------
# Dog Tasks
task1 = Task("Morning Walk", "walk", 30, 1, (480, 510))  # 8:00-8:30 AM
task2 = Task("Feed Dog", "feeding", 10, 2, (510, 520))   # 8:30-8:40 AM

# Cat Tasks
task3 = Task("Feed Cat", "feeding", 10, 1, (500, 510))    # 8:20-8:30 AM

dog.add_task(task1)
dog.add_task(task2)
cat.add_task(task3)

owner.add_pet(dog)
owner.add_pet(cat)

# ------------------------
# Step 4: Generate Schedule
# ------------------------
scheduler = Scheduler()
today_plan = scheduler.generate_daily_plan(owner)

# ------------------------
# Step 5: Print Today's Schedule (Readable Format)
# ------------------------
print("=== Today's Pet Care Schedule ===")
for pet, task in today_plan:
    start_time = (
        f"{task.time_window[0]//60:02d}:{task.time_window[0]%60:02d}"
        if task.time_window else "N/A"
    )
    end_time = (
        f"{task.time_window[1]//60:02d}:{task.time_window[1]%60:02d}"
        if task.time_window else "N/A"
    )
    print(
        f"{start_time} - {end_time} | {pet.name} ({pet.species}) -> {task.name} "
        f"[Priority: {task.priority}]"
    )

print("\nPlan Explanation:")
print(scheduler.explain_plan(today_plan))