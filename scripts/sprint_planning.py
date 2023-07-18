def assign_tasks(tasks, team_members):
    for i, task in enumerate(tasks):
        assignee = team_members[i % len(team_members)]
        print(f"Assigning task '{task}' to {assignee}")

tasks = ["Task 1", "Task 2", "Task 3", "Task 4"]
team_members = ["Alice", "Bob", "Charlie"]
assign_tasks(tasks, team_members)
