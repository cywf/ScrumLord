#!/bin/bash

# Create a directory for the project
#mkdir ScrumLord
#cd ScrumLord

# Create Python scripts
echo "def assign_tasks(tasks, team_members):
    for i, task in enumerate(tasks):
        assignee = team_members[i % len(team_members)]
        print(f\"Assigning task '{task}' to {assignee}\")

tasks = [\"Task 1\", \"Task 2\", \"Task 3\", \"Task 4\"]
team_members = [\"Alice\", \"Bob\", \"Charlie\"]
assign_tasks(tasks, team_members)" > sprint_planning.py

echo "def ask_progress(team_members):
    for member in team_members:
        print(f\"{member}, what did you work on yesterday? Any blockers?\")

team_members = [\"Alice\", \"Bob\", \"Charlie\"]
ask_progress(team_members)" > daily_standup.py

echo "def generate_report(tasks):
    for task in tasks:
        print(f\"Task: {task['name']}, Status: {task['status']}\")
        
tasks = [{\"name\": \"Task 1\", \"status\": \"Done\"}, {\"name\": \"Task 2\", \"status\": \"In Progress\"}]
generate_report(tasks)" > sprint_review.py

echo "def ask_feedback(team_members):
    for member in team_members:
        print(f\"{member}, do you have any feedback or suggestions for improvement?\")

team_members = [\"Alice\", \"Bob\", \"Charlie\"]
ask_feedback(team_members)" > retrospective.py

echo "def update_board(task, status):
    print(f\"Updating task '{task}' to status '{status}'\")

task = \"Task 1\"
status = \"Done\"
update_board(task, status)" > scrum_board.py

echo "def send_notification(member, message):
    print(f\"Sending notification to {member}: {message}\")

member = \"Alice\"
message = \"Don't forget about the sprint review meeting tomorrow!\"
send_notification(member, message)" > notifications.py

echo "Python scripts created successfully!"
