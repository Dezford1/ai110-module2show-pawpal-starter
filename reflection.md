# PawPal+ Project Reflection

## 1. System Design

1. **Add or Manage Pets**  
   Users can create a profile for each pet, specifying details such as name, species, age, and special care notes. They can also update or remove pet profiles as needed.

2. **Schedule and Manage Tasks**  
   Users can create tasks for each pet, including walks, feeding, medication, grooming, or vet appointments. Each task can have a duration, priority, and optional time constraints. Users can edit or remove tasks as necessary.

3. **View Daily Schedule / Plan**  
   Users can view a daily plan that organizes all tasks based on priority, time constraints, and conflicts. The system can highlight overlapping tasks and explain why certain tasks are scheduled at specific times.

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
  My initial UML design included four main classes: Owner, Pet, Task, and Scheduler.
  The **Owner** class is responsible for representing the user and managing their pets. It stores basic information like name and contact details and allows adding or removing pets.
  The **Pet** class represents each individual pet and is responsible for managing its associated tasks. It stores details such as name, species, and age, and provides methods to add or remove tasks.
  The **Task** class represents a specific pet care activity, such as feeding, walking, or giving medication. It holds information like duration, priority, and optional time constraints, and includes logic for checking conflicts with other tasks.
  The **Scheduler** class is responsible for generating a daily plan. It organizes tasks by priority, detects conflicts, and determines an efficient order for completing tasks.
  Overall, each class has a clear responsibility, which helps keep the system modular and easy to maintain.
  **b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
  After reviewing my class skeleton with Copilot, I identified a few important improvements to make the system more reliable and easier to extend.

First, I updated the **Task model** to better support scheduling and conflict detection. Originally, tasks only had a duration and an optional time window, which made it unclear how to determine actual overlaps. To fix this, I planned to introduce more explicit time handling (such as consistent start/end times or standardized time formats) so conflict detection can be more accurate.
Second, I recognized that the relationship between **Pet and Task** could become unclear when generating a daily plan. When tasks are combined across multiple pets, there was no clear way to track which pet each task belonged to. To address this, I decided that the schedule output should retain pet-task relationships (for example, by returning structured plan entries that include both the pet and the task).
Third, I noted that using strings for **time_window** could cause issues with comparisons and formatting. I plan to improve this by using a more consistent time representation (such as a standardized format or time objects) to avoid parsing errors and simplify scheduling logic.
Finally, I identified smaller improvements, such as defining clearer behavior for removing pets or tasks (especially when duplicates or missing items occur) and specifying a clear return type for the scheduler’s daily plan method. These changes will make the system more predictable and easier to debug.
Overall, these updates strengthen the design by improving time handling, preserving relationships between objects, and clarifying method behavior.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
  The scheduler only checks for exact overlaps in task time windows when detecting conflicts. It does not attempt to shift tasks slightly or optimize overlapping durations. Reasoning: This tradeoff simplifies the logic and ensures that the scheduler is predictable and easy to maintain. For a pet care scenario, exact conflict avoidance is usually sufficient—owners mostly want to know which tasks cannot happen at the same time rather than a perfectly optimized minute-by-minute schedule. This keeps the system reliable and understandable while still helping the owner plan their day.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
