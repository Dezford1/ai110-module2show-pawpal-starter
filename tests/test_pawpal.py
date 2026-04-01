import pytest
from pawpal_system import Task, Pet

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