import eel
import json
from datetime import datetime

# Initialize Eel with the web folder
eel.init('web')

# Load goals from file
def load_goals():
    try:
        with open('goals.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save goals to file
def save_goals(data):
    with open('goals.json', 'w') as f:
        json.dump(data, f, indent=2)

@eel.expose
def add_goal(date, goal):
    goals = load_goals()
    if date not in goals:
        goals[date] = []
    goals[date].append(goal)
    save_goals(goals)
    return goals[date]

@eel.expose
def get_goals(date):
    goals = load_goals()
    return goals.get(date, [])

# Start the app
eel.start('index.html', size=(400, 600))