# Task Manager CLI

This is a simple command-line interface (CLI) application for managing tasks. The `TaskManager` program allows users to add, view, update, and delete tasks. Each task has a title, description, and status (either "pending" or "completed").

## Features

- **Add a Task**: Create a new task with a title and description.
- **View Tasks**: Display all tasks with their titles, descriptions, and statuses.
- **Update a Task**: Modify the title or description of an existing task.
- **Delete a Task**: Remove a task by its title.
- **Mark Task as Completed**: Automatically handled when a task is created or updated.
  
## Classes

### `Task`

Represents a single task with the following attributes:

- `title`: The title of the task.
- `description`: A brief description of the task.
- `status`: The status of the task, which is `"pending"` by default.

**Methods**:

- `mark_completed()`: Marks the task as completed by setting the status to `"completed"`.
- `update(title=None, description=None)`: Updates the title and/or description of the task.
- `__str__()`: Returns a string representation of the task.

### `TaskManager`

Manages a collection of tasks.

**Attributes**:

- `tasks`: A list to store all the tasks.

**Methods**:

- `add_task(title, description)`: Creates a new `Task` and adds it to the `tasks` list.
- `view_tasks()`: Prints all tasks in the `tasks` list.
- `delete_task(title)`: Deletes a task by its title.
- `update_task(title, new_title=None, new_description=None)`: Updates an existing task's title and/or description.

## How to Use

1. Clone this repository or download the script.

2. Run the script using Python:

   ```bash
   python task_manager.py


## Example
```
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Choose an option: 1
Enter task title: Write README
Enter task description: Write a README file for the Task Manager project.

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Choose an option: 2
Task: Write README
Description: Write a README file for the Task Manager project.
Status: pending
--------------------
```
