def ask_progress(team_members):
    for member in team_members:
        print(f"{member}, what did you work on yesterday? Any blockers?")

team_members = ["Alice", "Bob", "Charlie"]
ask_progress(team_members)
