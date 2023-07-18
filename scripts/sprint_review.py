# V1

#def generate_report(tasks):
#    for task in tasks:
#        print(f"Task: {task['name']}, Status: {task['status']}")
#        
#tasks = [{"name": "Task 1", "status": "Done"}, {"name": "Task 2", "status": "In Progress"}]
#generate_report(tasks)

# ----------------------------

# V2

# Import necessary libraries
# import task_management_system_integration_library

def sprint_review(sprint_id):
    # Pull data from the task management system
    # tasks = task_management_system_integration_library.get_sprint_tasks(sprint_id)
    for task in tasks:
        print(f"Task: {task['name']}, Status: {task['status']}")
    # Generate metrics
    velocity = calculate_velocity(tasks)
    print(f"Sprint velocity: {velocity}")

def calculate_velocity(tasks):
    # Calculate the team's velocity based on the completed tasks
    completed_tasks = [task for task in tasks if task['status'] == 'Complete']
    velocity = len(completed_tasks)
    return velocity

sprint_id = "Sprint 1"
sprint_review(sprint_id)
