import pytest
from pawpal_system import Owner, Pet, Scheduler, Task

# ------------------------
# Test 1: Task Completion
# ------------------------
def test_task_completion():
    task = Task("Feed Dog", "feeding", 10, 1)
    assert not task.completed  # initially incomplete
    task.mark_complete()
    assert task.completed      # should be marked complete


# ------------------------
# Test 2: Task Addition to Pet
# ------------------------
def test_task_addition():
    pet = Pet("Buddy", "Dog", 3)
    initial_count = len(pet.tasks)
    
    task = Task("Morning Walk", "walk", 30, 1)
    pet.add_task(task)
    
    assert len(pet.tasks) == initial_count + 1
    assert pet.tasks[0].name == "Morning Walk"


def test_daily_recurring_task_spawns_next_instance():
    owner = Owner("Dezmond", "dezmond@example.com")
    pet = Pet("Buddy", "Dog", 3)
    owner.add_pet(pet)

    task = Task("Feed Dog", "feeding", 10, 1, recurring=True, recurrence="daily")
    pet.add_task(task)

    scheduler = Scheduler()
    next_task = scheduler.mark_task_complete(owner, "Buddy", "Feed Dog", completed_day="Monday")

    assert task.completed is True
    assert next_task is not None
    assert next_task.name == "Feed Dog"
    assert next_task.completed is False
    assert next_task.next_occurrence_day == "Tuesday"
    assert len(pet.tasks) == 2


def test_weekly_recurring_task_spawns_next_instance():
    owner = Owner("Dezmond", "dezmond@example.com")
    pet = Pet("Milo", "Cat", 2)
    owner.add_pet(pet)

    task = Task(
        "Feed Cat",
        "feeding",
        10,
        1,
        recurring=True,
        recurrence="weekly",
        recurrence_day="Friday",
    )
    pet.add_task(task)

    scheduler = Scheduler()
    next_task = scheduler.mark_task_complete(owner, "Milo", "Feed Cat", completed_day="Friday")

    assert task.completed is True
    assert next_task is not None
    assert next_task.name == "Feed Cat"
    assert next_task.completed is False
    assert next_task.next_occurrence_day == "Friday"
    assert len(pet.tasks) == 2