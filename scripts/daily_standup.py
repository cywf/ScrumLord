# V1

#def ask_progress(team_members):
#    for member in team_members:
#        print(f"{member}, what did you work on yesterday? Any blockers?")
#
#team_members = ["Alice", "Bob", "Charlie"]
#ask_progress(team_members)

# ----------------------------

# V2

# Import necessary libraries
# import chat_platform_integration_library
# import project_management_system_integration_library

def daily_standup(team_members):
    for member in team_members:
        # Send questions to each team member via chat platform
        # responses = chat_platform_integration_library.send_questions(member)
        print(f"{member}'s responses: {responses}")
        # Update task status in project management system based on responses
        # project_management_system_integration_library.update_task_status(responses)
        # Track blockers
        if "blocker" in responses:
            track_blocker(member)

def track_blocker(member):
    # Track if a team member consistently reports blockers and raise a flag for further investigation
    print(f"Tracking blocker for {member}")

team_members = ["Alice", "Bob", "Charlie"]
daily_standup(team_members)
