# V1

#def update_board(task, status):
#    print(f"Updating task '{task}' to status '{status}'")
#
#task = "Task 1"
#status = "Done"
#update_board(task, status)

# ----------------------------

# V2

# Import necessary libraries
# import scrum_board_library
# import version_control_library

def update_sprint_board(task, status):
    # Update task status on the sprint board
    scrum_board_library.update_task(task, status)
    # Check if the task is taking longer than expected
    if scrum_board_library.is_task_long(task):
        print(f"Task '{task}' is taking longer than expected")
    # Move tasks based on commit messages
    commit_message = version_control_library.get_latest_commit_message()
    if commit_message:
        task, status = parse_commit_message(commit_message)
        scrum_board_library.update_task(task, status)

def parse_commit_message(commit_message):
    # Parse the commit message to get the task and status
    # This would depend on the format of your commit messages
    task = "Task from commit message"
    status = "Status from commit message"
    return task, status

task = "Task 1"
status = "In Progress"
update_sprint_board(task, status)
