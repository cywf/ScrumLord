def generate_report(tasks):
    for task in tasks:
        print(f"Task: {task['name']}, Status: {task['status']}")
        
tasks = [{"name": "Task 1", "status": "Done"}, {"name": "Task 2", "status": "In Progress"}]
generate_report(tasks)
