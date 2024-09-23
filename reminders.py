import json
import os

REMINDER_FILE = 'data/reminders.json'

# Initialize the reminders file if it doesn't exist
if not os.path.exists(REMINDER_FILE):
    with open(REMINDER_FILE, 'w') as f:
        json.dump([], f)

def set_reminder(reminder):
    with open(REMINDER_FILE, 'r+') as file:
        reminders = json.load(file)
        reminders.append(reminder)
        file.seek(0)
        json.dump(reminders, file)
    return f"Reminder set: {reminder}"

def get_reminders():
    with open(REMINDER_FILE, 'r') as file:
        reminders = json.load(file)
    return reminders if reminders else "You have no reminders."

# Example usage
# print(set_reminder("Meeting at 3 PM"))
# print(get_reminders())
