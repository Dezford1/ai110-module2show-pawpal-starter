from dataclasses import dataclass, field
from typing import List, Tuple, Optional


# ------------------------
# Task Class
# ------------------------
@dataclass
class Task:
    name: str
    task_type: str
    duration: int  # minutes
    priority: int
    time_window: Optional[Tuple[int, int]] = None  # (start_min, end_min)
    completed: bool = False

    def mark_complete(self) -> None:
        #Mark task as completed.
        self.completed = True

    def is_conflict(self, other_task: "Task") -> bool:
        """Check if two tasks conflict based on time windows."""
        if self.time_window is None or other_task.time_window is None:
            return False

        start1, end1 = self.time_window
        start2, end2 = other_task.time_window

        return not (end1 <= start2 or end2 <= start1)


# ------------------------
# Pet Class
# ------------------------
@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
       # add a new task to this pet's task list.
        self.tasks.append(task)

    def remove_task(self, task_name: str) -> None:
        self.tasks = [t for t in self.tasks if t.name != task_name]
        #Remove a task by name from this pet's task list.
    def get_tasks(self) -> List[Task]:
        return self.tasks
    #Return a list of all tasks for this pet


# ------------------------
# Owner Class
# ------------------------
class Owner:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.pets: List[Pet] = []
        #Initialize owner with name and contact information.

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)
        #Add a pet to this owner's list of pets

    def remove_pet(self, pet_name: str) -> None:
        self.pets = [p for p in self.pets if p.name != pet_name]
        #Remove a pet by name from this owner's list of pets.

    def get_all_tasks(self) -> List[Tuple[Pet, Task]]:
        """
        Retrieve all tasks across all pets.
        Returns list of (Pet, Task)
        """
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))
        return all_tasks


# ------------------------
# Scheduler Class
# ------------------------
class Scheduler:
    def get_all_tasks(self, owner: Owner) -> List[Tuple[Pet, Task]]:
        """Retrieve all tasks from owner."""
        return owner.get_all_tasks()

    def sort_tasks(self, tasks: List[Tuple[Pet, Task]]) -> List[Tuple[Pet, Task]]:
        """
        Sort tasks by:
        1. Completion status (incomplete first)
        2. Priority (lower = higher priority)
        """
        return sorted(tasks, key=lambda x: (x[1].completed, x[1].priority))

    def detect_conflicts(self, tasks: List[Tuple[Pet, Task]]) -> List[Tuple[Task, Task]]:
        """Detect conflicts between tasks."""
        conflicts = []
        only_tasks = [t for _, t in tasks]

        for i in range(len(only_tasks)):
            for j in range(i + 1, len(only_tasks)):
                if only_tasks[i].is_conflict(only_tasks[j]):
                    conflicts.append((only_tasks[i], only_tasks[j]))

        return conflicts

    def generate_daily_plan(self, owner: Owner) -> List[Tuple[Pet, Task]]:
        """
        Generate a daily plan:
        - Get all tasks
        - Filter incomplete tasks
        - Sort by priority
        """
        tasks = self.get_all_tasks(owner)

        # Only include incomplete tasks
        tasks = [t for t in tasks if not t[1].completed]

        # Sort tasks
        tasks = self.sort_tasks(tasks)

        return tasks

    def explain_plan(self, plan: List[Tuple[Pet, Task]]) -> str:
        """
        Provide a simple explanation of the plan.
        """
        explanation = "Tasks are ordered by priority and completion status.\n"
        explanation += "Higher priority tasks are scheduled first.\n"

        if not plan:
            explanation += "No tasks to complete today."
            return explanation

        explanation += "\nPlanned Tasks:\n"
        for pet, task in plan:
            explanation += f"- {task.name} for {pet.name} (Priority {task.priority})\n"

        return explanation